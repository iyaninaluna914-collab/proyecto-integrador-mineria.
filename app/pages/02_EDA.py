import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página (Mantenemos tu diseño original)
st.set_page_config(page_title="02 EDA - Análisis Exploratorio", page_icon="📈", layout="wide")

st.title("📈 Análisis Exploratorio de Datos Interactivo (EDA)")
st.markdown("---")

# Cargar dataset limpio desde tu ruta JSON
try:
    df = pd.read_json("data/processed/streaming_users_clean.json")
    sns.set_theme(style="whitegrid")
    
    # ==========================================
    # 1. LIMPIEZA DE DATOS (Para unificar las categorías)
    # ==========================================
    df['favorite_genre'] = df['favorite_genre'].astype(str).str.lower().str.strip()

    mapeo_generos = {
        'sci-fi': 'Ciencia Ficción', 'ciencia ficción': 'Ciencia Ficción',
        'action': 'Acción', 'acción': 'Acción', 'accion': 'Acción',
        'comedy': 'Comedia', 'comedia': 'Comedia', 'drama': 'Drama',
        'horror': 'Terror', 'terror': 'Terror', 'romance': 'Romance',
        'thriller': 'Suspenso', 'suspenso': 'Suspenso',
        'documentary': 'Documental', 'documental': 'Documental', 'doc': 'Documental',
        'crime': 'Crimen', 'crimen': 'Crimen', 'unknown': 'Desconocido'
    }

    df['favorite_genre'] = df['favorite_genre'].replace(mapeo_generos)


    # ==========================================
    # GRÁFICO 1: Distribución por Género Favorito
    # ==========================================
    st.subheader("Distribución de Usuarios por Género")

    order_generos = df['favorite_genre'].value_counts().index
    fig1, ax1 = plt.subplots(figsize=(10, 5))

    sns.countplot(
        data=df, 
        y='favorite_genre', 
        order=order_generos, 
        palette='viridis', 
        hue='favorite_genre', 
        legend=False, 
        ax=ax1
    )

    plt.title('Distribución de Usuarios por Género Favorito')
    plt.xlabel('Cantidad de Usuarios')
    plt.ylabel('Género Favorito')
    st.pyplot(fig1)
    
    # EXPLICACIÓN DEL GRÁFICO 1
    st.markdown("""
    **💡 Análisis de Distribución:**
    * Este gráfico de barras permite identificar cuáles son las preferencias temáticas principales de nuestra base de usuarios analizada.
    * Al ordenar las categorías de mayor a menor, observamos de forma directa cuáles son los géneros que concentran la mayor masa de clientes (volumen) y cuáles tienen menor impacto comercial o de engagement en la plataforma de streaming.
    """)
    st.markdown("---")


    # ==========================================
    # GRÁFICO 2: Boxplot de Tiempo de Visualización
    # ==========================================
    st.subheader("Análisis del Tiempo de Visualización")

    fig2, ax2 = plt.subplots(figsize=(10, 6))

    sns.boxplot(
        data=df, 
        x='monthly_watch_time_mins', 
        y='favorite_genre', 
        palette='Set2',
        hue='favorite_genre',
        legend=False,
        ax=ax2
    )

    plt.title('Tiempo Mensual de Visualización según Género Favorito')
    plt.xlabel('Minutos Mensuales')
    plt.ylabel('Género')
    st.pyplot(fig2)
    
    # EXPLICACIÓN DEL GRÁFICO 2
    st.markdown("""
    **💡 Análisis del Consumo Mensual (Dispersión y Tendencia Central):**
    * El diagrama de caja (Boxplot) nos ayuda a entender el comportamiento de consumo (en minutos) sin que los promedios nos engañen.
    * **Línea central (Mediana):** Indica el punto medio del consumo de los usuarios para cada género. Nos permite comparar qué comunidades pasan más tiempo real frente a la pantalla.
    * **Ancho de la caja (Rango Intercuartílico):** Muestra la variabilidad o dispersión del consumo. Una caja más larga significa que los gustos y tiempos de esos usuarios son muy variados, mientras que una caja corta refleja un comportamiento de consumo más uniforme y predecible.
    """)
    st.markdown("---")


    # ==========================================
    # GRÁFICO 3: Pairplot (Análisis Multivariado)
    # ==========================================
    st.subheader("Análisis Multivariado de Perfil de Usuario")

    top_genres = df['favorite_genre'].value_counts().nlargest(3).index
    df_filtered = df[df['favorite_genre'].isin(top_genres)]

    variables_interes = ['age', 'monthly_watch_time_mins'] 
    num_vars = [col for col in variables_interes if col in df_filtered.columns]

    if len(num_vars) >= 2:
        g = sns.pairplot(data=df_filtered, vars=num_vars, hue='favorite_genre', palette='Dark2')
        
        labels_espanol = {'age': 'Edad', 'monthly_watch_time_mins': 'Minutos Mensuales'}
        for ax in g.axes.flat:
            if ax is not None:
                if ax.get_xlabel() in labels_espanol:
                    ax.set_xlabel(labels_espanol[ax.get_xlabel()])
                if ax.get_ylabel() in labels_espanol:
                    ax.set_ylabel(labels_espanol[ax.get_ylabel()])
                    
        plt.suptitle('Análisis Multivariado de Perfil de Usuario por Género Top', y=1.02)
        st.pyplot(g.fig)
        
        # EXPLICACIÓN DEL GRÁFICO 3
        st.markdown("""
        **💡 Análisis Cruzado de Perfil de Usuario:**
        * Este análisis multivariado cruza las variables demográficas y de consumo (**Edad** vs. **Minutos Mensuales**) segmentando el comportamiento por los **3 géneros más populares**.
        * **Gráficos diagonales (Densidad):** Muestran cómo se distribuye la edad o el tiempo de forma independiente para cada uno de los tres géneros líderes. Sirve para ver si un género atrae a un público más joven o mayor.
        * **Gráficos de dispersión (Scatterplots):** Permiten evaluar si existe alguna correlación o patrón oculto. Por ejemplo, ayuda a responder si a mayor edad disminuye o aumenta el tiempo de visualización según el tipo de contenido preferido.
        """)
    else:
        st.warning("No se encontraron suficientes variables numéricas válidas para generar el Pairplot.")

except Exception as e:
    st.error(f"Error al cargar el archivo de datos: {e}")
