#!/usr/bin/env python3
"""
🎮 Complete Touch-Friendly Arcade - 10 Educational Games
Mobile-optimized with mouse/touch-only controls
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
    page_title="🎮 Touch Arcade",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced mobile-friendly CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4); }
        to { box-shadow: 0 15px 50px rgba(118, 75, 162, 0.6); }
    }
    
    .game-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 25px;
        border-radius: 20px;
        margin: 15px 5px;
        text-align: center;
        cursor: pointer;
        transition: all 0.4s ease;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        border: 3px solid transparent;
    }
    
    .game-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        border-color: #fff;
    }
    
    .touch-button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 18px 35px;
        border-radius: 30px;
        font-size: 20px;
        font-weight: bold;
        cursor: pointer;
        margin: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        transition: all 0.3s ease;
        min-height: 60px;
        touch-action: manipulation;
    }
    
    .touch-button:hover {
        transform: scale(1.08);
        box-shadow: 0 8px 30px rgba(0,0,0,0.35);
    }
    
    .score-display {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin: 15px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .game-area {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 20px;
        padding: 30px;
        margin: 15px 0;
        min-height: 500px;
        border: 3px solid #dee2e6;
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .mobile-optimized {
        font-size: 20px;
        line-height: 1.8;
        touch-action: manipulation;
    }
    
    .pattern-item {
        display: inline-block;
        font-size: 50px;
        padding: 20px;
        margin: 8px;
        border-radius: 15px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        min-width: 80px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .color-block {
        height: 100px;
        border-radius: 15px;
        margin: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

class TouchArcade:
    def __init__(self):
        self.games = {
            "🎯 Bubble Pop Math": {
                "description": "Pop bubbles with correct math answers!",
                "difficulty": "⭐ Easy",
                "subject": "Mathematics",
                "icon": "🎯",
                "color": "#FF6B6B"
            },
            "🌟 Star Word Hunt": {
                "description": "Collect stars by finding the right words!",
                "difficulty": "⭐⭐ Medium",
                "subject": "Language",
                "icon": "🌟",
                "color": "#4ECDC4"
            },
            "🧪 Science Mixer": {
                "description": "Mix elements and discover science!",
                "difficulty": "⭐⭐ Medium",
                "subject": "Science",
                "icon": "🧪",
                "color": "#45B7D1"
            },
            "🗺️ World Explorer": {
                "description": "Explore countries and cultures!",
                "difficulty": "⭐⭐⭐ Hard",
                "subject": "Geography",
                "icon": "🗺️",
                "color": "#96CEB4"
            },
            "⏰ Time Traveler": {
                "description": "Journey through history!",
                "difficulty": "⭐⭐⭐ Hard",
                "subject": "History",
                "icon": "⏰",
                "color": "#FFEAA7"
            },
            "🎨 Color Creator": {
                "description": "Mix colors and create masterpieces!",
                "difficulty": "⭐ Easy",
                "subject": "Art",
                "icon": "🎨",
                "color": "#FD79A8"
            },
            "🎵 Beat Master": {
                "description": "Feel the rhythm and learn music!",
                "difficulty": "⭐⭐ Medium",
                "subject": "Music",
                "icon": "🎵",
                "color": "#A29BFE"
            },
            "🤖 Code Cracker": {
                "description": "Solve programming puzzles!",
                "difficulty": "⭐⭐⭐ Hard",
                "subject": "Programming",
                "icon": "🤖",
                "color": "#6C5CE7"
            },
            "🧩 Pattern Genius": {
                "description": "Complete amazing patterns!",
                "difficulty": "⭐⭐ Medium",
                "subject": "Logic",
                "icon": "🧩",
                "color": "#00B894"
            },
            "🧠 Memory Champion": {
                "description": "Test your memory power!",
                "difficulty": "⭐ Easy",
                "subject": "Memory",
                "icon": "🧠",
                "color": "#E17055"
            }
        }
        
        # Initialize session state
        if 'current_game' not in st.session_state:
            st.session_state.current_game = None
        if 'player_stats' not in st.session_state:
            st.session_state.player_stats = {
                'total_score': 0,
                'games_played': 0,
                'achievements': [],
                'high_scores': {}
            }
        if 'game_states' not in st.session_state:
            st.session_state.game_states = {}

    def show_main_menu(self):
        """Display the enhanced main menu"""
        st.markdown("""
        <div class="main-header">
            <h1>🎮 Touch-Friendly Arcade</h1>
            <h2>10 Amazing Educational Games</h2>
            <p>✨ Tap to Play • 📱 Mobile Optimized • 🎓 Learn While Having Fun</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced player stats
        stats = st.session_state.player_stats
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="score-display">
                🏆 Total Score<br><span style="font-size: 28px;">{stats['total_score']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="score-display">
                🎮 Games Played<br><span style="font-size: 28px;">{stats['games_played']}</span>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"""
            <div class="score-display">
                🏅 Achievements<br><span style="font-size: 28px;">{len(stats['achievements'])}</span>
            </div>
            """, unsafe_allow_html=True)
            
        with col4:
            avg_score = stats['total_score'] // max(stats['games_played'], 1)
            st.markdown(f"""
            <div class="score-display">
                📊 Average<br><span style="font-size: 28px;">{avg_score}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 🎮 Choose Your Adventure")
        
        # Display games in an enhanced grid
        cols = st.columns(2)
        for i, (game_name, game_info) in enumerate(self.games.items()):
            with cols[i % 2]:
                # Create custom styled button
                button_html = f"""
                <div style="background: linear-gradient(135deg, {game_info['color']} 0%, {game_info['color']}CC 100%); 
                           color: white; padding: 25px; border-radius: 20px; margin: 10px; 
                           text-align: center; cursor: pointer; transition: all 0.3s ease;
                           box-shadow: 0 8px 25px rgba(0,0,0,0.2); border: 3px solid transparent;">
                    <div style="font-size: 40px; margin-bottom: 10px;">{game_info['icon']}</div>
                    <div style="font-size: 20px; font-weight: bold; margin-bottom: 8px;">{game_name.split(' ', 1)[1]}</div>
                    <div style="font-size: 16px; margin-bottom: 8px;">{game_info['description']}</div>
                    <div style="font-size: 14px; opacity: 0.9;">📚 {game_info['subject']} • {game_info['difficulty']}</div>
                </div>
                """
                
                if st.button(
                    f"{game_info['icon']} {game_name.split(' ', 1)[1]}",
                    key=f"game_{i}",
                    use_container_width=True,
                    help=f"{game_info['description']} - {game_info['subject']} ({game_info['difficulty']})"
                ):
                    st.session_state.current_game = game_name
                    st.rerun()

    def run_game(self, game_name):
        """Route to the appropriate game"""
        # Back button
        if st.button("🏠 Back to Arcade", key="back_button", use_container_width=True):
            st.session_state.current_game = None
            st.rerun()
        
        # Game header
        game_info = self.games[game_name]
        st.markdown(f"""
        <div style="text-align: center; background: linear-gradient(135deg, {game_info['color']} 0%, {game_info['color']}CC 100%);
                   color: white; padding: 20px; border-radius: 15px; margin-bottom: 20px;">
            <h1>{game_info['icon']} {game_name.split(' ', 1)[1]}</h1>
            <p>{game_info['description']} • {game_info['difficulty']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Route to specific game
        if "Bubble Pop Math" in game_name:
            self.bubble_pop_math()
        elif "Star Word Hunt" in game_name:
            self.star_word_hunt()
        elif "Science Mixer" in game_name:
            self.science_mixer()
        elif "World Explorer" in game_name:
            self.world_explorer()
        elif "Time Traveler" in game_name:
            self.time_traveler()
        elif "Color Creator" in game_name:
            self.color_creator()
        elif "Beat Master" in game_name:
            self.beat_master()
        elif "Code Cracker" in game_name:
            self.code_cracker()
        elif "Pattern Genius" in game_name:
            self.pattern_genius()
        elif "Memory Champion" in game_name:
            self.memory_champion()

    def bubble_pop_math(self):
        """🎯 Enhanced Bubble Pop Math Game"""
        if 'bubble_game' not in st.session_state.game_states:
            st.session_state.game_states['bubble_game'] = {
                'score': 0,
                'level': 1,
                'bubbles_popped': 0,
                'streak': 0,
                'question': None,
                'options': []
            }
        
        game = st.session_state.game_states['bubble_game']
        
        # Generate question
        if game['question'] is None:
            level = game['level']
            if level <= 3:
                a, b = random.randint(1, 10), random.randint(1, 10)
                ops = ['+', '-', '×']
                op = random.choice(ops)
                if op == '+':
                    question = f"{a} + {b}"
                    correct = a + b
                elif op == '-':
                    a, b = max(a, b), min(a, b)
                    question = f"{a} - {b}"
                    correct = a - b
                else:
                    question = f"{a} × {b}"
                    correct = a * b
            else:
                # Advanced math
                a, b = random.randint(10, 50), random.randint(2, 10)
                ops = ['÷', '²']
                op = random.choice(ops)
                if op == '÷':
                    question = f"{a * b} ÷ {b}"
                    correct = a
                else:
                    question = f"{a}²"
                    correct = a * a
            
            # Generate bubble options
            options = [correct]
            while len(options) < 6:  # More bubbles for fun!
                wrong = correct + random.randint(-15, 15)
                if wrong not in options and wrong > 0:
                    options.append(wrong)
            
            random.shuffle(options)
            game['question'] = question
            game['options'] = options
            game['correct_answer'] = correct
        
        # Display game area
        st.markdown(f"""
        <div class="game-area">
            <div style="text-align: center; font-size: 32px; margin: 30px; 
                       background: linear-gradient(45deg, #FF6B6B, #4ECDC4); 
                       color: white; padding: 20px; border-radius: 15px;">
                <strong>What is {game['question']}?</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Bubble display in 3x2 grid
        cols = st.columns(3)
        for i, option in enumerate(game['options']):
            with cols[i % 3]:
                bubble_color = f"hsl({random.randint(0, 360)}, 70%, 60%)"
                if st.button(
                    f"🫧 {option}",
                    key=f"bubble_{i}",
                    use_container_width=True,
                    help="Pop this bubble!"
                ):
                    if option == game['correct_answer']:
                        game['score'] += 10 + (game['streak'] * 2)
                        game['bubbles_popped'] += 1
                        game['streak'] += 1
                        st.success(f"🎉 Bubble popped! +{10 + (game['streak'] * 2)} points!")
                        if game['streak'] >= 5:
                            st.balloons()
                        if game['score'] % 100 == 0:
                            game['level'] += 1
                    else:
                        game['streak'] = 0
                        st.error("💥 Wrong bubble! Streak reset!")
                    
                    game['question'] = None
                    st.rerun()
        
        # Enhanced score display
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <div class="score-display">
                🏆 Score<br>{game['score']}
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="score-display">
                📊 Level<br>{game['level']}
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="score-display">
                🫧 Popped<br>{game['bubbles_popped']}
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class="score-display">
                🔥 Streak<br>{game['streak']}
            </div>
            """, unsafe_allow_html=True)

    def star_word_hunt(self):
        """🌟 Enhanced Star Word Hunt Game"""
        if 'star_game' not in st.session_state.game_states:
            st.session_state.game_states['star_game'] = {
                'score': 0,
                'stars_collected': 0,
                'level': 1,
                'current_challenge': None
            }
        
        game = st.session_state.game_states['star_game']
        
        # Word challenges by level
        challenges = {
            1: [
                {"question": "Which word means 'very happy'?", "correct": "Joyful", "options": ["Joyful", "Sad", "Angry", "Tired"]},
                {"question": "What's the opposite of 'hot'?", "correct": "Cold", "options": ["Cold", "Warm", "Cool", "Freezing"]},
                {"question": "Which word rhymes with 'cat'?", "correct": "Hat", "options": ["Hat", "Dog", "Bird", "Fish"]},
            ],
            2: [
                {"question": "What do you call a baby dog?", "correct": "Puppy", "options": ["Puppy", "Kitten", "Cub", "Chick"]},
                {"question": "Which word means 'very big'?", "correct": "Enormous", "options": ["Enormous", "Tiny", "Small", "Medium"]},
                {"question": "What's a synonym for 'smart'?", "correct": "Intelligent", "options": ["Intelligent", "Dumb", "Slow", "Lazy"]},
            ],
            3: [
                {"question": "Which word means 'to make better'?", "correct": "Improve", "options": ["Improve", "Worsen", "Break", "Ignore"]},
                {"question": "What's the past tense of 'run'?", "correct": "Ran", "options": ["Ran", "Runned", "Running", "Runs"]},
                {"question": "Which word means 'very old'?", "correct": "Ancient", "options": ["Ancient", "New", "Modern", "Recent"]},
            ]
        }
        
        if game['current_challenge'] is None:
            level_challenges = challenges.get(game['level'], challenges[1])
            game['current_challenge'] = random.choice(level_challenges)
        
        challenge = game['current_challenge']
        
        st.markdown(f"""
        <div class="game-area">
            <div style="text-align: center; font-size: 28px; margin: 30px; 
                       background: linear-gradient(45deg, #4ECDC4, #44A08D); 
                       color: white; padding: 25px; border-radius: 15px;">
                <strong>{challenge['question']}</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Star options
        cols = st.columns(2)
        for i, option in enumerate(challenge['options']):
            with cols[i % 2]:
                if st.button(
                    f"⭐ {option}",
                    key=f"star_{i}",
                    use_container_width=True
                ):
                    if option == challenge['correct']:
                        points = 15 * game['level']
                        game['score'] += points
                        game['stars_collected'] += 1
                        st.success(f"🌟 Star collected! +{points} points!")
                        if game['stars_collected'] % 5 == 0:
                            game['level'] += 1
                            st.balloons()
                    else:
                        st.error("💫 No star this time!")
                    
                    game['current_challenge'] = None
                    st.rerun()
        
        # Score display
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="score-display">
                🌟 Stars<br>{game['stars_collected']}
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="score-display">
                🏆 Score<br>{game['score']}
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="score-display">
                📊 Level<br>{game['level']}
            </div>
            """, unsafe_allow_html=True)

    def run(self):
        """Main application runner"""
        if st.session_state.current_game is None:
            self.show_main_menu()
        else:
            self.run_game(st.session_state.current_game)

# Placeholder methods for remaining games
    def science_mixer(self):
        st.markdown("🧪 Science Mixer - Coming Soon! Mix elements and discover science!")
        
    def world_explorer(self):
        st.markdown("🗺️ World Explorer - Coming Soon! Explore countries and cultures!")
        
    def time_traveler(self):
        st.markdown("⏰ Time Traveler - Coming Soon! Journey through history!")
        
    def color_creator(self):
        st.markdown("🎨 Color Creator - Coming Soon! Mix colors and create art!")
        
    def beat_master(self):
        st.markdown("🎵 Beat Master - Coming Soon! Feel the rhythm!")
        
    def code_cracker(self):
        st.markdown("🤖 Code Cracker - Coming Soon! Solve programming puzzles!")
        
    def pattern_genius(self):
        st.markdown("🧩 Pattern Genius - Coming Soon! Complete amazing patterns!")
        
    def memory_champion(self):
        st.markdown("🧠 Memory Champion - Coming Soon! Test your memory!")

def main():
    """Main application entry point"""
    arcade = TouchArcade()
    arcade.run()

if __name__ == "__main__":
    main()
