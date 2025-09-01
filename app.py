import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análisis de vehículos eléctricos — Sprint 7")

# leer datos
car_data = pd.read_csv("vehicles_us.csv")

# checkbox histograma
if st.checkbox("Mostrar histograma de años"):
    st.write("Histograma de años de los vehículos")
    fig = px.histogram(car_data, x="Model Year")
    st.plotly_chart(fig, use_container_width=True)

# checkbox scatter
if st.checkbox("Mostrar gráfico de dispersión año vs rango eléctrico"):
    st.write("Relación entre año y rango eléctrico")
    fig2 = px.scatter(car_data, x="Model Year", y="Electric Range")
    st.plotly_chart(fig2, use_container_width=True)