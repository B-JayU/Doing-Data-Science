# -*- coding: euc-kr -*-
import pandas as pd

wine = pd.read_csv("./wine.csv")
# 기술 통계
print(wine.describe())

# 그룹 비교
# type별로 grouping 한 다음
# 해당 그룹별로 quality 값에 대한 기술 통계
print(wine.groupby('type')['quality'].describe())
print(wine.groupby('type')['quality'].mean())
print(wine.groupby('type')['quality'].std())
print(wine.groupby('type')['quality'].agg(['mean', 'std']))

# t-검정과 회귀 분석으로 그룹 비교

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

# 회귀 분석 모델로 새로운 샘플의 품질 등급 예측
sample1 = wine[wine.columns.difference(['quality', 'type'])]
sample1 = sample1[0:5][:]
sample1_predict = regression_result.predict(sample1)
print(sample1_predict)
print(wine[0:5]['quality'])
