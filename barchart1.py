import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    file_path = "Luas Daerah dan Jumlah Pulau Menurut Provinsi, 2023 Me.xlsx"
    df = pd.read_excel(file_path)
    return df[df["Provinsi"] != "Indonesia"].reset_index(drop=True)  # hapus baris "Indonesia"

df = load_data()

st.subheader("Bar Chart - Area per Province")
fig, ax = plt.subplots(figsize=(10, 6))
df_sorted_luas = df.sort_values(by="Luas Wilayah (Km2)", ascending=False)
sns.barplot(x=df_sorted_luas["Luas Wilayah (Km2)"], y=df_sorted_luas["Provinsi"], palette="viridis", ax=ax)
ax.set_xlabel("Luas Wilayah (Km²)")
ax.set_ylabel("Provinsi")
st.pyplot(fig)