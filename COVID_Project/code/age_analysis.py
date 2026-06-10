import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("../dataset/patient.csv")

current_year = datetime.now().year

df["age"] = current_year - df["birth_year"]

print(df["age"].describe())

df["age"].dropna().hist(bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Patients")

plt.savefig("../charts/age_distribution.png")

plt.show()