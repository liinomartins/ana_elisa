import streamlit as st
import pandas as pd 
import plotly.express as px

df = pd.read_csv('https://www.openml.org/data/get_csv/61/dataset_61_iris.arff')
st.title('Ana Elisa Braz - Avaliação 2 - Módulo 2')
st.write('Base Filtrada')
st.dataframe(df)
df.rename(columns = {'class':'Class'}, inplace=True)


classe = list(df['Class'].unique())
classe.append('Todas')
classe1 = st.selectbox('Selecione o class', options = classe)

    

# Visualizações Gráficas
st.title('Visualização Gráfica')
st.write(' ')
classe = df['Class'].unique()

box_x = st.selectbox('Variáveis do Blox Plot', options = df.columns, index = df.columns.get_loc('sepallength'))
box_cat = st.selectbox('Variáveis Categóricas', options = df.columns)
box_fig = px.box(df, x = box_cat, y = box_x, title = 'Box Plot do ' + box_cat, template = 'plotly_white', category_orders = classe)
st.write(box_fig)


# Download da tabela filtrada
st.write('Download da Tabela Filtrada')
def convert_df(df):
    return df.to_csv().encode('utf-8')   
csv = convert_df(df)
st.download_button(label = 'Download da base filtrada como CSV', data = csv, file_name = 'consulta.csv', mime = 'text/csv')
st.write('  ')

# Download da tabela filtrada
st.write('Download da Tabela Filtrada .json')
def convert_df(df):
    return df.to_json(orient = 'records')   
json = convert_df(df)
st.download_button(label = 'Download da base filtrada como JSON', data = json, file_name = 'consulta.json', mime = 'text/json')
