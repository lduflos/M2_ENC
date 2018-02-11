# Python - Chapitre 5 : Flask, un framework d'application web
## Les objets : introduction rapide
En programmation (particulièrement en python), les objets sont des éléments extrêmement importants

### Les classes
* **Classe** : famille d'objets équivalente à un nouveau type de données (ex : les classes `str` ou les classes `list`). Leur manipulation se fait à l'aide des méthodes.
* **Classe d'objets** : grande catégorie de valeurs qui sont régies par un ensemble de lois similaires et qui peuvent fonctionner de telle ou telle manière
  * classe : catégorie de valeurs
  * objet : instance des classes

``` python
print(type("Bonjour le monde")) # <class 'str'>
print(type("Au revoir le monde")) # <class 'str'>
print(type([1,25])) # <class 'list'>```

`Bonjour le monde` et `Au revoir le monde` sont des objets de la classe `str`.

### Les méthodes
Les objets peuvent posséder leurs propres fonctions. Les fonctions propres à des classes et à leurs objets sont appelées **méthodes**. Elles diffèrent des fonctions habituelles par leur syntaxe : une méthode est appelée après un point `.` et est uniquement accessible pour les classes qui la possèdent.
```python print("Bonjour le monde".replace("monde", "master TNAH"))  
# résultat : Bonjour le master TNAH```

### Les attributs
Un objet peut aussi avoir des **attributs**. Ce sont des propriétés/ valeurs de ces classes qui fonctionnent comme des variables ou des clés de dictionnaires

### Instancer un objet
Pour créer un objet qui ne fait pas partie des types principaux, on utilise généralement le no de la classe avec les paramètres de base dont elle a besoin (// utilisation d'une fonction)

Vocabulaire :
* classe : plan
* objet : réalisation du plan
* méthode : fonction propre à l'objet
* attribut : clé/propriété de l'objet
* instanciation : création d'un objet à partir d'une classe (= fait de créer l'objet)

--------------------------------------------------------------------------------------
## Flask
Il s'agit d'un framework (*back-end*) pour le dvpt d'application web en python.  
* Concurrent principal : Django
* c'est un package de python (commande *pip install flask*)

### Travailler sur son propre projet : recommandations
Utilisation d'un environnement virtuel (installation en vase clos de python pour ne pas interférer avec d'autres projets + installation limitée à un dossier particulier)  
Marche à suivre :
- `cd ~` *vous met dans votre dossier utilisateur*
- `mkdir nom_du_dossier` *crée un dossier appelé nom_du_dossier* (**A exécuter une fois seulement**)
- `cd nom_du_dossier` *vous déplace dans ce dossier*
- `python3 -m venv env` *crée un environnement virtuel dans un sous-dossier. Alternative à `virtualenv -p python3 env` (**A exécuter une fois seulement**)
- `source env/bin/activate` *remplace dans votre session de terminal le lien vers le python 3 global par un lien vers le python 3 de votre environnement virtuel*
- `pip install flask` *installe flask dans votre environnement virtuel* (**A exécuter une fois seulement**)

```python
from flask import Flask

app = Flask("Nom de l'application") # nom obligatoire dans Flask : permet d'avoir plusieurs applications tounant sur le même serveur et de les différencier pour le serveur

@app.route("/") # définit une route (précède la fonction)
def index(): # fonction qui suit est exécutée sur telle url
    return "Hello world !"

app.run() # lancement de l'application
```

### Route (rapport avec les URLs ?)
= un chemin 
