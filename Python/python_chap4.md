# Chapitre 4 - Les fichiers CSV, JSON et les requêtes
## 4.1
### Le format CSV
Un fichier CSV est un fichier de tableau simplifié au maximum :
* le fichier est **encodé en plein texte**, il peut être lu par un éditeur de texte lambda
* le fichier utilise un **séparateur de colonnes** (usuellement une virgule, un point-virgule ou une tabulation)
* le fichier utilise une **ligne par ligne** de tableur

--> format pour partager ces données mais une fois calculées  

### Les packages
= nom des librairies et bibliothèques en Python, par défaut  
C'est un ensemble de modules comportant des outils tels que des fonctions ou des objets et qui peuvent être assez simplement importés.  
chargement du package, que fait-il ?  
```Python
import csv```

affichage du contenu du package
```Python
dir(csv)```

#### Le package CSV
*lecture de la documentation Python, attention 3.5.4*  
parcer : lire un format et l'interpréter en langage informatique  
paramètre nommé (encodage, mode, ...) : valeur par défaut

##### *Fonction enumerate*
Utilisation sur un conteneur (liste ou le csv reader) => tuple qui renvoie une valeur simple le numéro et la valeur du texte originale  



('Le fonds Delphine Seyrig dans BnF archives et manuscrits', '', 'http://www.bnf.fr/fr/la_bnf/dpt_asp/s.actualites_arts_spectacle.html?first_Art=oui', '2017-11-22 13:02:02') : '' correspond au résumé donc pas tjs vide


## 4.2
### JSON
Forcément une liste ou un dictionnaire et en dessous :
* des listes,
* des dictionnaires,
* des booléens,
* des chaînes de caractères
* des entiers et des décimaux
* des objets "vides" (null, l'équivalent de None en Python)

json.load : pacer un contenu
json.loads : str (chaîne de caractères)

methode format : bien apprendre car utile pour la conténation des chaînes (les colle)

json.dump:  
json.dumps :


## 4.3
### Requêtes et Réponses
Lors d'une communication HTTP avec un serveur, la communication est scindable en deux : l'envoi de la requête et la réponse du serveur. Ces deux éléments de la communication répondent à un ensemble de standards très stricts permettant le fonctionnement du web tel que nous le connaissons.

#### Requêtes
La requête, c'est-à-dire l'information envoyée au serveur, est composée à minima de trois type d'informations :
- l'URL
- la méthode
- les headers

##### URL
L'URL est l'adresse dont on requiert le contenu. Typiquement, l'adresse est divisible en plusieurs parties. Celle qui peut être importante et qui changera sûrement suivant les utilisateurs est la partie *query* qui permet d'apporter des informations supplémentaires.

Par exemple, dans http://cts.dh.uni-leipzig.de/api/cts?request=GetCapabilities&urn=urn:cts:latinLit:phi1294 , on a deux paramètres fournis :

| Nom | Valeur |
| --- | ------ |
| urn | urn:cts:latinLit:phi1294 |
| request | GetCapabilities |

###### Décomposition de l'URL :

| https:// | www. | exemple | .fr | :300/ | path/resource | ?id=123 | #section-id |
| :------: | :--: | :-----: | :-: | :---: | :-----------: | :-----: | :---------: |
| 1        | 2    | 3       | 4   | 5     | 6             | 7       | 8           |

1. Schéma : définit comment la ressource sera obtenue
2. Sous-domaine : www est le plus commun mais n'est pas obligatoire
3. Domaine : une valeur unique au sein de l'extension
4. Extension (top-level domain) : il existe des centaines d'options d'extensions
5. Port : s'il n'est pas précisé, http se connecte au port 80, et https au port 443. Il y a aussi 21 pour FTP, 22 pour SSH, etc. Ce sont en quelques sortes les tuyaux par lesquels passent les communications
6. Chemin : il spécifie la ressource demandée. Il peut se terminer par une extension de type .html
7. Query String : données qui passent du côté serveur, elle correspond à la requête envoyée au serveur
8. Identifiant de fragment : assez peu utilisé, sauf pour renvoyer à des portions spécifiques de la page, ou dans des application qui utilisent java

##### Méthode
La méthode informe le serveur de ce que l'on veut faire. Elles permettent de ne pas multiplier les adresses, en ne changeant que la méthode, qui détermine le comportement possible.
90% des requêtes envoyées en navigant sur le web sont en GET : c'est-à-dire "récupérer l'information". Vient ensuite la requête POST (9.9% des cas), notamment quand on se connecte sur des comptes sur des sites.
Les autres méthodes possibles sont : `DELETE` ; `UPDATE` ; `PUT`.

cf cours sur données de G. Poupeau

##### Header
Le Header comporte des informations sur les attentes et le contexte de requêtage. Par exemple, on peut demander via les Headers un format de réponse particulier (d'après son [mimetype](https://fr.wikipedia.org/wiki/Type_MIME) : html, xml ou json par exemple :

| Headers Clé | Headers Valeur   |
| ----------- | ---------------- |
| Accept      | application/json |

##### (Optionnel) Le Corps (Body, data, etc.)

Dans le cadre de l'envoi d'un formulaire ou d'un fichier, on a un corps dans la requête. Beaucoup de formats différents sont possible dans ce cadre. De nombreuses API acceptent par exemple l'encodage en JSON des informations.

#### Réponses
La réponse envoyée par le serveur est composée que trois éléments :
- Headers
- code HTTP
- le corps

##### les Headers
Ils renvoient l'information sur la réponse.
| Headers Clé | Headers Valeur   | Note |
| ----------- | ---------------- | ---- |
| Content-type| application/json | Type Mime de la réponse |

##### le code HTTP
Le corps de la réponse informe sur le statut ou l'état de la réponse. Exemples :
- 200 : succès de la requête ;
- 301 et 302 : redirection, respectivement permanente et temporaire ;
- 401 : utilisateur non authentifié ;
- 403 : accès refusé ;
- 404 : page non trouvée ;
- 500 et 503 : erreur serveur.

##### le corps
Le corps de la réponse contient ce que l'on voit lorsque l'on fait une requête : le contenu html, plein texte, json, etc.

### Versionnement
`apparté sur les versions. ->` [Semantic Versioning](https://semver.org/)  
`2.0.0 -> le format de version de base.`  

| 2     | 0     | 0     |
| ----- | ----- | ----- |
| MAJOR | MINOR | PATCH |
