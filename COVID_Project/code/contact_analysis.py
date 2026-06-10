import pandas as pd

df = pd.read_csv("../dataset/patient.csv")

print("Contact Number Statistics:\n")
print(df["contact_number"].describe())