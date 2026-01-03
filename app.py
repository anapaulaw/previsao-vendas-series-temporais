import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


# -----------------------------------
# Configuração da página
# -----------------------------------
st.set_page_config(
    page_title="Previsão de Vendas - SARIMAX",
    layout="centered"
)

st.title("📈 Previsão de Vendas com SARIMAX")
st.write("Modelo estatístico treinado para previsão de vendas.")


# -----------------------------------
# Carregar modelo
# -----------------------------------
@st.cache_resource
def carregar_modelo():
    return joblib.load("modelo/sarimax_receita_final.joblib")

modelo = carregar_modelo()


# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.header("Configurações")
passos = st.sidebar.slider(
    "Número de períodos para previsão",
    min_value=7,
    max_value=180,
    value=30
)


# -----------------------------------
# Datas futuras
# -----------------------------------
indice_treino = modelo.model.data.row_labels
ultima_data = pd.to_datetime(indice_treino[-1])

datas_futuras = pd.date_range(
    start=ultima_data + pd.Timedelta(days=1),
    periods=passos,
    freq="D"
)


# -----------------------------------
# EXÓGENAS FUTURAS (AUTOMÁTICO)
# -----------------------------------
# Nomes das exógenas usadas no treino
nomes_exog = modelo.model.exog_names

exog_futuro = pd.DataFrame(
    0,
    index=datas_futuras,
    columns=nomes_exog
)

# Preenchimento inteligente 
if "fim_de_semana" in exog_futuro.columns:
    exog_futuro["fim_de_semana"] = exog_futuro.index.weekday.isin([5, 6]).astype(int)

if "mes" in exog_futuro.columns:
    exog_futuro["mes"] = exog_futuro.index.month

if "dia_semana" in exog_futuro.columns:
    exog_futuro["dia_semana"] = exog_futuro.index.weekday

# Todas as outras dummies (Natal, Black Friday, meses, etc.)
# ficam corretamente como ZERO


# -----------------------------------
# Previsão
# -----------------------------------
previsao = modelo.get_forecast(
    steps=passos,
    exog=exog_futuro
)

media = previsao.predicted_mean
intervalo = previsao.conf_int()

df_prev = pd.DataFrame({
    "Previsão": media,
    "Limite Inferior": intervalo.iloc[:, 0],
    "Limite Superior": intervalo.iloc[:, 1]
})


# -----------------------------------
# Gráfico
# -----------------------------------
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(df_prev.index, df_prev["Previsão"], label="Previsão")
ax.fill_between(
    df_prev.index,
    df_prev["Limite Inferior"],
    df_prev["Limite Superior"],
    alpha=0.3
)

ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.legend()
ax.grid(True)

st.pyplot(fig)


# -----------------------------------
# Tabela
# -----------------------------------
st.subheader("📄 Valores previstos")
st.dataframe(df_prev.round(2))




