# --- LÓGICA DEL MINIJUEGO (Inyección directa) ---
bomb_script = """
<div id="bomb" style="position:absolute; top:50px; left:50px; font-size:30px; z-index:99999; pointer-events:none; transition: none;">💣</div>
<script>
    (function() {
        const bomb = document.getElementById('bomb');
        if (!bomb) return;
        let mx = window.innerWidth / 2;
        let my = window.innerHeight / 2;
        let bx = mx, by = my, vx = 0, vy = 0;

        window.addEventListener('mousemove', e => { 
            mx = e.pageX; 
            my = e.pageY; 
        });

        function animate() {
            vx += (mx - bx) * 0.05;
            vy += (my - by) * 0.05;
            bx += (vx *= 0.75);
            by += (vy *= 0.75);
            bomb.style.left = bx + 'px';
            bomb.style.top = by + 'px';
            requestAnimationFrame(animate);
        }
        animate();
    })();
</script>
"""

# --- EN TU FLUJO ---
if st.session_state.get('show_bomb_game', False):
    # Usamos st.markdown para inyectar el HTML directamente en el DOM principal
    st.markdown(bomb_script, unsafe_allow_html=True)
    st.markdown('<p class="terminal-text" style="color:red;">> WARNING: BOMB_ACTIVE</p>', unsafe_allow_html=True)
