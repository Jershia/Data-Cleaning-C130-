import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')

del df["Unnamed: 0"]
del df["Unnamed: 5"]
del df["Star_Name"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]

#df = df.dropna()
df.to_csv('final_data.csv')

df.reset_index(drop=True,inplace = True)

print(df.dtypes)