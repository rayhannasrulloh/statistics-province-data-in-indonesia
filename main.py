import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

st.header("Visualization of Provincial Data in Indonesia")

@st.cache_data
def load_data():
    file_path = "Luas Daerah dan Jumlah Pulau Menurut Provinsi, 2023 Me.xlsx"
    df = pd.read_excel(file_path)
    return df[df["Provinsi"] != "Indonesia"].reset_index(drop=True)  # hapus baris "Indonesia"

df = load_data()

#sidebar
st.sidebar.header("Visualization of Provincial Data in Indonesia")
st.sidebar.subheader("Subject : Probability and Statistics")
st.sidebar.write("1. Rayhan Roshidi Nasrulloh | 001202400007")
st.sidebar.write("2. Syah Reza Palevi | 001202400033")
st.sidebar.write("3. Reza Fahlevi | 001202400066")
st.sidebar.image("me.jpg", caption="WebDev by Rayhan")
tab1, tab2, tabs3 = st.tabs(["Visualization", "Statistics", "Discrete Probability"])


#tab 1: Visualisasi
with tab1:
    st.subheader("Bar Chart - Area per Province")
    fig, ax = plt.subplots(figsize=(10, 6))
    df_sorted_luas = df.sort_values(by="Luas Wilayah (Km2)", ascending=False)
    sns.barplot(x=df_sorted_luas["Luas Wilayah (Km2)"], y=df_sorted_luas["Provinsi"], palette="viridis", ax=ax)
    ax.set_xlabel("Luas Wilayah (Km²)")
    ax.set_ylabel("Provinsi")
    st.pyplot(fig)

    st.subheader("Bar Chart - Number of Islands per Province")
    fig, ax = plt.subplots(figsize=(10, 6))
    df_sorted_pulau = df.sort_values(by="Jumlah Pulau", ascending=False)
    sns.barplot(x=df_sorted_pulau["Jumlah Pulau"], y=df_sorted_pulau["Provinsi"], palette="coolwarm", ax=ax)
    ax.set_xlabel("Jumlah Pulau")
    ax.set_ylabel("Provinsi")
    st.pyplot(fig)

    st.subheader("Pie Chart - Area Percentage")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(df["Persentase Terhadap Luas Wilayah"], labels=df["Provinsi"], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set3", len(df)))
    st.pyplot(fig)

    st.subheader("Scatter Plot - Relationship between Area and Number of Islands")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df["Luas Wilayah (Km2)"], y=df["Jumlah Pulau"], hue=df["Provinsi"], palette="tab20", s=100, edgecolor='black', ax=ax)
    ax.set_xlabel("Luas Wilayah (Km²)")
    ax.set_ylabel("Jumlah Pulau")
    st.pyplot(fig)

#tab 2: Statistik
with tab2:
    st.subheader("Statistics Descriptive")
    stats_summary = {
        "Mean Luas Wilayah (Km²)": np.mean(df["Luas Wilayah (Km2)"]),
        "Median Luas Wilayah (Km²)": np.median(df["Luas Wilayah (Km2)"]),
        "Mode Luas Wilayah (Km²)": stats.mode(df["Luas Wilayah (Km2)"], keepdims=True).mode[0],
        "Range Luas Wilayah (Km²)": np.ptp(df["Luas Wilayah (Km2)"]),
        "Standard Deviation Luas Wilayah (Km²)": np.std(df["Luas Wilayah (Km2)"], ddof=1),
        "Q1 (25th Percentile) Luas Wilayah": np.percentile(df["Luas Wilayah (Km2)"], 25),
        "Q3 (75th Percentile) Luas Wilayah": np.percentile(df["Luas Wilayah (Km2)"], 75),
        "Mean Jumlah Pulau": np.mean(df["Jumlah Pulau"]),
        "Median Jumlah Pulau": np.median(df["Jumlah Pulau"]),
        "Mode Jumlah Pulau": stats.mode(df["Jumlah Pulau"], keepdims=True).mode[0],
        "Range Jumlah Pulau": np.ptp(df["Jumlah Pulau"]),
        "Standard Deviation Jumlah Pulau": np.std(df["Jumlah Pulau"], ddof=1),
        "Q1 (25th Percentile) Jumlah Pulau": np.percentile(df["Jumlah Pulau"], 25),
        "Q3 (75th Percentile) Jumlah Pulau": np.percentile(df["Jumlah Pulau"], 75),
    }
    
    st.write(pd.DataFrame(stats_summary, index=[0]).T)

with tabs3:
    st.subheader("Discrete Probability Distributions: Number of Islands per Province")
    st.image("data1.png")
    st.image("data2.png")
    st.image("data/data (1).png")
    st.image("data/data (2).png")
    st.image("data/data (3).png")
    st.image("data/data (4).png")
    st.image("data/data (5).png")
    st.image("data/data (6).png")
    st.image("data/data (7).png")
    st.image("data/data (8).png")
    st.image("data/data (9).png")
