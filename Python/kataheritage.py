# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent,md
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Kata POO avancé
#
# Voici des exercices pour aller plus loin dans la programmation orientée objet.

# %% [markdown]
# ## La classe Animal
#
# Créez une classe Animal, qui a pour attribut espèce, initialisé dans le constructeur à partir d'un paramétre. Cet attribut doit être privé.
#
# Ajoutez une méthode get_espece() qui retourne la valeur de l'attribut espèce. Elle doit être privée. Ajoutez une propriété qui retourne la valeur de l'attribut espèce.
#
# Ajoutez une méthode crier, qui prend en paramétre un chaine, et qui retourn ce paramétre répété 3 fois (par exemple : paramétre = ha, retour = ha ha ha )
#

# %%
class Animal:
    def __init__(self, espece):
        self.__espece = espece

    def get_espece(self):
        """Valeur de l'attribut espèce
        :returns: espece

        """
        return self.__espece

    def crier(self, cri: str) -> str:
        """Retourne 3 fois le cri

        :cri: string
        :returns: string

        """
        return " ".join([cri, cri, cri])

# %% [markdown]
# ## La classe chien
#
# Créez une classe Chien qui hérite de la classe Animal. Le constructeur initialise un nom à partir d'un paramétre et initialise l'espèce, valeur "chien", en faisant appel au constructeur de la classe Animal.
#
# Ajoutez la méthode aboyer() qui retourne Wouaf Wouaf Wouaf, en faisant appel à la méthode parente crier()

# %%
class Chien(Animal):
    def __init__(self, nom: str):
        super().__init__("chien")
        self.nom = nom

    def aboyer(self) -> str:
        """Aboye

        :returns: str

        """
        return self.crier("Wouaf")

# %% [markdown]
# ## Une instance de Chien
#
# Ecrivez le code principal qui créée une instance de Chien, ayant pour nom 'Médor', qui affiche son espèce dans la console, ainsi que ses aboyements.

# %%

medor = Chien("Médor")

print(medor.get_espece())
print(medor.aboyer())

# %% [markdown]
# ## Une classe Doberman
#
# Créez une classe Doberman qui hérite de la classe Chien. Comme pour la classe parente, vous devez initialiser un attribut nom et un attribut espece. Initialisez aussi un attribut race (ici, doberman).
#
# Ecrivez une méthode decrire() qui retourne l'espèce, le nom et la race. Ecrire une méthode qui fait aboyer le doberman ( qui fait 3 fois "WOUAF")

# %%
class Doberman(Chien):
    def __init__(self, nom):
        super().__init__(nom)
        self.race = "Doberman"

    def decrire(self) -> str:
        """Return espece, nom et race

        :returns: str

        """
        return(f"{self.get_espece()} {self.nom} {self.race}")

    def aboyer(self) -> str:
        """Aboye

        :returns: str

        """
        return self.crier("WOUAF")

# %% [markdown]
# ## Une instance de Doberman
#
# Dans votre code principal, créez une instance de Doberman, avec pour nom "Droopy". Affichez dans la console sa description et ses aboyements.

# %%

droopy = Doberman("Droopy")
print(droopy.decrire())
print(droopy.aboyer())

# %% [markdown]
# ## Une classe Ornithorynque
#
# En vous inspirant de la classe Chien, créez une classe Ornithorynque qui hérite d'Animal.

# %%
class Ornithorynque(Animal):
    def __init__(self, nom: str):
        super().__init__("ornithorynque")
        self.nom = nom

    def crier(self) -> str:
        """Crie

        :returns: str

        """
        return "L'Ornithorynque ne crie pas."

# %% [markdown]
# ## Un petit zoo
#
# Dans le code principal, créez une collection d'objet, qui contient une instance de Chien, une instance de Doberman et une d'Onithorynque. Faite une boucle pour afficher les espèces de tous ces animaux.

# %%

animaux = [medor, droopy, Ornithorynque("Ornicar")]

for animal in animaux :
    print(animal.get_espece())

# %% [markdown]
# ## Pour aller plus loin
#
# Modifiez la classe Animal, pour que espèce deviennent une propriété en lecture seule.
#
# Ajoutez sur la classe Animal, une variable de classe, qui s'incrémente à chaque animal instancié.
#
# Créez une classe Zoo qui contient une collection d'objets de type Animal. Cette classe contient une méthode qui affiche toute les espèces du Zoo et une méthode qui affiche le nombre d'animal dans le Zoo.
#
# Vous pouvez aussi déclarer Animal comme une classe abstraite : [classe abstraite en Python.](https://pythonforge.com/classes-abstraites-en-python/)

# %%

class Animal:
    nb = 0
    def __init__(self, espece):
        self.__espece = espece
        nb += 1

    def get_espece(self):
        """Valeur de l'attribut espèce
        :returns: espece

        """
        return self.__espece

    def crier(self, cri: str) -> str:
        """Retourne 3 fois le cri

        :cri: string
        :returns: string

        """
        return " ".join([cri, cri, cri])

class Zoo:
    def __init__(self):
        self.animaux = []

    def get_espece(self):
        """Valeur de l'attribut espèce
        :returns: espece

        """
        esp = list()
        for animal in self.animaux :
            esp.append(animal.get_espece())
        return set(esp)

    def get_nb_animaux(self) -> int:
        return len(self.animaux)

    @property
    def nb(self) ->int:
        return self.get_nb_animaux()

zoo = Zoo()
zoo.animaux = animaux

print(zoo.get_espece())
print(zoo.get_nb_animaux())
print(zoo.nb)

