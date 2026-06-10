import pandas as pd

df = pd.read_csv("../dataset/patient.csv")

numeric_cols = [
    "birth_year",
    "infection_order",
    "contact_number"
]

print(df[numeric_cols].corr())