# Chapitre 4 : Les fichiers CSV, Json et les requêtes

## Format CSV
=> fichier CSV est un fichier de tableau simplifié au maximum :
* encodage plein texte, lecture par un éditeur de txt lambda
* séparateur de colonnes (virgule, point-virgule, tabulation)
* utilisation ligne par ligne de tableur

# Packages
Python est fait de nbses fonctions de base (ex: `len()` ou `print()`) + packages (librairies ou bibliothèques) par défaut  
**Package** : ensemble de modules comportant des outils (fonctions) et qui peuvent être assez simplement importés
`import csv`

## Package CSV
Important : lecture de la documentation (https://docs.python.org/3.5/library/csv.html)
### Lire : `reader()`
```python
import csv
with open('data/csv/eggs.csv', newline='') as csvfile: #newline='' pas important, peu utilisé
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|') #lecteur de fichier csv (parcer : lire un format et l'interpréter en langage informatique)
    for row in spamreader:
        print(row)
        print(', '.join(row))```

Analyse :
* `csv.reader()` prend comme premier argument un fichier ouvert
* `dialect` (ou paramètres) qui ne sont pas dvp dans la documentation de la fonction elle-même
* `**fmtparams` : ** signifie qu'il existe d'autres paramètres optionnels nominatifs

exemples paramètres :
* `delimiter` : délimiteur colonnes
* `quotechar` : "encapsulateur" permettant d'échapper les délimateurs

*fonction utile : fonction enumerate*  
=> permet de renvoyer un tuple sur une valeur simple afin de compter l'index de l'objet parcouru

### Ecrire : `writer()`  
```python
import csv
with open('data/csv/eggs.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL) #quoting : permet au csv comment il est rédigé
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans']) #liste (....)
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])```

Analyse :
* `csv.writer()` prend comme premier argument un fichier ouvert en mode écriture
* `dialect` (ou paramètres) qui ne sont pas dvp par la documentation de la fonction elle-même
* `**fmtparams` : ** signifie qu'il existe d'autres paramètres optionnels nominatifs.

exemples paramètres :
* `delimiter` : délimiteur colonnes
* `quotechar` : "encapsulateur" permettant d'échapper les délimateurs
* `quoting` qui d'après la documentation correspond à un mode de citation minimal (Utilisation des quotechar que lorsque cela est nécessaire.

On écrit une ligne en utilisant la méthode `.writerow()` qui prend comme argument une liste  
On utilise `.writerow()` autant de fois que nécessaire

*`from __ import __`: importation d'un sous-module ou d'une sous-fonction en particulier
