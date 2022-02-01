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

# TP sur les dictionnaires et les sets

## TP : Magasin en ligne

Dans cet exercice, nous nous familiarisons avec les manipulations de dictionnaires sur une thématique de magasin en ligne.
«Chez Geek and sons tout ce qui est inutile peut s'acheter, et tout ce qui peut s’acheter est un peu trop cher.»

La base de prix des produits de Geek and sons est représentée en Python par un dictionnaire avec :

- les noms de produits, de type `str`, comme clés.
- les prix des produits, de type `float`, comme valeurs associées.

**Attention : bien respecter l'ordre de présentation du code :**

1. Les imports
2. Les fonctions
3. Le programme principal

N'écrire aucun code entre les fonctions !



### Question 1
Donner une expression Python pour construire la base des produits correspondant à la
table suivante :
    
```
| Nom du produit     | Prix TTC |
| Sabre Laser        | 229      |
| Mitendo DX         | 127.30   |
| Coussin Linux      |  74.50   |
| Slip Goldorak      |  29.90   |
| Station Nextpresso | 184.60   |
```

```python tags=["remove-cell"]
#produits = [
#{ 'Nom du produit': 'Sabre Laser',        'Prix TTC': 229 },
#{ 'Nom du produit': 'Mitendo DX',         'Prix TTC': 127.30 },
#{ 'Nom du produit': 'Coussin Linux',      'Prix TTC':  74.50 },
#{ 'Nom du produit': 'Slip Goldorak',      'Prix TTC':  29.90 },
#{ 'Nom du produit': 'Station Nextpresso', 'Prix TTC': 184.60 }
#]

produits = {
    'Sabre Laser': 229,
    'Mitendo DX': 127.30,
    'Coussin Linux':  74.50,
    'Slip Goldorak':  29.90,
    'Station Nextpresso': 184.60
}

print(produits)
print(produits['Coussin Linux'])
```

<!-- #region -->
### Question 2
Écrire la fonction `disponibilite` qui étant donnés un nom de produit
et une base de produits, retourne `True` si le produit est présent dans la base, ou `False` sinon.

```python
def disponibilite(nom_prod, base_prod):
    ...
```
<!-- #endregion -->

```python
def disponibilite(nom_prod, base_prod):
    return nom_prod in base_prod
    ## en interrogant la clé
    #return base_prod[nom_prod] != none
    ## en parcourant toutes les clés
    #for prod in base_prod.keys():
    #    if prod == nom_prod:
    #        return True
    #return False

inventaire = {
    'Sabre Laser': 0,
    'Mitendo DX': 5,
    'Coussin Linux':  42,
    'Slip Goldorak':  1,
    'Station Nextpresso': 123
}


print(disponibilite('Coussin Linux', inventaire))
print(disponibilite('Sabre Laser', inventaire))
print(disponibilite('Un truc indisponnible', inventaire))

assert disponibilite('toto', inventaire) == False
assert disponibilite('Coussin Linux', inventaire) == True
```

<!-- #region -->
### Question 3
Écrire la fonction `prix_moyen` qui, étant donnée une base de produits (contenant
au moins un produit), retourne le prix moyen des produits disponibles.

```python
def prix_moyen(base_prod):
    ...
```
<!-- #endregion -->

```python
def prix_moyen(base_prod) -> float:
    '''Somme des prix / nombre de prix'''
    total = 0
    nb_produits = 0
    for produit in base_prod:
        #print(produit)
        total += produits[produit]
        nb_produits += 1
    return total / nb_produits

def prix_moyen2(base_prod) -> float:
    return sum(base_prod.values()) / len(base_prod.keys())

print(prix_moyen(produits))

print(prix_moyen2(produits))

```

<!-- #region -->
### Question 4
Écrire la fonction `fourchette_prix` qui, étant donnés un prix minimum
mini, un prix maximum maxi et une base de produits, retourne l'ensemble des noms de produits
disponibles dans cette fourchette de prix.

