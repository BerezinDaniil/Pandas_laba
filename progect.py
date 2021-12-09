import pandas as pd

df = pd.read_csv("transactions.csv")
print(df.head())
list_df = df[(df['STATUS'] == 'OK')]['SUM'].tolist()
list__df = df[(df['STATUS'] == 'OK') & (df['CONTRACTOR'] == 'Umbrella, Inc')]['SUM'].tolist()
print(sum(list__df))
sort_df = sorted(list_df, reverse=True)
print(sort_df[0], sort_df[1], sort_df[2])
