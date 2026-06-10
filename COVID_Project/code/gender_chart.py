import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dataset/patient.csv")

gender = df["sex"].value_counts()

gender.plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.savefig("charts/gender_distribution.png")
plt.show()