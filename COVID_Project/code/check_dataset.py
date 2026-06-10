import pandas as pd

df = pd.read_csv(r"C:\Users\acer\OneDrive\Documents\COVID_Project\dataset\patient.csv")

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


print("\nState Distribution:")
print(df['state'].value_counts())

print("\nCountry Distribution:")
print(df['country'].value_counts())

print("\nFirst 5 Rows:")
print(df.head())