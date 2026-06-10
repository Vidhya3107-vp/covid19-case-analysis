import pandas as pd

df = pd.read_csv("../dataset/patient.csv")

with open("report.txt", "w") as f:
    f.write("COVID-19 DATA ANALYSIS REPORT\n")
    f.write("="*40 + "\n\n")

    f.write(f"Dataset Shape: {df.shape}\n\n")

    f.write("Patient States:\n")
    f.write(str(df["state"].value_counts()))
    f.write("\n\n")

    f.write("Top Regions:\n")
    f.write(str(df["region"].value_counts().head(10)))

print("Report Generated Successfully!")