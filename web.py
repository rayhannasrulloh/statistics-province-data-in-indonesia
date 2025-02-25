import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import perm

# Membaca data dari file Excel
file_path = "Luas Daerah dan Jumlah Pulau Menurut Provinsi, 2023 Me.xlsx"
df = pd.read_excel(file_path)

# Judul Aplikasi
st.title("Analisis Statistik Luas Wilayah dan Jumlah Pulau per Provinsi di Indonesia")

# 1. Identifikasi Populasi & Sampel
st.write("Data mencakup seluruh provinsi di Indonesia, jadi ini adalah populasi.")

# 2. Quantitative & Qualitative Data
st.subheader("Jenis Data")
st.write("*Quantitative Data:*")
st.write("- Luas Wilayah (Km2)")
st.write("- Persentase Terhadap Luas Wilayah")
st.write("- Jumlah Pulau")

st.write("*Qualitative Data:*")
st.write("- Provinsi")

# 3. Histogram Luas Wilayah
st.subheader("Histogram Luas Wilayah")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["Luas Wilayah (Km2)"], bins=10, kde=True, color="blue", ax=ax)
ax.set_xlabel("Luas Wilayah (Km2)")
ax.set_ylabel("Frekuensi")
ax.set_title("Histogram Luas Wilayah")
st.pyplot(fig)

# Scatter plot Luas Wilayah vs Jumlah Pulau
st.subheader("Scatter Plot Luas Wilayah vs Jumlah Pulau")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=df["Luas Wilayah (Km2)"], y=df["Jumlah Pulau"], color="red", ax=ax)
ax.set_xlabel("Luas Wilayah (Km2)")
ax.set_ylabel("Jumlah Pulau")
ax.set_title("Scatter Plot Luas Wilayah vs Jumlah Pulau")
st.pyplot(fig)

# 4. Menghitung Mean, Median, Mode
st.subheader("Statistik Deskriptif")
mean_luas = df["Luas Wilayah (Km2)"].mean()
median_luas = df["Luas Wilayah (Km2)"].median()
mode_luas = df["Luas Wilayah (Km2)"].mode()[0]

mean_pulau = df["Jumlah Pulau"].mean()
median_pulau = df["Jumlah Pulau"].median()
mode_pulau = df["Jumlah Pulau"].mode()[0]

st.write(f"*Mean Luas Wilayah:* {mean_luas:.2f}")
st.write(f"*Median Luas Wilayah:* {median_luas:.2f}")
st.write(f"*Mode Luas Wilayah:* {mode_luas}")

st.write(f"*Mean Jumlah Pulau:* {mean_pulau:.2f}")
st.write(f"*Median Jumlah Pulau:* {median_pulau:.2f}")
st.write(f"*Mode Jumlah Pulau:* {mode_pulau}")

# 6. Population Standard Deviation
std_luas = np.std(df["Luas Wilayah (Km2)"], ddof=0)
std_pulau = np.std(df["Jumlah Pulau"], ddof=0)
st.subheader("Population Standard Deviation")
st.write(f"*Luas Wilayah:* {std_luas:.2f}")
st.write(f"*Jumlah Pulau:* {std_pulau:.2f}")

# 7. Permutations
n_provinsi = len(df)
permutasi_3 = perm(n_provinsi, 3)
st.subheader("Permutasi")
st.write(f"Jumlah kemungkinan permutasi untuk memilih 3 provinsi: {permutasi_3}")