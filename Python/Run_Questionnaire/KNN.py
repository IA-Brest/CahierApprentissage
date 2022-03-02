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
# Codez un script python qui permet de regrouper les DataSets de chacun en une seule DataSet.

# %%
import pandas as pd
import glob

df = pd.DataFrame()

for f in glob.glob("./Dataset/*.csv"):
    df_chunk = pd.read_csv(f)
    df = pd.concat([df, df_chunk], axis=0)
df.reset_index(inplace=True, drop=True)

df.shape

# %% [markdown]
# Appliquez les traitements nécessaires pour préparer la DataSet en utilisant Numpy et Pandas, (vous pouvez trouver un référentiel sur ressource).
#
# (présenter votre pipeline dans le compte rendu).
#
# NB. Le résultat de classification dépond essentiellement de la qualité du prétraitement.

# %%
df.columns.unique()

df.sample(10)

# %% [markdown]
# <strike>
# Pour les colones Q1 à Q10 :
# - Si la réponse est "a" "A" ou "1", remplacer par 1
# - Sinon Si la réponse est "b" "B" ou "2", remplacer par 2
# - Sinon Si la réponse est "c" "C" ou "3", remplacer par 3
# - Sinon, remplacer toutes les autres valeurs par NaN.
#
# Ne fonctionne pas, car les valeurs de Score et Interprétation ne sont pas calculées comme celà. Le problème vient de la saisie des données qui n'aurait pas dû autoriser de telles valeurs.
# </strike>
#
# Pour les colones Q1 à Q5 :
# - Si la réponse est "a", remplacer par 1
# - Sinon Si la réponse est "b", remplacer par 2
# - Sinon Si la réponse est "c", remplacer par 3
# - Sinon, remplacer toutes les autres valeurs par NaN.
#
# Pour les colones Q6 à Q10 :
# - Si la réponse est "1", remplacer par 1
# - Sinon Si la réponse est "2", remplacer par 2
# - Sinon Si la réponse est "3", remplacer par 3
# - Sinon, remplacer toutes les autres valeurs par NaN.
#

# %%
df_clean = df.copy()
df_clean.sample(10)

# %%
df_clean.isna().sum()

# %%
from numpy import nan as NaN

df_clean = df.copy()

for col in range(1, 6):
    col = str(f'Q{col}')
    df_clean[col] = df_clean[col].map({
        'a': 1,
        'b': 2,
        'c': 3,
        },
        na_action='ignore')

for col in range(6, 11):
    col = str(f'Q{col}')
    df_clean[col] = df_clean[col].map({'1': 1,
                                       '2': 2,
                                       '3': 3,
                                       },
                                      na_action='ignore')

df_clean.sample(10)

# %%
df_clean.isna().sum()

# %%
df_clean.fillna(0, inplace=True)

# %%
df_clean.isna().sum()

# %%
df_clean.sample(10)


# %% [markdown]
# ## Partie 2 : Développement et entraînement d’un modèle KNN
#
# La technique de classification KNN est considérée comme la technique la plus simple pour appliquer la classification supervisée, tout simplement, une nouvelle donnée de test sera classée comme la majorité de ses voisins (la distance la plus proche).
#
# À la suite de votre recherche sur le principe de KNN, nous développons notre modèle KNN.
#
# Pour cela :
#
# KNN From Scratch
#
# - Préparez une fonction permettant de calculer les 3 différentes distances : Euclidean, Manhattan et Minkowski, (def distance(metric=’ Euclidean’, **kargs)).

# %%
# Distance Amine :

def distance_amine(Data_1, Data_2, metric='euclidean', **kargs):

    if kargs.items():

        for key, value in kargs.items():
            if key == 'p':
                p = value
    else:
        p = 3

    if metric == 'euclidean':
        Dis = np.sqrt(np.sum((Data_1-Data_2)**2))
    elif metric == 'manhattan':
        Dis = np.abs(np.sum(Data_1-Data_2))
    elif metric == 'minkowski':
        Dis = (np.sum(np.abs(Data_1-Data_2))**p)**(1/p)
    return Dis


