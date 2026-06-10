import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dataset/patient.csv")

# Chart 1 - State Distribution
df["state"].value_counts().plot(kind="bar")
plt.title("Patient State Distribution")
plt.savefig("../charts/state_distribution.png")
plt.show()

# Chart 2 - Gender Distribution
df["sex"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.ylabel("")
plt.savefig("../charts/gender_distribution.png")
plt.show()

# Chart 3 - Top Regions
df["region"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Regions")
plt.savefig("../charts/top_regions.png")
plt.show()