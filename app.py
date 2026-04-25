import streamlit as st
import pandas as pd

st.set_page_config(page_title="Watch Arbitrage", layout="wide")

st.title("📈 Watch Arbitrage Dashboard")

data = [
    {"Modèle": "Longines HydroConquest", "Achat (€)": 750, "Revente (€)": 1200},
    {"Modèle": "LV Tambour GMT", "Achat (€)": 750, "Revente (€)": 1350},
    {"Modèle": "TAG Heuer Formula 1", "Achat (€)": 650, "Revente (€)": 850},
]

df = pd.DataFrame(data)
df["ROI (€)"] = df["Revente (€)"] - df["Achat (€)"]
df["ROI (%)"] = (df["ROI (€)"] / df["Achat (€)"] * 100).round(1)

st.dataframe(df, use_container_width=True)
