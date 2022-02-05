import pandas as pd

wine_df = pd.read_csv("./wine.csv")
print(wine_df.info())

wine_df.columns = wine_df.columns.str.replace(' ', '_')

# 상위 5개 
print(wine_df.head())
# 기술 통계
print(wine_df.describe())
# wine_df의 quality 값을 set
print(sorted(wine_df.quality.unique()))
# wine_df의 quality value를 counting
print(wine_df.quality.value_counts())