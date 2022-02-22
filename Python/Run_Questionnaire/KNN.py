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
df.reset_index(inplace = True, drop = True)

df.shape

# %% [markdown]
# Appliquez les traitements nécessaires pour préparer la DataSet en utilisant Numpy et Pandas, (vous pouvez trouver un référentiel sur ressource).
#
# (présenter votre pipeline dans le compte rendu).
#
# NB. Le résultat de classification dépond essentiellement de la qualité du prétraitement.

# %%
df.columns.unique()
df.head()

# %% [markdown]
# Pour les colones Q1 à Q10 :
# - Si la réponse est "a" "A" ou "1", remplacer par 1
# - Sinon Si la réponse est "b" "B" ou "2", remplacer par 2
# - Sinon Si la réponse est "c" "C" ou "3", remplacer par 3
# - Sinon, remplacer toutes les autres valeurs par NaN.

# %%
df_clean = df.copy()
df_loc[]

# %%
df_clean = df.copy()
df_clean.loc['Q1':'Q10' == "a", 'Q1':'Q10'] = 1
df_clean.head()

# %%

# %%