# %%
import numpy as np
from decimal import Decimal


# %%
def euclidean(a, b):
    """Return Euclidean distance from a to b

    :a: start point
    :b: end point
    :return: the Euclidean distance

    """
    if type(a) != np.array:
        a = np.array(a)
    if type(b) != np.array:
        b = np.array(b)
    return np.sqrt(np.sum(np.square(a - b)))


assert 0.0 == euclidean([0, 0, 0], [0, 0, 0]), "euclidean() origin point error"
assert 5.196152422706632 == euclidean(np.array((1, 2, 3)), np.array((4, 5, 6))), "eclidean() error"


# %%
def manhattan(a, b):
    """Return Manhattan distance from a to b

    :a: start point
    :b: end point
    :return: the Manhattan distance

    """
    return sum(abs(val1-val2) for val1, val2 in zip(a, b))


assert 0.0 == manhattan([0, 0, 0], [0, 0, 0]), "manhattan() origin point error"
assert 9 == manhattan([2, 4, 4, 6], [5, 5, 7, 8]), "manhattan() error"


# %%
def minkowski(a, b, p):
    """Return Minkowski distance from a to b

    :a: start point
    :b: end point
    :return: the Minkowski distance

    """
    if p == 1:
        return manhattan(a, b)
    elif p == 2:
        return euclidean(a, b)
    else:
        def p_root(value, root):
            root_value = 1 / float(root)
            return round(Decimal(value) ** Decimal(root_value), 3)
        # pass the p_root function to calculate
        # all the value of vector parallelly
        return float(p_root(sum(pow(abs(x - y), p) for x, y in zip(a, b)), p))


assert 0.0 == minkowski([0, 0, 0], [0, 0, 0], 1), "minkowski() origin error"
assert 0.0 == minkowski([0, 0, 0], [0, 0, 0], 2), "minkowski() origin error"
assert 0.0 == minkowski([0, 0, 0], [0, 0, 0], 3), "minkowski() origin error"

assert 5.196152422706632 == minkowski(np.array((1, 2, 3)), np.array((4, 5, 6)), 2), "minkowski(), p=2 error"
assert 9 == minkowski([2, 4, 4, 6], [5, 5, 7, 8], 1),  "minkowski(), p=1 error"
assert 3.503 == minkowski([0, 2, 3, 4], [2, 4, 3, 7], 3), "minkowski() error"


# %%
def distance(metric='Euclidean', **kargs) -> float:
    '''Return the distance between a and b

    :a: start point
    :b: end point
    :p: metric for Minkowski distance
    :metric: 'Euclidean', 'Manhattan' or 'Minkowski'
    :return: the distance
    '''
    if metric == 'Euclidean':
        return euclidean(kargs['a'], kargs['b'])
    elif metric == 'Manhattan':
        return manhattan(kargs['a'], kargs['b'])
    elif metric == 'Minkowski':
        return minkowski(kargs['a'], kargs['b'], kargs['p'])
    else:
        pass

# %%

# Test distance()
assert 0.0 == distance(a=[0, 0, 0], b=[0, 0, 0]), "distance() same point error"
assert 5.196152422706632 == distance(a=np.array((1, 2, 3)), b=np.array((4, 5, 6))), "no metric='' error"

assert 5.196152422706632 == distance(a=np.array((1, 2, 3)), b=np.array((4, 5, 6)), metric='Euclidean'), "metric='Euclidean' error"
assert 9 == distance(a=[2, 4, 4, 6], b=[5, 5, 7, 8], metric='Manhattan'),  "metric='Manhattan' error"

assert 5.196152422706632 == distance(a=np.array((1, 2, 3)), b=np.array((4, 5, 6)), metric='Minkowski', p=2), "metric='Minkowski', p=2 error"
assert 9 == distance(a=[2, 4, 4, 6], b=[5, 5, 7, 8], p=1, metric='Minkowski'),  "metric='Minkowski', p=1 error"
assert 3.503 == distance(a=[0, 2, 3, 4], b=[2, 4, 3, 7], p=3, metric='Minkowski'),  "metric='Minkowski', p=3 error"


