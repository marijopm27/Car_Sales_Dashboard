import pandas as pd
import streamlit as st

st.set_page_config(page_title="Car Sales", layout="wide")
df = pd.read_csv('CarSales.csv')
#st.dataframe(df,height=1500)

# ------------------------- SIDEBAR FILTERS -------------------------------------
#Creacion del SideBar de la aplicacion de Streamlit

#Esta seccion tendra los filtros a aplicar sobre el dataset de base

st.header("Car Sales Dashboard")

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

# model = st.sidebar.multiselect(
#     "Seleccione el modelo:",
#     options=df["Model"].unique(),
#     default=df["Model"].unique()
# )

engine = st.sidebar.multiselect(
    "Seleccione el engine:",
    options=df["Engine"].unique(),
    default=df["Engine"].unique()
)

# transmision = st.sidebar.multiselect(
#     "Seleccione el tipo de transmision:",
#     options=df["Transmission"].unique(),
#     default=df["Transmission"].unique()
# )
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

df_filtered = df.query(
    "Gender == @gender and Company == @company and  Engine == @engine and Color == @color and BodyStyle == @bodystyle"
)

st.dataframe(df_filtered)

# ------------------------- MAIN PAGE -------------------------------------

# Gráfico de ventas por compañía
st.header("Gráfico de Ventas por Compañía")
sales_by_company = df_filtered['Company'].value_counts()
st.bar_chart(sales_by_company)

# Gráfico de ventas por modelo
st.header("Gráfico de Ventas por Modelo")
sales_by_model = df_filtered['Model'].value_counts()
st.bar_chart(sales_by_model)

# Gráfico de ventas por región del distribuidor
st.header("Gráfico de Ventas por Región del Distribuidor")
sales_by_region = df_filtered['Dealer_Region'].value_counts()
st.bar_chart(sales_by_region)

# Calcular suma de montos totales por compañía
st.header("Suma de Montos Totales por Compañía")
total_sales_by_company = df_filtered.groupby('Company')['Price ($)'].sum()
st.bar_chart(total_sales_by_company)