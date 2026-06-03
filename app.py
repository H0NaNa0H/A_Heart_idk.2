import streamlit as st
import time
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

    /* Custom falling skulls (Calaveras) animation */
    .skull {
        position: fixed;
        top: -10%;
        user-select: none;
        pointer-events: none;
        z-index: 9999;
        animation: fall linear forwards;
    }
    @keyframes fall {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        90% {
            opacity: 0.9;
        }
        100% {
            transform: translateY(110vh) rotate(360deg);
            opacity: 0;
        }
    }
</style>
"""

# Apply the custom CSS
st.markdown(terminal_css, unsafe_allow_html=True)

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
    
    # Generate custom falling skulls (calaveras) animation in HTML
    skulls_html = ""
    for _ in range(45):
        left_pos = random.randint(1, 99)
        delay = random.uniform(0, 3.5)
        duration = random.uniform(2.5, 6)
        size = random.randint(18, 38)
        skulls_html += f'<div class="skull" style="left: {left_pos}vw; animation-delay: {delay}s; animation-duration: {duration}s; font-size: {size}px;">💀</div>'
    st.markdown(skulls_html, unsafe_allow_html=True)
    
    st.markdown('<p class="terminal-text" style="color: #00ffcc !important;">> [ACCESS GRANTED] Hi, Kralj! </p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="terminal-text">> ERROR 404: cuz idk like always.</p>', 
        unsafe_allow_html=True
    )
    st.markdown('<p class="terminal-text">> Executing protocol "Constant pain"...</p>', unsafe_allow_html=True)
    
    # Render our beautiful CSS neon green beating heart
    st.markdown('<div class="heart-container"><div class="css-heart"></div></div>', unsafe_allow_html=True)
    
    # Final dedication message
    st.markdown(
        '<p class="terminal-text" style="text-align: center; font-size: 20px; font-weight: bold;">'
        'Tbh idk what to put here so; I love u i guess...'
        '</p>', 
        unsafe_allow_html=True
    )
