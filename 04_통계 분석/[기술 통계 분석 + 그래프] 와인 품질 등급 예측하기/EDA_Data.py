import pandas as pd

wine_df = pd.read_csv("./wine.csv")
print(wine_df.info())

wine_df.columns = wine_df.columns.str.replace(' ', '_')

# ���� 5�� 
print(wine_df.head())
# ��� ���
print(wine_df.describe())
# wine_df�� quality ���� set
print(sorted(wine_df.quality.unique()))
# wine_df�� quality value�� counting
print(wine_df.quality.value_counts())