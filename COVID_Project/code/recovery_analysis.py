import pandas as pd

df = pd.read_csv("../dataset/patient.csv")

df["confirmed_date"] = pd.to_datetime(df["confirmed_date"])
df["released_date"] = pd.to_datetime(df["released_date"])

recovered = df.dropna(subset=["released_date"])

recovered["recovery_days"] = (
    recovered["released_date"]
    - recovered["confirmed_date"]
).dt.days

print(recovered["recovery_days"].describe())