import streamlit as st
import pandas as pd

# 1. Configuración (Sin espacios al principio)
st.set_page_config(page_title="Progreso Atleta")

# 2. Título principal
st.title("🚀 Control de Recuperación")

# 3. Formulario en el lateral
with st.sidebar:
    st.header("Nueva Sesión")
    peso = st.number_input("Peso (kg)", value=69.5)
    dolor = st.slider("Molestia (0-10)", 0, 10, 2)
    if st.button("Guardar"):
        st.success(f"Registrado: {peso}kg")

# 4. Gráfico central
st.subheader("Tu evolución hacia Atleta")
datos = pd.DataFrame({'Día': [1, 2, 3, 4], 'Carga': [65, 67, 69.5, 71]})
st.line_chart(datos.set_index('Día'))

st.info("Objetivo: Volver a ser atleta.")

