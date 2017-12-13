# Python - Chapitre 1
## Introduction
__*assignement*__ : assigner des valeurs aux variables, utilisation opérateur **=**  
**variable** : comme une boîte dans laquelle on range des choses et sur laquelle on marquerait le nom pour se souvenir du contenu.  
Peut contenir des nb (entier : *integer* / décimaux : *float*) ou du texte : chaîne de caractères ou *string*, utilisation **"..."**  
* Impce de l'interprétation du message d'erreur en programmation  
* choix du nom de la variable est libre mais attention au sens !
* màj variables : **+=**
* assignement possible d'une variable à une autre

```python
livre = "The Lord of the Flies"
en_cours_de_lecture = livre
print(en_cours_de_lecture)```  
## Manipulation des chaînes
notion *concaténation* : somme de chaînes de caractères  
### Indexation
=> Accès à chacun des caractères de la chaîne  
```python
premiere_lettre = nom[0]
print(premiere_lettre)

derniere_lettre = nom[5]
print(derniere_lettre)```  
* Remarque : Python index à partir de O
* variable [-1] : accéder à une chaîne depuis l'arrière
* fonction **len()** : retourne la longueur d'une chaîne
```Python
print(len(nom))```

### Tranches [... : ...]
**=** prendre tous les caractères jusqu'à arriver à l'index.  
L'index 0 est opionnel => ex : nom[0:2] <=> nom[:2]  
![schema](/media/lea/DE8B-26C9/M2_ENC/Python/python.png)

## Les listes
**=** une sorte de container => enregistrement d'un type d'information  
* **.split ()** : liste de mots d'une chaîne, python scinde la phrase sur les espaces et retourne une liste de mots.  
```python
mots = phrase.split()
print(mots)
['Le', 'nom', 'Python', 'est', 'dérivé', 'de', 'la', 'série', 'télévisée', 'Monty', "Python's", 'Flying', 'Circus.']```

* **.append()** : ajout de nvx obj dans une liste
```python
bonnes_lectures = []
bonnes_lectures.append("Twilight")
bonnes_lectures.append("Pour en finir avec le jugement de Dieu")
print(bonnes_lectures)```
modification :
```python
bonnes_lectures[0] = "Dracula"
print(bonnes_lectures)```

chaîne (*string*) : **immutable**, non changeable  
liste, dictionnaire : **mutable**, changeable  
**.remove()** : suppression dans une liste  
**.sort() : tri de la liste
### Listes imbriquées
```python
liste_imbriquee = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(liste_imbriquee[0])
print(liste_imbriquee[0][0])
print(liste_imbriquee[1][1])
print(liste_imbriquee[-1][-1])```

### Dictionnaires
Il se compose d'**entrées** ou de **clés** qui contiennent une **valeur**.  
Pour rechercher la valeur d'une clé donnée, nous 'indexons' le dictionnaire en utilisant la clé.
```Python
dictionnaire = {"livre"(clé) : "Dracula" (valeur)}```
Ajout nouvelle entrée dans un dictionnaire :
```python
bonnes_lectures = {}
bonnes_lectures["Les poèmes de Paul Celan"] = 8
bonnes_lectures["Voyage au bout de la nuit"] = 9
bonnes_lectures["Bourgeois gentilhomme"] = 5
print(bonnes_lectures)```

#### keys(), values()
liste des index dans un dictionnaire :
* **.keys()**
* **.values()**
* **.items**

#### générateurs et tuples
* **générateur** : sorte de liste qui n'accepte pas l'indexation, puisqu'elles n'ont pas encore été calculées. Liste qui est en cours de constitution  
Pour transformer un générateur en liste, on peut la retyper :
```python
bonnes_lectures_liste = list(bonnes_lectures.keys())
print(bonnes_lectures_liste[0])```

* **tuples** : listes simplifiées et immutables. Elles sont indexables mais, comme les chaînes, ne supportent pas les changements  
fonction de dezipper : clé à gauche, valeur à droite -> dezipper à l'intérieur de la bouble
```python
for cle_valeur in dict.items() :
  #[(1, "a"), (2, "b")...]
= for item in dict.items() :
  cle, valeur = item```

## Conditions
### Les conditions simples
Les opérateurs booléens :
* **!=** : n'est pas égal à
* **==** : est égal à
* **> ou <** : est plus grand que, ou est plus petit que
* **>= ou <=** : est plus grand ou égal à, ou est plus petit ou égal à

#### Si, ou si, et sinon (if, elif, and else)
```python
livre = "Le Retour du Roi"
if livre in bonnes_lectures:
    print(livre + " est dans la collection")
else:
    print(livre + " n'est pas dans la collection")```
=> on demande si la valeur assignée à livre est dans notre collection. La partie if sera évaluée en *true* ou *false*  
Si if fonctionne, les elif et else ne sont pas traités.  
Attention à l'indentation, seul délimiteur **:**.

#### Et, ou, non (and, or, not)
**and** :
* si tout est *true* -> *true*
* si un *false* -> *false* (pas d'affichage)

**or** : contrairement à **and**, accepte => utilisation des parenthèses. Attention à l'ordre des conditions, car continue tant qu'elle n'a pas trouvé une condition *true*.

**not** : teste les conditions qui ne sont pas vraies
* chaîne, entier, liste sont *true* car ils existent
* chaîne, liste, dictionnaire vides sont *false*

### Les boucles
**for** : itératif (= boucler/avancer sur l'élément)  
```python
for i in iterable :```
= pour chaque élément - que l'on stockera dans i - trouvable dans la variable iterable  
* afficher les éléments contenus dans une liste :
```python
couleurs = ["jaune", "rouge", "vert", "bleu", "violet"]
for nimportequoi in couleurs:
    print("C'est la couleur " + nimportequoi)```
* parcourir les clés et valeurs d'un dictionnaire (à chaque itération, retourne un *tuple* clé-valeur):
```python
for livre, note in bonnes_lectures.items():
    print(livre + " a une note de " + str(note))```

**while** : permet de répéter une séries de tâches tant qu'une condition n'est pas *true*, et exprimée de la manière suivante :

while (False):
