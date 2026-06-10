import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dataset/patient.csv")

df["confirmed_date"] = pd.to_datetime(df["confirmed_date"])
df["released_date"] = pd.to_datetime(df["released_date"])

recovered = df.dropna(subset=["released_date"]).copy()

recovered["recovery_days"] = (
    recovered["released_date"] -
    recovered["confirmed_date"]
).dt.days

plt.hist(recovered["recovery_days"])
plt.title("Recovery Time Distribution")
plt.xlabel("Days")
plt.ylabel("Patients")

plt.savefig("charts/recovery_distribution.png")
plt.show()