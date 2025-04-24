import streamlit as st
import pandas as pd

# Título del dashboard
st.title("Dashboard de IMC (Índice de Masa Corporal)")

# Cargar datos desde Excel
df = pd.read_excel("IMC_altura_peso.xlsx")

# Filtros
altura_sel = st.slider("Selecciona altura (m)", min_value=1.50, max_value=2.0, step=0.05)
peso_sel = st.slider("Selecciona peso (kg)", min_value=50, max_value=100, step=5)

# Filtrar y mostrar IMC correspondiente
fila = df[(df["Altura (m)"] == altura_sel) & (df["Peso (kg)"] == peso_sel)]

if not fila.empty:
    imc_val = fila["IMC"].values[0]
    st.metric("Tu IMC", f"{imc_val}")
    st.write("Clasificación IMC:")
    if imc_val < 18.5:
        st.warning("Bajo peso")
    elif imc_val < 24.9:
        st.success("Peso normal")
    elif imc_val < 29.9:
        st.warning("Sobrepeso")
    else:
        st.error("Obesidad")

# Mostrar la tabla completa si se desea
if st.checkbox("Mostrar tabla completa"):
    st.dataframe(df)
