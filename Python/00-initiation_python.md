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

# Initiation Python

Ces exercices ont pour but de vous faire réfléchir sur des algo puis de les coder en Python afin de comprendre les logiques du développement.

Pour chaque exercice, on vous propose une cellule pour écrire du pseudo code en commentaire, puis du Python.

## Exercice 1 : Parcours de liste

Créez une liste contenant au moins 3 noms d'acteurs.
Puis afficher, un par un, les noms de ces acteurs et afficher le nombre d'éléments dans la liste.

```python
'''
Pour chaque acteur de la liste acteurs
    afficher acteur

afficher taille(acteurs)
'''
```

```python
acteurs = ["Alain", "Bruno", "Chantal", "Dominique"]

for acteur in acteurs:
    print(acteur)

print("Nombre d'acteurs : ", len(acteurs))
```

## Exercice 2 : Boucle for

Additionnez les 9 premiers chiffres (de 1 à 9).

```python
'''
total <- 0
Pour nombre allant de 1 à 9
    total <- total + nombre
afficher total
'''
```

```python
total = 0
for nb in range(1, 10):
    total += nb
print(total)
```

## Exercice 3 : Boucle while

Ecrivez un code qui demande la saisie d'une lettre tant que 'x' n'est pas saisie.

```python
'''
répéter
    saisir lettre
jusqu'à ce que lettre = 'x'
'''
```

```python
lettre =''
while lettre != 'x':
    lettre = input()
```

## Exercice 4 : Parcours de chaine

Ecrivez un code qui permet d'afficher la chaine "Je code en python" à raison d'une lettre par ligne.

```python
'''
chaine <- "Je code en Python"
Pour chaque lettre de chaine
    afficher lettre
'''
```

```python
chaine = "Je code en python"
for lettre in chaine:
    print(lettre)
```

## Exercice 5 : Fonction

En vous inspirant du code précédent, écrire une fonction qui permet d'afficher une chaine de caractères à raison d'une lettre par ligne.

```python
'''
fonction afficher_par_ligne(chaine)
    Pour chaque lettre de chaine
        afficher lettre

afficher_par_ligne("Je code en Python")
'''
```

```python
def afficher_par_ligne(chaine):
    for lettre in chaine:
        print(lettre)

afficher_par_ligne("Je code en python")
```
