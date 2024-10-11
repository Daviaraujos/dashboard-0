import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.title('Dashboard de Análise de Dados')

# Carregar dados (exemplo com CSV)
data = pd.read_csv('dados.csv')

# Exibição dos dados em tabela
st.write("Visualização dos Dados")
st.dataframe(data)

# Gráfico de barras
st.write("Gráfico de Barras")
fig, ax = plt.subplots()
ax.bar(data['Categoria'], data['Valor'])
st.pyplot(fig)

# Filtro
filtro = st.selectbox('Selecione a Categoria:', data['Categoria'].unique())
dados_filtrados = data[data['Categoria'] == filtro]
st.write("Dados Filtrados", dados_filtrados)
