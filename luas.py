import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Define the path to the Excel file
xls = "Luas Daerah dan Jumlah Pulau Menurut Provinsi, 2023 Me.xlsx"

# Load the first sheet
df = pd.read_excel(xls, sheet_name="Sheet1")

# Display the first few rows to understand the structure
df.head()

# Menghapus baris yang berisi data total "Indonesia"
df_cleaned = df[df["Provinsi"] != "Indonesia"].reset_index(drop=True)
# Set style for visualization
sns.set(style="whitegrid")

# Figure setup
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Visualisasi ulang tanpa data Indonesia
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Bar Chart - Luas Wilayah per Provinsi
df_sorted_luas = df_cleaned.sort_values(by="Luas Wilayah (Km2)", ascending=False)
sns.barplot(x=df_sorted_luas["Luas Wilayah (Km2)"], y=df_sorted_luas["Provinsi"], ax=axes[0, 0], palette="viridis")
axes[0, 0].set_title("Luas Wilayah per Provinsi (Km²)")
axes[0, 0].set_xlabel("Luas Wilayah (Km²)")
axes[0, 0].set_ylabel("Provinsi")

# Bar Chart - Jumlah Pulau per Provinsi
df_sorted_pulau = df_cleaned.sort_values(by="Jumlah Pulau", ascending=False)
sns.barplot(x=df_sorted_pulau["Jumlah Pulau"], y=df_sorted_pulau["Provinsi"], ax=axes[0, 1], palette="coolwarm")
axes[0, 1].set_title("Jumlah Pulau per Provinsi")
axes[0, 1].set_xlabel("Jumlah Pulau")
axes[0, 1].set_ylabel("Provinsi")

# Pie Chart - Distribusi Luas Wilayah
axes[1, 0].pie(df_cleaned["Persentase Terhadap Luas Wilayah"], labels=df_cleaned["Provinsi"], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set3", len(df_cleaned)))
axes[1, 0].set_title("Persentase Luas Wilayah per Provinsi")

# Scatter Plot - Hubungan Luas Wilayah dan Jumlah Pulau
sns.scatterplot(x=df_cleaned["Luas Wilayah (Km2)"], y=df_cleaned["Jumlah Pulau"], hue=df_cleaned["Provinsi"], palette="tab20", ax=axes[1, 1], s=100, edgecolor='black')
axes[1, 1].set_title("Hubungan Luas Wilayah dan Jumlah Pulau")
axes[1, 1].set_xlabel("Luas Wilayah (Km²)")
axes[1, 1].set_ylabel("Jumlah Pulau")

plt.tight_layout()
plt.show()