# %% [markdown]
# - Codez l’algorithme de KNN sous forme une fonction `(def KNN(Data_Test, Data_Train, Label_Train, k=1, **kargs))` qui :
#   - Calcul la distance entre Data de test et Data d’apprentissage.
#   - Trouve la/les distances plus proche de « k » voisins.
#   - Classe Data de test selon la classe majoritaire de « k » voisins.
#   - Retourne la classe de Data Test.

# %%
def knn_search(Dt, Data, **kwargs) -> pd.DataFrame:
    """Return distances from Dt to all points in Data

    :Data: Dataframe of points
    :Dt: Point to compare
    :metric: @see distance().metric
    :returns: Nearest Neighbourgs

    """
    metric = kwargs.get("metric") if 'metric' in kwargs else "Euclidean"
    p = kwargs.get("p") if 'p' in kwargs else 2

    D = []
    for i in range(0, len(Data)):
        D.append(distance(metric, a=Dt, b=Data.iloc[i, :], p=p))
    D = pd.DataFrame(D, columns=['Distances'])
    return D


# %%
df_test = pd.DataFrame([[0, 0, 0], [3, 3, 3], [1, 2, 3], [4, 5, 6]])

print(knn_search([0, 0, 0], df_test))
# print(knn_search([1, 1, 1], df_test))
# print(knn_search([2, 2, 2], df_test))
# print(knn_search([3, 3, 3], df_test))
# print(knn_search([1, 2, 3], df_test))

assert pd.DataFrame([0.0, 5.196152422706632, 3.7416573867739413, 8.774964387392123], columns=['Distances']).equals(knn_search([0, 0, 0], df_test)), "knn_search error"


# %%
def pred(D, Y, k) -> pd.core.series.Series:
    """Catégorie la plus représentée dans les k plus petites distances

    :D: Distances
    :Y: Targets labels
    :k: Nombre de voisins
    :returns: Label

    """
    # Création d'un DataFrame Distances / Labels
    df = pd.concat([D, Y], axis=1)
    # Ordoné par ordre croissant pour pouvoir trouver les plus petites valeurs
    df = df.sort_values(by=[df.columns[0]], ascending=True, na_position='last')
    # On ne garde que les `k` premières valeurs
    df = df.iloc[:k]
    return df[df.columns[-1]].mode()


# %%

train_set = df_clean.iloc[:-1, :-2]
# print(train_set.sample(5, random_state=0))

label_set = df_clean.iloc[:-1, -1:]
# print(label_set.sample(5, random_state=0))

test_set = df_clean.iloc[-1:, :-2]
# print(test_set)

validation_set = df_clean.iloc[-1:, -1:]
# print(validation_set)

d_test = knn_search(test_set, train_set)

print(pred(d_test, label_set, 1))
print(pred(d_test, label_set, 2))
print(pred(d_test, label_set, 3))


# %%
def KNN(Data_Test, Data_Train, Label_Train, k=1, metric='Euclidean', **kwargs):
    """Prédictions

    :Data_Test: Jeu de tests
    :Data_Train: Jeu d'apprentissage
    :Label_Train: Y
    :k: Nombre de voisins
    :metric: @see distance().metric
    :returns: TODO

    """
    p = kwargs.get("p") if 'p' in kwargs else 2

    # Les prédictions à retourner
    labels = pd.DataFrame(data=[], columns=["Predictions"])
    # Pour chaque donnée du jeu de test
    for i, dt in Data_Test.iterrows():
        # On récupère les distances relatives aux jeux d'entrainement
        dist = knn_search(dt, Data_Train, metric=metric, p=p)
        # On récupère la catégorie la plus représentée dans les k plus proches voisins
        label = pred(dist, Label_Train, k)
        # On ajoute la prédiction aux résultats
        labels.loc[i] = label[0]
    return labels


# %%

