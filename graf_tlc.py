import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


st.title("Números que contam histórias")
st.write("Laboratório de Estatísticas II - Projeto de Grupo")
st.header("Teorema do Limite Central")

# Linha para escolher o número de amostras
n = st.slider("Tamanho da amostra", 1, 1000, 50)


# Simulações aleatórias
simulacoes = 1000
amostras = np.random.uniform(0, 1, size=(simulacoes, n))
medias_amostras = amostras.mean(axis=1)

# Média e desvio padrão teóricos
media_teorica= 0.5
desvio_padrao_teorico = np.sqrt(1 / 12) / np.sqrt(n)

# Criar espaço para o gráfico
fig, ax = plt.subplots()

# Criar histograma
ax.hist(medias_amostras,
        bins = 30, # quantidade de barras
        density = True, # comparar com curva teórica
        color = "lightblue", # cor das barras
        edgecolor = "black") # cor da borda das barras

# Distribuição Normal (teórico) - Linha vermelha
x = np.linspace(medias_amostras.min(), medias_amostras.max(), 100) # criar valores
y = norm.pdf(x, media_teorica, desvio_padrao_teorico) # altura da linha

# Apresentar linha, Definir título e label's
ax.plot(x, y, color = "red", linewidth = 2)
ax.set_title(f"Média Amostral (n = {n})")
ax.set_xlabel("Média")
ax.set_ylabel("Densidade")

st.pyplot(fig)