```python
def fourchette_prix(prix_min, prix_max, base_prod):
    ...
```
<!-- #endregion -->

```python
def fourchette_prix(prix_min, prix_max, base_prod):
    produits = []
    for produit in base_prod:
        pp = base_prod[produit]
        if prix_min <= pp and prix_max >= pp:
            produits.append(produit)
    return produits

pmin = 5
pmax = 100
print(fourchette_prix(pmin, pmax, produits))
print(produits)
assert fourchette_prix(20, 75, produits) == ['Coussin Linux', 'Slip Goldorak']
assert fourchette_prix(250, 750, produits) == []
```

### Question 5
Le panier est un concept omniprésent dans les sites marchands, Geeks and sons n’échappe pas à la règle. En Python, le panier du client sera représenté par un dictionnaire, avec :

- les noms de produits comme clés.
- une quantité d'achat comme valeurs associées.

Donner une expression Python correspondant à l'achat de 3 sabres lasers, de 2 coussins Linux
et de 1 slip Goldorak.

```python
panier = {
    "Sabre Laser" : 3,
    "Coussin Linux": 2,
    "Slip Goldorak": 1
}
```

<!-- #region -->
### Question 6
Écrire la fonction `tous_disponibles` qui, étant donnés un panier d'achat et une base de produits, retourne `True` si tous les produits demandés sont disponibles, ou `False` sinon.

```python
def tous_disponibles(panier_achat, base_prod):
    ...
```
<!-- #endregion -->

```python
def tous_disponibles(panier_achat, base_prod):
    rsp = True
    for achat in panier_achat:
        if not disponibilite(achat, base_prod):
            rsp = False
            break
    return rsp

print(tous_disponibles(panier, produits))
assert tous_disponibles(panier, produits) == True

test_panier_faux = {
    "Sabre Laser" : 3,
    "Coussin Linux": 0,
    "Un truc qui n'existe pas": 1
}
print(tous_disponibles(test_panier_faux, produits))
assert tous_disponibles(test_panier_faux, produits) == False

```

<!-- #region -->
### Question 7
Écrire la fonction `prix_achats` qui, étant donnés un panier d'achat et une base de produits, retourne le prix total correspondant.

- Faire une version qui suppose que tous les articles du panier sont disponibles dans la base des produits.
- Proposer une version qui renvoie une erreur si l'article du panier ne peut être trouvé dans la base.

```python
def prix_achats(panier_achat, base_prod):
    ...
```
<!-- #endregion -->

```python
def prix_achats(panier_achat, base_prod):
    total = 0
    for achat, nombre in panier_achat.items():
        if tous_disponibles(panier_achat, base_prod):
            total += produits[achat]*nombre
        else:
            total = [-1, f"Article [{ achat }] non disponnible"]
            break
    return total

print(prix_achats(panier, produits))
print(panier)
print(produits)
assert prix_achats(panier, produits) == 3*229 + 2*74.5 + 29.9

print(prix_achats(test_panier_faux, produits))
```

## TP : recettes de cuisine
Dans cet exercice, on s'intéresse à la définition de fonctions permettant de manipuler un livre
de recettes de cuisine. Comme tout bon livre de recettes qui se respecte, chaque recette décrit
notamment l'ensemble des ingrédients qui la composent. À titre d’exemple, un livre de
recettes de desserts pourrait contenir les informations suivantes :

```
|--------------------|----------------------------------------|
| Recette            | Ingrédients                            |
|--------------------|-----------------------------------------
| Gâteau au chocolat | chocolat, oeufs, farine, sucre, beurre |
| Gâteau au yaourt   | yaourt, oeufs, farine, sucre           |
| Crêpes             | oeufs, farine, lait                    |
| Quatre-quarts      | oeufs, farine, sucre, beurre           |
| Kouign Amann       | farine, sucre, beurre                  |
```

Un livre de recettes est donc représenté en Python par un dictionnaire avec :

