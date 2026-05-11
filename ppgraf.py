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

# GRÁFICO 1, RELAÇÃO - GÉNERO E DEPRESSÃO
# GRÁFICO DE DEPRESSED, escolha do nível de depressão

st.header("Relação - Género e Depressão")

# Criar caixa de seleção
g1_depressao_estado = st.selectbox(
    "Escolhe o estado de Depressão:",
    ["None", "Several", "Most"]
)

df_grafico_1 = df[df["Depressed"] == g1_depressao_estado]

# Preparar valores para gráfico
g1_ordem_faixa_etaria = [
    "18-19", "20-29", "30-39", "40-49",
    "50-59", "60-69", "70-79", "80+"
]

cor_das_barras = {
    "female": "#F06292",
    "male": "#64B5F6"
}

# Contar "female" e "male"
total_female = len(df_grafico_1[df_grafico_1["Gender"] == "female"])
total_male = len(df_grafico_1[df_grafico_1["Gender"] == "male"])

# Criar espaço para o gráfico
fig, ax = plt.subplots()

# Criar gráfico de barras
sns.countplot(
    data = df_grafico_1, # dataframe
    x = "AgeDecade", # eixo x
    hue = "Gender", # dividir barras por gênero
    order = g1_ordem_faixa_etaria, # ordem das barras
    hue_order = ["female", "male"], # ordem do gênero
    palette = cor_das_barras, # cores das barras
    linewidth = 1, # tamanho da borda das barra
    edgecolor = "black", # cor da borda das barra
    ax = ax # desenhar o gráfico
)

# Definir título e label's
ax.set_title(f"Depressed = {g1_depressao_estado}")
ax.set_xlabel("Faixa Etária")
ax.set_ylabel("Contagem")

# Dividir a página em 2 (colunas)
col1, col2 = st.columns([4.5, 0.8])

with col1: # Coluna do gráfico
    st.pyplot(fig)
with col2: # Coluna do total
    st.info(f"Mulheres: {total_female}")
    st.info(f"Homens: {total_male}")


st.text("Há mais pessoas do género masculino sem depressão, " \
"já nos outros dois estados de depressão analisados, " \
"o género feminino destaca-se.")



#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#


# GRÁFICO 2, RELAÇÃO - DEPRESSÃO E IDADE AO TER O PRIMEIRO FILHO

st.header("Relação - Depressão e Idade ao ter o primeiro filho")

df_grafico_2 = df[df["Age1stBaby"].notna()]

# Criar caixa de seleção
g2_depressao_estado = st.selectbox(
    "Estado de Depressão:",
    ["None", "Several", "Most"]
)

# Linha para escolher um intervalo
g2_intervalo_idade = st.slider(
    "Intervalo de idade ao ter o primeiro bebé:",
    min_value = int(df_grafico_2["Age1stBaby"].min()), # valor mínimo: 14
    max_value = int(df_grafico_2["Age1stBaby"].max()), # valor máximo: 39
    value = (18, 27), # intervalo inicial,
    key = "g2_slicer"
)

# Filtro, mulheres no intervalo
df_grafico_2_filtro = df[
    (df["Depressed"] == g2_depressao_estado) &
    (df["Age1stBaby"] >= g2_intervalo_idade[0]) &
    (df["Age1stBaby"] <= g2_intervalo_idade[1])
]

# Total, apresentar no lado esquedo do gráfico
total = len(df_grafico_2_filtro)

g2_g3_ordem_faixa_etaria = [
    "20-29", "30-39", "40-49",
    "50-59", "60-69", "70-79", "80+"
]

# Criar espaço para o gráfico
fig, ax = plt.subplots()

# Criar gráfico de barras
sns.countplot(
    data = df_grafico_2, # dataframe
    x = "AgeDecade", # eixo x
    order = g2_g3_ordem_faixa_etaria, # ordem das barras
    color = "#F06292", # cor das barras
    linewidth = 1, # tamanho da borda das barra
    edgecolor = "black", # cor da borda das barra
    ax = ax # desenhar o gráfico
)


# Definir título, label's e legenda
ax.set_title(
    f"Depressed = {g2_depressao_estado} | Age1stBaby entre {g2_intervalo_idade[0]} e {g2_intervalo_idade[1]}"
)
ax.set_xlabel("Faixa Etária")
ax.set_ylabel("Contagem")
ax.legend(
    ["female"],
    title = "Gender",
    loc = "upper right"
)

# Dividir a página em 2 (colunas)
g2_col1, g2_col2 = st.columns([4.5, 0.8])

with g2_col1: # Coluna do gráfico
    st.pyplot(fig)
with g2_col2: # Coluna do total
    st.info(f"Mulheres: {total}")

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

