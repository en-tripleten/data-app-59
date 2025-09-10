import streamlit as st
import pandas as pd
import plotly.express as px

datos = pd.read_csv('data/vehicles_us.csv')

st.header('Analisis de anuncios de ventas de autos')

tabla_check = st.checkbox('Mostrar datos')
hist_check = st.checkbox('Mostrar histograma')

if tabla_check:
    st.write('EDA: Tabla de datos')
    st.dataframe(datos)

if hist_check:
    st.write('Histograma: Distribucion del odometro del auto en venta')
    
    min_odo = int(datos['odometer'].min())
    max_odo = int(datos['odometer'].max())

    rango_odo = st.slider(
        'Selecciona el rango deseado del odometro para el histograma:',
        min_value=min_odo,
        max_value=max_odo,
        value=(min_odo, max_odo)
    )

    hist_filt = datos.query(f'odometer >= {rango_odo[0]} and odometer <= {rango_odo[1]}')

    hist = px.histogram(hist_filt['odometer'])

    st.plotly_chart(hist)
