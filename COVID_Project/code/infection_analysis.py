import pandas as pd

df = pd.read_csv("../dataset/patient.csv")

print(df["infection_reason"].value_counts())