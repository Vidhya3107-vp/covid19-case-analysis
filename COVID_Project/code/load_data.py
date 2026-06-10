import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\acer\OneDrive\Documents\COVID_Project\dataset\patient.csv")

state_counts = df["state"].value_counts()

plt.figure(figsize=(8,5))
state_counts.plot(kind="bar")

plt.title("COVID-19 Patient State Distribution")
plt.xlabel("State")
plt.ylabel("Number of Patients")

plt.tight_layout()

plt.savefig(r"C:\Users\acer\OneDrive\Documents\COVID_Project\charts\state_distribution.png")

plt.show()

print("Chart saved successfully!")

