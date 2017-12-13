# Les fonctions et les fichiers
Objectif :
* traitement de texte => nettoyage des données pour une analyse par la suite
* convertir une collection de textes en formats diff

## Lire des fichiers
1. Ouverture des fichiers avec fonction **open**
```python
fichier_ouvert = open('data/cid.v1071.1682.txt')```
Si on **print** : *<_io.TextIOWrapper name='data/cid.v1071.1682.txt' mode='r' encoding='UTF-8'>*  
  * mention "TextIOWrapper" : Python nous informe qu'il a ouvert une connexion au fichier 'data/cid.v1071.1682.txt''
  * encoding='UTF-8' : modèle d'encodage des caractères du fichier
2. Lecture des fichiers avec la fonction **read**
```Python
print(fichier_ouvert.read())```
Assigner le contenu du fichier à la variable **texte** :
```python
fichier_ouvert = open('data/cid.v1071.1682.txt')
texte = fichier_ouvert.read()```
=> la variable texte contient le contenu du fichier 'data...'
3. Fermeture des fichiers avec la fonction **close** :
```python
fichier_ouvert.close()```
4. Gérer un fichier à ouvrir et lire avec la fonction **with** :
```python
with open('data/cid.v1071.1682.txt') as fichier_cid :
  texte = fichier_cid.read()```
avantage : méthode qui ferme elle-même le fichier qui a été ouvert.

### assert
= vérification des travaux
```python
assert nombre_de_e == 182, "On devrait trouver 182 'e'"```

## Écrire sa première fonction
* fonction **.count**
```python
nombre_de_e = texte.count("e")
print(nombre_de_e)```
Attention : utilisation des espaces pour faire apparaître le mot, sinon c'est la chaîne qui apparait
```python
print(texte.count(" et "))```
* fonction **.split** : divise une chaîne sur les espaces et retourne une liste de plus petites chaînes

# Les Fonctions

Une fonction est composée de **paramètres/arguments** (aussi appelés *args* ou *params*). Elle renvoie une valeur, appelée valeur de retour (***return value***). On peut créer ses propres fonctions.

```python
def fonction_avec_parametres(parametre1, parametre2, parametre3):
    # Le code de la fonction```

```python
def fonction_sans_parametre():
    # le code la fonction```

Exemple de fonction qui prend en paramètres un élément à chercher, et un emplacement où le chercher :

```python
def compter_dans_une_autre_chaine(aiguille, botte_de_foin):
    mots_de_foin = botte_de_foin.split()
    nombre_daiguilles = mots_de_foin.count(aiguille)               
    return nombre_daiguilles```  

### Fonctions et Méthodes

Une méthode se différencie d'une fonction sa syntaxe. Alors qu'une fonction s'écrit nom_fonction(paramètres), une méthode s'écrit de la maniètre suivante : variable.methode(paramètres).

## Scope et portée

Une variable qui existe dans une fonction est séparée du reste du code : on ne peut pas faire appel à une variable utilisée dans la définition de la fonction ailleurs quand dans cette même définition.
