import streamlit as st
import time
import random

# Aesthetic webpage configuration (Dark Mode)
st.set_page_config(
    page_title="Terminal v1.0",
    page_icon="💚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS con el script de la bomba incluido y persistente
terminal_css = """
<style>
    .stApp { background-color: #0d0d0d !important; }
    header, footer { visibility: hidden !important; }
    
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap');
    
    .terminal-text { font-family: 'Fira Code', monospace !important; color: #39FF14 !important; text-shadow: 0 0 5px rgba(57, 255, 20, 0.7); font-size: 18px; line-height: 1.6; }
    .terminal-header { font-family: 'Fira Code', monospace !important; color: #39FF14 !important; text-shadow: 0 0 10px rgba(57, 255, 20, 0.9); font-size: 28px; font-weight: bold; text-align: center; border-bottom: 2px solid #39FF14; padding-bottom: 10px; margin-bottom: 30px; }
    
    .stButton>button { background-color: transparent !important; color: #39FF14 !important; border: 2px solid #39FF14 !important; border-radius: 5px !important; font-family: 'Fira Code', monospace !important; font-weight: bold !important; font-size: 16px !important; text-shadow: 0 0 3px rgba(57, 255, 20, 0.5); box-shadow: 0 0 8px rgba(57, 255, 20, 0.3) !important; transition: all 0.3s ease !important; width: 100%; }
    .stButton>button:hover { background-color: #39FF14 !important; color: #0d0d0d !important; box-shadow: 0 0 15px rgba(57, 255, 20, 0.8) !important; }
    
    .heart-container { display: flex; justify-content: center; align-items: center; height: 200px; margin-top: 20px; margin-bottom: 20px; }
    .css-heart { position: relative; width: 100px; height: 90px; animation: heartbeat 1s infinite; transform-origin: center; }
    .css-heart:before, .css-heart:after { position: absolute; content: ""; left: 50px; top: 0; width: 50px; height: 80px; background: #39FF14; border-radius: 50px 50px 0 0; transform: rotate(-45deg); transform-origin: 0 100%; box-shadow: 0 0 20px rgba(57, 255, 20, 0.8); }
    .css-heart:after { left: 0; transform: rotate(45deg); transform-origin: 100% 100%; }
    @keyframes heartbeat { 0% { transform: scale(0.9); } 30% { transform: scale(1.1); } 60% { transform: scale(0.95); } 100% { transform: scale(0.9); } }

    .skull { position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999; animation: fall linear forwards; }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); opacity: 1; } 90% { opacity: 0.9; } 100% { transform: translateY(110vh) rotate(360deg); opacity: 0; } }

    .warning-box { background-color: #1a0f00; border: 2px solid #ffaa00; padding: 20px; border-radius: 5px; margin-bottom: 25px; }
    .warning-text { font-family: 'Fira Code', monospace !important; color: #ffaa00 !important; text-shadow: 0 0 5px rgba(255, 170, 0, 0.7); font-size: 16px; line-height: 1.6; }

    /* Cursor bomba */
    #cursor-bomb { position: fixed; pointer-events: none; font-size: 30px; z-index: 999999; display: none; }
</style>

<div id="cursor-bomb">💣</div>

<script>
    const bomb = document.getElementById('cursor-bomb');
    
    // Función para actualizar posición
    window.addEventListener('mousemove', (e) => {
        bomb.style.left = (e.clientX + 15) + 'px';
        bomb.style.top = (e.clientY + 15) + 'px';
    });

    // Detectar si el acceso ya fue concedido previamente
    const access = localStorage.getItem('acceso_concedido');
    if (access === 'true') {
        document.body.style.cursor = 'none';
        bomb.style.display = 'block';
    }
</script>
"""

st.markdown(terminal_css, unsafe_allow_html=True)

if 'warning_accepted' not in st.session_state:
    st.session_state.warning_accepted = False

if not st.session_state.warning_accepted:
    st.markdown('<div class="terminal-header" style="color: #ff3333 !important; border-bottom-color: #ff3333 !important; text-shadow: 0 0 10px rgba(255, 51, 51, 0.9);">[ !!! SECURITY WARNING !!! ]</div>', unsafe_allow_html=True)
    st.markdown('''
        <div class="warning-box">
            <p class="warning-text">> SYSTEM DETECTED A SUSPICIOUS CONNECTION FROM: NaNa.EXE</p>
            <p class="warning-text" style="color: #ff3333 !important; text-shadow: 0 0 5px rgba(255, 51, 51, 0.7); font-weight: bold; margin-top: 15px;">
                WARNING: This is totally NOT a malware...
            </p>
            <p class="warning-text" style="margin-top: 15px; font-weight: bold;">> Are you sure you want to proceed and run the executable?</p>
        </div>
    ''', unsafe_allow_html=True)
    
    if st.button("PROCEED ANYWAY (I TRUST NANA)"):
        st.session_state.warning_accepted = True
        st.rerun()

else:
    st.markdown('<div class="terminal-header">[ SYSTEM INITIALIZATION NaNa.EXE ]</div>', unsafe_allow_html=True)
    
    if 'acceso_concedido' not in st.session_state:
        st.session_state.acceso_concedido = False

    if not st.session_state.acceso_concedido:
        if st.button("CLICK TO VALIDATE"):
            st.session_state.acceso_concedido = True
            # Guardamos estado en localstorage para que el JS lo detecte tras el rerun
            st.markdown("<script>localStorage.setItem('acceso_concedido', 'true'); document.body.style.cursor = 'none'; document.getElementById('cursor-bomb').style.display = 'block';</script>", unsafe_allow_html=True)
            st.rerun()
    else:
        # Forzamos la visibilidad de la bomba en cada render
        st.markdown("<script>document.body.style.cursor = 'none'; document.getElementById('cursor-bomb').style.display = 'block';</script>", unsafe_allow_html=True)
        
        skulls_html = "".join([f'<div class="skull" style="left: {random.randint(1,99)}vw; animation-delay: {random.uniform(0, 3)}s; animation-duration: {random.uniform(3, 6)}s; font-size: {random.randint(18, 38)}px;">💀</div>' for _ in range(45)])
        st.markdown(skulls_html, unsafe_allow_html=True)
        
        st.markdown('<p class="terminal-text" style="color: #00ffcc !important;">> [ACCESS GRANTED] Hi, Kralj! </p>', unsafe_allow_html=True)
        st.markdown('<div class="heart-container"><div class="css-heart"></div></div>', unsafe_allow_html=True)
        
        if 'heart_clicked' not in st.session_state:
            st.session_state.heart_clicked = False
        
        if st.button("💚 [ INTERACT WITH CONSTANT_HEART.SYS ] 💚"):
            st.session_state.heart_clicked = True
            
        if st.session_state.heart_clicked:
            st.markdown('<p class="terminal-text" style="color: #ff0055 !important;">> [DECRYPTING HEART_LOG.TXT...]</p>', unsafe_allow_html=True)
            st.markdown('<p class="terminal-text" style="background-color: #1a0000; border: 1px solid #ff0055; padding: 15px; border-radius: 5px; color: #ff3366 !important;">>> "Don\'t get used to this..."</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="terminal-text" style="text-align: center; font-size: 20px; font-weight: bold; margin-top: 30px;">Tbh idk what to put here so; I love u i guess...</p>', unsafe_allow_html=True)
