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
        color: #39FF14 !important;
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
        background: #39FF14;
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

    /* ---- Bomb link style ---- */
    .bomb-link {
        color: #ff3333 !important;
        text-decoration: underline dotted #ff3333;
        text-shadow: 0 0 8px rgba(255, 51, 51, 0.9);
        cursor: pointer;
        font-weight: bold;
        transition: all 0.2s ease;
        font-family: 'Fira Code', monospace !important;
    }
    .bomb-link:hover {
        color: #ff6666 !important;
        text-shadow: 0 0 15px rgba(255, 51, 51, 1);
    }
</style>
"""

st.markdown(terminal_css, unsafe_allow_html=True)

# ── Bomb mini-game HTML (self-contained, injected via components.html) ──────
BOMB_GAME_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap');

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: #0d0d0d;
    overflow: hidden;
    font-family: 'Fira Code', monospace;
    color: #39FF14;
    width: 100vw;
    height: 100vh;
    cursor: crosshair;
  }

  #game-canvas {
    position: relative;
    width: 100%;
    height: 100%;
  }

  #bomb {
    position: absolute;
    font-size: 48px;
    pointer-events: none;
    transition: none;
    filter: drop-shadow(0 0 8px rgba(255,80,0,0.9));
    transform: translate(-50%, -50%);
    z-index: 10;
  }

  #hud {
    position: absolute;
    top: 14px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 13px;
    color: #39FF14;
    text-shadow: 0 0 6px rgba(57,255,20,0.8);
    letter-spacing: 2px;
    z-index: 20;
    text-align: center;
    white-space: nowrap;
  }

  #close-btn {
    position: absolute;
    top: 10px;
    right: 16px;
    background: transparent;
    border: 1px solid #ff3333;
    color: #ff3333;
    font-family: 'Fira Code', monospace;
    font-size: 12px;
    padding: 4px 10px;
    cursor: pointer;
    z-index: 30;
    text-shadow: 0 0 5px rgba(255,51,51,0.7);
    border-radius: 3px;
    transition: all 0.2s;
  }
  #close-btn:hover {
    background: #ff3333;
    color: #0d0d0d;
  }

  /* scan-line overlay */
  #game-canvas::before {
    content: "";
    position: absolute;
    inset: 0;
    background: repeating-linear-gradient(
      to bottom,
      transparent 0px,
      transparent 3px,
      rgba(0,0,0,0.18) 3px,
      rgba(0,0,0,0.18) 4px
    );
    pointer-events: none;
    z-index: 5;
  }

  /* ── GAME OVER screen ── */
  #game-over {
    display: none;
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.92);
    z-index: 50;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 18px;
  }

  .go-glitch {
    font-size: clamp(28px, 6vw, 52px);
    font-weight: 700;
    color: #ff2222;
    text-shadow:
      0 0 10px #ff0000,
      0 0 30px #ff0000,
      2px 2px 0 #880000;
    letter-spacing: 4px;
    animation: glitch 0.4s infinite;
  }

  @keyframes glitch {
    0%   { clip-path: inset(0 0 95% 0); transform: translateX(-4px); }
    20%  { clip-path: inset(30% 0 50% 0); transform: translateX(4px); }
    40%  { clip-path: inset(60% 0 10% 0); transform: translateX(-2px); }
    60%  { clip-path: inset(80% 0 5% 0);  transform: translateX(3px); }
    80%  { clip-path: inset(10% 0 80% 0); transform: translateX(-3px); }
    100% { clip-path: inset(0 0 0 0);     transform: translateX(0); }
  }

  .go-sub {
    font-size: clamp(13px, 2.5vw, 18px);
    color: #ff6644;
    text-shadow: 0 0 8px rgba(255,100,60,0.8);
    letter-spacing: 2px;
  }

  .go-emoji { font-size: clamp(48px, 10vw, 80px); animation: shake 0.3s infinite; }

  @keyframes shake {
    0%,100% { transform: rotate(-8deg) scale(1.1); }
    50%      { transform: rotate(8deg)  scale(0.95); }
  }

  #retry-btn {
    margin-top: 8px;
    background: transparent;
    border: 2px solid #ff3333;
    color: #ff3333;
    font-family: 'Fira Code', monospace;
    font-size: 14px;
    padding: 8px 24px;
    cursor: pointer;
    text-shadow: 0 0 5px rgba(255,51,51,0.7);
    border-radius: 4px;
    letter-spacing: 2px;
    transition: all 0.2s;
  }
  #retry-btn:hover { background: #ff3333; color: #0d0d0d; }
</style>
</head>
<body>
<div id="game-canvas">
  <div id="hud">💣 BOMB.EXE — SURVIVE AS LONG AS YOU CAN</div>
  <button id="close-btn" onclick="closeGame()">✕ ESC</button>
  <div id="bomb">💣</div>

  <!-- Game Over overlay -->
  <div id="game-over">
    <div class="go-emoji">💥</div>
    <div class="go-glitch">ERROR: TOO SLOW</div>
    <div class="go-sub">> process terminated. you couldn't outrun it.</div>
    <div class="go-sub" id="go-time" style="color:#ffaa00;"></div>
    <button id="retry-btn" onclick="restartGame()">[ RETRY ]</button>
  </div>
</div>

<script>
  const bomb   = document.getElementById('bomb');
  const gameOver = document.getElementById('game-over');
  const goTime   = document.getElementById('go-time');
  const hud      = document.getElementById('hud');

  let bx = window.innerWidth  / 2;
  let by = window.innerHeight / 2;
  let mx = window.innerWidth  / 2;
  let my = window.innerHeight / 2;

  let speed       = 1.8;   // initial chase fraction per frame
  let startTime   = Date.now();
  let alive       = true;
  let rafId       = null;

  const CATCH_DIST = 46; // px – how close = caught

  document.addEventListener('mousemove', e => {
    mx = e.clientX;
    my = e.clientY;
  });

  // Touch support
  document.addEventListener('touchmove', e => {
    mx = e.touches[0].clientX;
    my = e.touches[0].clientY;
  }, { passive: true });

  function tick() {
    if (!alive) return;

    const elapsed = (Date.now() - startTime) / 1000;
    // Speed ramps up: starts at 1.8%, caps at 8% per frame
    speed = Math.min(0.018 + elapsed * 0.0012, 0.08);

    // Chase cursor
    bx += (mx - bx) * speed;
    by += (my - by) * speed;

    bomb.style.left = bx + 'px';
    bomb.style.top  = by + 'px';

    // Rotate towards cursor for drama
    const angle = Math.atan2(my - by, mx - bx) * (180 / Math.PI);
    bomb.style.transform = `translate(-50%,-50%) rotate(${angle + 90}deg)`;

    // HUD timer
    hud.textContent = `💣 BOMB.EXE  —  ${elapsed.toFixed(1)}s survived`;

    // Catch check
    const dist = Math.hypot(mx - bx, my - by);
    if (dist < CATCH_DIST) {
      triggerGameOver(elapsed);
      return;
    }

    rafId = requestAnimationFrame(tick);
  }

  function triggerGameOver(elapsed) {
    alive = false;
    bomb.style.fontSize = '80px';
    bomb.style.transform = 'translate(-50%,-50%) scale(1.4)';
    gameOver.style.display = 'flex';
    goTime.textContent = `> survival time: ${elapsed.toFixed(2)}s`;
  }

  function restartGame() {
    alive = true;
    bx = window.innerWidth  / 2;
    by = window.innerHeight / 2;
    startTime = Date.now();
    speed = 1.8;
    bomb.style.fontSize = '48px';
    gameOver.style.display = 'none';
    cancelAnimationFrame(rafId);
    tick();
  }

  function closeGame() {
    // Post a message to the Streamlit parent to close the game
    window.parent.postMessage({ type: 'closeBombGame' }, '*');
  }

  // Start
  tick();
</script>
</body>
</html>
"""

