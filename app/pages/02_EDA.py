import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. LIMPIEZA DE DATOS (Para unificar las categorías)
# ==========================================

# Pasamos TODA la columna a minúsculas y quitamos espacios para agrupar registros repetidos
df['favorite_genre'] = df['favorite_genre'].astype(str).str.lower().str.strip()

# Diccionario definitivo para unificar idiomas, mayúsculas y abreviaciones en español
mapeo_generos = {
    'sci-fi': 'Ciencia Ficción',
    'ciencia ficción': 'Ciencia Ficción',
    
    'action': 'Acción',
    'acción': 'Acción',
    'accion': 'Acción',
    
    'comedy': 'Comedia',
    'comedia': 'Comedia',
    
    'drama': 'Drama',
    
    'horror': 'Terror',
    'terror': 'Terror',
    
    'romance': 'Romance',
    
    'thriller': 'Suspenso',
    'suspenso': 'Suspenso',
    
    'documentary': 'Documental',
    'documental': 'Documental',
    'doc': 'Documental',
    
    'crime': 'Crimen',
    'crimen': 'Crimen',
    
    'unknown': 'Desconocido'
}

# Aplicamos el reemplazo para limpiar la columna en el DataFrame original
df['favorite_genre'] = df['favorite_genre'].replace(mapeo_generos)


# ==========================================
# GRÁFICO 1: Distribución por Género Favorito
# ==========================================
st.subheader("Distribución de Usuarios por Género")

# Calculamos el orden basado en el conteo limpio
order_generos = df['favorite_genre'].value_counts().index

# Configuramos la figura de Matplotlib
fig1, ax1 = plt.subplots(figsize=(10, 5))

# Armamos el gráfico de barras horizontales
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

# Lo mostramos en la app web de Streamlit
st.pyplot(fig1)


# ==========================================
# GRÁFICO 2: Boxplot de Tiempo de Visualización
# ==========================================
st.subheader("Análisis del Tiempo de Visualización")

# Configuramos la figura del Boxplot
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Armamos el boxplot limpio
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

# Lo mostramos en la app web de Streamlit
st.pyplot(fig2)


# ==========================================
# GRÁFICO 3: Pairplot (Análisis Multivariado)
# ==========================================
st.subheader("Análisis Multivariado de Perfil de Usuario")

# Filtramos los 3 géneros más comunes para evitar que el pairplot se sobrecargue
top_genres = df['favorite_genre'].value_counts().nlargest(3).index
df_filtered = df[df['favorite_genre'].isin(top_genres)]

# Seleccionamos solo las variables numéricas reales de interés (dejando afuera user_id)
variables_interes = ['age', 'monthly_watch_time_mins'] 
num_vars = [col for col in variables_interes if col in df_filtered.columns]

if len(num_vars) >= 2:
    # Generamos el pairplot estructurado de Seaborn
    g = sns.pairplot(data=df_filtered, vars=num_vars, hue='favorite_genre', palette='Dark2')
    
    # Traducimos los ejes del Pairplot automáticamente a español
    labels_espanol = {'age': 'Edad', 'monthly_watch_time_mins': 'Minutos Mensuales'}
    for ax in g.axes.flat:
        if ax is not None:
            if ax.get_xlabel() in labels_espanol:
                ax.set_xlabel(labels_espanol[ax.get_xlabel()])
            if ax.get_ylabel() in labels_espanol:
                ax.set_ylabel(labels_espanol[ax.get_ylabel()])
                
    plt.suptitle('Análisis Multivariado de Perfil de Usuario por Género Top', y=1.02)
    
    # Mostramos el pairplot usando la figura interna del objeto 'g'
    st.pyplot(g.fig)
else:
    st.warning("No se encontraron suficientes variables numéricas válidas para generar el Pairplot.")
