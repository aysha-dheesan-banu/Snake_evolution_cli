"""
Logic Puzzle Game - Game 9
Develop logical thinking and problem-solving
"""

import streamlit as st
from utils.translations import TRANSLATIONS

def get_text(key: str) -> str:
    return TRANSLATIONS[st.session_state.language].get(key, key)

def run_game(level: int):
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; margin-bottom: 2rem;">
        <h2>🧩 Logic Puzzle</h2>
        <p>Level {level} - Develop Logical Thinking!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("🚧 Logic Puzzle game is under development. Coming soon with brain-teasing challenges!")
    
    if st.button("🏠 Back to Main Menu"):
        st.session_state.game_state = 'main_menu'
        st.session_state.current_game = None
        st.rerun()
