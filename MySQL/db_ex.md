# Exercice *Database*

## Auteur
* "être originaire de" : présence obligatoire et une fois
* "pays" : présence 0 à n fois
=> auteur originaire d'au moins un pays

* "rédiger" : présence de 0 à n fois
=> un auteur a rédiger un livre au moins

## Livre
* "appartenir" : présence obligatoire et une fois
* "type Livre" : présence de 0 à n fois
=> un livre doit appartenir au moins à un type

* "correspondre" : présence de 0 à n fois
* "exemplaire" : présence obligatoire et une fois
=> un livre doit correspondre à un exemplaire

## Exemplaire
* "paraître" : présence obligatoire et une fois
* "édition" : présence de 0 à n fois
=> un exemplaire doit paraître dans une ou plusieurs éditions

* "concerner" : présence de 0 à n fois
* "emprunt" : présence obligatoire et une fois
=> un exemplaire concerne un seul emprunt

## Emprunt
* "effectuer" : présence obligatoire et une fois
* "inscrit" : présence de 0 à
=> emprunt effectué par un ou plusieurs inscrits