def data_split(df, nb_test=1, random_state=0):
    """Split the dataframe in 4 parts

    :df: Dataframe to split
    :nb_test: How many tests ?
    :random_state: use this seed for  random split
    :returns: (train_set, label_set, test_set, validation_set)

    """
    train_set = df_clean.iloc[:-nb_test, :-2]
    label_set = df_clean.iloc[:-nb_test, -1:]
    test_set = df_clean.iloc[-nb_test:, :-2]
    validation_set = df_clean.iloc[-nb_test:, -1:]

    return (train_set, label_set, test_set, validation_set)


# %%
nb_test = int(len(df_clean)*20/100)
nb_test = 10
train_set, label_set, test_set, validation_set = data_split(df_clean, nb_test, random_state=0)

# print("test",test_set)
# print("train",train_set)
# print("label",label_set)
# print("----")
targets = validation_set[-nb_test:]
# print("Targets : ", targets)
# print(type(targets))
# print(targets.index)

predictions = KNN(test_set, train_set, label_set, 1)
# predictions = predictions.set_index(targets.index)
# print("Predictions : ", predictions)
# print(type(predictions))

comparaison = pd.concat([targets, predictions], axis=1)

# comparaison = pd.merge(targets, predictions, left_index=True, right_index=True)
# comparaison = targets.join(predictions)
# comparaison = targets.join(predictions, lsuffix='_caller', rsuffix='_other')

# comparaison = targets
# comparaison["Prédictions"] = predictions

print(comparaison)

# %% [markdown]
# - Réalisez des expérimentations en variant la distance et le nombre de « k ».

# %%
for k in range(1, 10):
    predictions = KNN(test_set, train_set, label_set, k)
    comparaison = pd.concat([targets, predictions], axis=1)
    print("K:", k, comparaison)


# %% [markdown]
# - Calculez les performances (exemple : Acc) et tracez la courbe de performance de chaque expérimentation. (Les résultats avec interprétation/argumentation doivent figurer dans le notebook comme dans le compte rendu).

# %%
def accuracy(df):
    """Calcule la précision des prédictions

    :df: Prédictions à évaluer
    :returns: prédictions justes / Total
    """
    total = len(df)
    justes = 0
    # Pour chaque prédiction
    for pred in df.values:
        # Si la prédiction est juste
        if pred[0] == pred[1]:
            # On la compte
            justes += 1
    return justes/total


assert 1.0 == accuracy(pd.DataFrame([("A", "A"), ("B", "B"), ("A", "A")]))
assert 2/3 == accuracy(pd.DataFrame([("A", "A"), ("B", "B"), ("A", "B")]))
assert 0.0 == accuracy(pd.DataFrame([("A", "B"), ("B", "C"), ("A", "C")]))

# %%
# Calcul des performances

perf_euclidean = pd.DataFrame({'k': pd.Series(dtype='int'),
                               'Accuracy': pd.Series(dtype='float')})

for k in range(1, 20):
    predictions = KNN(test_set, train_set, label_set, k)
    comparaison = pd.concat([targets, predictions], axis=1)
    perf = pd.DataFrame([{"k": k, "Accuracy": accuracy(comparaison)}])
    perf_euclidean = perf_euclidean.append(perf, ignore_index=True)

print(perf_euclidean)

# %%
plt_euclidean = perf_euclidean.plot(kind='line', x='k', y='Accuracy')

targets.Interpretation.value_counts()

# %%
perf_manhattan = pd.DataFrame({'k': pd.Series(dtype='int'),
                               'Accuracy': pd.Series(dtype='float')})

for k in range(1, 20):
    predictions = KNN(test_set, train_set, label_set, k, metric='Manhattan')
    comparaison = pd.concat([targets, predictions], axis=1)
    perf = pd.DataFrame([{"k": k, "Accuracy": accuracy(comparaison)}])
    perf_manhattan = perf_manhattan.append(perf, ignore_index=True)

print(perf_manhattan)

# %%
plt_manhattan = perf_manhattan.plot(kind='line', x='k', y='Accuracy')

# %%
perf_minkowski = pd.DataFrame({'k': pd.Series(dtype='int'),
                               'Accuracy': pd.Series(dtype='float')})

