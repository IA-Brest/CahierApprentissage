---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Manipulation de tableaux

## 1 - Exercice : la moyenne

Soit la liste `lst_temperatures = [12, 13, 14, 28]`, écrire un programme qui permet de calculer la moyenne de ces valeurs :

- Avec une boucle `for`
- Avec une boucle `while`

```python slideshow={"slide_type": "subslide"}
lst_temperatures = [12, 13, 14, 28]

total = 0
nb_values = 0
for tmp in lst_temperatures :
    total += tmp
    nb_values += 1
print(total / nb_values)

total = 0
nb_values = 0
while nb_values < len(lst_temperatures):
    total += lst_temperatures[nb_values]
    nb_values += 1
print(total / nb_values)
```

## 2 - Exercice : les jours de la semaine

Constituer une liste contenant le nom des sept jours de la semaine. À partir de cette liste comment peut-on récupérer :

- Les 5 premiers jours de la semaine
- Ceux du week-end
- Uniquement le dernier élément
- Tous les éléments sauf le dernier 

Indications :

- Tester vos propositions
- Quel est le type des éléments renvoyés ?

```python
semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

print(type(semaine[:5]), semaine[:5])
print(type(semaine[-2:]), semaine[-2:])
print(type(semaine[-1]), semaine[-1])
print(type(semaine[:-1]), semaine[:-1])
```

## 3 - Exercice : inversion de l'ordre d'une liste

Soit une liste quelconque d'éléments, écrire un programme qui en inverse l'ordre.

On utilisera une seule liste pour effectuer l'opération.

```python
print(semaine[::-1])
```

## 4 - Exercice : nombres pairs et impairs dans des listes

On souhaite stocker dans deux listes différentes les nombres saisis par l'utilisateur selon s'il s'agit d'un nombre pair ou d'un nombre impair.

Le programme se terminera lorsque l'utilisateur aura entré la valeur `-1`.

```python
pair = list()
impair = list()

saisie = int(input())

while saisie != -1:
    if saisie %2 == 0:
        pair[-1:-1] = [saisie]
    else:
        impair[-1:-1] = [saisie]
    saisie = int(input())
print(pair)
print(impair)
```

<!-- #region -->
Le programme ci-dessus fonctionne, mais il ne gère pas les erreurs de saisie.

En effet si l'utilisateur ne saisit pas un nombre, le programme s'interrompt brutalement (erreur Python).
En Python, on peut contrôler si une valeur est numérique avec la **méthode** `isnumeric()` qui s'applique (uniquement) sur une chaîne de caractères et qui renvoie `True` ou `False`.

Exemples :

```python
valeur = "1"
valeur.isnumeric()  # True
valeur = "a"
valeur.isnumeric()  # False
valeur = "-1"
valeur.isnumeric()  # False
valeur = 1
valeur.isnumeric()  # Erreur !
```

En utilisant `isnumeric()`, modifier le programme ci-dessus afin d'afficher un message d'erreur à l'utilisateur s'il saisit une valeur non numérique.
<!-- #endregion -->

```python
def saisir():
    saisie = input()
    if saisie.isnumeric():
        saisie = int(saisie)
    elif saisie == "-1":
        saisie = -1
    else:
        print("La valeur " + saisie + " n'est pas une valeur numérique")
        return(saisir())
    return saisie

pair = list()
impair = list()

nombre = saisir()

print(nombre)

while nombre != -1:
    if nombre %2 == 0:
        pair[-1:-1] = [nombre]
    else:
        impair[-1:-1] = [nombre]
    nombre = saisir()

print(pair)
print(impair)
```

## 5 - Exercice : des étoiles

Ecrire un programme qui permet d'afficher un "graphique" de ce type :
```
*
**
***
****
*****
```

- Le nombre d'étoiles sera défini au préalable dans une variable.
- Faire une version avec une boucle `for` et une version avec avec une boucle `while`.

