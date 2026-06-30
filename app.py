import pandas as pd
import plotly.graph_objects as go
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
st.header('Análisis de anuncios de coches')

# --- PARTE 1: LOS BOTONES  ---
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Has pulsado el botón')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    st.plotly_chart(fig, width='stretch')

# --- PARTE 2: LAS CASILLAS (para agregar ---

build_histogram = st.checkbox('Construir un histograma de odómetro')
if build_histogram:
    st.write('Has marcado la casilla')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    st.plotly_chart(fig, width='stretch')