#!/usr/bin/env python3
"""
🎮 EduVerse Enhanced Arcade - 10 Touch-Friendly Games
Mobile-optimized educational games with mouse/touch-only controls
"""

import streamlit as st
import random
import time
import json
import math
from datetime import datetime
from typing import Dict, List, Tuple, Any

# Configure page for mobile-first design
st.set_page_config(
    page_title="🎮 EduVerse Arcade",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for mobile-friendly interface
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .game-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin: 10px;
        text-align: center;
        cursor: pointer;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .game-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .touch-button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 25px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        margin: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .touch-button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .score-display {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .game-area {
        background: #f8f9fa;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        min-height: 400px;
        border: 2px solid #e9ecef;
    }
    
    .mobile-optimized {
        font-size: 18px;
        line-height: 1.6;
        touch-action: manipulation;
    }
</style>
""", unsafe_allow_html=True)

class ArcadeGameManager:
    def __init__(self):
        self.games = {
            "🎯 Bubble Pop Math": {
                "description": "Pop bubbles with correct math answers!",
                "difficulty": "Easy",
                "subject": "Mathematics",
                "icon": "🎯"
            },
            "🌟 Star Collector": {
                "description": "Collect stars by solving word puzzles!",
                "difficulty": "Medium",
                "subject": "Language",
                "icon": "🌟"
            },
            "🧪 Lab Mixer": {
                "description": "Mix chemicals by matching science facts!",
                "difficulty": "Medium",
                "subject": "Science",
                "icon": "🧪"
            },
            "🗺️ World Explorer": {
                "description": "Explore the world through geography challenges!",
                "difficulty": "Hard",
                "subject": "Geography",
                "icon": "🗺️"
            },
            "⏰ Time Machine": {
                "description": "Travel through history solving puzzles!",
                "difficulty": "Hard",
                "subject": "History",
                "icon": "⏰"
            },
            "🎨 Color Master": {
                "description": "Create art by matching colors and patterns!",
                "difficulty": "Easy",
                "subject": "Art",
                "icon": "🎨"
            },
            "🎵 Rhythm Hero": {
                "description": "Hit the beats and learn music theory!",
                "difficulty": "Medium",
                "subject": "Music",
                "icon": "🎵"
            },
            "🤖 Code Breaker": {
                "description": "Solve coding puzzles by dragging blocks!",
                "difficulty": "Hard",
                "subject": "Programming",
                "icon": "🤖"
            },
            "🧩 Pattern Master": {
                "description": "Complete patterns using logic!",
                "difficulty": "Medium",
                "subject": "Logic",
                "icon": "🧩"
            },
            "🧠 Memory Matrix": {
                "description": "Remember sequences and improve memory!",
                "difficulty": "Easy",
                "subject": "Memory",
                "icon": "🧠"
            }
        }
        
        # Initialize session state
        if 'current_game' not in st.session_state:
            st.session_state.current_game = None
        if 'player_score' not in st.session_state:
            st.session_state.player_score = 0
        if 'player_level' not in st.session_state:
            st.session_state.player_level = 1
        if 'game_state' not in st.session_state:
            st.session_state.game_state = {}

    def show_main_menu(self):
        """Display the main arcade menu"""
        st.markdown("""
        <div class="main-header">
            <h1>🎮 EduVerse Enhanced Arcade</h1>
            <h3>10 Touch-Friendly Educational Games</h3>
            <p>Tap to play • Learn while having fun • Mobile optimized</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Player stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="score-display">
                🏆 Total Score<br>{st.session_state.player_score}
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="score-display">
                📊 Level<br>{st.session_state.player_level}
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"""
            <div class="score-display">
                🎯 Games Played<br>{len(st.session_state.get('completed_games', []))}/10
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 🎮 Choose Your Adventure")
        
        # Display games in a grid
        cols = st.columns(2)
        for i, (game_name, game_info) in enumerate(self.games.items()):
            with cols[i % 2]:
                if st.button(
                    f"{game_info['icon']} {game_name}\n{game_info['description']}\n📚 {game_info['subject']} • {game_info['difficulty']}",
                    key=f"game_{i}",
                    use_container_width=True
                ):
                    st.session_state.current_game = game_name
                    st.rerun()

    def run_arcade(self):
        """Main arcade runner"""
        if st.session_state.current_game is None:
            self.show_main_menu()
        else:
            # Back button
            if st.button("🏠 Back to Arcade", key="back_button"):
                st.session_state.current_game = None
                st.rerun()
            
            # Run the selected game
            game_name = st.session_state.current_game
            st.markdown(f"<h2 style='text-align: center;'>{game_name}</h2>", unsafe_allow_html=True)
            
            # Route to appropriate game
            if "Bubble Pop Math" in game_name:
                self.bubble_pop_math()
            elif "Star Collector" in game_name:
                self.star_collector()
            elif "Lab Mixer" in game_name:
                self.lab_mixer()
            elif "World Explorer" in game_name:
                self.world_explorer()
            elif "Time Machine" in game_name:
                self.time_machine()
            elif "Color Master" in game_name:
                self.color_master()
            elif "Rhythm Hero" in game_name:
                self.rhythm_hero()
            elif "Code Breaker" in game_name:
                self.code_breaker()
            elif "Pattern Master" in game_name:
                self.pattern_master()
            elif "Memory Matrix" in game_name:
                self.memory_matrix()

    def bubble_pop_math(self):
        """🎯 Bubble Pop Math Game - Touch-friendly math game"""
        st.markdown("""
        <div class="game-area">
            <h3 style="text-align: center;">🎯 Pop the bubble with the correct answer!</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Initialize game state
        if 'bubble_game' not in st.session_state.game_state:
            st.session_state.game_state['bubble_game'] = {
                'score': 0,
                'level': 1,
                'question': None,
                'options': [],
                'correct_answer': None
            }
        
        game = st.session_state.game_state['bubble_game']
        
        # Generate new question if needed
        if game['question'] is None:
            level = game['level']
            if level <= 3:
                # Basic arithmetic
                a, b = random.randint(1, 10), random.randint(1, 10)
                op = random.choice(['+', '-', '*'])
                if op == '+':
                    question = f"{a} + {b}"
                    correct = a + b
                elif op == '-':
                    question = f"{a + b} - {b}"  # Ensure positive result
                    correct = a
                else:
                    question = f"{a} × {b}"
                    correct = a * b
            else:
                # Advanced math
                a, b = random.randint(10, 50), random.randint(2, 10)
                op = random.choice(['÷', '²', '%'])
                if op == '÷':
                    question = f"{a * b} ÷ {b}"
                    correct = a
                elif op == '²':
                    question = f"{a}²"
                    correct = a * a
                else:
                    question = f"{a} % {b}"
                    correct = a % b
            
            # Generate options
            options = [correct]
            while len(options) < 4:
                wrong = correct + random.randint(-10, 10)
                if wrong not in options and wrong > 0:
                    options.append(wrong)
            
            random.shuffle(options)
            
            game['question'] = question
            game['options'] = options
            game['correct_answer'] = correct
        
        # Display question
        st.markdown(f"""
        <div style="text-align: center; font-size: 24px; margin: 20px;">
            <strong>What is {game['question']}?</strong>
        </div>
        """, unsafe_allow_html=True)
        
        # Display bubble options
        cols = st.columns(2)
        for i, option in enumerate(game['options']):
            with cols[i % 2]:
                if st.button(
                    f"🫧 {option}",
                    key=f"bubble_{i}",
                    use_container_width=True
                ):
                    if option == game['correct_answer']:
                        game['score'] += 10
                        st.success("🎉 Correct! Bubble popped!")
                        if game['score'] % 50 == 0:
                            game['level'] += 1
                            st.balloons()
                    else:
                        st.error("💥 Wrong bubble! Try again!")
                    
                    # Reset for next question
                    game['question'] = None
                    st.rerun()
        
        # Display score
        st.markdown(f"""
        <div class="score-display">
            Score: {game['score']} | Level: {game['level']}
        </div>
        """, unsafe_allow_html=True)

    def star_collector(self):
        """🌟 Star Collector - Word puzzle game"""
        st.markdown("""
        <div class="game-area">
            <h3 style="text-align: center;">🌟 Collect stars by choosing the right word!</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Word challenges
        challenges = [
            {"question": "Which word means 'very happy'?", "correct": "Joyful", "options": ["Joyful", "Sad", "Angry", "Tired"]},
            {"question": "What's the opposite of 'hot'?", "correct": "Cold", "options": ["Cold", "Warm", "Cool", "Freezing"]},
            {"question": "Which word rhymes with 'cat'?", "correct": "Hat", "options": ["Hat", "Dog", "Bird", "Fish"]},
            {"question": "What do you call a baby dog?", "correct": "Puppy", "options": ["Puppy", "Kitten", "Cub", "Chick"]},
        ]
        
        if 'star_game' not in st.session_state.game_state:
            st.session_state.game_state['star_game'] = {
                'score': 0,
                'stars': 0,
                'current_challenge': random.choice(challenges)
            }
        
        game = st.session_state.game_state['star_game']
        challenge = game['current_challenge']
        
        st.markdown(f"""
        <div style="text-align: center; font-size: 20px; margin: 20px;">
            <strong>{challenge['question']}</strong>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(2)
        for i, option in enumerate(challenge['options']):
            with cols[i % 2]:
                if st.button(
                    f"⭐ {option}",
                    key=f"star_{i}",
                    use_container_width=True
                ):
                    if option == challenge['correct']:
                        game['score'] += 15
                        game['stars'] += 1
                        st.success("🌟 Star collected!")
                        st.balloons()
                    else:
                        st.error("💫 No star this time!")
                    
                    game['current_challenge'] = random.choice(challenges)
                    st.rerun()
        
        st.markdown(f"""
        <div class="score-display">
            Stars: {game['stars']} ⭐ | Score: {game['score']}
        </div>
        """, unsafe_allow_html=True)

    def lab_mixer(self):
        """🧪 Lab Mixer - Science matching game"""
        st.markdown("""
        <div class="game-area">
            <h3 style="text-align: center;">🧪 Mix the right elements!</h3>
        </div>
        """, unsafe_allow_html=True)
        
        science_facts = [
            {"question": "What gas do plants produce?", "correct": "Oxygen", "options": ["Oxygen", "Carbon", "Nitrogen", "Helium"]},
            {"question": "How many bones are in an adult human body?", "correct": "206", "options": ["206", "150", "300", "100"]},
            {"question": "What planet is closest to the Sun?", "correct": "Mercury", "options": ["Mercury", "Venus", "Earth", "Mars"]},
            {"question": "What is H2O?", "correct": "Water", "options": ["Water", "Salt", "Sugar", "Oil"]},
        ]
        
        if 'lab_game' not in st.session_state.game_state:
            st.session_state.game_state['lab_game'] = {
                'score': 0,
                'experiments': 0,
                'current_fact': random.choice(science_facts)
            }
        
        game = st.session_state.game_state['lab_game']
        fact = game['current_fact']
        
        st.markdown(f"""
        <div style="text-align: center; font-size: 20px; margin: 20px;">
            <strong>{fact['question']}</strong>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(2)
        for i, option in enumerate(fact['options']):
            with cols[i % 2]:
                if st.button(
                    f"🧪 {option}",
                    key=f"lab_{i}",
                    use_container_width=True
                ):
                    if option == fact['correct']:
                        game['score'] += 20
                        game['experiments'] += 1
                        st.success("🧪 Perfect mix!")
                        st.balloons()
                    else:
                        st.error("💥 Experiment failed!")
                    
                    game['current_fact'] = random.choice(science_facts)
                    st.rerun()
        
        st.markdown(f"""
        <div class="score-display">
            Experiments: {game['experiments']} 🧪 | Score: {game['score']}
        </div>
        """, unsafe_allow_html=True)

    def world_explorer(self):
        """🗺️ World Explorer - Geography game"""
        st.markdown("""
        <div class="game-area">
            <h3 style="text-align: center;">🗺️ Explore the world!</h3>
        </div>
        """, unsafe_allow_html=True)
        
        geography_questions = [
            {"question": "What is the capital of France?", "correct": "Paris", "options": ["Paris", "London", "Berlin", "Rome"]},
            {"question": "Which continent is Egypt in?", "correct": "Africa", "options": ["Africa", "Asia", "Europe", "America"]},
            {"question": "What is the largest ocean?", "correct": "Pacific", "options": ["Pacific", "Atlantic", "Indian", "Arctic"]},
            {"question": "Which country has the most people?", "correct": "China", "options": ["China", "India", "USA", "Brazil"]},
        ]
        
        if 'world_game' not in st.session_state.game_state:
            st.session_state.game_state['world_game'] = {
                'score': 0,
                'countries_visited': 0,
                'current_question': random.choice(geography_questions)
            }
        
        game = st.session_state.game_state['world_game']
        question = game['current_question']
        
        st.markdown(f"""
        <div style="text-align: center; font-size: 20px; margin: 20px;">
            <strong>{question['question']}</strong>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(2)
        for i, option in enumerate(question['options']):
            with cols[i % 2]:
                if st.button(
                    f"🌍 {option}",
                    key=f"world_{i}",
                    use_container_width=True
                ):
                    if option == question['correct']:
                        game['score'] += 25
                        game['countries_visited'] += 1
                        st.success("🗺️ New country discovered!")
                        st.balloons()
                    else:
                        st.error("🚫 Wrong destination!")
                    
                    game['current_question'] = random.choice(geography_questions)
                    st.rerun()
        
        st.markdown(f"""
        <div class="score-display">
            Countries: {game['countries_visited']} 🌍 | Score: {game['score']}
        </div>
        """, unsafe_allow_html=True)

    def time_machine(self):
        """⏰ Time Machine - History game"""
        st.markdown("""
        <div class="game-area">
            <h3 style="text-align: center;">⏰ Travel through time!</h3>
        </div>
        """, unsafe_allow_html=True)
        
        history_questions = [
            {"question": "Who was the first person on the moon?", "correct": "Neil Armstrong", "options": ["Neil Armstrong", "Buzz Aldrin", "John Glenn", "Alan Shepard"]},
            {"question": "When did World War II end?", "correct": "1945", "options": ["1945", "1944", "1946", "1943"]},
            {"question": "Who built the pyramids?", "correct": "Egyptians", "options": ["Egyptians", "Romans", "Greeks", "Babylonians"]},
            {"question": "What year did the Titanic sink?", "correct": "1912", "options": ["1912", "1910", "1914", "1911"]},
        ]
        
        if 'time_game' not in st.session_state.game_state:
            st.session_state.game_state['time_game'] = {
                'score': 0,
                'time_periods': 0,
                'current_question': random.choice(history_questions)
            }
        
        game = st.session_state.game_state['time_game']
        question = game['current_question']
        
        st.markdown(f"""
        <div style="text-align: center; font-size: 20px; margin: 20px;">
            <strong>{question['question']}</strong>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(2)
        for i, option in enumerate(question['options']):
            with cols[i % 2]:
                if st.button(
                    f"⏰ {option}",
                    key=f"time_{i}",
                    use_container_width=True
                ):
                    if option == question['correct']:
                        game['score'] += 30
                        game['time_periods'] += 1
                        st.success("⏰ Time travel successful!")
                        st.balloons()
                    else:
                        st.error("🌀 Time paradox!")
                    
                    game['current_question'] = random.choice(history_questions)
                    st.rerun()
        
        st.markdown(f"""
        <div class="score-display">
            Time Periods: {game['time_periods']} ⏰ | Score: {game['score']}
        </div>
        """, unsafe_allow_html=True)

# Additional games will be implemented in separate files
# This is the main framework for the enhanced arcade system

def main():
    """Main application entry point"""
    arcade = ArcadeGameManager()
    arcade.run_arcade()

if __name__ == "__main__":
    main()
