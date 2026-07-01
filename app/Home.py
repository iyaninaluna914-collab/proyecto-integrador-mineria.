import streamlit as st

# Configuración de la página (¡Debe ser la primera línea de Streamlit!)
st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos",
    page_icon="🎬",
    layout="wide"
)

# Título principal
st.title("🎬 Plataforma de Streaming - Analytics Dashboard")
st.markdown("---")

# Introducción del proyecto
st.subheader("¡Bienvenido al Sistema de Análisis de Usuarios!")
st.write(
    """
    Esta aplicación interactiva fue desarrollada para el módulo de **Minería de Datos**. 
    El objetivo principal es explorar el comportamiento de los usuarios de una plataforma de streaming ficticia, 
    evaluando sus niveles de consumo mensual, preferencias de contenido y la retención general tras el proceso de ETL.
    """
)

# Estructura del menú lateral
st.sidebar.success("Selecciona una sección en el menú superior/lateral.")

# Cuadro informativo con la estructura de la App
with st.expander("📂 Estructura del Tablero de Control", expanded=True):
    st.markdown(
        """
        A través del menú lateral podés navegar por las siguientes secciones obligatorias de la cátedra:
        *   **01 Dataset:** Visualización del estado inicial de los datos, el proceso de calidad y la bitácora (`pipeline_log.csv`).
        *   **02 EDA:** Análisis Exploratorio de Datos interactivo mediante los 5 gráficos estratégicos seleccionados.
        *   **03 PCA:** Resultados de la reducción de dimensionalidad con Análisis de Componentes Principales.
        *   **04 Conclusiones:** Hallazgos principales y recomendaciones de negocio para la toma de decisiones.
        """
    )

st.info("💡 Consejo: Navegá paso a paso utilizando las páginas numeradas de la izquierda para mantener el hilo del reporte.")