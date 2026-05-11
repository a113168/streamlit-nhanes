import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

st.title("Teorema do Limite Central")

# Slider simples
n = st.slider("Tamanho da amostra", 1, 1000, 50)

# Parâmetros
repeticoes = 1000

# Gerar amostras (uniforme)
amostras = np.random.uniform(0, 1, size=(repeticoes, n))
medias = amostras.mean(axis=1)

# Média e desvio padrão teóricos
media = 0.5
desvio = np.sqrt(1 / 12) / np.sqrt(n)

# Gráfico
fig, ax = plt.subplots()

# Histograma
ax.hist(medias, bins=30, density=True,
        color="lightblue", edgecolor="black")

# Linha vermelha (Normal)
x = np.linspace(medias.min(), medias.max(), 300)
y = norm.pdf(x, media, desvio)

ax.plot(x, y, color="red", linewidth=2)

ax.set_title(f"Média Amostral (n = {n})")
ax.set_xlabel("Média")
ax.set_ylabel("Densidade")

st.pyplot(fig)