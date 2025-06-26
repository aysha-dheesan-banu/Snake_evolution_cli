#!/usr/bin/env python3
"""
🎮 Enhanced Arcade Games - Remaining 5 Games
Touch-friendly implementations for Color Master, Rhythm Hero, Code Breaker, Pattern Master, Memory Matrix
"""

import streamlit as st
import random
import time
import json
from typing import List, Dict, Any

def color_master_game():
    """🎨 Color Master - Art and color matching game"""
    st.markdown("""
    <div class="game-area">
        <h3 style="text-align: center;">🎨 Match the colors and create art!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    colors = {
        "Red": "#FF0000",
        "Blue": "#0000FF", 
        "Yellow": "#FFFF00",
        "Green": "#00FF00",
        "Purple": "#800080",
        "Orange": "#FFA500",
        "Pink": "#FFC0CB",
        "Brown": "#A52A2A"
    }
    
    color_questions = [
        {"question": "What color do you get when you mix Red + Yellow?", "correct": "Orange", "mix": ["Red", "Yellow"]},
        {"question": "What color do you get when you mix Blue + Yellow?", "correct": "Green", "mix": ["Blue", "Yellow"]},
        {"question": "What color do you get when you mix Red + Blue?", "correct": "Purple", "mix": ["Red", "Blue"]},
        {"question": "What is the primary color that is not Red or Blue?", "correct": "Yellow", "mix": []},
    ]
    
    if 'color_game' not in st.session_state.game_state:
        st.session_state.game_state['color_game'] = {
            'score': 0,
            'artworks': 0,
            'current_question': random.choice(color_questions)
        }
    
    game = st.session_state.game_state['color_game']
    question = game['current_question']
    
    # Show color mixing if applicable
    if question['mix']:
        st.markdown("### 🎨 Color Mixing:")
        cols = st.columns(len(question['mix']) + 1)
        for i, color in enumerate(question['mix']):
            with cols[i]:
                st.markdown(f"""
                <div style="background-color: {colors[color]}; height: 80px; border-radius: 10px; 
                           display: flex; align-items: center; justify-content: center; 
                           color: white; font-weight: bold; margin: 5px;">
                    {color}
                </div>
                """, unsafe_allow_html=True)
        
        with cols[-1]:
            st.markdown("""
            <div style="background-color: #ddd; height: 80px; border-radius: 10px; 
                       display: flex; align-items: center; justify-content: center; 
                       font-size: 30px; margin: 5px;">
                = ?
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; font-size: 20px; margin: 20px;">
        <strong>{question['question']}</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Color options
    color_options = list(colors.keys())
    random.shuffle(color_options)
    color_options = color_options[:4]
    if question['correct'] not in color_options:
        color_options[0] = question['correct']
        random.shuffle(color_options)
    
    cols = st.columns(2)
    for i, color in enumerate(color_options):
        with cols[i % 2]:
            if st.button(
                f"🎨 {color}",
                key=f"color_{i}",
                use_container_width=True
            ):
                if color == question['correct']:
                    game['score'] += 15
                    game['artworks'] += 1
                    st.success("🎨 Beautiful artwork created!")
                    st.balloons()
                else:
                    st.error("🎭 Color doesn't match!")
                
                game['current_question'] = random.choice(color_questions)
                st.rerun()
    
    st.markdown(f"""
    <div class="score-display">
        Artworks: {game['artworks']} 🎨 | Score: {game['score']}
    </div>
    """, unsafe_allow_html=True)

def rhythm_hero_game():
    """🎵 Rhythm Hero - Music and rhythm game"""
    st.markdown("""
    <div class="game-area">
        <h3 style="text-align: center;">🎵 Hit the beats and feel the rhythm!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    music_questions = [
        {"question": "How many beats are in 4/4 time?", "correct": "4", "options": ["4", "3", "2", "8"]},
        {"question": "What instrument has 88 keys?", "correct": "Piano", "options": ["Piano", "Guitar", "Violin", "Drums"]},
        {"question": "Which note comes after 'Do'?", "correct": "Re", "options": ["Re", "Mi", "Fa", "So"]},
        {"question": "What does 'forte' mean in music?", "correct": "Loud", "options": ["Loud", "Soft", "Fast", "Slow"]},
    ]
    
    if 'rhythm_game' not in st.session_state.game_state:
        st.session_state.game_state['rhythm_game'] = {
            'score': 0,
            'beats_hit': 0,
            'current_question': random.choice(music_questions),
            'rhythm_pattern': []
        }
    
    game = st.session_state.game_state['rhythm_game']
    question = game['current_question']
    
    # Generate rhythm pattern
    if not game['rhythm_pattern']:
        game['rhythm_pattern'] = [random.choice(['🎵', '🎶', '🎼', '🎹']) for _ in range(4)]
    
    # Show rhythm pattern
    st.markdown("### 🎵 Follow the Rhythm:")
    cols = st.columns(4)
    for i, note in enumerate(game['rhythm_pattern']):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; font-size: 40px; padding: 20px; 
                       background: linear-gradient(45deg, #FF6B6B, #4ECDC4); 
                       border-radius: 15px; margin: 5px;">
                {note}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; font-size: 20px; margin: 20px;">
        <strong>{question['question']}</strong>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, option in enumerate(question['options']):
        with cols[i % 2]:
            if st.button(
                f"🎵 {option}",
                key=f"rhythm_{i}",
                use_container_width=True
            ):
                if option == question['correct']:
                    game['score'] += 20
                    game['beats_hit'] += 1
                    st.success("🎵 Perfect rhythm!")
                    st.balloons()
                else:
                    st.error("🎶 Off beat!")
                
                game['current_question'] = random.choice(music_questions)
                game['rhythm_pattern'] = []
                st.rerun()
    
    st.markdown(f"""
    <div class="score-display">
        Beats Hit: {game['beats_hit']} 🎵 | Score: {game['score']}
    </div>
    """, unsafe_allow_html=True)

def code_breaker_game():
    """🤖 Code Breaker - Programming logic game"""
    st.markdown("""
    <div class="game-area">
        <h3 style="text-align: center;">🤖 Break the code with programming logic!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    coding_questions = [
        {"question": "What does 'if' do in programming?", "correct": "Makes decisions", "options": ["Makes decisions", "Repeats code", "Stores data", "Prints text"]},
        {"question": "What is a 'loop' used for?", "correct": "Repeat actions", "options": ["Repeat actions", "Store numbers", "Make websites", "Send emails"]},
        {"question": "What does '==' mean in code?", "correct": "Compare values", "options": ["Compare values", "Add numbers", "Assign value", "Subtract"]},
        {"question": "What is a 'variable'?", "correct": "Stores information", "options": ["Stores information", "Deletes files", "Plays music", "Draws pictures"]},
    ]
    
    if 'code_game' not in st.session_state.game_state:
        st.session_state.game_state['code_game'] = {
            'score': 0,
            'codes_broken': 0,
            'current_question': random.choice(coding_questions),
            'code_blocks': []
        }
    
    game = st.session_state.game_state['code_game']
    question = game['current_question']
    
    # Generate code blocks
    if not game['code_blocks']:
        blocks = ['if', 'for', 'while', 'def', 'print', 'input']
        game['code_blocks'] = random.sample(blocks, 4)
    
    # Show code blocks
    st.markdown("### 🤖 Code Blocks:")
    cols = st.columns(4)
    for i, block in enumerate(game['code_blocks']):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; font-family: monospace; font-size: 16px; 
                       padding: 15px; background: #2d3748; color: #68d391; 
                       border-radius: 10px; margin: 5px; border: 2px solid #4a5568;">
                {block}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; font-size: 20px; margin: 20px;">
        <strong>{question['question']}</strong>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, option in enumerate(question['options']):
        with cols[i % 2]:
            if st.button(
                f"🤖 {option}",
                key=f"code_{i}",
                use_container_width=True
            ):
                if option == question['correct']:
                    game['score'] += 25
                    game['codes_broken'] += 1
                    st.success("🤖 Code cracked!")
                    st.balloons()
                else:
                    st.error("💻 Access denied!")
                
                game['current_question'] = random.choice(coding_questions)
                game['code_blocks'] = []
                st.rerun()
    
    st.markdown(f"""
    <div class="score-display">
        Codes Broken: {game['codes_broken']} 🤖 | Score: {game['score']}
    </div>
    """, unsafe_allow_html=True)

def pattern_master_game():
    """🧩 Pattern Master - Logic and pattern recognition"""
    st.markdown("""
    <div class="game-area">
        <h3 style="text-align: center;">🧩 Complete the pattern!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if 'pattern_game' not in st.session_state.game_state:
        st.session_state.game_state['pattern_game'] = {
            'score': 0,
            'patterns_solved': 0,
            'current_pattern': None,
            'pattern_type': None
        }
    
    game = st.session_state.game_state['pattern_game']
    
    # Generate new pattern if needed
    if game['current_pattern'] is None:
        pattern_types = ['number', 'shape', 'color']
        game['pattern_type'] = random.choice(pattern_types)
        
        if game['pattern_type'] == 'number':
            # Number sequence
            start = random.randint(1, 10)
            step = random.randint(2, 5)
            sequence = [start + i * step for i in range(4)]
            next_num = start + 4 * step
            
            game['current_pattern'] = {
                'sequence': sequence,
                'correct': next_num,
                'options': [next_num, next_num + step, next_num - step, next_num + 2*step],
                'display': [str(x) for x in sequence] + ['?']
            }
            
        elif game['pattern_type'] == 'shape':
            # Shape pattern
            shapes = ['🔴', '🔵', '🟡', '🟢', '🟣', '🟠']
            pattern_length = 3
            base_pattern = random.sample(shapes, pattern_length)
            sequence = base_pattern + base_pattern[:1]  # Repeat first element
            next_shape = base_pattern[1]
            
            game['current_pattern'] = {
                'sequence': sequence,
                'correct': next_shape,
                'options': random.sample(shapes, 4),
                'display': sequence + ['?']
            }
            
        else:  # color
            # Color pattern
            colors = ['🔴', '🟦', '🟨', '🟩']
            pattern = [colors[i % len(colors)] for i in range(4)]
            next_color = colors[4 % len(colors)]
            
            game['current_pattern'] = {
                'sequence': pattern,
                'correct': next_color,
                'options': colors,
                'display': pattern + ['?']
            }
        
        # Ensure correct answer is in options
        if game['current_pattern']['correct'] not in game['current_pattern']['options']:
            game['current_pattern']['options'][0] = game['current_pattern']['correct']
        random.shuffle(game['current_pattern']['options'])
    
    pattern = game['current_pattern']
    
    # Display pattern
    st.markdown("### 🧩 Pattern Sequence:")
    cols = st.columns(len(pattern['display']))
    for i, item in enumerate(pattern['display']):
        with cols[i]:
            if item == '?':
                st.markdown(f"""
                <div style="text-align: center; font-size: 40px; padding: 20px; 
                           background: #ddd; border-radius: 15px; margin: 5px;
                           border: 3px dashed #666;">
                    ?
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="text-align: center; font-size: 40px; padding: 20px; 
                           background: linear-gradient(45deg, #667eea, #764ba2); 
                           color: white; border-radius: 15px; margin: 5px;">
                    {item}
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-size: 20px; margin: 20px;">
        <strong>What comes next in the pattern?</strong>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, option in enumerate(pattern['options']):
        with cols[i % 2]:
            if st.button(
                f"🧩 {option}",
                key=f"pattern_{i}",
                use_container_width=True
            ):
                if option == pattern['correct']:
                    game['score'] += 30
                    game['patterns_solved'] += 1
                    st.success("🧩 Pattern completed!")
                    st.balloons()
                else:
                    st.error("🔍 Pattern doesn't match!")
                
                game['current_pattern'] = None
                st.rerun()
    
    st.markdown(f"""
    <div class="score-display">
        Patterns Solved: {game['patterns_solved']} 🧩 | Score: {game['score']}
    </div>
    """, unsafe_allow_html=True)

def memory_matrix_game():
    """🧠 Memory Matrix - Memory and concentration game"""
    st.markdown("""
    <div class="game-area">
        <h3 style="text-align: center;">🧠 Remember the sequence!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if 'memory_game' not in st.session_state.game_state:
        st.session_state.game_state['memory_game'] = {
            'score': 0,
            'sequences_remembered': 0,
            'current_sequence': [],
            'player_sequence': [],
            'showing_sequence': False,
            'sequence_length': 3,
            'show_time': 0
        }
    
    game = st.session_state.game_state['memory_game']
    
    # Generate new sequence if needed
    if not game['current_sequence']:
        colors = ['🔴', '🔵', '🟡', '🟢']
        game['current_sequence'] = [random.choice(colors) for _ in range(game['sequence_length'])]
        game['player_sequence'] = []
        game['showing_sequence'] = True
        game['show_time'] = time.time()
    
    # Show sequence for limited time
    if game['showing_sequence']:
        if time.time() - game['show_time'] < 3:  # Show for 3 seconds
            st.markdown("### 🧠 Memorize this sequence:")
            cols = st.columns(len(game['current_sequence']))
            for i, color in enumerate(game['current_sequence']):
                with cols[i]:
                    st.markdown(f"""
                    <div style="text-align: center; font-size: 50px; padding: 25px; 
                               background: linear-gradient(45deg, #FF6B6B, #4ECDC4); 
                               border-radius: 20px; margin: 10px; animation: pulse 1s infinite;">
                        {color}
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="text-align: center; font-size: 18px; margin: 20px;">
                <strong>Time remaining: {3 - int(time.time() - game['show_time'])} seconds</strong>
            </div>
            """, unsafe_allow_html=True)
            
            time.sleep(0.1)
            st.rerun()
        else:
            game['showing_sequence'] = False
            st.rerun()
    
    else:
        # Player input phase
        st.markdown("### 🧠 Now repeat the sequence:")
        
        # Show player's current input
        if game['player_sequence']:
            st.markdown("Your sequence so far:")
            cols = st.columns(len(game['player_sequence']))
            for i, color in enumerate(game['player_sequence']):
                with cols[i]:
                    st.markdown(f"""
                    <div style="text-align: center; font-size: 40px; padding: 20px; 
                               background: #e2e8f0; border-radius: 15px; margin: 5px;">
                        {color}
                    </div>
                    """, unsafe_allow_html=True)
        
        # Color buttons for input
        colors = ['🔴', '🔵', '🟡', '🟢']
        cols = st.columns(4)
        for i, color in enumerate(colors):
            with cols[i]:
                if st.button(
                    color,
                    key=f"memory_{i}",
                    use_container_width=True
                ):
                    game['player_sequence'].append(color)
                    
                    # Check if sequence is complete
                    if len(game['player_sequence']) == len(game['current_sequence']):
                        if game['player_sequence'] == game['current_sequence']:
                            game['score'] += 40
                            game['sequences_remembered'] += 1
                            game['sequence_length'] = min(game['sequence_length'] + 1, 6)
                            st.success("🧠 Perfect memory!")
                            st.balloons()
                        else:
                            st.error("🤔 Sequence doesn't match!")
                            game['sequence_length'] = max(game['sequence_length'] - 1, 3)
                        
                        # Reset for next round
                        game['current_sequence'] = []
                        time.sleep(1)
                    
                    st.rerun()
    
    st.markdown(f"""
    <div class="score-display">
        Sequences: {game['sequences_remembered']} 🧠 | Score: {game['score']} | Level: {game['sequence_length']}
    </div>
    """, unsafe_allow_html=True)

# Export functions for use in main arcade
__all__ = [
    'color_master_game',
    'rhythm_hero_game', 
    'code_breaker_game',
    'pattern_master_game',
    'memory_matrix_game'
]
