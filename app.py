import streamlit as st
import pandas as pd

st.title("Consulta Centro de Custo e Conversão de CFOP")

# Carregar planilha
df = pd.read_excel("CENTRO_DE_CUSTO.xlsx")

# CONSULTA CENTRO DE CUSTO
st.header("Consulta Centro de Custo")

centro = st.text_input("Digite o Centro de Custo")

if centro:
    resultado = df[df["centro"].astype(str) == centro]

    if not resultado.empty:
        cliente = resultado.iloc[0]["cliente"]
        tipo = resultado.iloc[0]["tipo"]
        icms = resultado.iloc[0]["icms"]
        pis = resultado.iloc[0]["pis_cofins"]

        st.write("Cliente:", cliente)
        st.write("Tipo de entrada:", tipo)
        st.write("ICMS:", icms)
        st.write("PIS/COFINS:", pis)
    else:
        st.write("Centro de custo não encontrado")

# CONVERSÃO CFOP
st.header("Conversão de CFOP")

cfop = st.text_input("Digite o CFOP da nota")

if cfop:
    if cfop.startswith("5"):
        entrada = "1" + cfop[1:]
    elif cfop.startswith("6"):
        entrada = "2" + cfop[1:]
    else:
        entrada = cfop

    st.write("CFOP de entrada:", entrada)