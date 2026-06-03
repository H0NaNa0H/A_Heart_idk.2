import streamlit as st
import streamlit.components.v1 as components
import time
import random

# Aesthetic webpage configuration (Dark Mode)
st.set_page_config(
    page_title="Terminal v1.0",
    page_icon="💚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS INTEGRADO ---
terminal_css = """
<style>
    .stApp { background-color: #0d0d0d !important; }
    header, footer { visibility: hidden !important; }
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght=400;700&display=swap');
    
    .terminal-text { font-family: 'Fira Code', monospace !important; color: #39FF14 !important; text-shadow: 0 0 5px rgba(57, 255, 20, 0.7); font-size: 18px; line-height: 1.6; }
    .terminal-header { font-family: 'Fira Code', monospace !important; color: #39FF14 !important; text-shadow: 0 0 10px rgba(57, 255, 20, 0.9); font-size: 28px; font-weight: bold; text-align: center; border-bottom: 2px solid #39FF14; padding-bottom: 10px; margin-bottom: 30px; }
    
    .stButton>button { background-color: transparent !important; color: #39FF14 !important; border: 2px solid #39FF14 !important; border-radius: 5px !important; font-family: 'Fira Code', monospace !important; font-weight: bold !important; font-size: 16px !important; transition: all 0.3s ease !important; width: 100%; }
    .stButton>button:hover { background-color: #39FF14 !important; color: #0d0d0d !important; }
    
    .heart-container { display: flex; justify-content: center; align-items: center; height: 200px; margin-top: 20px; }
    .css-heart { position: relative; width: 100px; height: 90px; animation: heartbeat 1s infinite; }
    .css-heart:before, .css-heart:after { position: absolute; content: ""; left: 50px; top: 0; width: 50px; height: 80px; background: #39FF14; border-radius: 50px 50px 0 0; transform: rotate(-45deg); transform-origin: 0 100%; }
    .css-heart:after { left: 0; transform: rotate(45deg); transform-origin: 100% 100%; }
    @keyframes heartbeat { 0%, 100% { transform: scale(0.9); } 30% { transform: scale(1.1); } }
    
    .skull { position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999; animation: fall linear forwards; }
    @keyframes fall { 100% { transform: translateY(110vh) rotate(360deg); opacity: 0; } }
</style>
"""
st.markdown(terminal_css, unsafe_allow_html=True)

# --- LÓGICA DEL MINIJUEGO DE LA BOMBA (PERSEGUIDORA) ---
bomb_html = """
<div id="bomb" style="position:absolute; font-size:30px; z-index:10000; left:50px; top:50px; pointer-events:none;">💣</div>
<script>
    const bomb = document.getElementById('bomb');
    // Inicializamos las coordenadas en el centro de la pantalla
    let mx = window.innerWidth / 2;
    let my = window.innerHeight / 2;
    let bx = mx, by = my, vx = 0, vy = 0;

    // Seguimos al ratón en cualquier posición del viewport
    window.addEventListener('mousemove', e => { 
        mx = e.clientX; 
        my = e.clientY; 
    });

    function animate() {
        // Aceleración suave hacia el cursor
        vx += (mx - bx) * 0.002;
        vy += (my - by) * 0.002;
        
        // Fricción para suavizar el desplazamiento
        bx += vx *= 0.90;
        by += vy *= 0.90;
        
        // Aplicamos la posición
        bomb.style.left = bx + 'px';
        bomb.style.top = by + 'px';
        
        requestAnimationFrame(animate);
    }
    animate();
</script>
"""

# --- INICIALIZACIÓN DE ESTADOS ---
if 'warning_accepted' not in st.session_state: st.session_state.warning_accepted = False
if 'acceso_concedido' not in st.session_state: st.session_state.acceso_concedido = False
if 'show_bomb_game' not in st.session_state: st.session_state.show_bomb_game = False

# --- FLUJO ---
if not st.session_state.warning_accepted:
    st.markdown('<div class="terminal-header">[ !!! SECURITY WARNING !!! ]</div>', unsafe_allow_html=True)
    if st.button("PROCEED ANYWAY"):
        st.session_state.warning_accepted = True
        st.rerun()
else:
    if not st.session_state.acceso_concedido:
        if st.button("CLICK TO VALIDATE"):
            st.session_state.acceso_concedido = True
            st.rerun()
    else:
        st.markdown('<div class="terminal-header">[ SYSTEM INITIALIZED ]</div>', unsafe_allow_html=True)
        
        # Botón para activar el minijuego
        if st.button("⚠️ ACTIVATE BOMBA ⚠️"):
            st.session_state.show_bomb_game = True
        
        if st.session_state.show_bomb_game:
            components.html(bomb_html, height=0)
            st.markdown('<p class="terminal-text" style="color:red;">> WARNING: BOMB_ACTIVE</p>', unsafe_allow_html=True)
            # Renderizado condicional
        if st.session_state.get('show_bomb_game', False):
            # Usamos un height mayor para ver que el script se carga
            components.html(bomb_html, height=100) 
            st.write("Juego activo en segundo plano...")

        # Contenido original
        st.markdown('<p class="terminal-text">> [ACCESS GRANTED] Hi, Kralj!</p>', unsafe_allow_html=True)
        st.markdown('<div class="heart-container"><div class="css-heart"></div></div>', unsafe_allow_html=True)
