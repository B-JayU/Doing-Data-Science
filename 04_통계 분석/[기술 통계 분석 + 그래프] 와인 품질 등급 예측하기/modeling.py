# -*- coding: euc-kr -*-
import pandas as pd

wine = pd.read_csv("./wine.csv")
# ��� ���
print(wine.describe())

# �׷� ��
# type���� grouping �� ����
# �ش� �׷캰�� quality ���� ���� ��� ���
print(wine.groupby('type')['quality'].describe())
print(wine.groupby('type')['quality'].mean())
print(wine.groupby('type')['quality'].std())
print(wine.groupby('type')['quality'].agg(['mean', 'std']))

# t-������ ȸ�� �м����� �׷� ��

from scipy import stats
from statsmodels.formula.api import ols, glm

red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.columns)

stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False)
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'

regression_result = ols(Rformula, data=wine).fit()
print(regression_result.summary())

# ȸ�� �м� �𵨷� ���ο� ������ ǰ�� ��� ����
sample1 = wine[wine.columns.difference(['quality', 'type'])]
sample1 = sample1[0:5][:]
sample1_predict = regression_result.predict(sample1)
print(sample1_predict)
print(wine[0:5]['quality'])
