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

# Régression Logistique

## 1. Importez les bibliothéques necessaires 

```python
import pandas as pd
```

## 2. Importez le jeu de données 'weatherAUS.csv'

Ce jeu de données contient des observations météorologiques quotidiennes de nombreuses stations météorologiques australiennes.

Pour plus d'information sur le jeu de données: https://www.kaggle.com/jsphyg/weather-dataset-rattle-package

```python
path='./Data_logit/weatherAUS.csv'
df = pd.read_csv(path)
```

## 3. Exploration des données


### Dimension de du jeu de données

```python
df.shape

```

### Prévisulaiser le jeu de données

```python
df.head()

```

### Afficher la liste des labels des colonnes 


```python
df.columns
```

### Supprimer la colonne 'RISK_MM' du jeu de données

```python
df.drop(columns=['RISK_MM'], inplace=True)
```

### Vérifier si la colonne est supprimée

```python
assert 'RISK_MM' not in df.columns
```

### Afficher un summary du jeu de données

```python
df.describe()
```

### Afficher la liste des noms des variables qualitatives 

```python
qual = [col for col in df.columns if col not in df.describe().columns]
# df.select_dtypes(include=object, exclude=None).columns
qual
```

##### Afficher le contenu de ces variables qualitatives

```python
for var in qual:
    print(var, df[var].unique())
```

### Checker le nombre des valeurs manquantes dans chaque variable qualitative

```python
df[[var for var in qual]].isnull().sum()
```

### Afficher les variables qualitatives qui contiennent des valeurs manquantes

```python
df[[var for var in qual]].isnull().any()
```

### Afficher la fréquence des variables qualitatives

```python
for var in qual:
    print(pd.crosstab(df[var], "freq"))
```

### Nombre de labels: cardinalité

Le nombre de labels dans une variable qualitative est appelé la cardinalité. Un nombre élevé de labels dans une variable est appelé cardinalité élevée. Une cardinalité élevée peut poser de sérieux problèmes dans le modèle d'apprentissage automatique. Donc, Afficher la cardinalité de chaque variable qualitative.

```python
df[[var for var in qual]].apply(pd.Series.nunique)

#df[[var for var in df.select_dtypes(include=object, exclude=None).columns]].apply(pd.Series.nunique)

```

## 4. Manipulation d'une variable de type date


### Transformer la variable 'Date', qui est codé  comme strings, à une variable 'Date' de type datetime format

```python
df['Date'] = pd.to_datetime(df.Date)

```

### Extraire l'année à partir de la variable Date et l'ajouter dans le jeu de données dans une colonne separée 'Years' 

```python
df['Years'] = df.Date.dt.to_period('Y')

```

### Extraire le mois à partir de la variable Date et l'ajouter dans le  jeu de données dans une colonne separée 'Month' 

```python
df['Month'] = df.Date.dt.month

```

### Extraire le jour à partir de la variable Date et l'ajouter dans le  jeu de données dans une colonne separée 'Day' 

```python
df['Day'] = df.Date.dt.day

```

### Supprimer la variable Date du  jeu de données

```python
df.drop(columns=['Date'], inplace=True)
assert 'Date' not in df.columns
```

```python
df.head()
```

## 5. Exploration des variables quantitatives


### Afficher la liste des variables quantitatives dans le jeu de données

```python

```

### Visualiser le contenu des variables quantitatives dans le jeu de données

```python

```

### Checker les valeurs manquantes dans les variables quantitatives

```python

```

### Afficher le résumé statistique des variables quantitatives (describe())

```python

```

## 6. Notre variable target (Y) est le RainTomorrow, Récuprer X et Y à partir du jeu de données 

```python

```

## 7. Fractionnement le jeu de données en jeu d'entraînement et jeu de test (20% pour le test)

```python

```

## 8. Checker les valeurs manquantes des variables quantitatives du jeu d'entraînement et de test

```python
# Récupérer tout d'abord les variables quantitatives (numerical)



# Vérifier les valeurs manquantes dans la variable X_train



# Vérifier les valeurs manquantes dans la variable X_test


```

## 9. En utilisant SimpleImputer de Scikit-Learn remplacer les valeurs manquantes dans les variables numérique (entraînement et test) par la moyenne

```python

```

## 10. Vérifier que les valeurs manquantes n'existent plus dans les variables quantitatives (entraînement et test)

```python

```

## 11. En utilisant la fonction fillna() et mode() remplacer les valeurs manquantes dans les variables qualitatives par la valeur la plus fréquante pour chaque variable.

```python

# Récuperer tout d'abord les variables qualitatives


```

## 12. Vérifier que les valeurs manquantes n'existent plus dans les variables qualitative (entraînement et test)

```python

```

## 13. Encoder la variable qualitative 'RainToday' en utilisant le module category_encoders et la fonction BinaryEncoder(cols=['RainToday']) pour le jeu d'entraînement et de test.

```python
# Installation: Dans Anaconda Prompt tapez la commande: pip install category_encoders
# conda install -c conda-forge category_encoders


```

## 14. Recréer un nouveau jeu d'entrainement en concatenant les variables numériques du jeu d'entrainement précedent avec les deux colonnes RainToday_0', 'RainToday_1'qui vont se créer à l'aide de l'étape précedente, plus les variables qualitatives transformées à des variables muettes avec la fonction get_dummies() de pandas 

```python

```

## 15. Refaire l'étape précedente pour le jeu de test

```python

```

## 16. Standariser votre jeu d'entrainement et de test à l'aide de StandardScaler

```python

```

```python

```

```python

```

## 17. Créer votre modèle de régression logistique et entraînez le sur les données d'entraînement

```python
# train a logistic regression model on the training set



# instantiate the model


# fit the model

```

## 18. Predire les résultats du modèle sur l'ensemble du test

```python

```

### Calculer la probabilité que demain va pleuvoir ou pas en utilisant la fonction predict_proba sur le jeu de test

```python

```

### Afficher l'accuracy score en utilisant la fonction accuracy_score sur le jeu de test

```python

```

### Comparer l'accuracy du modèle sur l'ensemble d'apprentissage et l'ensemble de test, qu'est ce que vous remarquez ?


```python

# Affichage du score sur les données d'apprentissage et de test


```

##  19. Afficher la matrice de confusion, TP, TN, FP, FN sur le jeu du test en utilisant la fonction confusion_matrix


```python

```

##  20. Calculer les métriques de classification (accuracy, classification error, precision, recall, specificity) en utilisant seulement les valeurs de TP, TN, FP, FN.

```python

```
