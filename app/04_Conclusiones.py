import streamlit as st

st.set_page_config(page_title="04 Conclusiones", page_icon="💡", layout="wide")

st.title("💡 Conclusiones y Recomendaciones Estratégicas")
st.markdown("---")

st.header("🎯 Cierre del Proyecto Integrador")

st.markdown(
    """
    ### 📌 Hallazgos Clave del Análisis
    
    1. **Trazabilidad y Calidad Garantizada:** 
       A través del log automatizado (`pipeline_log.csv`), se demostró un control riguroso de la pérdida de datos, manteniendo una tasa de retención óptima y justificando cada imputación sin sesgar las métricas operativas.
    
    2. **Segmentación y Comportamiento (EDA):** 
       Las visualizaciones interactivas revelaron que la concentración de usuarios por género permite priorizar la adquisición de licencias específicas, optimizando el presupuesto de contenidos de la plataforma.
       
    3. **Eficiencia de Datos (PCA):** 
       La reducción de dimensionalidad probó que podemos resumir el comportamiento de uso reduciendo significativamente la complejidad estructural de las variables correlacionadas.
    
    ### 🚀 Recomendaciones para la Toma de Decisiones
    *   **Personalización Automática:** Implementar modelos de recomendación basados en la categoría de "Unknown" imputada estratégicamente para recuperar usuarios con perfiles difusos.
    *   **Campañas de Retención:** Monitorear de forma constante el tiempo mensual de visualización (`monthly_watch_time_mins`) detectado en los gráficos de cajas para lanzar alertas tempranas de cancelación del servicio (churn).
    """
)

st.success("🎉 ¡Estructura de la aplicación completada con éxito para la entrega del grupo!")