- les noms des recettes, de type `str`, comme clés.
- l'ensemble des ingrédients, de type `set` (chaque ingrédient du `set` étant un `str`).

<!-- #region -->
### Présentation des sets

Inspiration : https://python.sdv.univ-paris-diderot.fr/13_dictionnaires_tuples_sets/

Les variables de type `set` représentent un autre type d'objet séquentiel qui peut se révéler très pratique. Ils ont la particularité d'être **non modifiables**, **non ordonnés** et de ne contenir que des éléments ont la **valeur est unique**. Pour créer un nouveau set on peut utiliser les accolades :

```python
>>> s = {1, 2, 3, 3}
>>> s
{1, 2, 3}
>>> type(s)
<class 'set'>
```

Notez que :

- La répétition du 3 dans la définition du set en ligne 1 donne au final un seul 3 car chaque élément ne peut être présent qu'une seule fois. 

- Les set et et les dictionnaires utilisent tous les deux des accolades. Cependant, le set sera défini seulement par des valeurs comme `{val1, val2, ...}` alors que le dictionnaire aura toujours des couples clé/valeur `{clé1: val1, clé2: val2, ...}`.

```python
s1 = {1, 2, 3}
>>> type(s1)
<class 'set'>
d1 = {'a1': 1, 'a2': 2}
>>> type(d1)
<class 'dict'>
```

Pour initialiser un set vide, on ne peut pas utiliser `{}` car il y a confusion avec les dictionnaires. Ainsi on utilisera simplement la fonction `set()`.

```python
s = set()
```

De plus la fonction `set()` peut prendre en argument n'importe quel objet itérable (c'est à dire qu'on peut parcourir) et le convertit en set (opération de casting), par exemple :

```python
>>> set([1, 2, 4, 1])  # Conversion d'une liste en set
{1, 2, 4}
>>> set((2, 2, 2, 1))  # Conversion d'un tuple en set
{1, 2}
>>> set(range(5))
{0, 1, 2, 3, 4}
>>> set({"clé1": 1, "clé2": 2})
{'clé1', 'clé2'}
>>> set(["ti", "to", "to"])
{'ti', 'to'}
>>> set("Maître corbeau sur un arbre perché")
{'h', 'u', 'o', 'b', ' ', 'M', 'a', 'p', 'n', 'e', 'é', 'c', 'î', 's', 't', 'r'}
```

Nous avons dit plus haut que les sets ne sont pas ordonnés :

```python
>>> s1 = {1, 2, 3}
>>> s2 = {2, 1, 3}
>>> s1 == s2
True
```

Par conséquent, il est impossible de récupérer un élément par sa position. Il est également impossible de modifier un de ses éléments.

```python
>>> s = set([1, 2, 4, 1])
>>> s[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
```

Par contre, les sets sont itérables :

```python
>>> for elt in s:
...     print(elt)
...
1
2
4
```

Si on ne peut pas modifier le contenu directement, on peut ajouter ou supprimer des éléments :

```python
>>> s = {1, 2, 3}
>>> s.remove(1)
>>> s
{2, 3}
>>> s.add(1)
>>> s
{1, 2, 3}
```

Les variables de type `set` sont très utiles pour rechercher les éléments uniques d'une suite d'éléments. Cela revient à éliminer tous les doublons. Par exemple :

```python
>>> lst = [1, 2, 2, 3, 3]
>>> s = set(lst)
>>> s
{1, 2, 3}
>>> lst2 = list(s)
>>> lst2
[1, 2, 3]
```
<!-- #endregion -->

### Question 1
Donner une représentation en Python de la base des recettes.

```python
# | Recette | Ingrédients |
livre_recettes = {
	"Gâteau au chocolat": {"chocolat", "oeufs", "farine", "sucre", "beurre"},
	"Gâteau au yaourt":   {"yaourt", "oeufs", "farine", "sucre"},
	"Crêpes":             {"oeufs", "farine", "lait"},
	"Quatre-quarts":      {"oeufs", "farine", "sucre", "beurre"},
	"Kouign Amann":       {"farine", "sucre", "beurre"},
}

print(livre_recettes)
```

