import streamlit as st
import pandas as pd 
import plotly.express as px

df = pd.read_csv('https://www.openml.org/data/get_csv/1586225/php0iVrYT')
df.rename(columns = {'V1':'Recency','V2':'Frequency','V3':'Monetary','V4':'Time','Class':'Target'}, inplace=True)
st.title('Ana Elisa Braz - Avaliação 2 - Módulo 2')
st.write('Base Filtrada')
st.dataframe(df)
df['Target'].astype(str)
target = list(df['Target'].unique())
target.append('Todas')
targets = st.selectbox('Selecione o Target', options = target)
# Função que mostra a quantidade de linhas 
def mostra_qntd_linhas(df):
    qntd_linhas = st.slider('Selecione a quantidade de linhas que deseja mostrar na tabela',min_value = 1, max_value = len(df), step =1)
    st.write(df.head(qntd_linhas).style.format(subset = ['Target'], formatter = "{:.2f}"))

if target !='Todas':
    df = df.query('Target == @target')
    mostra_qntd_linhas(df)
else:
    mostra_qntd_linhas(df)

# Visualizações Gráficas
st.title('Visualização Gráfica')
st.write(' ')
quantidade = df.grouby(['Target']).Target.count().sort_values()
target1 = df['Target'].unique()

fig = px.bar(x=quantidade, y = target1, orientation = 'h', title = 'Nome do Gráfico', labels = {'x':'Quantidade','y':'Target'})
st.pyplot_chart(fig)



# Download da tabela filtrada
st.write('Download da Tabela Filtrada')
def convert_df(df):
    return df.to_csv().encode('utf-8')   
csv = convert_df(df)
st.download_button(label = 'Download da base filtrada como CSV', data = csv, file_name = 'consulta.csv', mime = 'text/csv')

# Download da tabela filtrada
st.write('Download da Tabela Filtrada .json')
def convert_df(df):
    return df.to_json(orient = 'records')   
json = convert_df(df)
st.download_button(label = 'Download da base filtrada como JSON', data = json, file_name = 'consulta.json', mime = 'text/json')
