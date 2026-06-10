import pandas as pd

df = pd.read_csv("../dataset/patient.csv")

print("Dataset Shape:", df.shape)

print("\nPatient States:")
print(df["state"].value_counts())

print("\nGender Distribution:")
print(df["sex"].value_counts())

print("\nTop Regions:")
print(df["region"].value_counts().head(10))

import matplotlib.pyplot as plt

df["state"].value_counts().plot(kind="bar")

plt.title("Patient State Distribution")
plt.show()