import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="02 EDA - Análisis Exploratorio", page_icon="📈", layout="wide")

st.title("📈 Análisis Exploratorio de Datos Interactivo (EDA)")
st.markdown("---")

# Cargar dataset limpio
try:
    df = pd.read_json("data/processed/streaming_users_clean.json")
    sns.set_theme(style="whitegrid")
    
    # --- FILTRO EN EL MENÚ LATERAL ---
    st.sidebar.header("Filtros Globales")
    generos_disponibles = ["Todos"] + list(df['favorite_genre'].unique())
    genero_seleccionado = st.sidebar.selectbox("Seleccioná un Género Favorito:", generos_disponibles)
    
    # Aplicar filtro si no es "Todos"
    if genero_seleccionado != "Todos":
        df_filtrado = df[df['favorite_genre'] == genero_seleccionado]
    else:
        df_filtrado = df.copy()
        
    st.markdown(f"Mostrando análisis para: **{genero_seleccionado}** ({len(df_filtrado)} usuarios encontrados)")
    
    # --- BLOQUE 1: UNIVARIADO ---
    st.header("📊 1. Análisis Univariado")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Gráfico 1: Tiempo Mensual de Visualización")
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.histplot(data=df_filtrado, x='monthly_watch_time_mins', kde=True, color='skyblue', bins=30, ax=ax1)
        ax1.set_xlabel('Minutos Mensuales')
        ax1.set_ylabel('Cantidad de Usuarios')
        st.pyplot(fig1)
        st.caption("Interpretación: Concentración y sesgo en las horas de consumo de la audiencia seleccionada.")
        
    with col2:
        st.subheader("Gráfico 2: Distribución por Género Favorito")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        order = df['favorite_genre'].value_counts().index
        # Muestra el total general sombreado para comparar el filtro actual
        sns.countplot(data=df, y='favorite_genre', order=order, color='lightgray', ax=ax2)
        sns.countplot(data=df_filtrado, y='favorite_genre', order=order, palette='viridis', ax=ax2)
        ax2.set_xlabel('Cantidad de Usuarios')
        ax2.set_ylabel('Género')
        st.pyplot(fig2)
        st.caption("Interpretación: Participación de mercado por categoría e impacto de la imputación 'Unknown'.")

    st.markdown("---")
    
    # --- BLOQUE 2: BIVARIADO ---
    st.header("📈 2. Análisis Bivariado")
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Gráfico 3: Tiempo de Visualización por Género")
        fig3, ax3 = plt.subplots(figsize=(6, 4))
        sns.boxplot(data=df_filtrado, x='monthly_watch_time_mins', y='favorite_genre', palette='Set2', ax=ax3)
        ax3.set_xlabel('Minutos Mensuales')
        ax3.set_ylabel('Género')
        st.pyplot(fig3)
        st.caption("Interpretación: Comparación de medianas y dispersión del engagement entre géneros.")
        
    with col4:
        st.subheader("Gráfico 4: Matriz de Correlación Numérica")
        fig4, ax4 = plt.subplots(figsize=(6, 4))
        numeric_cols = df_filtrado.select_dtypes(include=[np.number])
        if not numeric_cols.empty and numeric_cols.shape[1] >= 2:
            corr_matrix = numeric_cols.corr()
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, ax=ax4)
        else:
            ax4.text(0.5, 0.5, "Datos insuficientes para correlación", ha='center', va='center')
        st.pyplot(fig4)
        st.caption("Interpretación: Intensidad y dirección de las relaciones lineales de comportamiento.")

    st.markdown("---")
    
    # --- BLOQUE 3: MULTIVARIADO ---
    st.header("🕸️ 3. Análisis Multivariado")
    st.subheader("Gráfico 5: Relación Cruzada de Variables Clave (Pairplot)")
    
    top_genres = df['favorite_genre'].value_counts().nlargest(3).index
    df_multiv = df_filtrado[df_filtrado['favorite_genre'].isin(top_genres)]
    num_vars = df_multiv.select_dtypes(include=[np.number]).columns[:3].tolist()
    
    if len(num_vars) >= 2:
        fig5 = sns.pairplot(data=df_multiv, vars=num_vars, hue='favorite_genre', palette='Dark2')
        st.pyplot(fig5.fig)
        st.caption("Interpretación: Interacción simultánea de múltiples métricas para identificar clusters de usuarios.")
    else:
        st.warning("Se requieren más variables numéricas para generar el gráfico multivariado.")

except FileNotFoundError:
    st.error("❌ Error: Ejecute el pipeline de limpieza antes de abrir esta sección.")