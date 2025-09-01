Este proyecto corresponde al **Sprint 7 del Bootcamp de Data Analyst**.  
El objetivo es crear y desplegar una **aplicación web interactiva** con **Streamlit**, mostrando un análisis exploratorio de datos.

---

## 📊 Dataset
Se utilizó un dataset público de **vehículos eléctricos registrados en EE. UU.**, que contiene información sobre:
- Año del modelo (`Model Year`)  
- Fabricante y modelo (`Make`, `Model`)  
- Tipo de vehículo (`Battery Electric Vehicle`, `Plug-in Hybrid`, etc.)  
- Rango eléctrico (`Electric Range`)  
- Ubicación geográfica  

---

## 🚀 Funcionalidad de la aplicación
La aplicación permite al usuario explorar los datos mediante gráficos interactivos:

- ✅ **Histograma de años de los vehículos eléctricos**  
- ✅ **Gráfico de dispersión** que muestra la relación entre `Model Year` y `Electric Range`  
- ✅ Interacción mediante **casillas de verificación** (`st.checkbox`)  

Tecnologías usadas:
- Python  
- Pandas  
- Plotly Express  
- Streamlit  

---

## 📂 Estructura del proyecto

├── README.md
├── app.py
├── requirements.txt
├── vehicles_us.csv
└── notebooks
└── EDA.ipynb

---

## 🌐 Deploy
La aplicación está desplegada en **Render** y disponible públicamente en:  
👉 [https://sprint7-app-6b4b.onrender.com](https://sprint7-app-6b4b.onrender.com)

---

## 📝 Notas
- Este proyecto cumple con los criterios de evaluación solicitados en el Sprint 7:  
  - Encabezado en la app  
  - Al menos un histograma  
  - Al menos un gráfico de dispersión  
  - Botón o casilla de verificación para mostrar los gráficos  
  - App accesible públicamente  
