# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Arbres décisionnels
#
# Apprentissage supervisé - Regression, DecisionTreeRegressor
#
# ## Préparation des données
#
# ### Téléchargement de données
# Téléchargez le jeu de données housing.csv.
# Placez le dans le même répertoire de votre fichier (Python ou Notebook).
#

# %% [markdown]
# ### Information sur les données
# 1. Créez un code qui lit le fichier "housing.csv"
# et affiche ses premières lignes.
# Pour ce faire, utilisez les fonctions "read_csv" et "head" de la bibliothèque pandas.
#

# %%
import pandas as pd

df = pd.read_csv("housing.csv")

df.head()

# %% [markdown]
# Sachant que la valeur cible est "median_house_value", traitons-nous un problème de classification ou de régression ?

# %%
df.median_house_value.dtype
# -> Régression

# %% [markdown]
# 2. Créez un code qui affiche le nombre de lignes et de colonnes des données, le type des attributs et le nombre de valeurs non nulles.
#

# %%
df.info()

# %% [markdown]
# Quelle remarque sur l’attribut "total_bedrooms" par rapport aux autres attributs ?
#

# %% [markdown]
#     C'est une colonne qui contient moins de valeurs que les autres.

# %%
df.total_bedrooms.isnull().sum()

# %% [markdown]
#
# 3. A travers la question précédente, vous avez du remarquez que le type dans valeurs utilisées dans l’attribut "ocean_proximity" est un objet (forcément un texte vu qu’on manipule un fichier CSV).
# Il est intéressant de connaître ses valeurs.
# Pour cette finalité, créez un code qui affiche l’occurrence des valeurs utilisées dans cet attribut.

# %%
df.ocean_proximity.value_counts()

# %% [markdown]
#
# 4. Créez un code qui affiche des statistiques sur les attributs de ton jeu de données.

# %%
df.describe()

# %% [markdown]
#
# 5. Créez un code qui affiche les histogrammes des différents attributs.
# Le nombre de "bins" à saisir est 50 et la taille de chaque histogramme "figsize=(20,15)".

# %%
df.hist(bins=50, figsize=(20, 15))

# %% [markdown]
#
# ### Répartition des données
#
# 1. Créez un code qui partitionne les données en base d’apprentissage et base de test. Optez pour 80% pour l’apprentissage et 20% pour le test.

# %%
from sklearn.model_selection import train_test_split

y = df.median_house_value
X = df.drop("median_house_value", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 20/100, random_state = 42)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

# %% [markdown]
#
# 2. Affichez l’en-tête de la base de test

# %%
X_test.head()

# %% [markdown]
# Nous nous intéresserons par la suite uniquement à la base d’apprentissage.
# Pour cette raison, le terme données fera référence à la base d’apprentissage.

# %% [markdown]
# ### Découverte et visualisation des données
# L’information géographique (latitude et longitude) existe dans la base de données, il est intéressant de créer des graphes illustrant une visualisation géographique des données.

# %% [markdown]
# 1. Créez un code qui affiche en abscisse la longitude et en ordonnée la latitude.
# Optez pour le type scatter dans la fonction plot pour l’affichage et une valeur d’alpha (c’est un paramètre qui joue sur la transparence de la courbe) de 0.1 pour un affichage plus clair.

# %%
df.plot.scatter(x='longitude',
                y='latitude',
                alpha=0.1,
                c='DarkBlue')

# %% [markdown]
# 2. Créez un code qui permet d’avoir une idée sur le lien entre la position géographique et le prix des maisons (target).Optez pour une valeur égale à False de "sharex".

# %%
df[['longitude', 'latitude', ]].corrwith(df['median_house_value'])

# %%
df.plot.scatter(x='longitude',
                y='latitude',
                c='median_house_value',
                alpha=0.1,
                sharex=False,
                title='California',
                cmap='viridis')
                #cmap='Accent')


# %% [markdown]
# 3. Modifiez le graphe de la question précédente pour savoir la raison du prix élevé de quelques maisons.
#
# Pour ce faire :
# - Téléchargez l’image de la californie
# - Utilisez la fonction imread du sous-module image du module matplotlib
# - Utilisez la fonction imshow du sous-module pyplot du module matplotlib

# %%
import matplotlib.pyplot as plt 

img_array=plt.imread("california.png")[50:300,30:300]
plt.imshow(img_array)
plt.title('Californication')
plt.axis('off')
plt.show()

# %%
df.plot.scatter(x='longitude',
                y='latitude',
                c='median_house_value',
                alpha=0.1,
                sharex=False,
                title='California',
                cmap='viridis')
                #cmap='Accent')

# %%
