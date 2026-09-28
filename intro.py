import streamlit as st
import base64
import os


def obtener_imagen_base64(ruta_imagen):
    if os.path.exists(ruta_imagen):
        with open(ruta_imagen, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None


# 1. Configuración básica de la página
st.set_page_config(
    page_title="Portafolio de Aplicaciones", 
    page_icon="🎓", 
    layout="wide"
)

# 2. Inyección de CSS para el diseño minimalista (modo claro, tarjetas, sombras)
st.markdown("""
<style>
/* Fondo de toda la aplicación */
.stApp {
    background-color: #f4f6f9;
}

/* Título principal superior */
.main-title {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    color: #1e293b;
    font-size: 1.5rem;
    font-weight: 600;
    padding-bottom: 15px;
    border-bottom: 1px solid #cbd5e1;
    margin-bottom: 30px;
    margin-top: 10px;
}

/* Estructura de la tarjeta */
.card {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
    text-decoration: none;
    color: inherit;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    height: 130px;
    border: 1px solid #f1f5f9;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.08);
}

/* Contenedor izquierdo para la imagen/ícono */
.card-img-container {
    width: 80px;
    height: 80px;
    background-color: #f8fafc;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-shrink: 0;
    font-size: 2.2rem; /* Tamaño del emoji si no hay imagen */
    overflow: hidden;
    border: 1px solid #e2e8f0;
}

/* Ajuste para cuando agregues tus propias imágenes */
.card-img-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Contenedor derecho para los textos */
.card-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    overflow: hidden;
    width: 100%;
}

.card-title {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 1rem;
    color: #0f172a;
    margin: 0 0 4px 0;
    line-height: 1.2;
}

.card-url {
    font-size: 0.75rem;
    color: #64748b;
    margin: 0 0 10px 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Estilo de la etiqueta (Clasificación, Regresión, etc.) */
.card-tag {
    font-size: 0.65rem;
    font-weight: 600;
    background-color: #f1f5f9;
    color: #475569;
    padding: 3px 8px;
    border-radius: 12px;
    align-self: flex-start;
    display: inline-block;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
</style>
""", unsafe_allow_html=True)

# 3. Título de la página
st.markdown('<div class="main-title">PORTAFOLIO DE APLICACIONES - PROGRAMACIÓN AVANZADA.</div>', unsafe_allow_html=True)

# 4. Diccionario con la información de tus apps
# He deducido las categorías (Clasificación, Regresión, etc.) basado en el tipo de app.
apps = [
    {"title": "¿Qué fruta es más parecida?", "url": "https://classfruta-f.streamlit.app/", "tag": "Clasificación", "imagen": "ClasificacionFrutas.jpeg"},
    {"title": "Predictor de Sensación Térmica", "url": "https://detertorhumedad-nvjwjmhhrsty7bwfgstxa3.streamlit.app/", "tag": "Regresión", "imagen": "RegrecionPredictiva.jpeg"},
    {"title": "Descenso de Gradiente Interactivo", "url": "https://classgradiente-rilcadzxbznff36rzktne4.streamlit.app/#descenso-de-gradiente-interactivo", "tag": "Optimización", "imagen": "DesensoGradiente.jpeg"},
    {"title": "Diagnóstico de fertilidad del suelo", "url": "https://fertilidadearth-rfvcy72pchvfvwzgd5wdlg.streamlit.app/", "tag": "Clasificación", "imagen": "ClasificacionFertilidad.jpeg"},
    {"title": "¿Lloverá mañana? — Reg. Logística", "url": "https://modelostemphumedviento-6b2ajmpd6qz9scxbakf4uz.streamlit.app/", "tag": "Regresión", "imagen": "RegrecionLogistica.jpeg"},
    {"title": "Detector de Anomalías", "url": "https://arc.net/l/quote/xoxiyzae", "tag": "Big-O", "imagen": "Big-OComplexity.jpeg"},
    {"title": "Series de tiempo reales", "url": "https://processdata-pqmxqgcg4yacx9gpcowjsh.streamlit.app/", "tag": "Forecasting", "imagen": "SeriesTiempoReal.jpeg"},
    {"title": "Predictor de calidad del aire", "url": "https://pronosticomodelo-9pytzljfpl47tmyrlntbde.streamlit.app/", "tag": "Regresión", "imagen": "seriesLinealesArima.jpeg"},
    {"title": "Regresión — Conceptos clave", "url": "https://regrecionclass-9zycjwxkrqzg3reuqub5zr.streamlit.app/", "tag": "Optimización", "imagen": "Regression.jpeg"},
    {"title": "Series de Tiempo — Sensor IoT", "url": "https://sensorsimulado-by8ou9uzu8yw4nxbzegbdt.streamlit.app/", "tag": "Streaming", "imagen": "SeriesTiempoReal.jpeg"}, # Reutilizando imagen si no tienes una específica
    {"title": "Nivel de ríos y quebradas", "url": "https://tallerportafolio1-df6dptfca4jgc7gf2nzoq8.streamlit.app/", "tag": "Forecasting", "imagen": "NivelRiosQUbradas.jpeg"}
]

# Generar la cuadrícula de 3 columnas
cols = st.columns(3)

for idx, app in enumerate(apps):
    col = cols[idx % 3]
    
    # Limpiamos un poco la URL
    display_url = app['url'].replace('https://', '').split('/')[0]
    
    # Obtenemos el código Base64 de la imagen
    img_base64 = obtener_imagen_base64(app['imagen'])
    
    # Si la imagen existe, creamos el tag <img> con el base64. Si no, ponemos un emoji por defecto.
    if img_base64:
        img_html = f'<img src="data:image/jpeg;base64,{img_base64}" alt="{app["title"]}">'
    else:
        img_html = '📁' # Emoji de respaldo en caso de que escribas mal el nombre del archivo
    
    card_html = f"""
    <a href="{app['url']}" target="_blank" class="card">
        <div class="card-img-container">
            {img_html}
        </div>
        <div class="card-content">
            <h3 class="card-title">{app['title']}</h3>
            <p class="card-url">{display_url}</p>
            <span class="card-tag">{app['tag']}</span>
        </div>
    </a>
    """
    
    col.markdown(card_html, unsafe_allow_html=True)
