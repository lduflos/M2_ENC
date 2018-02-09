# Chapitre 11 : Jointure SQL et Update

Après avoir fait des insertions, il est possible de :

* lier les auteurs à une publication
* mettre à jour les données d'un objet

## La jointure
En SQL, la jointure est une requête effectuée sur plusieurs tables ensemble => permet d'éviter de multiplier les communications avec le serveur SQL. Mal faites = pb de performance

Avantage SQLAlchemy : jointures sont faciles à effectuer.  
Ici, nos utilisateurs pouvant créer ou éditer des objets, ont une relation de n-n (*many-to-many*) entre notre Place et notre User => création d'une table de liaison entre nos objets : `table authorship`  

Documentation sur les jointures :  http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html

### Configuration Flask / MySQL

```python
# On remet en place la configuration Flask / MySQL

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("Nom")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://gazetteer_user:password@localhost/gazetteer'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

```

### Code
* `default` : peut prendre une fonction (exécution à l'enregistrement simplement en fournissant le nom de la fonction)
* `ForeignKey`: lier un champ à un autre champ d'une autre table. Utilisation des guillemets (syntaxe MySQL et non python (`nomdetable.champ`))
* `__table__`: imposer un nom de table

```python
import datetime

# création d'un db.Model Authorship
class Authorship(db.Model):
    __tablename__ = "authorship" # introduction __tablename__ : spécifier un nom de table pour SQLAlchemy
    authorship_id = db.Column(db.Integer, nullable=True, autoincrement=True, primary_key=True)
    authorship_place_id = db.Column(db.Integer, db.ForeignKey('place.place_id')) 
    authorship_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    authorship_date = db.Column(db.DateTime, default=datetime.datetime.utcnow) # utilisation de la fonction datetime.utcnow (exécution à chaque insertion)
    user = db.relationship("User", back_populates="authorships")
    place = db.relationship("Place", back_populates="authorships")

class User(db.Model):
    user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    user_nom = db.Column(db.Text, nullable=False)
    user_login = db.Column(db.String(45), nullable=False, unique=True)
    user_email = db.Column(db.Text, nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
    # Seul changement pour user
    authorships = db.relationship("Authorship", back_populates="user")
    
class Place(db.Model):
    place_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    place_nom = db.Column(db.Text)
    place_description = db.Column(db.Text)
    place_longitude = db.Column(db.Float)
    place_latitude = db.Column(db.Float)
    place_type = db.Column(db.String(45))
    # Seul changement pour lieu
    authorships = db.relationship("Authorship", back_populates="place")
```

### Construction des relations en python
**4** nouveautés, dans les 3 classes, introduites *via* `db.relationship()`

```python
class Authorship(db.Model):
    # ...
    user = db.relationship("User", back_populates="authorships")
    place = db.relationship("Place", back_populates="authorships")

class User(db.Model):
    # ...
    authorships = db.relationship("Authorship", back_populates="user")
    
class Place(db.Model):
    # ...
    authorships = db.relationship("Authorship", back_populates="place")
```

#### db.relationship
`db.relationship` : construire des relations directes entre les obj et naviguer entre eux => dans l'insertion, on n'utilise pas `place_id` ou `user.id` mais bien `place` et `user`  
Contrairement à `db.Column()`, elle n'intervient pas sur la structure MySQL des classes mais permet simplement la connexion entre les différentes classes.  
Construction sur **2** paramètres : 

* nom de la classe python qui est liée à la propriété
* `back_populates` (optionnel) : propriété dans la classe cible qui contient la même information en miroir => `Authorship.user` lie vers `User` tandis que `User.authorships` lie vers `Authorship`

```python
class A(db.Model):
    propriete_de_relation = db.relationship(
        "NomDeLaClasseLiée",
        back_populates="a"
    )
class NomDeLaClasseLiée(db.Model):
    a = db.relationship(
        "A",
        back_populates="propriete_de_relation"
    )
```

## Update

En MySql et en gestion de données, on parle généralement de CRUD : *Create-Read-Update-Delete*. Nous avons vu les deux premiers, le quatrième s'écrite simplement `Place.query.get(1).delete()` ce qui n'est pas très compliqué... Alors, comment corriger un enregistrement ?

La modification d'une ligne SQL se fait assez simplement :
1. On récupère l'objet
2. On modifie les propriétés que l'on souhaite modifier
3. On ajoute l'objet dans à la session de changement
4. On commit

Soit :

```python 
# 1.
place = Place.query.filter(Place.place_nom.like("%settlement%")).first()
print(place.place_nom)
# 2.
place.place_nom = "Lipara"
# 3. 
db.session.add(place)
# 4.
db.session.commit()

# Résultats:

print(Place.query.filter(Place.place_nom.like("%settlement%")).count())

```
`Resultat : Lipara (settlement)
0`