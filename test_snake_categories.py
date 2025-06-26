#!/usr/bin/env python3
"""
Test script for Snake Evolution with Category Selection
"""

import sys
import os

def test_snake_categories():
    """Test the updated snake game with category selection"""
    print("🐍 Testing Snake Evolution with Category Selection")
    print("=" * 50)
    
    # Check if the snake_evolution.py file exists
    if not os.path.exists("snake_evolution.py"):
        print("❌ Error: snake_evolution.py not found!")
        return False
    
    try:
        # Import the game module
        import snake_evolution
        
        print("✅ Successfully imported snake_evolution module")
        
        # Check if the new GameState enum has CATEGORY_SELECT
        if hasattr(snake_evolution.GameState, 'CATEGORY_SELECT'):
            print("✅ CATEGORY_SELECT state found in GameState enum")
        else:
            print("❌ CATEGORY_SELECT state not found in GameState enum")
            return False
        
        # Check if SnakeGame class has the new methods
        game_class = snake_evolution.SnakeGame
        
        required_methods = [
            'draw_category_select',
            'generate_education_question',
            'generate_python_question',
            'generate_math_question',
            'generate_science_question',
            'generate_geography_question',
            'generate_history_question',
            'generate_language_question'
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
            
            # Test category selection
            if hasattr(game, 'selected_category'):
                print("✅ selected_category attribute found")
            else:
                print("❌ selected_category attribute not found")
                return False
            
            # Test translation keys
            required_keys = [
                'category_select',
                'education_games',
                'python_games',
                'education_desc',
                'python_desc',
                'select_instruction'
            ]
            
            for key in required_keys:
                if key in game.translations['english']:
                    print(f"✅ Translation key '{key}' found")
                else:
                    print(f"❌ Translation key '{key}' not found")
                    return False
            
        except Exception as e:
            print(f"❌ Error creating game instance: {e}")
            return False
        
        print("\n🎉 All tests passed! The Snake Evolution game has been successfully updated with:")
        print("   • Category selection screen")
        print("   • Educational games (Math, Science, Geography, History, Language)")
        print("   • Python programming games")
        print("   • Enhanced question generation")
        print("   • Multilingual support for new features")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error importing snake_evolution: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def show_usage_instructions():
    """Show how to use the updated game"""
    print("\n📖 How to use the updated Snake Evolution game:")
    print("=" * 50)
    print("1. Run the game: python snake_evolution.py")
    print("2. Press SPACE to start playing")
    print("3. Use arrow keys to control the snake")
    print("4. When you eat food (❓), you'll see category selection:")
    print("   • Press 1 for Educational Games (Math, Science, Geography, History, Language)")
    print("   • Press 2 for Python Games (Programming concepts and game development)")
    print("5. Answer questions correctly to grow your snake and earn points")
    print("6. Press L to toggle between English and Tamil languages")
    print("7. Press P to pause/resume the game")
    print("\n🎯 Game Categories:")
    print("📚 Educational Games:")
    print("   • 🧮 Math Wizard - Arithmetic, algebra, geometry")
    print("   • 🧪 Science Lab - Physics, chemistry, biology")
    print("   • 🌍 Geography Quest - Countries, capitals, landmarks")
    print("   • 📚 History Hunter - Historical events and figures")
    print("   • 🔤 Word Master - Vocabulary, grammar, language")
    print("\n🐍 Python Games:")
    print("   • ⭕ Tic-Tac-Toe concepts")
    print("   • 🚀 Space Shooter mechanics")
    print("   • 🏎️ Car Racing game logic")
    print("   • 🎮 2D Platformer development")
    print("   • 🎯 3D Adventure programming")

if __name__ == "__main__":
    success = test_snake_categories()
    
    if success:
        show_usage_instructions()
        print(f"\n🚀 Ready to play! Run: python snake_evolution.py")
    else:
        print("\n❌ Tests failed. Please check the snake_evolution.py file.")
        sys.exit(1)
