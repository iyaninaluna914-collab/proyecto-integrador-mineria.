import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="01 Dataset - Control de Calidad", page_icon="📊", layout="wide")

st.title("📊 Control de Calidad y Estado del Dataset")
st.markdown("---")

# Intentar cargar los datos procesados y los logs
try:
    df_clean = pd.read_json("data/processed/streaming_users_clean.json")
    df_log = pd.read_csv("logs/pipeline_log.csv")
    
    st.subheader("📋 Registro de Cambios (Bitácora ETL)")
    st.markdown("**Evidencia de Trazabilidad:** Historial de modificaciones e impacto de retención en cada hito del pipeline.")
    
    # Mostrar el dataframe del log estilizado
    st.dataframe(df_log, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("🔍 Muestra del Dataset Limpio (`streaming_users_clean.json`)")
    st.markdown(f"Actualmente el dataset cuenta con **{df_clean.shape[0]}** filas y **{df_clean.shape[1]}** columnas listas para análisis.")
    
    # Filtro interactivo rápido en la visualización de los datos
    filas_mostrar = st.slider("Cantidad de filas a visualizar en la muestra:", min_value=5, max_value=50, value=10)
    st.dataframe(df_clean.head(filas_mostrar), use_container_width=True)

except FileNotFoundError as e:
    st.error("❌ Error de consistencia: No se encontraron los archivos procesados o la bitácora de logs.")
    st.warning("Asegurate de haber ejecutado por completo los Notebooks 02 de tu pipeline antes de lanzar la aplicación.")