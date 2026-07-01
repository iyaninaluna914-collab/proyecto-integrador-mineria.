import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="03 PCA - Análisis Dimensional", page_icon="🕸️", layout="wide")

st.title("🕸️ Análisis de Componentes Principales (PCA)")
st.markdown("---")

try:
    # Cargar datos limpios
    df = pd.read_json("data/processed/streaming_users_clean.json")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    st.subheader("⚙️ Escalamiento y Ajuste del Modelo")
    st.markdown(
        """
        **Justificación Metodológica:** Las Componentes Principales son altamente sensibles a las escalas. 
        Por ello, aplicamos un escalamiento previo estándar (`StandardScaler`) para garantizar que la varianza de ninguna variable domine artificialmente.
        """
    )
    
    # Procesamiento PCA
    X = df[numeric_cols]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    pca = PCA()
    X_pca = pca.fit_transform(X_scaled)
    
    varianza_explicada = pca.explained_variance_ratio_
    varianza_acumulada = np.cumsum(varianza_explicada)
    
    # Distribución en columnas para pantalla dividida
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write("**Gráfico de Codo (Varianza Explicada Acumulada)**")
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(range(1, len(varianza_explicada) + 1), varianza_explicada, alpha=0.6, align='center', label='Individual')
        ax.step(range(1, len(varianza_acumulada) + 1), varianza_acumulada, where='mid', label='Acumulada', color='red')
        ax.set_ylabel('Porcentaje de Varianza')
        ax.set_xlabel('Componentes Principales')
        ax.set_xticks(range(1, len(varianza_explicada) + 1))
        ax.legend(loc='best')
        st.pyplot(fig)
        
    with col2:
        st.write("**Reporte de Cobertura**")
        df_var = pd.DataFrame({
            "Componente": [f"PC {i}" for i in range(1, len(varianza_explicada) + 1)],
            "Varianza Individual (%)": [round(v * 100, 2) for v in varianza_explicada],
            "Varianza Acumulada (%)": [round(a * 100, 2) for a in varianza_acumulada]
        })
        st.dataframe(df_var, use_container_width=True, hide_index=True)
        
    st.markdown("---")
    st.subheader("📊 Matriz de Cargas (Loadings)")
    st.markdown("Pesos de las variables originales sobre cada una de las componentes principales principales:")
    
    loadings = pd.DataFrame(
        pca.components_.T, 
        columns=[f'PC{i}' for i in range(1, len(numeric_cols) + 1)], 
        index=numeric_cols
    )
    st.dataframe(loadings.round(3), use_container_width=True)
    
except FileNotFoundError:
    st.error("❌ Archivos no encontrados. Asegurate de correr los notebooks de la fase previa.")