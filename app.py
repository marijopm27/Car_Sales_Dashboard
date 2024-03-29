import pandas as pd
import streamlit as st

st.set_page_config(page_title="Car Sales",page_icon="chart_with_upwards_trend", layout="wide")
df = pd.read_csv('CarSales.csv')

# Convertir la columna 'Date' al formato de fecha adecuado
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y').dt.date

# ------------------------- SIDEBAR FILTERS -------------------------------------
# Creacion del SideBar de la aplicacion de Streamlit

# Esta seccion tendra los filtros a aplicar sobre el dataset de base

st.header("Car Sales Dashboard")

st.sidebar.header("Por favor seleccione uno de los filtros")
gender = st.sidebar.multiselect(
    "Seleccione el género:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)
# Obtener las fechas únicas y ordenarlas
dates = sorted(df['Date'].unique())

# Agregar filtro de rango de fechas con slider
selected_dates = st.sidebar.slider(
    "Seleccione un rango de fechas:",
    min_value=dates[0],
    max_value=dates[-1],
    value=(dates[0], dates[-1])
)
company = st.sidebar.multiselect(
    "Seleccione la compañía:",
    options=df["Company"].unique(),
    default=df["Company"].unique()
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

# Filtrar el DataFrame según las selecciones del usuario
df_filtered = df.query(
    "Gender == @gender and Company == @company and  Transmission == @transmision and Color == @color and BodyStyle == @bodystyle and Date >= @selected_dates[0] and Date <= @selected_dates[1]"
)

# Obtener los modelos disponibles basados en las compañías seleccionadas
available_models = df_filtered[df_filtered['Company'].isin(company)]['Model'].unique()

# Permitir al usuario seleccionar modelos basados en las compañías filtradas
selected_models = st.sidebar.multiselect(
    "Seleccione el modelo:",
    options=available_models,
    default=available_models
)

# Aplicar el filtro de modelos seleccionados
df_filtered = df_filtered[df_filtered['Model'].isin(selected_models)]

st.dataframe(df_filtered)

# ------------------------- MAIN PAGE -------------------------------------

# Gráfico de ventas por compañía
st.subheader("Gráfico de Ventas por Compañía")
sales_by_company = df_filtered['Company'].value_counts()
st.bar_chart(sales_by_company)

# Gráfico de ventas por modelo
st.subheader("Gráfico de Ventas por Modelo")
sales_by_model = df_filtered['Model'].value_counts()
st.bar_chart(sales_by_model)

# Gráfico de ventas por región del distribuidor
st.subheader("Gráfico de Ventas por Región del Distribuidor")
sales_by_region = df_filtered['Dealer_Region'].value_counts()
st.bar_chart(sales_by_region)

# Calcular suma de montos totales por compañía
st.subheader("Suma de Montos Totales por Compañía")
total_sales_by_company = df_filtered.groupby('Company')['Price ($)'].sum()
st.bar_chart(total_sales_by_company)
