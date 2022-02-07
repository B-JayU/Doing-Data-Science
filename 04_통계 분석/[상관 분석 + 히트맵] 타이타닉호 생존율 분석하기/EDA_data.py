# -*- coding: euc-kr -*-
import seaborn as sns
import pandas as pd

tt = sns.load_dataset("titanic")

tt['age'] = tt['age'].fillna(tt['age'].median())

# print(titanic['embarked'].value_counts())
tt['embarked'] = tt['embarked'].fillna('S')

# print(titanic['embark_town'].value_counts())
tt['embark_town'] = tt['embark_town'].fillna('Southampton')

# print(titanic['deck'].value_counts())
tt['deck'] = tt['deck'].fillna('C')

# print(tt.info())
# print(tt.describe())

# 생존자 수 확인하기
print(tt['survived'].value_counts())