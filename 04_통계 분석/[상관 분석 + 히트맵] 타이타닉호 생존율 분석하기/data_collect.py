# -*- coding: euc-kr -*- 
import seaborn as sns
import pandas as pd

titanic = sns.load_dataset("titanic")
# titanic.to_csv("./titanic.csv", index = False)

titanic['age'] = titanic['age'].fillna(titanic['age'].median())

# print(titanic['embarked'].value_counts())
titanic['embarked'] = titanic['embarked'].fillna('S')

# print(titanic['embark_town'].value_counts())
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')

# print(titanic['deck'].value_counts())
titanic['deck'] = titanic['deck'].fillna('C')

print(titanic.isnull().sum())