### Question 2
Écrire la fonction `nb_ingredients` qui, étant donné un livre de recettes et
le nom d'une recette contenue dans le livre, renvoie le nombre d'ingrédients nécessaires à la
recette.

```python
def nb_ingredients(livre, recette):
    total = 0
#    ingredients = livre[recette] ## .get()
    ingredients = livre.get(recette)
    if ingredients is not None :
        total = len(ingredients)
    return total


print(nb_ingredients(livre_recettes, 'Crêpes'))
print(nb_ingredients(livre_recettes, 'Sabre Laser'))

assert nb_ingredients(livre_recettes, 'Crêpes') == 3
assert nb_ingredients(livre_recettes, 'Tiramisu') == 0

for recette in livre_recettes:
    print(recette, ": ", nb_ingredients(livre_recettes, recette))
```

### Question 3
Écrire la fonction `recette_avec` qui, étant donnés un livre de recettes et le
nom d'un ingrédient, renvoie l'ensemble des recettes qui utilisent cet ingrédient.

```python
def recette_avec(livre, ingredient):
    recettes = set()
    for recette, ingredients in livre.items():
        if ingredient in ingredients:
            recettes.add(recette)
    return recettes

recettes_avec = recette_avec

print(recette_avec(livre_recettes, "oeufs"))
print(recette_avec(livre_recettes, "chocolat"))
print(recette_avec(livre_recettes, "Sabre Laser"))
#print(livre_recettes)
assert recette_avec(livre_recettes, 'oeufs') == {'Gâteau au chocolat', 'Gâteau au yaourt',
                                                 'Crêpes', 'Quatre-quarts'}
assert recette_avec(livre_recettes, 'café') == set()

```

### Question 4
Écrire la fonction `tous_ingredients` qui, étant donné un livre de recettes renvoie l'ensemble des ingrédients (sans doublons).

```python
def tous_ingredients(livre):
    rst = set()
    #for recette, ingredients in livre.items():
    #    for ingredient in livre[recette]:
    #        rst.add(ingredient)
    for ingredients in livre.values():
        for ingredient in ingredients:
            rst.add(ingredient)
    return rst

print(tous_ingredients(livre_recettes))
assert tous_ingredients(livre_recettes) == {'farine', 'sucre', 'beurre', 'yaourt', 'lait', 'chocolat', 'oeufs'}
assert tous_ingredients(livre_recettes) == {'beurre', 'farine', 'sucre', 'chocolat', 'yaourt', 'oeufs'}
```

<!-- #region -->
### Question 5
Tout livre de recettes contient une table des ingrédients (index) permettant d'associer à chaque ingrédient l'ensemble des recettes qui l'utilisent. On peut représenter en Python une telle table par un dictionnaire dans lequel une clé est un ingrédient et la valeur associée est l'ensemble des recettes qui l’utilisent.
Écrire la fonction `table_ingredients` qui, étant donné un livre de recettes, renvoie la table des ingrédients associée.

Exemple :
```python
{
    'chocolat': {'gâteau chocolat'},
    'oeufs': {'crêpes', 'gâteau chocolat', 'gâteau yaourt', 'quatre-quarts'},
    ...
}
```
<!-- #endregion -->

