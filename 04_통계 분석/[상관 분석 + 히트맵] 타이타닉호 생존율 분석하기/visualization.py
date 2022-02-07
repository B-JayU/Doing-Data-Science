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

f, ax = plt.subplots(1, 2, figsize = (10,5))
tt['survived'][tt['sex'] == 'male'].value_counts().plot.pie(explode=[0,0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)
ax[0].set_title("Survived (Male)")
tt['survived'][tt['sex'] == 'male'].value_counts().plot.pie(explode=[0,0.1], autopct = '%1.1f%%', ax = ax[1], shadow = True)
ax[1].set_title('Survived (Female)')
plt.show()


