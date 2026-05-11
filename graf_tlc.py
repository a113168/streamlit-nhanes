import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Título
st.title("Teorema do Limite Central")

# Sidebar
st.sidebar.header("Parâmetros")

n_amostras = st.sidebar.slider(
    "Tamanho da amostra (n)",
    min_value=1,
    max_value=500,
    value=30,
    step=1
)

n_repeticoes = st.sidebar.slider(
    "Número de repetições",
    min_value=100,
    max_value=10000,
    value=1000,
    step=100
)

# Distribuição original (Uniforme)
dist = np.random.uniform(0, 1, size=(n_repeticoes, n_amostras))

# Médias amostrais
medias = dist.mean(axis=1)

# Parâmetros teóricos
media_teorica = 0.5
desvio_teorico = np.sqrt(1 / 12) / np.sqrt(n_amostras)

# Plot
fig, ax = plt.subplots()

# Histograma
ax.hist(
    medias,
    bins=30,
    density=True,
    alpha=0.6,
    color="lightblue",
    edgecolor="black"
)

# Curva Normal
x = np.linspace(medias.min(), medias.max(), 300)
ax.plot(
    x,
    norm.pdf(x, media_teorica, desvio_teorico),
    color="red",
    linewidth=2
)

# Labels
ax.set_title("Distribuição da Média Amostral")
ax.set_xlabel("Média amostral")
ax.set_ylabel("Densidade")

st.pyplot(fig)

# Explicação
st.markdown(
    f"""
**Observação:**  
À medida que o tamanho da amostra (**n**) aumenta, a distribuição das médias 
se aproxima cada vez mais de uma **Normal**, conforme o Teorema do Limite Central.
"""
)
