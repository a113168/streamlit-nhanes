import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nhanes = pd.read_csv("df_NHANES.csv", sep = ";")
df = pd.DataFrame(nhanes)
df["Depressed"] = df["Depressed"].fillna("None")

st.title("Números que contam histórias")
st.write("Laboratório de Estatísticas II - Projeto de Grupo")

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

# GRÁFICO DE DEPRESSED, escolha do nível de depressão

st.header("Gráfico de Barras - Género, Faixa Etária e Depressão")

# Criar caixa de seleção
estado = st.selectbox(
    "Escolhe o estado de Depressão:",
    ["None", "Several", "Most"]
)


df_filtro = df[df["Depressed"] == estado]

# Ordem correta das idades
ordem_faixa_etaria = [
    "18-19", "20-29", "30-39", "40-49",
    "50-59", "60-69", "70-79", "80+"
]

# Cor das barras
cor_das_barras = {
    "female": "#F06292",
    "male": "#64B5F6"
}

# Contar "female" e "male"
total_female = len(df_filtro[df_filtro["Gender"] == "female"])
total_male = len(df_filtro[df_filtro["Gender"] == "male"])


# Criar espaço para o gráfico
fig, ax = plt.subplots()

# Criar gráfico de barras
sns.countplot(
    data = df_filtro, # dataframe
    x = "AgeDecade", # eixo x
    hue = "Gender", # dividir barras por gênero
    order = ordem_faixa_etaria, # ordem das barras
    hue_order = ["female", "male"], # ordem do gênero
    palette = cor_das_barras, # cores das barras
    linewidth = 1, # borda
    edgecolor = "black", # cor da borda
    ax = ax # desenhar o gráfico
)

ax.set_title(f"Distribuição por Idade e Género (Depressed = {estado})")
ax.set_xlabel("Faixa Etária")
ax.set_ylabel("Contagem")

# Dividir a página em 2 (colunas)
col1, col2 = st.columns([4.5, 0.8])

# Coluna do gráfico
with col1:
    st.pyplot(fig)

# Coluna do total
with col2:
    st.info(f"Mulheres: {total_female}")
    st.info(f"Homens: {total_male}")



#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#


# Gráfico 2

st.title("Idade, Depressão e Idade ao ter o Primeiro Bebé")

# Remover NA's
df = df.dropna(subset=["Age1stBaby"])
df["Age1stBaby"] = df["Age1stBaby"].astype(int)

# Criar caixa de seleção
estado = st.selectbox(
    "Estado de Depressão:",
    ["None", "Several", "Most"]
)

# Criar linha para selecionar a idade
idade_ao_ter_o_primeiro_filho = st.slider(
    "Idade ao ter o primeiro bebé:",
    min_value=int(df["Age1stBaby"].min()),
    max_value=int(df["Age1stBaby"].max()),
    value=30 # ponto que aparece na 1ªvez
)

df_filtro = df[
    (df["Depressed"] == estado) &
    (df["Age1stBaby"] == idade_ao_ter_o_primeiro_filho) &
    (df["Gender"] == "female")
]

# Contar todos os casos do filtro
total = len(df_filtro)

# 
age_order = [
    "18-19", "20-29", "30-39", "40-49",
    "50-59", "60-69", "70-79", "80+"
]

# ✅ Criar gráfico
fig, ax = plt.subplots()

sns.countplot(
    data=df_filtrado,
    x="AgeDecade",
    order=age_order,
    color="#F06292",
    edgecolor="black",
    linewidth=1,
    ax=ax
)

# ✅ Legenda manual (apenas female)
ax.legend(
    ["female"],
    title="Gender",
    loc="upper right"
)

ax.set_title(f"Depressed = {estado} | Age1stBaby = {idade_bebe}")
ax.set_xlabel("Faixa Etária")
ax.set_ylabel("Contagem")

# ✅ Layout igual ao gráfico 3 (gráfico + total)
col1, col2 = st.columns([4.5, 0.8])

