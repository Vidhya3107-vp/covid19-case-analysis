import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dataset/patient.csv")

region = df["region"].value_counts().head(10)

region.plot(kind="bar")
plt.title("Top 10 Regions")
plt.xlabel("Region")
plt.ylabel("Cases")

plt.savefig("charts/region_distribution.png")
plt.show()