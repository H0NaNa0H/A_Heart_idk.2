import streamlit as st
import time
# -------------------------------------------------------------
# CAMBIO 1: Importamos la librería 'random' para poder generar
# valores aleatorios (posiciones, tamaños y velocidades de las calaveras)
# -------------------------------------------------------------
import random

# Aesthetic webpage configuration (Dark Mode)
# IMPORTANT! This must be the very first Streamlit command executed
st.set_page_config(
    page_title="Terminal v1.0",
    page_icon="💚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to transform Streamlit into a hacker/coder terminal with custom skull rain
terminal_css = """
<style>
    /* Dark terminal background and hide default UI elements */
    .stApp {
        background-color: #0d0d0d !important;
    }
    header, footer {
        visibility: hidden !important;
    }
    
    /* Neon green console font */
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght=400;700&display=swap');
    
    .terminal-text {
        font-family: 'Fira Code', monospace !important;
        color: #39FF14 !important; /* Neon Green */
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
    
    /* Custom console-style button */
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
    
    /* CSS animated 3D heartbeat */
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
        background: #39FF14; /* Neon green heart */
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

    /* ------------------------------------------------------------- */
    /* CAMBIO 2: Estilos CSS para el diseño y movimiento de las calaveras. */
    /* Definimos que empiecen flotando arriba, vayan bajando y rotando */
    /* ------------------------------------------------------------- */
    .skull {
        position: fixed;
        top: -10%;            /* Aparecen justo encima del borde superior */
        user-select: none;    /* Evita que el usuario las pueda seleccionar sin querer */
        pointer-events: none; /* Permite hacer clic "a través" de ellas */
        z-index: 9999;        /* Las posiciona por encima de todo el contenido */
        animation: fall linear forwards; /* Aplica la animación de caída */
    }
    
    @keyframes fall {
        0% {
            transform: translateY(0) rotate(0deg); /* Empieza sin caída y derecha */
            opacity: 1;                            /* Totalmente visible */
        }
        90% {
            opacity: 0.9;                          /* Sigue muy visible antes del final */
        }
        100% {
            transform: translateY(110vh) rotate(360deg); /* Cae hasta el fondo y da una vuelta completa */
            opacity: 0;                                  /* Se desvanece por completo */
        }
    }

    /* Estilos para el bloque de Advertencia / Alerta de Seguridad */
    .warning-box {
        background-color: #1a0f00;
        border: 2px solid #ffaa00;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 25px;
    }
    .warning-text {
        font-family: 'Fira Code', monospace !important;
        color: #ffaa00 !important;
        text-shadow: 0 0 5px rgba(255, 170, 0, 0.7);
        font-size: 16px;
        line-height: 1.6;
    }
</style>
"""

# Apply the custom CSS
st.markdown(terminal_css, unsafe_allow_html=True)

# -------------------------------------------------------------
# NUEVO FLUJO: Página de Warning de Malware / Regalo Bomba
# -------------------------------------------------------------
if 'warning_accepted' not in st.session_state:
    st.session_state.warning_accepted = False

if not st.session_state.warning_accepted:
    # Encabezado rojo/naranja de advertencia
    st.markdown('<div class="terminal-header" style="color: #ff3333 !important; border-bottom-color: #ff3333 !important; text-shadow: 0 0 10px rgba(255, 51, 51, 0.9);">[ !!! SECURITY WARNING !!! ]</div>', unsafe_allow_html=True)
    
    st.markdown('''
        <div class="warning-box">
            <p class="warning-text">> SYSTEM DETECTED A SUSPICIOUS CONNECTION FROM: NaNa.EXE</p>
            <p class="warning-text">> Threat classification: SARCASM_HEAVY_LOAD</p>
            <p class="warning-text" style="color: #ff3333 !important; text-shadow: 0 0 5px rgba(255, 51, 51, 0.7); font-weight: bold; margin-top: 15px;">
                WARNING: This is totally NOT a malware... or is it?
            </p>
            <p class="warning-text" style="margin-top: 10px;">
                But honestly, next time you should probably think twice before clicking random links or opening untrusted packages.
            </p>
            <p class="warning-text" style="margin-top: 10px; font-style: italic;">
                Otherwise, next birthday I might actually send you a real bomb instead of a present ;).
            </p>
            <p class="warning-text" style="margin-top: 15px; font-weight: bold;">> Are you sure you want to proceed and run the executable?</p>
        </div>
    ''', unsafe_allow_html=True)
    
    if st.button("PROCEED ANYWAY (I TRUST NANA)"):
        st.session_state.warning_accepted = True
        st.rerun()

else:
    # Console-style header
    st.markdown('<div class="terminal-header">[ SYSTEM INITIALIZATION NaNa.EXE ]</div>', unsafe_allow_html=True)

    # Interactive initialization messages
    st.markdown('<p class="terminal-text">> Loading modules...</p>', unsafe_allow_html=True)
    st.markdown('<p class="terminal-text">> Connecting to server: my_illness_ip...</p>', unsafe_allow_html=True)

    # Create an interactive "Access" button using session state
    if 'acceso_concedido' not in st.session_state:
        st.session_state.acceso_concedido = False

    if not st.session_state.acceso_concedido:
        st.markdown('<p class="terminal-text">> WARNING: Identity verification required.</p>', unsafe_allow_html=True)
        if st.button("CLICK TO VALIDATE"):
            st.session_state.acceso_concedido = True
            st.rerun()
    else:
        # Quick hacker-like loading simulation
        with st.spinner("Processing data..."):
            time.sleep(1)
        
        # -------------------------------------------------------------
        # CAMBIO 3: Bucle generador de lluvia de calaveras.
        # En lugar de st.balloons(), construimos HTML dinámico con Python
        # -------------------------------------------------------------
        skulls_html = ""
        for _ in range(45): # Generamos 45 calaveras individuales
            left_pos = random.randint(1, 99)   # Posición en el ancho de la pantalla (1% al 99% de ancho)
            delay = random.uniform(0, 3.5)     # Tiempo de retraso aleatorio antes de empezar a caer (segundos)
            duration = random.uniform(2.5, 6)  # Tiempo de duración (velocidad) de la caída (segundos)
            size = random.randint(18, 38)      # Tamaño aleatorio de la calavera en píxeles (px)
            
            # Juntamos los datos generados en una etiqueta HTML 'div'
            skulls_html += f'<div class="skull" style="left: {left_pos}vw; animation-delay: {delay}s; animation-duration: {duration}s; font-size: {size}px;">💀</div>'
            
        # Inyectamos el bloque completo de calaveras en el navegador
        st.markdown(skulls_html, unsafe_allow_html=True)
        
        st.markdown('<p class="terminal-text" style="color: #00ffcc !important;">> [ACCESS GRANTED] Hi, Kralj! </p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="terminal-text">> ERROR 404: cuz idk like always.</p>', 
            unsafe_allow_html=True
        )
        st.markdown('<p class="terminal-text">> Executing protocol "Constant pain"...</p>', unsafe_allow_html=True)
        
        # Render our beautiful CSS neon green beating heart
        st.markdown('<div class="heart-container"><div class="css-heart"></div></div>', unsafe_allow_html=True)
        
        # -------------------------------------------------------------
        # NUEVO CAMBIO: Estado de sesión para saber si se hizo clic en el corazón
        # -------------------------------------------------------------
        if 'heart_clicked' not in st.session_state:
            st.session_state.heart_clicked = False
        
        # Botón interactivo debajo del corazón con estilo de terminal hacker
        if st.button("💚 [ INTERACT WITH CONSTANT_HEART.SYS ] 💚"):
            st.session_state.heart_clicked = True
            
        if st.session_state.heart_clicked:
            st.markdown('<p class="terminal-text" style="color: #ff0055 !important;">> [DECRYPTING HEART_LOG.TXT...]</p>', unsafe_allow_html=True)
            time.sleep(0.3)
            st.markdown(
                '<p class="terminal-text" style="background-color: #1a0000; border: 1px solid #ff0055; padding: 15px; border-radius: 5px; font-weight: bold; color: #ff3366 !important;">'
                '>> "Don\'t get used to this because I\'m just learning and I\'m not good at these things, let alone being \'romantic?\'"'
                '</p>', 
                unsafe_allow_html=True
            )
        
        # Final dedication message
        st.markdown(
            '<p class="terminal-text" style="text-align: center; font-size: 20px; font-weight: bold; margin-top: 30px;">'
            'Tbh idk what to put here so; I love u i guess...'
            '</p>', 
            unsafe_allow_html=True
        )