with col1:
    st.pyplot(fig)

with col2:
    st.info(f"{total}")

# BOXPLOT
st.header("Boxplot da Depressão por Idade ao ter o Primeiro Filho")

# -------- Preparação dos dados --------
df_box = df[
    (df["Gender"] == "female") &
    (df["Age1stBaby"].notna()) &
    (df["Depressed"].notna())
]

df_box["Age1stBaby"] = df_box["Age1stBaby"].astype(int)

# Garantir ordem correta da depressão
depressed_order = ["None", "Several", "Most"]

# -------- Gráfico --------
fig, ax = plt.subplots()

sns.boxplot(
    data=df_box,
    x="Depressed",
    y="Age1stBaby",
    order=depressed_order,
    color="#F48FB1",
    linewidth=1.2,
    ax=ax
)

ax.set_xlabel("Estado de Depressão")
ax.set_ylabel("Idade ao ter o Primeiro Filho")

st.pyplot(fig)


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

# Gráfico 3

st.title("Faixa Etária, Educação e Idade do Primeiro Bebé")

# Ler dados
df = pd.read_csv("df_NHANES.csv", sep=";")

# Limpeza básica
df = df.dropna(subset=["Age1stBaby", "Education"])
df["Age1stBaby"] = df["Age1stBaby"].astype(int)

# Apenas mulheres (Age1stBaby faz sentido)
df = df[df["Gender"] == "female"]

# ---- CONTROLOS ----


education_order = [
    "8th Grade",
    "9 - 11th Grade",
    "High School",
    "Some College",
    "College Grad"
]

df["Education"] = pd.Categorical(
    df["Education"],
    categories=education_order,
    ordered=True
)

educacao = st.selectbox(
    "Nível de Educação:",
    education_order,
    key="education_select"
)



idade_bebe = st.slider(
    "Idade ao ter o primeiro bebé:",
    min_value=int(df["Age1stBaby"].min()),
    max_value=int(df["Age1stBaby"].max()),
    value=30,
    key="age1stbaby_slider"
)


# Filtro
df_filtrado = df[
    (df["Education"] == educacao) &
    (df["Age1stBaby"] == idade_bebe)
]

# Total de contagem
total = len(df_filtrado)

# Criar gráfico
fig, ax = plt.subplots()

sns.countplot(
    data=df_filtrado,
    x="AgeDecade",
    order=age_order,
    color="#F48FB1",
    edgecolor="black",
    linewidth=1,
    ax=ax
)

ax.set_title(
    f"Education = {educacao} | Age1stBaby = {idade_bebe}"
)
# ✅ Legenda manual (apenas female)
ax.legend(
    ["female"],
    title="Gender",
    loc="upper right"
)
ax.set_xlabel("Faixa Etária")
ax.set_ylabel("Contagem")

# Layout lado a lado
col1, col2 = st.columns([4.5, 0.8]) # perporções do gráfico e caixa de texto

with col1:
    st.pyplot(fig)

with col2:
    st.info(f"{total}")

# BOXPLOT


st.header("Boxplot da Idade ao ter o Primeiro Filho por Nível de Escolaridade")

# Apenas mulheres e valores válidos
df_box = df[
    (df["Gender"] == "female") &
    (df["Age1stBaby"].notna()) &
    (df["Education"].notna())
]

df_box["Age1stBaby"] = df_box["Age1stBaby"].astype(int)


education_order = [
    "8th Grade",
    "9 - 11th Grade",
    "High School",
    "Some College",
    "College Grad"
]

fig, ax = plt.subplots(figsize=(8, 5))

sns.boxplot(
    data=df_box,
    x="Education",
    y="Age1stBaby",
    order=education_order,
    color="#F48FB1",          # rosa claro (estilo R)
    linewidth=1.2,
    ax=ax
)

ax.set_xlabel("Nível de Escolaridade")
ax.set_ylabel("Idade ao ter o Primeiro Filho")

st.pyplot(fig)


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#