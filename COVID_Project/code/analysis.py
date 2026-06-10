import pandas as pd

df = pd.read_csv("../dataset/patient.csv")

print("Age Information")
print(df["birth_year"].describe())

print("\nGender Distribution")
print(df["sex"].value_counts())

print("\nTop Regions")
print(df["region"].value_counts().head(10))