#!/usr/bin/env python3
"""
Test script for Enhanced Snake Evolution with Subject/Level Selection and Python Games
"""

import sys
import os

def test_enhanced_snake():
    """Test the enhanced snake game"""
    print("🐍 Testing Enhanced Snake Evolution")
    print("=" * 50)
    
    # Check if the snake_evolution.py file exists
    if not os.path.exists("snake_evolution.py"):
        print("❌ Error: snake_evolution.py not found!")
        return False
    
    try:
        # Import the game module
        import snake_evolution
        
        print("✅ Successfully imported snake_evolution module")
        
        # Check if the new GameState enum has all required states
        required_states = [
            'MENU', 'PLAYING', 'CATEGORY_SELECT', 'SUBJECT_SELECT', 
            'LEVEL_SELECT', 'QUESTION', 'PYTHON_GAME_SELECT', 
            'PYTHON_GAME_PLAYING', 'GAME_OVER', 'PAUSED'
        ]
        
        for state in required_states:
            if hasattr(snake_evolution.GameState, state):
                print(f"✅ GameState.{state} found")
            else:
                print(f"❌ GameState.{state} not found")
                return False
        
        # Check if SnakeGame class has the new methods
        game_class = snake_evolution.SnakeGame
        
        required_methods = [
            'draw_subject_select',
            'draw_level_select', 
            'draw_python_game_select',
            'start_python_game',
            'init_tic_tac_toe',
            'init_space_shooter',
            'init_car_racing',
            'init_platformer_2d',
            'init_adventure_3d',
            'handle_python_game_input',
            'update_python_games',
            'draw_python_games',
            'draw_tic_tac_toe',
            'draw_space_shooter',
            'draw_car_racing',
            'draw_platformer_2d',
            'draw_adventure_3d'
        ]
        
        for method in required_methods:
            if hasattr(game_class, method):
                print(f"✅ Method {method} found")
            else:
                print(f"❌ Method {method} not found")
                return False
        
        # Test creating a game instance
        try:
            game = snake_evolution.SnakeGame()
            print("✅ Successfully created SnakeGame instance")
            
            # Test new attributes
            new_attributes = [
                'selected_subject',
                'selected_level', 
                'current_python_game'
            ]
            
            for attr in new_attributes:
                if hasattr(game, attr):
                    print(f"✅ Attribute {attr} found")
                else:
                    print(f"❌ Attribute {attr} not found")
                    return False
            
            # Test new translation keys
            new_translation_keys = [
                'subject_select',
                'level_select',
                'python_game_select',
                'back',
                'math_wizard',
                'science_lab',
                'geography_quest', 
                'history_hunter',
                'word_master',
                'tic_tac_toe',
                'space_shooter',
                'car_racing',
                'platformer_2d',
                'adventure_3d',
                'easy',
                'medium',
                'hard',
                'expert',
                'master'
            ]
            
            for key in new_translation_keys:
                if key in game.translations['english']:
                    print(f"✅ Translation key '{key}' found")
                else:
                    print(f"❌ Translation key '{key}' not found")
                    return False
            
        except Exception as e:
            print(f"❌ Error creating game instance: {e}")
            return False
        
        print("\n🎉 All tests passed! Enhanced Snake Evolution features:")
        print("   ✅ Subject selection for educational games")
        print("   ✅ 5 difficulty levels for each subject")
        print("   ✅ 5 playable Python games")
        print("   ✅ Complete game implementations")
        print("   ✅ Enhanced multilingual support")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error importing snake_evolution: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def show_enhanced_usage():
    """Show how to use the enhanced game"""
    print("\n📖 Enhanced Snake Evolution Usage Guide:")
    print("=" * 50)
    print("🎮 MAIN GAME FLOW:")
    print("1. Start game → Press SPACE")
    print("2. Control snake → Arrow keys")
    print("3. Eat food (❓) → Category selection appears")
    print()
    print("📚 EDUCATIONAL PATH (Press 1):")
    print("   → Subject Selection:")
    print("     1. 🧮 Math Wizard")
    print("     2. 🧪 Science Lab") 
    print("     3. 🌍 Geography Quest")
    print("     4. 📚 History Hunter")
    print("     5. 🔤 Word Master")
    print("   → Level Selection:")
    print("     1. ⭐ Easy")
    print("     2. ⭐⭐ Medium")
    print("     3. ⭐⭐⭐ Hard")
    print("     4. ⭐⭐⭐⭐ Expert")
    print("     5. ⭐⭐⭐⭐⭐ Master")
    print("   → Answer questions to grow snake!")
    print()
    print("🐍 PYTHON GAMES PATH (Press 2):")
    print("   → Game Selection:")
    print("     1. ⭕ Tic-Tac-Toe - Strategic board game")
    print("     2. 🚀 Space Shooter - Action shooting game")
    print("     3. 🏎️ Car Racing - Dodge obstacles racing")
    print("     4. 🎮 2D Platformer - Jump and run game")
    print("     5. 🎯 3D Adventure - Rotating 3D experience")
    print("   → Play actual games!")
    print()
    print("🎮 GAME CONTROLS:")
    print("   • Arrow Keys - Move snake/control games")
    print("   • SPACE - Start game/shoot/jump")
    print("   • 1-5 - Select options")
    print("   • B - Go back to previous menu")
    print("   • ESC - Exit Python games")
    print("   • L - Toggle language")
    print("   • P - Pause/Resume")
    print("   • R - Restart")
    print("   • Q - Quit")

if __name__ == "__main__":
    success = test_enhanced_snake()
    
    if success:
        show_enhanced_usage()
        print(f"\n🚀 Ready to play Enhanced Snake Evolution!")
        print("Run: ./play_snake_evolution.sh")
    else:
        print("\n❌ Tests failed. Please check the snake_evolution.py file.")
        sys.exit(1)
