import streamlit as st
import time
import random

# 1. Configuración de página
st.set_page_config(
    page_title="Terminal v1.0",
    page_icon="💚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS Global (Todo el estilo va aquí, ordenado)
terminal_css = """
<style>
    .stApp { background-color: #0d0d0d !important; }
    header, footer { visibility: hidden !important; }
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght=400;700&display=swap');
    
    .terminal-text { font-family: 'Fira Code', monospace !important; color: #39FF14 !important; font-size: 18px; line-height: 1.6; }
    .terminal-header { font-family: 'Fira Code', monospace !important; color: #39FF14 !important; text-shadow: 0 0 10px rgba(57, 255, 20, 0.9); font-size: 28px; font-weight: bold; text-align: center; border-bottom: 2px solid #39FF14; padding-bottom: 10px; margin-bottom: 30px; }
    
    .stButton>button { background-color: transparent !important; color: #39FF14 !important; border: 2px solid #39FF14 !important; border-radius: 5px !important; font-family: 'Fira Code', monospace !important; font-weight: bold !important; width: 100%; }
    .stButton>button:hover { background-color: #39FF14 !important; color: #0d0d0d !important; }
    
    /* Calaveras */
    .skull { position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999; animation: fall linear forwards; }
    @keyframes fall { to { transform: translateY(110vh) rotate(360deg); opacity: 0; } }

    /* Estilo de la bomba */
    .bomb-cursor { position: fixed; font-size: 25px; pointer-events: none; z-index: 10000; text-shadow: 0 0 5px #39FF14; }
    
    /* Corazón */
    .heart-container { display: flex; justify-content: center; align-items: center; height: 200px; margin-top: 20px; margin-bottom: 20px; }
    .css-heart { position: relative; width: 100px; height: 90px; animation: heartbeat 1s infinite; transform-origin: center; }
    .css-heart:before, .css-heart:after { position: absolute; content: ""; left: 50px; top: 0; width: 50px; height: 80px; background: #39FF14; border-radius: 50px 50px 0 0; transform: rotate(-45deg); transform-origin: 0 100%; box-shadow: 0 0 20px rgba(57, 255, 20, 0.8); }
    .css-heart:after { left: 0; transform: rotate(45deg); transform-origin: 100% 100%; }
    @keyframes heartbeat { 0% { transform: scale(0.9); } 30% { transform: scale(1.1); } 60% { transform: scale(0.95); } 100% { transform: scale(0.9); } }

    /* Box de advertencia */
    .warning-box { background-color: #1a0f00; border: 2px solid #ffaa00; padding: 20px; border-radius: 5px; margin-bottom: 25px; }
    .warning-text { font-family: 'Fira Code', monospace !important; color: #ffaa00 !important; font-size: 16px; }
</style>
"""
st.markdown(terminal_css, unsafe_allow_html=True)

# 3. Lógica principal
if 'warning_accepted' not in st.session_state: st.session_state.warning_accepted = False

if not st.session_state.warning_accepted:
    st.markdown('<div class="terminal-header" style="color: #ff3333 !important; border-bottom-color: #ff3333 !important;">[ !!! SECURITY WARNING !!! ]</div>', unsafe_allow_html=True)
    if st.button("PROCEED ANYWAY (I TRUST NANA)"):
        st.session_state.warning_accepted = True
        st.rerun()
else:
    # Si ya pasó el warning, verificamos el acceso
    if 'acceso_concedido' not in st.session_state: st.session_state.acceso_concedido = False
    
    if not st.session_state.acceso_concedido:
        st.markdown('<div class="terminal-header">[ SYSTEM INITIALIZATION NaNa.EXE ]</div>', unsafe_allow_html=True)
        st.markdown('<p class="terminal-text">> WARNING: Identity verification required.</p>', unsafe_allow_html=True)
        if st.button("CLICK TO VALIDATE"):
            st.session_state.acceso_concedido = True
            st.rerun()
    else:
        # A. INYECCIÓN DE LA BOMBA (Solo al acceder)
        st.markdown("""
        <div id="bomb" class="bomb-cursor">💣</div>
        <script>
            const bomb = document.getElementById('bomb');
            let bx = window.innerWidth/2, by = window.innerHeight/2;
            let mx = 0, my = 0;
            document.addEventListener('mousemove', (e) => { mx = e.clientX; my = e.clientY; });
            
            function animate() {
                // La bomba sigue al cursor
                bx += (mx - bx) * 0.05; 
                by += (my - by) * 0.05;
                bomb.style.left = bx + 'px'; 
                bomb.style.top = by + 'px';
                
                // Detección de colisión
                if (Math.hypot(bx - mx, by - my) < 30) {
                    document.body.innerHTML = '<div style="display:flex; justify-content:center; align-items:center; height:100vh; color:#39FF14; font-size: 80px; font-family: monospace; background:#0d0d0d;">DEMASIADO LENTO</div>';
                }
                requestAnimationFrame(animate);
            }
            animate();
        </script>
        """, unsafe_allow_html=True)

        # B. Lluvia de calaveras
        skulls_html = "".join([f'<div class="skull" style="left: {random.randint(1,99)}vw; animation-delay: {random.uniform(0, 4)}s; animation-duration: {random.uniform(3, 7)}s;">💀</div>' for _ in range(30)])
        st.markdown(skulls_html, unsafe_allow_html=True)
        
        # C. Contenido final
        st.markdown('<div class="terminal-header">[ SYSTEM INITIALIZATION NaNa.EXE ]</div>', unsafe_allow_html=True)
        st.markdown('<p class="terminal-text">> [ACCESS GRANTED] Hi, Kralj! </p>', unsafe_allow_html=True)
        st.markdown('<p class="terminal-text">> ERROR 404: cuz idk like always.</p>', unsafe_allow_html=True)
        st.markdown('<p class="terminal-text">> Executing protocol "Constant pain"...</p>', unsafe_allow_html=True)
        
        # Corazón
        st.markdown('<div class="heart-container"><div class="css-heart"></div></div>', unsafe_allow_html=True)
        
        if 'heart_clicked' not in st.session_state: st.session_state.heart_clicked = False
        if st.button("💚 [ INTERACT WITH CONSTANT_HEART.SYS ] 💚"):
            st.session_state.heart_clicked = True
        
        if st.session_state.heart_clicked:
            st.markdown('<p class="terminal-text" style="color: #ff0055 !important;">> [DECRYPTING HEART_LOG.TXT...]</p>', unsafe_allow_html=True)
            time.sleep(0.3)
            st.markdown('<p class="terminal-text" style="background-color: #1a0000; border: 1px solid #ff0055; padding: 15px; border-radius: 5px; font-weight: bold; color: #ff3366 !important;">>> "Don\'t get used to this because I\'m just learning and I\'m not good at these things, let alone being \'romantic?\'"</p>', unsafe_allow_html=True)

        # Mensaje final
        st.markdown('<p class="terminal-text" style="text-align: center; font-size: 20px; font-weight: bold; margin-top: 30px;">Tbh idk what to put here so; I love u i guess...</p>', unsafe_allow_html=True)
