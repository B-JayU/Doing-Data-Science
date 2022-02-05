# -*- coding: euc-kr -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols, glm

wine = pd.read_csv("./wine.csv")
red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.columns)

stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False)
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'

regression_result = ols(Rformula, data=wine).fit()
print(regression_result.summary())

# 와인 유형에 따른 품질 등급 히스토그램 그리기
'''
sns.set_style('dark')
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')
sns.distplot(white_wine_quality, kde = True, color = "white", label = 'white wine')
plt.title('Quality of wine Type')
plt.legend()
plt.show()
'''

# 부분 회귀 플롯으로 시각화하기
others = list(set(wine.columns).difference(set(['fixed_acidity', 'quality'])))
p, resids = sm.graphics.plot_partregress("quality", "fixed_acidity", others, data=wine, ret_coords = True)
plt.show()
fig = plt.figure(figsize = (8, 13))
sm.graphics.plot_partregress_grid(regression_result, fig = fig)
plt.show()