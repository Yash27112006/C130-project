import pandas as pd
import csv

df = pd.read_csv('merged_dataset_stars.csv')

del df["Unnamed: 0"]
del df["Luminosity"]
del df["Unnamed: 6"]
del df["Star_Name"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]

final_data = df.dropna()
final_data.to_csv('final_data.csv')

print(final_data.dtypes)
