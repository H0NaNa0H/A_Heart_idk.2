import streamlit as st
import time
import random

# Configuración estética (Dark Mode)
st.set_page_config(
    page_title="Terminal v1.0",
    page_icon="💚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Integración completa de estilos y scripts
terminal_css = """
<style>
    .stApp { background-color: #0d0d0d !important; cursor: none !important; }
    header, footer { visibility: hidden !important; }
    
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght=400;700&display=swap');
    
    .terminal-text { font-family: 'Fira Code', monospace !important; color: #39FF14 !important; text-shadow: 0 0 5px rgba(57, 255, 20, 0.7); font-size: 18px; line-height: 1.6; }
    .terminal-header { font-family: 'Fira Code', monospace !important; color: #39FF14 !important; text-shadow: 0 0 10px rgba(57, 255, 20, 0.9); font-size: 28px; font-weight: bold; text-align: center; border-bottom: 2px solid #39FF14; padding-bottom: 10px; margin-bottom: 30px; }
    
    .stButton>button { background-color: transparent !important; color: #39FF14 !important; border: 2px solid #39FF14 !important; border-radius: 5px !important; font-family: 'Fira Code', monospace !important; font-weight: bold !important; font-size: 16px !important; width: 100%; transition: all 0.3s ease; }
    .stButton>button:hover { background-color: #39FF14 !important; color: #0d0d0d !important; }

    .heart-container { display: flex; justify-content: center; align-items: center; height: 200px; margin-top: 20px; margin-bottom: 20px; }
    .css-heart { position: relative; width: 100px; height: 90px; animation: heartbeat 1s infinite; }
    .css-heart:before, .css-heart:after { position: absolute; content: ""; left: 50px; top: 0; width: 50px; height: 80px; background: #39FF14; border-radius: 50px 50px 0 0; transform: rotate(-45deg); transform-origin: 0 100%; box-shadow: 0 0 20px rgba(57, 255, 20, 0.8); }
    .css-heart:after { left: 0; transform: rotate(45deg); transform-origin: 100% 100%; }
    @keyframes heartbeat { 0% { transform: scale(0.9); } 30% { transform: scale(1.1); } 60% { transform: scale(0.95); } 100% { transform: scale(0.9); } }

    .skull { position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999; animation: fall linear forwards; }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); opacity: 1; } 100% { transform: translateY(110vh) rotate(360deg); opacity: 0; } }

    .warning-box { background-color: #1a0f00; border: 2px solid #ffaa00; padding: 20px; border-radius: 5px; margin-bottom: 25px; }
    .warning-text { font-family: 'Fira Code', monospace !important; color: #ffaa00 !important; font-size: 16px; line-height: 1.6; }

    #fatal-error-screen { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: black; z-index: 9999999; display: none; justify-content: center; align-items: center; flex-direction: column; color: red; font-family: 'Fira Code', monospace; }
    #bomb-element { position: fixed; font-size: 40px; cursor: none; z-index: 99999; display: none; transition: transform 0.1s ease; pointer-events: none; }
</style>

<div id="bomb-element">💣</div>
<div id="fatal-error-screen">
    <h1 style="font-size: 100px; text-shadow: 0 0 20px red;">ERROR FATAL</h1>
    <p>SYSTEM COMPROMISED. CONNECTION TERMINATED.</p>
    <button onclick="location.reload()" style="margin-top: 20px; padding: 10px 20px; background: red; color: white; border: none; cursor: pointer;">REBOOT SYSTEM</button>
</div>

<script>
    const bomb = document.getElementById('bomb-element');
    const fatalScreen = document.getElementById('fatal-error-screen');
    let active = false;

    function activateBomb() {
        active = true;
        bomb.style.display = 'block';
    }

    document.addEventListener('mousemove', (e) => {
        if (!active) return;
        bomb.style.left = (e.clientX - 20) + 'px';
        bomb.style.top = (e.clientY - 20) + 'px';
        const rect = bomb.getBoundingClientRect();
        const dist = Math.hypot(e.clientX - (rect.left + 20), e.clientY - (rect.top + 20));
        if (dist < 30) {
            fatalScreen.style.display = 'flex';
            active = false;
            bomb.style.display = 'none';
        }
    });
</script>
"""

st.markdown(terminal_css, unsafe_allow_html=True)

# Lógica del flujo
if 'warning_accepted' not in st.session_state: st.session_state.warning_accepted = False

if not st.session_state.warning_accepted:
    st.markdown('<div class="terminal-header" style="color: #ff3333 !important;">[ !!! SECURITY WARNING !!! ]</div>', unsafe_allow_html=True)
    st.markdown('''<div class="warning-box">
                <p class="warning-text">> SYSTEM DETECTED A SUSPICIOUS CONNECTION FROM: NaNa.EXE</p>
                <p class="warning-text">> Threat classification: SARCASM_HEAVY_LOAD</p>
                <p class="warning-text" style="color: #ff3333 !important; font-weight: bold;">WARNING: This is totally NOT a malware... or is it?</p>
                <p class="warning-text">Otherwise, next birthday I might actually send you a real bomb instead of a harmless present ;).</p>
                </div>''', unsafe_allow_html=True)
    if st.button("PROCEED ANYWAY (I TRUST NANA)"):
        st.session_state.warning_accepted = True
        st.rerun()
else:
    st.markdown('<div class="terminal-header">[ SYSTEM INITIALIZATION NaNa.EXE ]</div>', unsafe_allow_html=True)
    
    if 'acceso_concedido' not in st.session_state: st.session_state.acceso_concedido = False

    if not st.session_state.acceso_concedido:
        st.markdown('<p class="terminal-text">> WARNING: Identity verification required.</p>', unsafe_allow_html=True)
        if st.button("CLICK TO VALIDATE"):
            st.session_state.acceso_concedido = True
            st.rerun()
    else:
        # Lluvia de calaveras
        skulls_html = "".join([f'<div class="skull" style="left: {random.randint(1, 99)}vw; animation-delay: {random.uniform(0, 3)}s; animation-duration: {random.uniform(2, 5)}s;">💀</div>' for _ in range(30)])
        st.markdown(skulls_html, unsafe_allow_html=True)
        
        st.markdown('<p class="terminal-text" style="color: #00ffcc !important;">> [ACCESS GRANTED] Hi, Kralj!</p>', unsafe_allow_html=True)
        st.markdown('<div class="heart-container"><div class="css-heart"></div></div>', unsafe_allow_html=True)
        
        if 'heart_clicked' not in st.session_state: st.session_state.heart_clicked = False
        if st.button("💚 [ INTERACT WITH CONSTANT_HEART.SYS ] 💚"): 
            st.session_state.heart_clicked = True
            
        if st.session_state.heart_clicked:
            st.markdown('<p class="terminal-text" style="color: #ff0055 !important;">> [DECRYPTING HEART_LOG.TXT...]</p>', unsafe_allow_html=True)
            time.sleep(0.3)
            st.markdown('<p class="terminal-text" style="background-color: #1a0000; border: 1px solid #ff0055; padding: 15px; border-radius: 5px; color: #ff3366 !important;">>> "Don\'t get used to this because I\'m just learning and I\'m not good at these things..."</p>', unsafe_allow_html=True)
            st.markdown("<script>activateBomb();</script>", unsafe_allow_html=True)
        
        st.markdown('<p class="terminal-text" style="text-align: center; font-size: 20px; font-weight: bold; margin-top: 30px;">Tbh idk what to put here so; I love u i guess...</p>', unsafe_allow_html=True)
