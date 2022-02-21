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

# Kata POO, la suite

Voici de nouveaux exercice sur la POO pour apprendre à manipuler les objets.


## La classe acteur

Créez une classe acteur, elle doit avoir un constructeur qui initialise, à partir des paramétres, deux attributs : le nom et le prénom.

Puis, créez 3 objets : Chantal Lauby, Dominique Farougia et Alain Chabat.

```python

class Acteur:

  """Represente un acteur par son Nom et son  Prénom"""

  def __init__(self, nom, prenom):
    """Nom et Prénom de l'Acteur

    :nom: TODO
    :prenom: TODO

    """
    self._nom = nom
    self._prenom = prenom

  def __str__(self):
    return(f"{self._prenom} {self._nom}")
    
alain = Acteur("Chabat", "Alain")
bruno = Acteur("Carette", "Bruno")
chantal = Acteur("Lauby", "Chantal")
dominique = Acteur("Farougia", "Dominique")

print(alain, bruno, chantal, dominique, sep=', ')
```

## La classe film

Créez une classe Film et initialisez ses attributs titre et genre à partir des paramétres d'un constructeur. Créez un objet film, de titre "La Cité de la Peur" et de genre "Comédie". 

```python
class Film:

  """Represente un Film"""

  def __init__(self, titre, genre):
    """Titre et genre du film

    :titre: Titre du Film
    :genre: Genre du Film

    """
    self._titre = titre
    self._genre = genre

  def __str__(self):
    return(f"{self._titre} ({self._genre})")
    
film_culte = Film(titre="La Cité de la Peur", genre="Comédie")
print(film_culte)
```

## Une liste d'acteurs

Ajoutez dans votre code un liste python qui doit contenir les 3 objets acteurs créés précédement.

```python
acteurs = list([alain, chantal, dominique])
print(acteurs)
for a in acteurs:
    print(a)
```

## Une liste d'acteurs pour les films

Modifiez le constructeur de la classe Film pour pouvoir initialiser une liste d'acteurs à partir de celle que vous avez créez dans votre code. 

Ajoutez les 3 acteurs déjà créés au film "La Cité de la Peur".

```python
class Film:

  """Represente un Film"""

  def __init__(self, titre, genre, acteurs=list()):
    """Titre et genre du film

    :titre: Titre du Film
    :genre: Genre du Film
    :acteurs: Acteurs principaux

    """
    self._titre = titre
    self._genre = genre
    self._acteurs = acteurs

  def __str__(self):
    acteurs = ', '.join(str(acteur) for acteur in self._acteurs)
    return(f"{self._titre} ({self._genre}) : {acteurs}")
    
film_culte = Film(titre="La Cité de la Peur", genre="Comédie", acteurs=acteurs)
print(film_culte)
```

## Ajout d'un acteur

Ajoutez dans la classe Film une méthode qui permet d'ajouter un nouvelle acteur à la liste.

Ajoutez Gérard Darmon aux acteurs du film "La Cité de la Peur".

```python
class Film:

  """Represente un Film"""

  def __init__(self, titre, genre, acteurs=list()):
    """Titre et genre du film

    :titre: Titre du Film
    :genre: Genre du Film
    :acteurs: Acteurs principaux

    """
    self._titre = titre
    self._genre = genre
    self._acteurs = acteurs

  def add_acteur(self, acteur):
    """Ajouter un acteur

    :acteur: Acteur à ajouter
    :returns: Nothing if allright

    """
    self._acteurs.append(acteur)

  def __str__(self):
    d
    return(f"{self._titre} ({self._genre}) : {acteurs}")
    
film_culte = Film(titre="La Cité de la Peur", genre="Comédie", acteurs=acteurs)
film_culte.add_acteur(Acteur("Darmon", "Gérard"))
print(film_culte)
```

## Evolution de la classe Acteur

Ajoutez un attribut métier sur la classe Acteur. Il est initialisé, par défaut, à "acteur". Attention, un acteur peut avoir plusieurs métiers.

```python
class Acteur:

  """Represente un acteur par son Nom et son  Prénom"""

  def __init__(self, nom, prenom, metier="acteur"):
    """Nom et Prénom de l'Acteur

    :nom: TODO
    :prenom: TODO

    """
    self._nom = nom
    self._prenom = prenom
    self._metiers = list()
    self._metiers.append(metier)

  def __str__(self):
    metier = ', '.join(str(m) for m in self._metiers)
    return(f"{self._prenom} {self._nom} ({metier})")
    
alain = Acteur("Chabat", "Alain")
bruno = Acteur("Carette", "Bruno")
chantal = Acteur("Lauby", "Chantal")
dominique = Acteur("Farougia", "Dominique")

print(alain, bruno, chantal, dominique, sep=' / ')

```

## Changement de métier

Ajouter une méthode qui permet de modifier le métier d'un acteur à partir d'un attribut.

Dominique Farougia et Alain Chabat deviennent acteurs et réalisateurs. Chantal Lauby est aussi scénariste.

```python
class Acteur:

  """Represente un acteur par son Nom et son  Prénom"""

  def __init__(self, nom, prenom, metier="acteur"):
    """Nom et Prénom de l'Acteur

    :nom: TODO
    :prenom: TODO

    """
    self._nom = nom
    self._prenom = prenom
    self._metiers = list()
    self.add_metier(metier)

  def __str__(self):
    metier = ', '.join(str(m) for m in self._metiers)
    return(f"{self._prenom} {self._nom} ({metier})")

  def add_metier(self, metier):
    self._metiers.append(metier)
    
    
    
alain = Acteur("Chabat", "Alain")
alain.add_metier("réalisateur")
bruno = Acteur("Carette", "Bruno")
chantal = Acteur("Lauby", "Chanutal")
chantal.add_metier("sénariste")
dominique = Acteur("Farougia", "Dominique")
dominique.add_metier("réalisateur")

print(film_culte)

```

## Pour aller plus loin

Modifiez le constructeur de la classe Acteur pour générer tous les attributs à partir d'un liste passée en paramètre.

```python

```

## Un peu de documentation

Voici un nouveau lien vers un tuto sur la programmation orientée objet en Python : [Cours Pyton](https://courspython.com/classes-et-objets.html#la-notion-de-constructeur)

Suivez l'exemple jusqu'au chapitre *La notion de constructeur* inclus.