```python
nb_etoiles = 6

for star in range(nb_etoiles):
    print("*" * star)

star = 0
while star < nb_etoiles:
    print("*" * star)
    star += 1
```

<!-- #region -->
## 6 - Exercice : copie de listes

Etant données deux listes, on souhaite copier la première dans la deuxième et ainsi pouvoir modifier une valeur dans la deuxième liste sans que cela ne modifie la première.

- `lst1 = [1, 2, 3]`.
- On copie `lst1` dans `lst2`.
- On modifie le premier élément de `lst2` en mettant la valeur `4`.
- On doit obtenir :
  - `lst1` : `[1, 2, 3]` (inchangée)
  - `lst2` : `[4, 2, 3]`

Le programme suivant a été écrit :

```python
lst1 = [1, 2, 3]
lst2 = lst1
lst2[0] = 4
print(lst2)
print(lst1)
```
- Que remarquez-vous ?

<!-- #endregion -->

```python
lst1 = [1, 2, 3]
lst2 = lst1
lst2[0] = 4
print(lst2)
print(lst1)
### Les deux listes ont été modifiées
```

- Modifiez le pour qu'il réponde au problème posé.

```python
lst1 = [1, 2, 3]
lst2 = list(lst1)
lst2[0] = 4
print(lst1)
print(lst2)

```

## 7 - Exercice : le jeu du + ou du -

L'ordinateur choisit un nombre au hasard entre 1 et 100 et l'utilisateur doit deviner ce nombre mystère en respectant la règle suivante :

- Version 1
  - L'utilisateur propose un nombre.
  - Le programme lui dit s'il est trop petit ou trop grand.
  - Et ainsi de suite tant que l'utilisateur n'a pas trouvé le nombre mystère.
- Version 2
  - Ajouter une gestion d'erreur si l'utilisateur ne rentre pas un nombre entre 1 et 100 ou s'il rentre autre chose qu'un nombre.
- Version 3
  - Indiquer à l'utilisateur en combien de coups il a trouvé le nombre mystère.

```python
from random import randint

# Valeur minimale à trouver
min = 1
# Valeur maximale à trouver
max = 100

# Une valeur au hasard
cible = randint(min, max)
# Nombre de coups joués
coups = 0
# Proposition du joueur
proposition = 0

while proposition != cible:
    # On saisie un essai et on incrémente le nombre de coups joués
    proposition = input(f'Trouvez un nombre compris entre {min} et {max} :')
    coups += 1
    
    # On vérifie que la valeur saisie est un nombre
    if not proposition.isnumeric():
        print(str(proposition) + " n'est pas un nombre !")
        continue
    else:
        proposition = int(proposition)
    
    # On regarde si on a la solution
    if proposition == cible:
        print("Bravo !")
        break
    elif proposition < cible:
        print(f"Trop petit !")
    elif proposition > cible:
        print("Trop grand !")
    else:
        print(f"le nombre {proposition} n'est pas entre {min} et {max}...")
print(f"Trouvé en {coups} coups.")
```

## 8 - Exercice : des étoiles (avec fonction)

