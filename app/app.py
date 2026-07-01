import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página del Dashboard
st.set_page_config(
    page_title="Dashboard Minería de Datos I - ITSE",
    page_icon="📊",
    layout="wide"
)

# Título Principal
st.title("📊 Proyecto Integrador: Minería de Datos I")
st.markdown(f"**Estudiante:** Yannina Alejandra Luna | **Institución:** ITSE (2026)")
st.hr()

# Barra lateral para navegación
st.sidebar.title("Navegación del Proyecto")
opcion = st.sidebar.radio(
    "Seleccioná una etapa del análisis:",
    ["01. Inspección Inicial", "02. Limpieza & Trazabilidad", "03. Análisis Exploratorio (EDA)", "04. Reducción (PCA)", "05. Modelado Final"]
)

# Secciones del Dashboard según la opción seleccionada
if opcion == "01. Inspección Inicial":
    st.header("🔍 01. Inspección Inicial de los Datos")
    st.write("Acá vas a poder visualizar las primeras filas de tu dataset original, sus dimensiones y los tipos de datos de cada columna.")
    # Ejemplo de tabla interactiva
    st.info("Estructura de datos cargada correctamente.")

elif opcion == "02. Limpieza & Trazabilidad":
    st.header("🪓 02. Limpieza de Datos y Control de Trazabilidad")
    st.write("Muestra el procesamiento de valores nulos, duplicados y outliers filtrados.")
    # Contenedor para mostrar métricas breves
    col1, col2 = st.columns(2)
    col1.metric("Registros Originales", "100%")
    col2.metric("Registros Limpios", "95%", delta="-5% Removidos")

elif opcion == "03. Análisis Exploratorio (EDA)":
    st.header("📈 03. Análisis Exploratorio de Datos")
    st.write("Espacio interactivo para visualizar histogramas, diagramas de dispersión y la matriz de correlación entre las variables primarias.")

elif opcion == "04. Reducción (PCA)":
    st.header("🧬 04. Reducción de Dimensionalidad (PCA)")
    st.write("Visualización del porcentaje de varianza explicada acumulada y distribución de componentes principales.")

elif opcion == "05. Modelado Final":
    st.header("🤖 05. Modelado e Interpretación de Resultados")
    st.write("Presentación de las métricas de desempeño finales y conclusiones de los modelos aplicados sobre el conjunto de datos.")
