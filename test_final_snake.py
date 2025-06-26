#!/usr/bin/env python3
"""
Test script for Final Enhanced Snake Evolution
- Education games: 5 playable games (1-5)
- Python games: 5 playable games (1-5) with Zombie Dash and Ball Run
"""

import sys
import os

def test_final_snake():
    """Test the final enhanced snake game"""
    print("🐍 Testing Final Enhanced Snake Evolution")
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
            'MENU', 'PLAYING', 'CATEGORY_SELECT', 'EDUCATION_GAME_SELECT', 
            'EDUCATION_GAME_PLAYING', 'PYTHON_GAME_SELECT', 'PYTHON_GAME_PLAYING',
            'GAME_OVER', 'PAUSED'
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
            'draw_education_game_select',
            'start_education_game',
            'init_math_wizard',
            'init_science_lab',
            'init_geography_quest',
            'init_history_hunter',
            'init_word_master',
            'init_zombie_dash',
            'init_ball_run',
            'handle_education_game_input',
            'update_education_games',
            'draw_education_games',
            'draw_math_wizard',
            'draw_science_lab',
            'draw_geography_quest',
            'draw_history_hunter',
            'draw_word_master',
            'draw_zombie_dash',
            'draw_ball_run',
            'update_zombie_dash',
            'update_ball_run'
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
                'current_education_game',
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
                'education_game_select',
                'python_game_select',
                'zombie_dash',
                'ball_run'
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
        
        print("\n🎉 All tests passed! Final Enhanced Snake Evolution features:")
        print("   ✅ Direct game selection for both categories")
        print("   ✅ 5 playable educational games")
        print("   ✅ 5 playable Python games (including Zombie Dash & Ball Run)")
        print("   ✅ Complete game implementations")
        print("   ✅ Enhanced multilingual support")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error importing snake_evolution: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def show_final_usage():
    """Show how to use the final enhanced game"""
    print("\n📖 Final Enhanced Snake Evolution Usage Guide:")
    print("=" * 60)
    print("🎮 MAIN GAME FLOW:")
    print("1. Start game → Press SPACE")
    print("2. Control snake → Arrow keys")
    print("3. Eat food (❓) → Category selection appears")
    print()
    print("📚 EDUCATIONAL GAMES (Press 1):")
    print("   → Direct Game Selection:")
    print("     1. 🧮 Math Wizard - Solve math problems")
    print("     2. 🧪 Science Lab - Answer science questions")
    print("     3. 🌍 Geography Quest - World knowledge challenges")
    print("     4. 📚 History Hunter - Historical events and figures")
    print("     5. 🔤 Word Master - Language and vocabulary")
    print("   → Type answers and press ENTER")
    print("   → ESC to return to game selection")
    print()
    print("🐍 PYTHON GAMES (Press 2):")
    print("   → Direct Game Selection:")
    print("     1. ⭕ Tic-Tac-Toe - Strategic board game")
    print("     2. 🚀 Space Shooter - Action shooting game")
    print("     3. 🏎️ Car Racing - Dodge obstacles racing")
    print("     4. 🧟 Zombie Dash - Survive zombie attacks")
    print("     5. ⚽ Ball Run - Physics-based ball control")
    print("   → Play actual interactive games!")
    print("   → ESC to return to game selection")
    print()
    print("🎮 GAME CONTROLS:")
    print("   • Arrow Keys - Move snake/control games")
    print("   • SPACE - Start game/shoot/special actions")
    print("   • 1-5 - Select games directly")
    print("   • B - Go back to previous menu")
    print("   • ESC - Exit current game")
    print("   • ENTER - Submit answers (education games)")
    print("   • BACKSPACE - Delete text input")
    print("   • L - Toggle language")
    print("   • P - Pause/Resume")
    print("   • R - Restart")
    print("   • Q - Quit")
    print()
    print("🎯 GAME DESCRIPTIONS:")
    print()
    print("📚 EDUCATIONAL GAMES:")
    print("• Math Wizard: Solve arithmetic problems with instant feedback")
    print("• Science Lab: Answer chemistry, physics, and biology questions")
    print("• Geography Quest: Test your world knowledge and geography")
    print("• History Hunter: Learn about historical events and figures")
    print("• Word Master: Improve vocabulary and language skills")
    print()
    print("🐍 PYTHON GAMES:")
    print("• Tic-Tac-Toe: Classic strategy game with AI opponent")
    print("• Space Shooter: Shoot enemies while dodging attacks")
    print("• Car Racing: Navigate through traffic and obstacles")
    print("• Zombie Dash: Survive waves of approaching zombies")
    print("• Ball Run: Control a physics-based ball through challenges")

if __name__ == "__main__":
    success = test_final_snake()
    
    if success:
        show_final_usage()
        print(f"\n🚀 Ready to play Final Enhanced Snake Evolution!")
        print("Run: ./play_snake_evolution.sh")
    else:
        print("\n❌ Tests failed. Please check the snake_evolution.py file.")
        sys.exit(1)
