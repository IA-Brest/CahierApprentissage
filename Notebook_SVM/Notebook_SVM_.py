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
# <h1><center>Le classifieur SVM</center></h1>
#

# %% [markdown]
# ### Importer les bibliothéques necessaires 

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# #### 1. Importer votre DataSet

# %%
df = pd.read_csv('accent-mfcc-data-1.csv')

# %% [markdown]
# ##### Print

# %%
df.head()

# %% [markdown]
# #### 2. Checker les variables quantitatives/qualitatives et les valeurs manquantes 

# %%
df.info()

# %%
df.shape

# %%
df.shape[0]
len(df)

# %%
df.columns

# %%
# Quantitatives
df.describe()

# %%
# Qualitatives
df.language.value_counts()

# %%
df.isnull().any()

# %% [markdown]
# #### 3. Visualiser les targets, et que remarquez vous ?
# (combien d'instances de chaque valeur de la target)

# %%
# Nombre de valeurs
df.language.nunique()

# %%
# Valeurs
df.language.unique()

# %%
# Fréquences de chaque valeurs
pd.crosstab(df.language, "freq") #.plot(kind="hist")

# %% [markdown]
# ##### #### 4. Notre variable target (Y) est 'language', Récuprer X et y à partir du jeu de données 

# %%
X = df.iloc[:,1:]  # type (X) -> DataFrame
# X = df.language  # type (X) -> Series
# X = df["language"]  # type (X) -> Series
# X = df.select_dtypes('number')  # type (X) -> DataFrame
X

# %%
y = df.iloc[:,:1]  # type(y) -> DataFrame
# y = df.iloc[:,0]  # type(y) -> Series
# y = df.language  # type(y) -> Series
# y = df['language']  # type(y) -> Series
# y = df.select_dtypes('object') # type(y) -> DataFrame
y


# %% [markdown]
# #### 5. Diviser la DataSet en donneés d'apprentissage et de test (20% pour le test)

# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 20/100, random_state = 0)

# %%
for split in [X_train, X_test, y_train, y_test]:
  print(split.shape)

# %% [markdown]
# #### 6. Appliquer une normalisation centrée-réduite aux données en utilisant "StandardScaler"

# %% [markdown]
# Former votre modèle de normalisation
#

# %%
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train.copy())

# %% [markdown]
# Utiliser la classe ".mean_" et ".scale_" pour afficher la moyenne et l'écart-type, respectivement.

# %%
scaler.mean_

# %%
scaler.scale_

# %% [markdown]
# Appliquer la normalisation sur la base d'apprentissage et la base de test sans écraser les données brutes.

# %%
X_train_scaled = scaler.transform(X_train.copy())
X_test_scaled = scaler.transform(X_test.copy())

# %% [markdown]
# Vérifier que la moyenne se rapproche à 0

# %%
X_train_scaled.mean()

# %% [markdown]
# Vérifier que l'écart-type se rapproche à 1

# %%
X_train_scaled.std()

# %% [markdown]
# #### 5. Apprentissage supervisé SVM

# %% [markdown]
# Réaliser le Pipeline expérimental

# %% [markdown]
# - Data
# - Analyse, visualisation et prétraitement (si nécessaire)
# - Préparation des données
# - Apprentissage et Normalisation
# - Configuration des SVMs avec différent paramétrage
# - Apprentissage et Test
# - Matrice de confusion
# - Mesure de performance
# - Conclusion

# %%

# %% [markdown]
# ## Etude de cas
# Un client cherche un produit pour identifier que l’accent italien et l’accent français.
# Quel est votre proposition pour ce client ?

# %%
# 2 possibilité :
# - Supprimer les classes non utilisées
# - Grouper les classes non utilisées en une seule classe commune

# %% [markdown]
# J'ai programmé une gonction pour vous faciliter la classification d'un nouveau Voice, la fonction est "rec_accent".
# Les inputs de la fonction sont :
# - classifier : le modèle SVM ou autre.
# - Record=True : pour faire votre propre enregistrement.
# - Record=False : pour charger un enregistrement existant.
#
# Output est votre reconnaissance.

# %%
import sounddevice as sd #sinon pip install sounddevice
import time #sinon pip install python-time
import scipy.io.wavfile as wav
from python_speech_features import mfcc #sinon pip install python_speech_features==0.4
import tkinter as tk #sinon pip install tk
from tkinter import filedialog

def rec_accent(classifier, Record=True):
    if Record == True :
        #Enregistrement
        print("Attention, l'enregistrement commence dans :")
        (rate,sig) = wav.read("beep-04.wav")
        sd.play(sig, rate)
        for i in range(0,6):
            time.sleep(1)
            print(5-i)
        time.sleep(1)
        freq = 44100
        duration = 1
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        print("Parler maintenant ...!!")
        sd.wait()  
        print("Fin...")
    else :
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        (rate,recording) = wav.read(file_path)
            
    # Caractérisation
    mfcc_feat = mfcc(recording,rate, numcep=12)
    mfcc_feat = np.expand_dims(np.mean(mfcc_feat, axis=0), axis=0)
    pred = classifier.predict(mfcc_feat)
    print('------------------')
    print('Accent : ', pred[0])
    print('------------------')


# %%
rec_accent(trained_classifier, Record=False)

# %%
