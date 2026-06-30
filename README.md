# Proyecto Integrador: Minería de Datos y Análisis Reproducible
**Institución:** Instituto Tecnológico de Santiago del Estero (ITSE)  
**Materia:** Minería de Datos I  
**Estudiante:** Yannina Alejandra Luna  

## 📌 Descripción del Proyecto
Este repositorio contiene el desarrollo completo del Proyecto Integrador de Minería de Datos, enfocado en el análisis masivo, limpieza con trazabilidad y reducción de dimensionalidad de un conjunto de datos estructurado. El flujo de trabajo está diseñado bajo estándares profesionales de ciencia de datos, garantizando la reproducibilidad de cada etapa mediante Jupyter Notebooks y una interfaz interactiva de visualización.

## 📁 Estructura del Repositorio
* `notebooks/`: Proceso secuencial dividido en 5 notebooks (.ipynb):
  * `01_inspeccion_inicial.ipynb` - Análisis de tipos de datos y estructuras.
  * `02_limpieza_trazabilidad.ipynb` - Tratamiento de nulos, duplicados y outliers.
  * `03_eda_exploratorio.ipynb` - Análisis exploratorio de datos y correlaciones.
  * `04_pca_dimensionalidad.ipynb` - Reducción de dimensions mediante PCA.
  * `05_modelado_final.ipynb` - Implementación de modelos de minería.
* `app/`: Código fuente de la aplicación interactiva desplegada en **Streamlit** (`app.py`).
* `logs/`: Archivos log de control (`limpieza_log.txt`) que registran la trazabilidad de los cambios en los datos.
* `docs/`: Informe técnico final del proyecto en formato PDF.

## 🛠️ Tecnologías Utilizadas
* **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
* **Jupyter Notebooks**
* **Streamlit** (para la aplicación del Dashboard)
* **Git & GitHub** (para el control de versiones)

## 🚀 Cómo Ejecutar la Aplicación
1. Clonar este repositorio.
2. Instalar las dependencias necesarias.
3. Ejecutar en la terminal de la consola:
   ```bash
   streamlit run app/app.py