for k in range(1, 20):
    predictions = KNN(test_set, train_set, label_set, k, metric="Minkowski", p=5)
    comparaison = pd.concat([targets, predictions], axis=1)
    perf = pd.DataFrame([{"k": k, "Accuracy": accuracy(comparaison)}])
    perf_minkowski = perf_minkowski.append(perf, ignore_index=True)

print(perf_minkowski)

# %%
plt_minkowski = perf_minkowski.plot(kind='line', x='k', y='Accuracy')

# %%
import matplotlib.pyplot as plt

plt.figure(1)
plt.subplot(3, 1, 1)
perf_euclidean.plot(kind='line', x='k', y='Accuracy', ax=plt.gca(), title="Euclidean")
plt.subplot(3, 1, 2)
perf_manhattan.plot(kind='line', x='k', y='Accuracy', ax=plt.gca(), title="Manhatann")
plt.subplot(3, 1, 3)
perf_minkowski.plot(kind='line', x='k', y='Accuracy', ax=plt.gca(), title="Minkowsky")
plt.show()

# %%
import matplotlib.pyplot as plt

k_ideal = df_clean.shape[1]/2+1

ax = perf_euclidean.plot(kind='line', x='k', y='Accuracy', label="Euclidean", marker='o', title="Accuracy")
perf_manhattan.plot(kind='line', x='k', y='Accuracy', label="Manhatann", marker='o', ax=ax)
perf_minkowski.plot(kind='line', x='k', y='Accuracy', label="Minkowsky", marker='o', ax=ax)
ax.axvline(k_ideal, label="k idéal", color='k', linestyle='--')
ax.text(k_ideal+0.5, 0.9, 'k idéal', transform=ax.get_xaxis_text1_transform(0)[0])
ax.locator_params(integer=True)
plt.show()

# %% [markdown]
#
# KNN Sklearn
#
# La bibliothèque Sklearn propose un panel des techniques de classification, y compris le KNN.
#
# - Dans cette étape, vous êtes orientés vers la classe « sklearn.neighbors » pour maitriser les paramètres et les options possibles.

# %%
# Import LabelEncoder
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

# %%
# creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
interpretation_encoded = le.fit_transform(df_clean.Interpretation)
print(interpretation_encoded)

# %%
features = df_clean.iloc[:, :-2]

label = interpretation_encoded

# %%
# Initiation du modèle
model = KNeighborsClassifier(n_neighbors=3)

# Apprentissage du modèle
model.fit(features, label)

# Predictions
predicted = model.predict(test_set)

target_labels = targets.T.to_numpy()[0]
predicted_labels = le.inverse_transform(predicted)
print(target_labels)
print(predicted_labels)


# %%
print(model.get_params())

model.score(test_set, predicted_labels)
print(model)

from sklearn. metrics import accuracy_score
print("Accuracy : ", accuracy_score(target_labels, predicted_labels))

# %% [markdown]
# - Vous êtes censés à préparer un modèle performant pour notre application tout en respectant les consignes de la conception d’un modèle IA (Data préparée, K-fold validation, hyperparamètre, Gridsearch). (N’oubliez pas de présenter une comparaison entre KNN From Scratch et KNN Sklearn dans le compte rendu).

# %%

# %%
# K-Fold Amine :
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.metrics import accuracy_score

X = df_clean.iloc[:, :-2]
y = df_clean.iloc[:, -1:]
print(X, y)

kf = KFold(n_splits=3)
kf.get_n_splits(X)

for train_index, test_index in kf.split(X):
    X_Train = X[train_index, :]
    Y_Train = y[train_index]

    X_Test = X[test_index, :]
    Y_Test = y[test_index]

    model = KNN(n_neighbors=3)
    model.fit(X_Train, Y_Train)
    y_pred = model.predict(X_Test)
    P = accuracy_score(Y_Test, y_pred)

    print("Performance:", P)

# %%

# %% [markdown]
# ## Partie 3 : Mettre en place la solution dans l’application de test de personnalité
#
# - Utilisez la fonction « joblib » pour enregistrer votre modèle, une fois vous avez préparé votre meilleur modèle de classification Faites intégrer cette solution à l’Application **Test de Personnalité** et adapter l’application pour comparer le résultat avec et sans IA.

# %%