```python
def table_ingredients(livre):
    table = dict() # {}
    # Onrécupère la liste de tout les ingrédients du livre de recettes
    for ingredient in tous_ingredients(livre):
        #print("INGREDIENT : ", ingredient)
        # On récupère la liste des recettes contant l'ingrédient
        for recettes in recettes_avec(livre, ingredient):
            #print("RECETTES : ", recettes)
            recettes_ingredients = {recettes}
            # Si l'ingrédient n'est pas dans la table on l'ajoute
            if ingredient not in table:
                #print('Add -> ', ingredient)
                table[ingredient] = recettes_ingredients
            else:
                #print('Update ~> ', ingredient, table[ingredient])
                table[ingredient].update(recettes_ingredients)
    #print("---------")
    return table

def table_ingredients_cor(livre):
    table = {}
    for recette, ingredients in livre.items():
        for ingredient in ingredients:
            recettes_existantes = table.get(ingredient)
            if recettes_existantes is None:
                table[ingredient] = {recette}
            else:
                recettes_existantes.add(recette)
    return table

print(table_ingredients(livre_recettes))
print(table_ingredients_cor(livre_recettes))
```


### Question 6
Écrire la fonction `ingredient_principal` qui, étant donné un livre de recettes, renvoie le nom de l'ingrédient utilisé par le plus grand nombre de recettes.

```python
def ingredient_principal(livre):
    max = 0
    rsp = ""
    for ingredient, recettes in table_ingredients(livre).items():
        #print(ingredient, recettes)
        if max < len(recettes):
            max = len(recettes)
            rsp = ingredient
    return rsp

print(ingredient_principal(livre_recettes))
```

### Question 7
Certaines personnes sont allergiques à certains ingrédients. On aimerait donc pouvoir ne
conserver d'un livre de recettes que celles qui n'utilisent pas un ingrédient donné.

Écrire la fonction `recettes_sans` qui, étant donné un livre de recettes et un ingrédient, renvoie un nouveau livre de recettes ne contenant que des recettes n'utilisant pas l’ingrédient.

```python
def recettes_sans(livre, ingredient):
    rsp = dict(livre)
    allergenes = recettes_avec(livre, ingredient)
    for recette in livre:
        if recette in allergenes:
            rsp.pop(recette)
    return rsp

#print(recettes_sans(livre_recettes, 'chocolat'))
print(recettes_sans(livre_recettes, 'oeufs'))
#print(recettes_sans(livre_recettes, 'farine'))
```

## TP : Gestion de bibliothèque

Dans cet exercice, nous illustrons la manipulation des dictionnaires en travaillant sur une "base de données" de livres empruntables dans une bibliothèque.

La base permet de rechercher rapidement un livre à partir de son titre (clé du dictionnaire). On
obtient alors l'auteur du livre ainsi que le nombre d’exemplaire(s) empruntable(s) en stock.

Par exemple :

```python

```

L'auteur du livre *Notre-Dame de Paris* est *Victor Hugo* et il est disponible en *4* exemplaires.

**Question** : quel est le *type* de variable des valeurs des clés du dictionnaire ?


### Question 1

Écrire la fonction `auteurs` qui, étant donnée une base de livres, retourne l'ensemble des auteurs de cette base.

```python

```

```python

```

<!-- #region -->
### Question 2


Écrire la fonction `nb_exemplaires_total` qui, étant donnée une base de livres, retourne le nombre total d'exemplaires disponibles.
<!-- #endregion -->

```python

```

```python

```

### Question 3

Écrire la fonction `est_disponible` qui, étant donnée une base de livres, un titre et un auteur, indique si le livre est disponible (la fonction renverra `True` ou `False`. Si le livre et l'auteur correspondant n'existent pas, la fonction renverra `None`.

```python

```

### Question 4

Écrire la fonction `titres_empruntables` qui, étant donné unee base de livres, retourne l'ensemble des livres empruntables.

```python

```

### Question 5

Écrire la fonction `titres_auteur` qui, étant donnés un nom d'auteur et une base de livres, retourne l'ensemble des titres de livres écrits par cet auteur.

```python
liste = list([[1,2,3], [4,5,6],])
print(liste)

class maliste(list):
    def __str__(self):
        return "[1,2,3]"
        
lst = maliste([[1,2,3], [4,5,6],])

print(lst)

```

```python
class dog:
    def __str__(self):
        return "Waf !"
    
milord = dog()
print(milord)
```

```python

```

```python

```
