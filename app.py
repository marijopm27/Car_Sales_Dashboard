import pandas as pd
import streamlit as st

st.set_page_config(page_title="Car Sales", layout="wide")
df = pd.read_csv('CarSales.csv')
#st.dataframe(df,height=1500)


#Creacion del SideBar de la aplicacion de Streamlit

#Esta seccion tendra los filtros a aplicar sobre el dataset de base


st.sidebar.header("Por favor seleccione uno de los filtros")
gender = st.sidebar.multiselect(
    "Seleccione el género:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

company = st.sidebar.multiselect(
    "Seleccione la compañía:",
    options=df["Company"].unique(),
    default=df["Company"].unique()
)

model = st.sidebar.multiselect(
    "Seleccione el modelo:",
    options=df["Model"].unique(),
    default=df["Model"].unique()
)

engine = st.sidebar.multiselect(
    "Seleccione el engine:",
    options=df["Engine"].unique(),
    default=df["Engine"].unique()
)

transmision = st.sidebar.multiselect(
    "Seleccione el tipo de transmision:",
    options=df["Transmission"].unique(),
    default=df["Transmission"].unique()
)
color = st.sidebar.multiselect(
    "Seleccione el color del vehículo:",
    options=df["Color"].unique(),
    default=df["Color"].unique()
)

bodystyle = st.sidebar.multiselect(
    "Seleccione el estilo del vehículo:",
    options=df["BodyStyle"].unique(),
    default=df["BodyStyle"].unique()
)

df_seleccion = df.query(
    "Gender == @gender and Company == @company and Model == @model and Engine == @engine and Transmission == @transmision and Color == @color and BodyStyle == @bodystyle"
)

st.dataframe(df_seleccion)
