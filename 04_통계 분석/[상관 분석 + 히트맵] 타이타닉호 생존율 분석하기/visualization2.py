# -*- coding: euc-kr -*-
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tt = sns.load_dataset("titanic")
tt['age'] = tt['age'].fillna(tt['age'].median())

# print(titanic['embarked'].value_counts())
tt['embarked'] = tt['embarked'].fillna('S')

# print(titanic['embark_town'].value_counts())
tt['embark_town'] = tt['embark_town'].fillna('Southampton')

# print(titanic['deck'].value_counts())
tt['deck'] = tt['deck'].fillna('C')

tt.to_csv("./titanic.csv", index = False)
# print(tt.info())
# print(tt.describe())

# 생존자 수 확인하기
# print(tt['survived'].value_counts())

sns.countplot('pclass', hue='survived', data = tt)
plt.title('Pclass vs Survived')
plt.show()


