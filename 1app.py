
# Configuración estética de la página web (Tema Oscuro)
st.set_page_config(
    page_title="Terminal de Amor v1.0",
    page_icon="💚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS personalizado para transformar Streamlit en una terminal de hacker/coder
terminal_css = """
<style>
    /* Fondo negro de terminal y ocultar elementos innecesarios */
    .stApp {
        background-color: #0d0d0d !important;
    }
    header, footer {
        visibility: hidden !important;
    }
    
    /* Fuente de consola color verde neón */
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap');
    
    .terminal-text {
        font-family: 'Fira Code', monospace !important;
        color: #39FF14 !important; /* Verde Neón */
        text-shadow: 0 0 5px rgba(57, 255, 20, 0.7);
        font-size: 18px;
        line-height: 1.6;
    }
    
    .terminal-header {
        font-family: 'Fira Code', monospace !important;
        color: #39FF14 !important;
        text-shadow: 0 0 10px rgba(57, 255, 20, 0.9);
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        border-bottom: 2px solid #39FF14;
        padding-bottom: 10px;
        margin-bottom: 30px;
    }
    
    /* Botón personalizado estilo consola */
    .stButton>button {
        background-color: transparent !important;
        color: #39FF14 !important;
        border: 2px solid #39FF14 !important;
        border-radius: 5px !important;
        font-family: 'Fira Code', monospace !important;
        font-weight: bold !important;
        font-size: 16px !important;
        text-shadow: 0 0 3px rgba(57, 255, 20, 0.5);
        box-shadow: 0 0 8px rgba(57, 255, 20, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #39FF14 !important;
        color: #0d0d0d !important;
        box-shadow: 0 0 15px rgba(57, 255, 20, 0.8) !important;
    }
    
    /* El Corazón animado por CSS (Latido 3D) */
    .heart-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    .css-heart {
        position: relative;
        width: 100px;
        height: 90px;
        animation: heartbeat 1s infinite;
        transform-origin: center;
    }
    
    .css-heart:before,
    .css-heart:after {
        position: absolute;
        content: "";
        left: 50px;
        top: 0;
        width: 50px;
        height: 80px;
        background: #39FF14; /* Corazón verde neón a juego */
        border-radius: 50px 50px 0 0;
        transform: rotate(-45deg);
        transform-origin: 0 100%;
        box-shadow: 0 0 20px rgba(57, 255, 20, 0.8);
    }
    
    .css-heart:after {
        left: 0;
        transform: rotate(45deg);
        transform-origin: 100% 100%;
    }
    
    @keyframes heartbeat {
        0% { transform: scale(0.9); }
        30% { transform: scale(1.1); }
        60% { transform: scale(0.95); }
        100% { transform: scale(0.9); }
    }
</style>
"""

# Aplicar el CSS personalizado
st.markdown(terminal_css, unsafe_allow_html=True)

# Encabezado estilo terminal
st.markdown('<div class="terminal-header">[ SYSTEM INITIALIZATION DE_AMOR.EXE ]</div>', unsafe_allow_html=True)

# Mensaje de inicialización interactivo
st.markdown('<p class="terminal-text">> Cargando módulos de sentimientos...</p>', unsafe_allow_html=True)
st.markdown('<p class="terminal-text">> Conectando con servidor: mi_corazón_ip...</p>', unsafe_allow_html=True)

# Creamos un botón interactivo de "Acceso"
if 'acceso_concedido' not in st.session_state:
    st.session_state.acceso_concedido = False

if not st.session_state.acceso_concedido:
    st.markdown('<p class="terminal-text">> ADVERTENCIA: Se requiere verificación de identidad.</p>', unsafe_allow_html=True)
    if st.button("HACER CLIC PARA VALIDAR AMOR"):
        st.session_state.acceso_concedido = True
        st.rerun()
else:
    # Simulación de carga hacker súper rápida
    with st.spinner("Procesando datos..."):
        time.sleep(1)
    
    st.balloons() # Lluvia de globos para festejar el acceso
    
    st.markdown('<p class="terminal-text" style="color: #00ffcc !important;">> [ACCESO CONCEDIDO] ¡Hola, mi amor! ❤️</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="terminal-text">> ERROR 404: La cantidad de amor que siento por ti ha superado el espacio de almacenamiento del disco duro local.</p>', 
        unsafe_allow_html=True
    )
    st.markdown('<p class="terminal-text">> Ejecutando protocolo "Latido Constante"...</p>', unsafe_allow_html=True)
    
    # Renderizamos nuestro hermoso corazón animado con CSS verde neón
    st.markdown('<div class="heart-container"><div class="css-heart"></div></div>', unsafe_allow_html=True)
    
    # Dedicatoria de cierre
    st.markdown(
        '<p class="terminal-text" style="text-align: center; font-size: 20px; font-weight: bold;">'
        'Sinceramente tuyo/a desde la primera línea de código. ¡Te amo con todo mi sistema operativo! 🥰'
        '</p>', 
        unsafe_allow_html=True