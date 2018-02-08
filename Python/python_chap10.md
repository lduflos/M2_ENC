# Chapitre 10 : session utilisations et insertions SQL

## Créer des comptes
Création de compte est une tâche des plus courantes dans le cadre de dvpt applicatif => !! : aussi l'une des plus dangereuses : responsabilité de la sécurité de vos utilisateurs et de leurs données.

### Gérer des mots de passe
Pour enregistrer un mdp, on va *a minima* l'encrypter => __*hash*__ : contrairement à l'encryptage, il n'est pas réversible. 

* seul moyen de trouver l'original est de *brute-forcer* le *hash* => générer tous les mdp possibles
* casser un *hash* : algorithme de hashage de cassé (3 actuellement recommandés : http://security.blogoverflow.com/2013/09/about-secure-password-hashing/)

Pour Flask, *werkzeug* fournit **2** fonctions :
* `generate_password_hash`
* `check_password_hash`

Pour plus de sécurité : oAuth1 ou Auth2 mais un coût supplémentaire pour l'utilisateur (mappage utilisateur)

### Constante de sécurité
Création d'un fichier `constantes.py` pour une configuration générale + stockage d'un "secret" qui permet à Flask d'effectuer des transactions sécurisées

```python
from warnings import warn

LIEUX_PAR_PAGE = 2
SECRET_KEY = "JE SUIS UN SECRET !"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)
```

`LIEUX_PAR_PAGE` + intégration `SECRET_KEY`: permet à Flask d'ajouter ou non des sessions utilisateurs  

Attaque *Man in the middle* : envoie d'un réseau qui porte le même nom, se connecte au réseau et récupère toutes les données transmises (se rend compte de rien)

* protocole https (encrypter les formulaires)
* encrypter données sessions et cookies
* clé de cryptage

Le sel devant être unique et non-devinable, on rajoute un avertissement au cas où la personne mettant ce site en fonctionnement n'avait pas connaissance de ce changement de configuration.

### Méthode propre
#### Classe `User`  

```python
class User(db.Model):
    user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    user_nom = db.Column(db.Text, nullable=False)
    user_login = db.Column(db.String(45), nullable=False, unique=True)
    user_email = db.Column(db.Text, nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
```

#### Fonction pour vérification d'une connexion
Vérification validité de l'identification de l'utilisateur : retrouve l'utilisateur, compare le *hash* généré du mdp avec celui enregistré :

```python
def identification(login, motdepasse):
    """ Identifie un utilisateur. Si cela fonctionne, renvoie les données de l'utilisateur
    
    :param login: Login de l'utilisateur
    :param motdepasse: Mot de passe envoyé par l'utilisateur
    :returns: Si réussite, données de l'utilisateur. Sinon None
    :rtype: User or None
    """
    utilisateur = User.query.filter(User.user_login == login).first() # regarde si utilisateur existant (requête)
    if utilisateur and check_password_hash(utilisateur.user_password, motdepasse): # fonctionne si j'en trouve un, sinon renvoi "none"
        return utilisateur
    return None
```

Pour que cette fonction soit facile à retrouver, on va l'enregistrer sous la responsabilité de la classe `User` :

```python
class User(db.Model):
    user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    user_nom = db.Column(db.Text, nullable=False)
    user_login = db.Column(db.String(45), nullable=False, unique=True)
    user_email = db.Column(db.Text, nullable=False)
    user_password = db.Column(db.String(64), nullable=False)
    
    @staticmethod # précéde la fonction de l'@
    # enregistrement de la fonction comme une méthode statique d'utilisateur (on pourrait mettre user.identification(log, mdp)). Statique car elle ne porte pas sur un utilisateur particulier.
    def identification(login, motdepasse):
        """ Identifie un utilisateur. Si cela fonctionne, renvoie les données de l'utilisateur

        :param login: Login de l'utilisateur
        :param motdepasse: Mot de passe envoyé par l'utilisateur
        :returns: Si réussite, données de l'utilisateur. Sinon None
        :rtype: User or None
        """
        utilisateur = User.query.filter(User.user_login == login).first()
        if utilisateur and check_password_hash(utilisateur.user_password, motdepasse):
            return utilisateur
        return None
```

On précède notre fonction de `@staticmethod` pour mettre d'appeler cette fonction ainsi :

```python
utilisateur = User.identification(login, motdepasse) # étiquette qui accroche la fonction précédemment définie
```

### Premier insert
Fonction création de compte : créer un enregistrement ou une màj, MySQL et SQLAlchemy fonctionne par session de changement (//git) : 

* création d'un ensemble de modifications
* stockage pour envoi : `db.session.add(la_chose_a_envoyer)`
* envoi à MySQL : `db.session.commit()`

```python
class User(db.model):
    # ...
    @staticmethod
    def creer(login, email, nom, motdepasse):
        """ Crée un compte utilisateur-rice. Retourne un tuple (booléen (succes ou echec de la fonction), User ou liste).
        Si il y a une erreur, la fonction renvoie False suivi d'une liste d'erreur
        Sinon, elle renvoie True suivi de la donnée enregistrée

        :param login: Login de l'utilisateur-rice
        :param email: Email de l'utilisateur-rice
        :param nom: Nom de l'utilisateur-rice
        :param motdepasse: Mot de passe de l'utilisateur-rice (Minimum 6 caractères)

        """
        erreurs = []
        if not login:
            erreurs.append("Le login fourni est vide")
        if not email:
            erreurs.append("L'email fourni est vide")
        if not nom:
            erreurs.append("Le nom fourni est vide")
        if not motdepasse or len(motdepasse) < 6:
            erreurs.append("Le mot de passe fourni est vide ou trop court")

        # On vérifie que personne n'a utilisé cet email ou ce login
        unique = User.query.filter(
            db.or_(User.user_email == email, User.user_login == login)
        ).count()
        if uniques > 0:
            erreurs.append("L'email ou le login sont déjà inscrits dans notre base de données")

        # Si on a au moins une erreur
        if len(erreurs) > 0:
            return False, erreurs # il s'agit d'un tuple (il est possible de ne pas mettre les ())

        # On crée un utilisateur
        utilisateur = User(
            user_nom=nom,
            user_login=login,
            user_email=email,
            user_password=generate_password_hash(motdepasse)
        )

        try:
            # On l'ajoute au transport vers la base de données
            db.session.add(utilisateur)
            # On envoie le paquet
            db.session.commit()

            # On renvoie l'utilisateur
            return True, utilisateur
        except Exception as erreur:
            return False, [str(erreur)]
```

### Formulaire d'inscription
Ajout de la route pour s'inscrire (avec lien dans le menu)

```python
from flask import flash, redirect, request # fonction flask.flash pour afficher les messages d'erreurs (elles peuvent avoir des catégories) // cf. container.html
# flask.redirect : rediriger vers une url précise


@app.route("/register", methods=["GET", "POST"]) # ajout de paramètres methods "GET" (request.args), "POST" (request.form)
def inscription():
    """ Route gérant les inscriptions
    """
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST": # vérification de la méthode utilisée (request.method)
        statut, donnees = User.creer(
            login=request.form.get("login", None),
            email=request.form.get("email", None),
            nom=request.form.get("nom", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if statut is True:
            flash("Enregistrement effectué. Identifiez-vous maintenant", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")
```

### Se connecter
Session utilisateur : ensemble de données qui sont transmises d'une page à l'autre  
`flask-login`: plug-in de gestion des utilisateurs (pip install)

#### Configuration
Même configuration que Flask SQLAlchamy : ajout dans le fichier `app.py`  

```python
from flask_login import LoginManager
app = Flask(...)
# ...
login = LoginManager(app)
```

Une fois cela fait, configuration de l'objet SQLAlchemy User pour qu'il puisse être compris par Flask Login, rajout de **4** fonctions :

* `is_authenticated` (propriété) : retourne *True* si l'utilisateur-rice est connecté-e, *False* sinon
* `is_active` (propriété) : retourne *True* si l'utilisateur-rice est actif-ve, *False* sinon
	* Le caractère actif des membres de notre site n'est pas utilisé, pourtant, il faudra remplir cette case. On renverra donc *True*
* `is_anonymous` (propriété) : retourne *False* pour les utilisateur-rices non-anonymes
* `get_id(identifier)` (fonction) : retourne l'utilisateur pour l'ID donné => récupération d'un id `User.query.get(id)`

Flask Login propose un outil pour ne pas avoir à coder cela soit même : `flask_login.UserMixin` => en ajoutant `UserMixin` à `db.Model`, on donne à Python l'information que User est à la fois un `UserMixin` et un `db.Model`.

```python
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .. app import db

class User(UserMixin, db.Model):
# ...

```

**Malheureusement**, le `get_id` par défaut de `UserMixin` n'est pas complètement compatible avec notre `User`, car il a besoin d'une propriété `.id` pour que `get_id()` fonctionne. 

``` python 
user.cree() # méthode statique : fonction de user mais pas rattachée à un en particulier
"a".replace("a", "b") # méthode (// programmation orientée objet) : replace a conscient de ce qu'il remplace```

On va donc écrire par-dessus:

```python
class User(UserMixin, db.Model):
    # ...
    def get_id(self): # self qui permet de faire comprendre à get_id quel est l'utilisateur courant à identifier
        """ Retourne l'id de l'objet actuellement utilisé 
        
        :returns: ID de l'utilisateur
        :rtype: int
        """
        return self.user_id
```

Ici, `self` prend la valeur de l'utilisateur courant. Par exemple :

```python
Laurel = User(user_id=1)
Hardy = User(user_id=2)

print(Laurel.get_id())
>>> 1
print(Hardy.get_id())
>>> 2
```

Il va quand même falloir définir nous même une fonction qui permettra de récupérer un utilisateur en fonction de son identifiant (toujours dans `utilisateur.py`) :

```python
from app import login

# ...
@login.user_loader
def trouver_utilisateur_via_id(id):
    return User.query.get(int(id))
```

### Formulaire de connexion

Ajout d'un nouveau formulaire avec un nouveau menu dans le container principal :

```html
{% extends "conteneur.html" %}

{% block titre %}| Connexion{%endblock%}

{% block corps %}

<h1>Inscription</h1>
<form class="form" method="POST" action="{{url_for("connexion")}}">
  <div class="form-group row">
    <label for="register-login" class="col-sm-2 col-form-label">Login</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="register-login" name="login" placeholder="Nom d'utilisateur pour se connecter">
    </div>
  </div>
  <div class="form-group row">
    <label for="register-password" class="col-sm-2 col-form-label">Password</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="register-password" placeholder="Mot de passe" name="motdepasse">
    </div>
  </div>
  <div>
    <button type="submit" class="btn btn-primary">Connexion</button>
    <a href="{{url_for("inscription")}}" class="btn btn-secondary">Inscription</a>
  </div>
</form>
{% endblock %}
```

et la route qui correspondra 

```python
from flask_login import login_user, current_user
from .app import login


@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route gérant les connexions
    """
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté-e", "info")
        return redirect("/")
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        utilisateur = User.identification(
            login=request.form.get("login", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if utilisateur:
            flash("Connexion effectuée", "success")
            login_user(utilisateur)
            return redirect("/")
        else:
            flash("Les identifiants n'ont pas été reconnus", "error")

    return render_template("pages/connexion.html")
        
login.login_view = 'connexion'
# login : Manager de session
# connexion : nom de la fonction qui sert à afficher la page de connexion
# redirection possible vers la page de connexion
```

#### Remarques
* obtenir utilisateur courant : on appelle `flask_login.current_user`
* valider authentification : on passe à la fonction `flask_login.login_user` la variable comportant l'utilisateur
* marquer la route définie comme celle de connexion

### Deconnexion

Route de déconnexion : utiliser la fonction `flask_login.logout_user`

```python
from flask_login import logout_user, current_user

@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté-e", "info")
    return redirect("/")
```

### Afficher l'utilisateur courant dans les templates

Affichage de l'utilisateur dans les templates : utilisation variable `{{ current_user }}`: 

```html
<ul class="navbar-nav mr-auto">
    {% if not current_user.is_authenticated %}
      <li class="nav-item">
        <a class="nav-link" href="{{url_for("inscription")}}">Inscription</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{{url_for("connexion")}}">Connexion</a>
      </li>
    {% else %}
      <li class="nav-item">
        <a class="nav-link" href="{{url_for("deconnexion")}}">Déconnexion ({{current_user.user_nom}})</a>
      </li>
    {% endif %}
```