# ── Session state ─────────────────────────────────────────────────────────────
if 'warning_accepted' not in st.session_state:
    st.session_state.warning_accepted = False
if 'show_bomb_game' not in st.session_state:
    st.session_state.show_bomb_game = False

# ── Bomb mini-game page ───────────────────────────────────────────────────────
if st.session_state.show_bomb_game:
    st.markdown(
        '<div class="terminal-header" style="color:#ff3333 !important;border-bottom-color:#ff3333 !important;">'
        '[ BOMB.EXE — RUNNING ]</div>',
        unsafe_allow_html=True
    )
    components.html(BOMB_GAME_HTML, height=520, scrolling=False)
    if st.button("◀ BACK TO WARNING"):
        st.session_state.show_bomb_game = False
        st.rerun()

# ── Warning page ──────────────────────────────────────────────────────────────
elif not st.session_state.warning_accepted:
    st.markdown(
        '<div class="terminal-header" style="color: #ff3333 !important; border-bottom-color: #ff3333 !important; '
        'text-shadow: 0 0 10px rgba(255, 51, 51, 0.9);">[ !!! SECURITY WARNING !!! ]</div>',
        unsafe_allow_html=True
    )

    # ── Warning box — "bomb" is now a clickable Streamlit-friendly button link ──
    # We split the text around the word "bomb" and inject a styled span with
    # an onclick that posts a message; a small JS listener triggers st.rerun via URL param.
    # Simpler approach: use a dedicated st.button rendered below the box.
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
                Otherwise, next birthday I might actually send you a real
                <span class="bomb-link" id="bomb-word" title="click me... if you dare 💣">bomb</span>
                instead of a harmless present (at least you should already know how to defuse that one) ;).
            </p>
            <p class="warning-text" style="margin-top: 15px; font-weight: bold;">> Are you sure you want to proceed and run the executable?</p>
        </div>
    ''', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("PROCEED ANYWAY (I TRUST NANA)"):
            st.session_state.warning_accepted = True
            st.rerun()
    with col2:
        if st.button("💣 CLICK THE BOMB"):
            st.session_state.show_bomb_game = True
            st.rerun()

# ── Main terminal page ────────────────────────────────────────────────────────
else:
    st.markdown('<div class="terminal-header">[ SYSTEM INITIALIZATION NaNa.EXE ]</div>', unsafe_allow_html=True)

    st.markdown('<p class="terminal-text">> Loading modules...</p>', unsafe_allow_html=True)
    st.markdown('<p class="terminal-text">> Connecting to server: my_illness_ip...</p>', unsafe_allow_html=True)

    if 'acceso_concedido' not in st.session_state:
        st.session_state.acceso_concedido = False
    if 'validating' not in st.session_state:
        st.session_state.validating = False

    if not st.session_state.acceso_concedido:
        st.markdown('<p class="terminal-text">> WARNING: Identity verification required.</p>', unsafe_allow_html=True)

        if st.session_state.validating:
            # ── Animated terminal loading sequence ─────────────────────────
            steps = [
                ("> Initializing identity protocol...",          8),
                ("> Scanning biometric signature...",           18),
                ("> Cross-referencing neural fingerprint...",   31),
                ("> Checking retinal pattern database...",      45),
                ("> Decrypting user credentials...",            57),
                ("> Verifying access clearance level...",       70),
                ("> Bypassing firewall layer 3...",             82),
                ("> Compiling authorization token...",          93),
                ("> Access validation complete.",              100),
            ]

            log_placeholder  = st.empty()
            bar_placeholder  = st.empty()
            logs_so_far = []

            for message, pct in steps:
                logs_so_far.append(message)

                # Render all log lines so far
                logs_html = "".join(
                    f'<p class="terminal-text" style="margin:2px 0;">{line}</p>'
                    for line in logs_so_far
                )
                log_placeholder.markdown(logs_html, unsafe_allow_html=True)

                # Build ASCII progress bar  [████░░░░░░] 45%
                filled   = int(pct / 5)          # out of 20 blocks
                empty    = 20 - filled
                bar_str  = "█" * filled + "░" * empty
                bar_html = (
                    f'<p class="terminal-text" style="letter-spacing:1px; margin-top:8px;">'
                    f'> [<span style="color:#39FF14;">{bar_str}</span>] '
                    f'<span style="color:#00ffcc;">{pct}%</span></p>'
                )
                bar_placeholder.markdown(bar_html, unsafe_allow_html=True)

                time.sleep(0.45)

            time.sleep(0.3)
            st.session_state.acceso_concedido = True
            st.session_state.validating = False
            st.rerun()

        else:
            if st.button("CLICK TO VALIDATE"):
                st.session_state.validating = True
                st.rerun()

    else:
        # spinner already done during validation animation, skip extra sleep
        pass

        skulls_html = ""
        for _ in range(45):
            left_pos = random.randint(1, 99)
            delay    = random.uniform(0, 3.5)
            duration = random.uniform(2.5, 6)
            size     = random.randint(18, 38)
            skulls_html += (
                f'<div class="skull" style="left: {left_pos}vw; '
                f'animation-delay: {delay}s; animation-duration: {duration}s; '
                f'font-size: {size}px;">💀</div>'
            )
        st.markdown(skulls_html, unsafe_allow_html=True)

        st.markdown('<p class="terminal-text" style="color: #00ffcc !important;">> [ACCESS GRANTED] Hi, Kralj! </p>', unsafe_allow_html=True)
        st.markdown('<p class="terminal-text">> ERROR 404: cuz idk like always.</p>', unsafe_allow_html=True)
        st.markdown('<p class="terminal-text">> Executing protocol "Constant pain"...</p>', unsafe_allow_html=True)

        st.markdown('<div class="heart-container"><div class="css-heart"></div></div>', unsafe_allow_html=True)

        if 'heart_clicked' not in st.session_state:
            st.session_state.heart_clicked = False

        if st.button("💚 [ INTERACT WITH CONSTANT_HEART.SYS ] 💚"):
            st.session_state.heart_clicked = True

        if st.session_state.heart_clicked:
            st.markdown('<p class="terminal-text" style="color: #ff0055 !important;">> [DECRYPTING HEART_LOG.TXT...]</p>', unsafe_allow_html=True)
            time.sleep(0.3)
            st.markdown(
                '<p class="terminal-text" style="background-color: #1a0000; border: 1px solid #ff0055; '
                'padding: 15px; border-radius: 5px; font-weight: bold; color: #ff3366 !important;">'
                '>> "Don\'t get used to this cuz I\'m just learning and I\'m not good at these things, '
                'let alone being \'romantic?\'"'
                '</p>',
                unsafe_allow_html=True
            )

        st.markdown(
            '<p class="terminal-text" style="text-align: center; font-size: 20px; font-weight: bold; margin-top: 30px;">'
            'Tbh idk what to put here so; I love u i guess...'
            '</p>',
            unsafe_allow_html=True
        )
