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

st.subheader("Bar Chart - Number of Islands per Province")
fig, ax = plt.subplots(figsize=(10, 6))
df_sorted_pulau = df.sort_values(by="Jumlah Pulau", ascending=False)
sns.barplot(x=df_sorted_pulau["Jumlah Pulau"], y=df_sorted_pulau["Provinsi"], palette="coolwarm", ax=ax)
ax.set_xlabel("Jumlah Pulau")
ax.set_ylabel("Provinsi")
st.pyplot(fig)