Reprendre [l'exercice sur les étoiles](#exercice-des-etoiles), mais en l'intégrant dans une fonction `affiche_etoiles` qui prend en paramètres le nombre d'étoiles.

```python
def affiche_etoiles(nb_etoiles):
    for star in range(nb_etoiles):
        print("*" * star)

affiche_etoiles(6)

```

## 9 - Exercice : `print` ou `return` ?

### Version 1

Dans un programme principal, on a écrit la commande suivante : `print(function1(5))`.

Écrire la fonction `function1` de telle sorte que l'exécution de la commande précédente affiche comme résultat **6** dans l'interpréteur Python.

### Version 2

Dans un programme principal, on a écrit la commande suivante : `function2(5)`.

Écrire la fonction `function2` de telle sorte que l’exécution de la commande précédente affiche comme résultat **6** dans l’interpréteur Python.

```python
def function1(nb):
    return(6)

def function2(nb):
    print(function1(nb))
    
print(function1(5))
function2(5)
```

## 10 - Exercice : fonction du maximum

Ecrire une fonction `mon_maximum` qui prend en entrée une liste de valeurs et qui renvoie le maximum ainsi que son indice dans la liste.

```python
def mon_maximum(lst):
    max = -1
    indice = -1
    for i, l in enumerate(lst):
        if l > max:
            max = l
            indice = i
    return [max, indice]

liste = [1,2,3,4,5,6]

result = mon_maximum(liste)
print(result)

liste = liste[::-1]
result = mon_maximum(liste)
print(result)

liste = [3,2,1,6,5,6]
result = mon_maximum(liste)
print(result)
```

<!-- #region -->
## 11 - Exercice : que fait ce programme (1) ?

**Sans écrire** ce programme indiquez ce que produit le programme suivant à l'écran :

```python
def compute1(a, b):
    add1 = a + b
    return add1

def compute2(a, b):
    add2 = a + b

res1 = compute1(4, 5)
print(res1)

res2 = compute2(5, 6)
print(res2)

print(add2)
```
<!-- #endregion -->


    9
    
    Une erreur pour `print(add2) qui n'existe que dans le scope de la fonction `compute2`



## 12 - Exercice : la balance

Ecrire un programme qui en fonction du poids d'un coli, nous donne le prix de l'envoi.

- Ecrire une fonction `lit_poids` qui renvoie le poids du coli (dans notre cas on simulera la pesée en demandant le poids à l'utilisateur).
- Ecrire une fonction `donne_prix` qui renvoie le prix du coli en fonction de son poids :
  - poids inférieur à 100 g : 2 €
  - poids compris entre 100 et 500 g : 5 €
  - poids compris entre 500 et 1000 g : 10 €
  - poids compris entre 1000 et 30000 g : 30 €

- Au-delà de 30 kg, on indiquera une erreur à l'utilisateur. Ce n'est pas la fonction `donne_prix` qui effectuera l'affichage de l'erreur, mais le programme principal.

```python
def lit_poids():
    p = input("Quel est le poids du coli (en grammes) ?")
    if not p.isnumeric():
        print(str(p) + " n'est pas un nombre")
        p = 0
    else:
        p = int(p)
    return p

def donne_prix(masse):
    p = 0
    if masse <= 0:
        p = 0
    elif masse < 100:
        p = 2
    elif masse < 500:
        p = 5
    elif masse < 1000:
        p = 10
    elif masse <= 30000:
        p = 30
    else:
        p = -1            
    return p

saisie = lit_poids()
prix = donne_prix(saisie)

if prix <= 0:
    print(f"Erreur : {saisie} n'est pas compris entre 1g et 3Kg !")
else:
    print(f"Prix à payer : {prix} €.")
```

## 13 - Exercice : le palindrome

Le palindrome est une figure de style désignant un texte ou un mot dont l'ordre des lettres reste le même qu'on le lise de gauche à droite ou de droite à gauche (plus d'informations sur [Wikipédia](https://fr.wikipedia.org/wiki/Palindrome)). Exemples de mots : "ici", "kayak", "Laval", ...

Ecrire une fonction `est_palindrome` qui prend en paramètre une chaîne de caractères et qui renvoie `True` ou `False`.

- Faire un jeu de tests dans le programme principal avec une liste de mots.
- Penser à ignorer les majuscules / minuscules.

```python
def est_palindrome(mot):
    '''
    >>> "Palindrome"
    False
    >>> "kayak"
    True
    >>> "Laval"
    True
    '''
    endroit = str(mot).lower()
    envers = endroit[::-1]
    return endroit == envers

tests = ["Palindrome", "ici", "là", "12345", "kayak", "12321", "Laval", 12345, 12321]
for m in tests:
    print(f"{m} : {est_palindrome(m)}")


```

## 14 - Exercice : tri de mots

Soit la chaîne de cararactères contenant les mots suivants : "python physique maths anglais".

Ecrire une fonction `tri_mots` qui prend en paramètre une chaîne contenant des mots dans un ordre quelconque et qui retourne une chaîne avec des mots triés par ordre alphabétique.

```python
tests = "python physique maths anglais"

def tri_mots(chaine):
    '''
    >>> "python physique maths anglais"
    ['anglais', 'maths', 'physique', 'python']
    '''
    liste = []
    nb_mots = chaine.count(" ")
    #print(nb_mots)
    # indices de début et fin de chaque chaîne à extraire
    i_deb = 0
    i_fin = len(chaine)
    
    for indice in range(nb_mots):
    #    while i_deb < i_fin :
        # indices de début et fin de la chaîne à extraire
        min = i_deb
        max = chaine.find(" ", min)
        #print(f"[{min}:{max}]")
        liste.append(str(chaine[min : max]))
        # la chaine suivante commence après le prochain espace
        i_deb = max + 1
    # On ajoute le dernier mot (qui ne fini pas par un espace)
    liste.append(chaine[i_deb:i_fin])
    
    # On trie la liste par ordre alphabéthique
    liste.sort()
    
    return liste


print(tri_mots(tests))
```

<!-- #region -->
## 15 - Introduction aux tests unitaires : l'instruction `assert`

Un des principaux problèmes de la programmation informatique est la détection de dysfonctionnements (bugs). Pour pallier à cela, on peut écrire des tests qui "garantissent" que le programme fonctionne conformément à nos attentes et qu'il fonctionne toujours même après si des modifications ont été apportées (par exemple des améliorations).

Pour effectuer ces vérifications, on peut insérer des `print`.
Cependant cela requiert que le programmeur vérifie à l'écran ce qui se passe, ce qui n'est ni commode ni très fiable.

Une alternative (rudimentaire) est d'utiliser l'instruction `assert <condition_booléenne>`.
Si la condition boolénne est fausse, le programme s'interrompera en provoquant une erreur.

Exemple :
```python
a, b, c = True, False, True
assert a  # Ok
assert b  # Erreur et interruption du programme
assert c  # Jamais exécutée car le programme a été interrompu
```

Autre exemple :
```python
mot = "bonjour"
assert len(mot) == 7  # Ok
```
<!-- #endregion -->

## 16 - Exercice : assert avec le palindrome

Reprendre [l'exercice sur le palindrome](#exercice-le-palindrome) et dans le programme principal, utiliser l'instruction `assert` pour valider le bon résultat de la fonction `est_palindrome`.

- Faire une version avec des listes
- Faire une version avec des dictionnaires

```python
def est_palindrome(mot):
    '''
    >>> "Palindrome"
    False
    >>> "kayak"
    True
    >>> "Laval"
    True
    '''
    endroit = str(mot).lower()
    envers = endroit[::-1]
    return endroit == envers

'''
Avec une liste
''' 
tests = ["Palindrome", "ici", "là", "12345", "kayak", "12321", "Laval", 12345, 12321]
verif = [False, True, False, False, True, True, True, False, True]
# Test cassant l'assertion (kayak)
#verif = [False, True, False, False, False, True, True, False, True]

for indice, m in enumerate(tests):
    pal = est_palindrome(m)
    print(f"{m} : {pal}")
    assert verif[indice] == pal

'''
Avec un dictionnaire
'''
dico = {
    'Palindrome': False,
    'ici': True,
    'là': False,
    '12345': False,
    'kayak': True,
    '12321': True,
    'Laval': True,
    12345: False,
    12321: True,
}
# Test cassant l'assertion (kayak)
dico = {'Palindrome': False, 'ici': True, 'là': False, '12345': False, 'kayak': False, '12321': True, 'Laval': True, 12345: False, 12321: True}

for mot, verif in dico.items():
    pal = est_palindrome(mot)
    print(f"{mot} : {pal}")
    assert verif == pal, f"Erreur : '{mot}' : {verif} != {pal}"

```
