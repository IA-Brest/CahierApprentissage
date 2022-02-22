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
# Valeurs continues -> Régression

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

train_set, test_set = train_test_split(df, test_size = 20/100, random_state = 42)

y = df.median_house_value
X = df.drop("median_house_value", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 20/100, random_state = 42)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

# %% [markdown]
#
# 2. Affichez l’en-tête de la base de test

# %%
test_set.head()

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
                label="Population",
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
                label="Population",
                cmap='gist_rainbow')
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

img_array=plt.imread("california.png")  #[0:300,0:300]
plt.imshow(img_array)
plt.title('Californication')
plt.axis('off')
plt.show()

# %%
img_array.shape
# (674, 594, 3) : Taille : 674*594 en 3 couleurs (RGB)

#plt.imshow(img_array[1,:,:])
#plt.imshow(img_array[:,1,:])
plt.imshow(img_array[:,:,1])

# %%
img_california=plt.imread("california.png")

plt.title('California')

plt.imshow(img_california, zorder=0, extent=[df.longitude.min(), df.longitude.max(), df.latitude.min(), df.latitude.max()])
aspect=img_california.shape[0]/float(img_california.shape[1])*((df.longitude.max() - df.longitude.min())/(df.latitude.max() - df.latitude.min()))
plt.gca().set_aspect(aspect)

plt.scatter(x=df.longitude,
            y=df.latitude,
            zorder=1,
            c=df.median_house_value,
            alpha=0.1,
            label="Population",
            cmap='gist_rainbow')
            #cmap='Accent')

plt.show()



# %% [markdown]
# 4. Une pratique très intéressante dans l’analyse de données est l’étude des corrélation entre les variables.
#
# Créez un code qui affiche, en valeur, la corrélation de l’attribut "median_house_value" avec les autres attributs.
#
# Qu’est ce que vous remarquez ?

# %%
df.corrwith(df.median_house_value)

# %%
# La valeur du bien est corrélé avec le revenu moyen de leur propriétaire

# %% [markdown]
# ## Nettoyage des données
# Avant d’intégrer les données dans un algorithme d’apprentissage automatique, il est indispensable de séparer le "features" et la valeur cible (target).
#
# 1. Créez un code permettant de créer deux variables :
#
#  - Une première contenant que les input. Utilisez la fonction drop du module pandas
#  - Une deuxième contenant que les labels. Utilisez la fonction copy du module pandas

# %%
inputs = train_set.drop("median_house_value", axis=1)

labels = train_set.median_house_value.copy()

inputs.head()
labels.head()

# %% [markdown]
#
# 2. Dans la question 8, vous avez dû remarquer que l’attribut "total_bedrooms" a des valeurs manquantes (NaN).
#
# Pour remédier à ceci, il existes trois options :
# - Supprimer les valeurs manquantes (NaN)
# - Supprimer l’attribut "total_bedrooms"
# - Remplacer les valeurs manquantes par une autre valeur (0, la moyenne, la médiane, ...)
# Nous optons pour cette méthode.
#
# Ecrivez un code qui remplace les valeurs manquantes par la médiane.

# %%
inputs.info()
inputs.total_bedrooms.isna().sum()

# %% [markdown]
# Utilisez les fonctions median et fillna du module Pandas.

# %%
# df[df.columns] = df[df.columns].apply(pd.to_numeric, errors='coerce')

inputs.total_bedrooms = inputs.total_bedrooms.fillna(inputs.total_bedrooms.median())  # works

# %% [markdown]
# Vérifiez avec la fonction "info" si le problème a été résolu.

# %%
inputs.info()
inputs.total_bedrooms.isna().sum()

# %% [markdown]
#
# 3. Les algorithmes d’apprentissage profond préfèrent travailler avec des données numériques.
# Ceci est valable pour tous les attributs sauf "ocean_proximity".
# Vérifiez ceci en affichant 10 de ces valeurs.

# %%
df.ocean_proximity.sample(frac=0.42)

# %% [markdown]
# Transformer les valeurs qualitatives en des valeurs numériques.

# %%
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(df.ocean_proximity)
list(le.classes_)

# %% [markdown]
#
# 4. Affichez les données pour vérifier le résultat.

# %%
inputs.ocean_proximity = le.transform(inputs.ocean_proximity)

inputs.ocean_proximity.head()

# %%
list(le.inverse_transform(inputs.ocean_proximity))

# %% [markdown]
# ## Sélection, apprentissage et évaluation du modèle
#
# 1. Créez un code permettant d’appliquer la régression linéaire sur les données d’apprentissage.

# %%

# %% [markdown]
#
# 2. Créez un code qui prédit les classes de la base d’apprentissage.
#
# Pour ce faire, utilisez la méthode predict de la classe LinearRegression en donnant comme argument les données d’apprentissage.

# %%

# %% [markdown]
# Ensuite, affichez les valeurs cible réelles et celles prédites.

# %%

# %% [markdown]
# 3. Calculez la mesure RMSE du modèle de la régression linéaire.

# %%

# %% [markdown]
# 4. Refaites les deux étapes précédentes avec le modèle DecisionTreeRegressor.

# %%

# %% [markdown]
# Calculez la mesure RMSE du modèle DecisionTreeRegressor qui existe dans le sous-module tree du module sklearn.

# %%

# %% [markdown]
# Pour plus d’informations sur les arbres de décision:
#
# http://cedric.cnam.fr/vertigo/cours/ml2/tpArbresDecision.html
#
# 5. Même si la valeur de RMSE de DecisionTreeRegressor est égale à 0, on ne peut pas conclure que ce modèle fonctionne parfaitement sur la base d’apprentissage.
#
# Pour s’assurer, on va répartir la base d’apprentissage en base d’apprentissage et en base de test en utilisant la méthode 10-fold cross-validation.
#
# Pour ce faire, utilisez la fonction cross_val_score du sousmodule model_selection du module sklearn.

# %%

# %% [markdown]
#
# Ensuite, affichez :
# - La valeur MSE de chaque fold

# %%

# %% [markdown]
# - La moyenne des MSE de tous les folds

# %%

# %% [markdown]
# - L’écart type de tous les folds

# %%

# %% [markdown]
#
# 6. Suivre les étapes de la question précédente sur le modèle de la régression linéaire.

# %%

# %% [markdown]
#
# Ensuite, comparez les résultats avec ceux du DecisionTreeRegressor.

# %%

# %% [markdown]
#
# Quel modèle présente un problème d’apprentissage ?

# %%

# %% [markdown]
#
# pourquoi ?

# %%

# %% [markdown]
# ## Fine-Tunning
#
# ### Grid Search
# Dans cette, partie nous allons chercher les paramètres du modèle de régression qui donnent les meilleurs résultats
#
# 1. Écrire un code qui :
# - Crée un objet de la classe RandomForestRegressor
#
# Pour plus d’informations sur RandomForestRegressor:
# https://medium.com/datadriveninvestor/random-forest-regression-9871bc9a25eb
#
# - Crée la variable suivante :
# param_grid = [′n_estimators′ : [3, 10, 30],′ max_ f eatures′ : [2, 4, 6, 8]]
#
# Cette variable contient un dictionnaire avec quelques valeurs de deux paramètres de la
# méthode RandomForestRegressor.
#
# Au total, 4x3=12 combinaisons vont être testées.

# %%

# %%
