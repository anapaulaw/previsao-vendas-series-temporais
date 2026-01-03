import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Previsão de Vendas - SARIMAX",
    layout="centered"
)

st.title("📈 Previsão de Vendas com SARIMAX")
st.write("Modelo estatístico treinado para previsão de vendas.")


# Carregar modelo

@st.cache_resource
def carregar_modelo():
    return joblib.load("modelo/sarimax_receita_final.joblib")

modelo = carregar_modelo()


# Sidebar

st.sidebar.header("Configurações")
passos = st.sidebar.slider(
    "Número de períodos para previsão",
    min_value=7,
    max_value=180,
    value=30
)


# Previsão

previsao = modelo.get_forecast(steps=passos)
media = previsao.predicted_mean
intervalo = previsao.conf_int()

df_prev = pd.DataFrame({
    "Previsão": media,
    "Limite Inferior": intervalo.iloc[:, 0],
    "Limite Superior": intervalo.iloc[:, 1]
})


# Gráfico

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_prev["Previsão"], label="Previsão")
ax.fill_between(
    df_prev.index,
    df_prev["Limite Inferior"],
    df_prev["Limite Superior"],
    alpha=0.3
)
ax.legend()
ax.grid(True)

st.pyplot(fig)


# Tabela

st.subheader("📄 Valores previstos")
st.dataframe(df_prev.round(2))