# BOXPLOT, DEPRESSÃO POR IDADE AO TER O PRIMEIRO FILHO
st.header("Boxplot da Depressão por Idade ao ter o Primeiro Filho")

df_g2_g3_boxplot = df[
    (df["Gender"] == "female") &
    (df["Age1stBaby"].notna()) &
    (df["Depressed"].notna())
]

# Ordenar estados de depressão
ordem_estados_depressao = ["None", "Several", "Most"]

# Criar espaço para o gráfico
fig, ax = plt.subplots()

sns.boxplot(
    data = df_g2_g3_boxplot, # dataframe
    x = "Depressed", # eixo x
    y = "Age1stBaby", # eixo y
    order = ordem_estados_depressao, # ordem dos boxplots
    color = "#F48FB1", # cor dos boxplots
    linewidth = 1, # tamanho da borda das barra
    ax = ax # desenhar o gráfico
)

# Definir label's
ax.set_xlabel("Estado de Depressão")
ax.set_ylabel("Idade ao ter o Primeiro Filho")

st.pyplot(fig)

st.text("O género feminino quando mais cedo tem o seu primeiro filho, " \
"tende a ter um estado de depressão maior.")


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

# GRAFICO 3 - EDUCAÇÃO E IDADE AO TER O PRIMEITO FILHO

st.header("Relação - Educação e Idade ao ter o primeiro filho")


df_grafico_3 = df[df["Age1stBaby"].notna()]

df_grafico_3 = df_grafico_3[df_grafico_3["Gender"] == "female"]

# Criar caixa de seleção
nivel_de_escolaridade = st.selectbox(
    "Nível de Educação:",
    ["8th Grade", "9 - 11th Grade", "High School",
     "Some College", "College Grad"]
    # key="education_select"
)

# Linha para escolher um intervalo
g3_intervalo_idade = st.slider(
    "Intervalo de idade ao ter o primeiro bebé:",
    min_value = int(df_grafico_3["Age1stBaby"].min()), # valor mínimo: 14
    max_value = int(df_grafico_3["Age1stBaby"].max()), # valor máximo: 39
    value = (18, 27), # intervalo inicial
    key = "g3_slicer" # destinguir slicers
)

# Filtro, mulheres no intervalo
df_grafico_3_filtro = df[
    (df["Education"] == nivel_de_escolaridade) &
    (df["Age1stBaby"] >= g3_intervalo_idade[0]) &
    (df["Age1stBaby"] <= g3_intervalo_idade[1])
]

# Total, apresentar no lado esquedo do gráfico
total = len(df_grafico_3_filtro)

# Criar espaço para o gráfico
fig, ax = plt.subplots()

# Criar gráfico de barras
sns.countplot(
    data = df_grafico_3_filtro, # dataframe
    x = "AgeDecade", # eixo x
    order = g2_g3_ordem_faixa_etaria, # ordem das barras
    color = "#F48FB1", # cor das barras
    edgecolor = "black", # tamanho da borda das barra
    linewidth = 1, # cor da borda das barra
    ax = ax # desenhar o gráfico
)

# Definir título, label's e legenda
ax.set_title(
    f"Education = {nivel_de_escolaridade} | Age1stBaby entre {g3_intervalo_idade[0]} e {g3_intervalo_idade[1]}"
)
ax.set_xlabel("Faixa Etária")
ax.set_ylabel("Contagem")
ax.legend(
    ["female"],
    title = "Gender",
    loc = "upper right"
)

# Dividir a página em 2 (colunas)
g3col1, g3col2 = st.columns([4.5, 0.8])

with g3col1: # Coluna do gráfico
    st.pyplot(fig)
with g3col2: # Coluna do total
    st.info(f"Mulheres: {total}")

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

# BOXPLOT, NÍVEL DE ESCOLARIDADE POR IDADE AO TER O PRIMEIRO FILHO
st.header("Boxplot do Nível de Escolaridade por Idade ao ter o Primeiro Filho")

ordem_nivel_de_escolaridade = ["8th Grade", "9 - 11th Grade", "High School",
                           "Some College", "College Grad"]

# Criar espaço para o gráfico
fig, ax = plt.subplots()

# Criar espaço para o gráfico
sns.boxplot(
    data = df_g2_g3_boxplot, # dataframe
    x = "Education", # eixo x
    y = "Age1stBaby", # eixo y
    order = ordem_nivel_de_escolaridade, # ordem dos boxplots
    color = "#F48FB1", # cor dos boxplots
    linewidth = 1, # tamanho da borda das barra
    ax = ax # desenhar o gráfico
)

# Definir label's
ax.set_xlabel("Nível de Escolaridade")
ax.set_ylabel("Idade ao ter o Primeiro Filho")

st.pyplot(fig)

st.text("O género feminino quanto tem um maior nível de escolaridade, " \
"mais tarde tem o seu primeiro filho.")