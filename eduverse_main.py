"""
EduVerse: The 10 Realms of Genius
Complete Educational Game Platform with AWS Integration
"""

import streamlit as st
import json
import random
import time
import uuid
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
from typing import Dict, List, Any
import base64
from PIL import Image
import io

# Configure Streamlit page
st.set_page_config(
    page_title="EduVerse: The 10 Realms of Genius",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import game modules
from games import (
    math_wizard, word_master, science_lab, geography_quest, history_hunter,
    art_creator, music_maestro, code_ninja, logic_puzzle, memory_palace
)
from utils import translations, aws_client, game_data

# Initialize session state
def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        'language': 'en',
        'player_name': '',
        'player_id': str(uuid.uuid4()),
        'current_game': None,
        'current_level': 1,
        'game_state': 'menu',
        'player_data': {},
        'leaderboard_data': [],
        'game_session_id': None,
        'game_start_time': None,
        'total_score': 0,
        'achievements': [],
        'sound_enabled': True,
        'theme': 'light'
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def get_text(key: str) -> str:
    """Get translated text based on current language"""
    return translations.TRANSLATIONS[st.session_state.language].get(key, key)

def load_css():
    """Load custom CSS styles"""
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .game-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 2px solid transparent;
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .game-card:hover {
        border-color: #667eea;
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    .achievement-badge {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin: 0.2rem;
        display: inline-block;
    }
    
    .score-display {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
        text-align: center;
    }
    
    .level-indicator {
        background: #667eea;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: bold;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    }
    
    .game-progress {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .leaderboard-entry {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    
    .correct-answer {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #c3e6cb;
    }
    
    .incorrect-answer {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #f5c6cb;
    }
    </style>
    """, unsafe_allow_html=True)

def show_header():
    """Display the main header"""
    st.markdown(f"""
    <div class="main-header">
        <h1>🎓 {get_text('title')}</h1>
        <p style="font-size: 1.2rem; margin: 0;">{get_text('subtitle')}</p>
    </div>
    """, unsafe_allow_html=True)

def show_sidebar():
    """Display the sidebar with navigation and settings"""
    with st.sidebar:
        st.markdown("### 🎓 EduVerse")
        
        # Language selector
        languages = {'en': 'English 🇺🇸', 'ta': 'தமிழ் 🇮🇳'}
        selected_lang = st.selectbox(
            get_text('select_language'),
            options=list(languages.keys()),
            format_func=lambda x: languages[x],
            index=list(languages.keys()).index(st.session_state.language)
        )
        
        if selected_lang != st.session_state.language:
            st.session_state.language = selected_lang
            st.rerun()
        
        st.markdown("---")
        
        # Player information
        player_name = st.text_input(
            get_text('player_name'),
            value=st.session_state.player_name,
            placeholder="Enter your name..."
        )
        
        if player_name != st.session_state.player_name:
            st.session_state.player_name = player_name
            if player_name:
                load_player_data()
        
        if st.session_state.player_name:
            st.success(f"Welcome, {st.session_state.player_name}! 👋")
            
            # Player stats
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Score", st.session_state.total_score)
            with col2:
                st.metric("Achievements", len(st.session_state.achievements))
        
        st.markdown("---")
        
        # Navigation buttons
        nav_buttons = [
            ('🏠', 'main_menu', 'Main Menu'),
            ('🏆', 'leaderboard', 'Leaderboard'),
            ('📊', 'progress', 'My Progress'),
            ('🎯', 'achievements', 'Achievements'),
            ('⚙️', 'settings', 'Settings')
        ]
        
        for icon, state, label in nav_buttons:
            if st.button(f"{icon} {get_text(label.lower().replace(' ', '_'))}", key=f"nav_{state}"):
                st.session_state.game_state = state
                st.session_state.current_game = None
                st.rerun()
        
        st.markdown("---")
        
        # Quick stats
        if st.session_state.player_name:
            st.markdown("### 📈 Quick Stats")
            
            # Games completed
            games_completed = sum(1 for game_id in range(1, 11) 
                                if f"game_{game_id}" in st.session_state.player_data)
            st.progress(games_completed / 10)
            st.caption(f"{games_completed}/10 Games Started")
            
            # Recent achievements
            if st.session_state.achievements:
                st.markdown("### 🏅 Recent Achievements")
                for achievement in st.session_state.achievements[-3:]:
                    st.markdown(f"🏆 {achievement}")

def load_player_data():
    """Load player data from local storage or API"""
    try:
        # In a real implementation, this would call the AWS API
        # For now, we'll use session state
        if 'player_data_loaded' not in st.session_state:
            st.session_state.player_data = {}
            st.session_state.total_score = 0
            st.session_state.achievements = []
            st.session_state.player_data_loaded = True
    except Exception as e:
        st.error(f"Error loading player data: {e}")

def save_player_data():
    """Save player data to API"""
    try:
        # In a real implementation, this would call the AWS API
        pass
    except Exception as e:
        st.error(f"Error saving player data: {e}")

def show_main_menu():
    """Display the main game selection menu"""
    show_header()
    
    if not st.session_state.player_name:
        st.warning(f"👋 {get_text('please_enter_name')}")
        return
    
    st.markdown(f"## 🎮 {get_text('choose_your_realm')}")
    
    # Game grid
    games = game_data.GAMES
    
    # Create 2 columns for game layout
    col1, col2 = st.columns(2)
    
    for i, (game_id, game_info) in enumerate(games.items()):
        col = col1 if i % 2 == 0 else col2
        
        with col:
            with st.container():
                st.markdown(f"""
                <div class="game-card">
                    <h3>{game_info['icon']} {game_info['name'][st.session_state.language]}</h3>
                    <p>{game_info['description'][st.session_state.language]}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Progress indicator
                game_key = f"game_{game_id}"
                if game_key in st.session_state.player_data:
                    progress = len(st.session_state.player_data[game_key])
                    total_levels = game_info['levels']
                    st.progress(progress / total_levels)
                    st.caption(f"Progress: {progress}/{total_levels} levels")
                else:
                    st.progress(0)
                    st.caption("Not started")
                
                # Play button
                if st.button(
                    f"🎮 {get_text('play_now')}",
                    key=f"play_{game_id}",
                    use_container_width=True
                ):
                    start_game(game_id)

def start_game(game_id: int):
    """Start a specific game"""
    st.session_state.current_game = game_id
    st.session_state.current_level = 1
    st.session_state.game_state = 'game'
    st.session_state.game_session_id = str(uuid.uuid4())
    st.session_state.game_start_time = time.time()
    st.rerun()

def show_game():
    """Display the current game"""
    if not st.session_state.current_game:
        st.session_state.game_state = 'main_menu'
        st.rerun()
        return
    
    game_id = st.session_state.current_game
    game_info = game_data.GAMES[game_id]
    
    # Game header
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; margin-bottom: 2rem;">
        <h2>{game_info['icon']} {game_info['name'][st.session_state.language]}</h2>
        <div class="level-indicator">Level {st.session_state.current_level}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Game content based on game_id
    game_modules = {
        1: math_wizard,
        2: word_master,
        3: science_lab,
        4: geography_quest,
        5: history_hunter,
        6: art_creator,
        7: music_maestro,
        8: code_ninja,
        9: logic_puzzle,
        10: memory_palace
    }
    
    if game_id in game_modules:
        game_modules[game_id].run_game(st.session_state.current_level)
    else:
        st.error("Game not implemented yet!")
        if st.button("🏠 Back to Menu"):
            st.session_state.game_state = 'main_menu'
            st.rerun()

def show_leaderboard():
    """Display the leaderboard"""
    st.markdown("## 🏆 Leaderboard")
    
    # Leaderboard tabs
    tab1, tab2, tab3 = st.tabs(["🌍 Global", "🎮 By Game", "📅 Today"])
    
    with tab1:
        show_global_leaderboard()
    
    with tab2:
        show_game_leaderboard()
    
    with tab3:
        show_daily_leaderboard()

def show_global_leaderboard():
    """Show global leaderboard"""
    st.markdown("### 🌍 Global Champions")
    
    # Sample leaderboard data
    leaderboard_data = [
        {"rank": 1, "name": "Alex Chen", "score": 9850, "games": 10},
        {"rank": 2, "name": "Priya Sharma", "score": 9200, "games": 9},
        {"rank": 3, "name": "Mohammed Ali", "score": 8750, "games": 8},
        {"rank": 4, "name": "Sarah Johnson", "score": 8500, "games": 10},
        {"rank": 5, "name": "Raj Patel", "score": 8200, "games": 7}
    ]
    
    for entry in leaderboard_data:
        medal = "🥇" if entry["rank"] == 1 else "🥈" if entry["rank"] == 2 else "🥉" if entry["rank"] == 3 else f"{entry['rank']}."
        
        st.markdown(f"""
        <div class="leaderboard-entry">
            <strong>{medal} {entry['name']}</strong><br>
            Score: {entry['score']} | Games: {entry['games']}/10
        </div>
        """, unsafe_allow_html=True)

def show_game_leaderboard():
    """Show game-specific leaderboard"""
    st.markdown("### 🎮 Game Champions")
    
    selected_game = st.selectbox(
        "Select Game",
        options=list(game_data.GAMES.keys()),
        format_func=lambda x: f"{game_data.GAMES[x]['icon']} {game_data.GAMES[x]['name']['en']}"
    )
    
    st.info(f"Leaderboard for {game_data.GAMES[selected_game]['name']['en']} will be displayed here.")

def show_daily_leaderboard():
    """Show today's leaderboard"""
    st.markdown("### 📅 Today's Champions")
    st.info("Today's top performers will be displayed here.")

def show_progress():
    """Display player progress"""
    st.markdown("## 📊 My Progress")
    
    if not st.session_state.player_name:
        st.warning("Please enter your name to view progress.")
        return
    
    # Overall progress
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Score", st.session_state.total_score)
    
    with col2:
        games_started = len(st.session_state.player_data)
        st.metric("Games Started", f"{games_started}/10")
    
    with col3:
        st.metric("Achievements", len(st.session_state.achievements))
    
    with col4:
        avg_score = st.session_state.total_score / max(games_started, 1)
        st.metric("Avg Score", f"{avg_score:.0f}")
    
    # Progress chart
    st.markdown("### 📈 Game Progress")
    
    progress_data = []
    for game_id, game_info in game_data.GAMES.items():
        game_key = f"game_{game_id}"
        if game_key in st.session_state.player_data:
            levels_completed = len(st.session_state.player_data[game_key])
            total_levels = game_info['levels']
            progress_data.append({
                'Game': game_info['name']['en'],
                'Progress': (levels_completed / total_levels) * 100,
                'Levels': f"{levels_completed}/{total_levels}"
            })
        else:
            progress_data.append({
                'Game': game_info['name']['en'],
                'Progress': 0,
                'Levels': f"0/{game_info['levels']}"
            })
    
    if progress_data:
        df = pd.DataFrame(progress_data)
        fig = px.bar(df, x='Game', y='Progress', title='Game Completion Progress')
        fig.update_layout(yaxis_title='Completion %', xaxis_title='Games')
        st.plotly_chart(fig, use_container_width=True)

def show_achievements():
    """Display achievements"""
    st.markdown("## 🎯 Achievements")
    
    # Achievement categories
    achievement_categories = {
        "🏆 Game Master": ["Complete all levels in any game", "Complete 5 games", "Complete all 10 games"],
        "🎯 Score Hunter": ["Score 1000+ points", "Score 5000+ points", "Score 10000+ points"],
        "⚡ Speed Demon": ["Complete a level in under 30 seconds", "Complete 5 levels quickly", "Speed master"],
        "🧠 Genius": ["Answer 100 questions correctly", "Perfect score in any game", "Maintain 90%+ accuracy"],
        "🌟 Explorer": ["Try all 10 games", "Play for 7 consecutive days", "Play 100 games total"]
    }
    
    for category, achievements in achievement_categories.items():
        st.markdown(f"### {category}")
        
        for achievement in achievements:
            if achievement in st.session_state.achievements:
                st.markdown(f"✅ {achievement}")
            else:
                st.markdown(f"⭕ {achievement}")

def show_settings():
    """Display settings"""
    st.markdown("## ⚙️ Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎵 Audio Settings")
        sound_enabled = st.checkbox("Enable Sound Effects", value=st.session_state.sound_enabled)
        st.session_state.sound_enabled = sound_enabled
        
        st.markdown("### 🎨 Theme Settings")
        theme = st.selectbox("Theme", ["Light", "Dark"], index=0 if st.session_state.theme == 'light' else 1)
        st.session_state.theme = theme.lower()
    
    with col2:
        st.markdown("### 🌐 Language Settings")
        st.info("Language can be changed from the sidebar.")
        
        st.markdown("### 📊 Data Settings")
        if st.button("Reset Progress", type="secondary"):
            if st.button("Confirm Reset", type="primary"):
                st.session_state.player_data = {}
                st.session_state.total_score = 0
                st.session_state.achievements = []
                st.success("Progress reset successfully!")
                st.rerun()

def main():
    """Main application function"""
    init_session_state()
    load_css()
    show_sidebar()
    
    # Route to appropriate page based on game_state
    if st.session_state.game_state == 'main_menu':
        show_main_menu()
    elif st.session_state.game_state == 'game':
        show_game()
    elif st.session_state.game_state == 'leaderboard':
        show_leaderboard()
    elif st.session_state.game_state == 'progress':
        show_progress()
    elif st.session_state.game_state == 'achievements':
        show_achievements()
    elif st.session_state.game_state == 'settings':
        show_settings()
    else:
        show_main_menu()

if __name__ == "__main__":
    main()
