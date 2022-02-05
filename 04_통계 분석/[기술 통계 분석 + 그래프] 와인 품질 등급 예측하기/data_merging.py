# -*- coding: euc-kr -*-
import pandas as pd

red_df = pd.read_csv("./winequality-red2.csv")
red_df.insert(0, column="type", value="red")

white_df = pd.read_csv("./winequality-white2.csv")
white_df.insert(0, column="type", value="white")

# 두 dataFrame 합치기 -> pd.concat
wine = pd.concat([red_df, white_df])
wine.to_csv("./wine.csv", index = False)