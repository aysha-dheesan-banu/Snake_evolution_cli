#!/usr/bin/env python3
"""
Demo script for Snake Evolution game
Tests core functionality without requiring a display
"""

import sys
import os

# Add current directory to path to import snake_evolution
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_game_components():
    """Test the core game components"""
    print("🐍 Testing Snake Evolution Components...")
    print("="*50)
    
    try:
        # Import the game module
        import snake_evolution
        print("✅ Game module imported successfully")
        
        # Test Question class
        from snake_evolution import Question
        test_question = Question(
            question="2 + 3 = ?",
            answer=5,
            options=[3, 5, 7, 9],
            difficulty=1,
            subject="math"
        )
        print(f"✅ Question class working: {test_question.question}")
        
        # Test Direction enum
        from snake_evolution import Direction
        print(f"✅ Direction enum working: {Direction.UP.value}")
        
        # Test GameState enum
        from snake_evolution import GameState
        print(f"✅ GameState enum working: {GameState.MENU}")
        
        # Test SnakeGame class initialization (without pygame display)
        print("🧪 Testing SnakeGame class...")
        
        # Mock pygame for testing
        class MockPygame:
            def init(self): pass
            def quit(self): pass
            
            class display:
                @staticmethod
                def set_mode(size): return MockSurface()
                @staticmethod
                def set_caption(title): pass
                @staticmethod
                def flip(): pass
            
            class time:
                @staticmethod
                def Clock(): return MockClock()
                @staticmethod
                def get_ticks(): return 1000
            
            class font:
                @staticmethod
                def Font(name, size): return MockFont()
            
            class event:
                @staticmethod
                def get(): return []
            
            QUIT = 1
            KEYDOWN = 2
            K_SPACE = 32
        
        class MockSurface:
            def fill(self, color): pass
            def blit(self, surface, pos): pass
            def get_rect(self): return MockRect()
            def set_alpha(self, alpha): pass
        
        class MockRect:
            def __init__(self):
                self.center = (0, 0)
        
        class MockFont:
            def render(self, text, antialias, color):
                return MockSurface()
        
        class MockClock:
            def tick(self, fps): pass
        
        # Temporarily replace pygame for testing
        original_pygame = sys.modules.get('pygame')
        sys.modules['pygame'] = MockPygame()
        
        try:
            # Test game initialization
            game = snake_evolution.SnakeGame()
            print("✅ SnakeGame class initialized successfully")
            
            # Test question generation
            question = game.generate_question()
            print(f"✅ Question generation working: {question.question}")
            print(f"   Answer: {question.answer}")
            print(f"   Options: {question.options}")
            print(f"   Difficulty: {question.difficulty}")
            
            # Test translations
            english_text = game.get_text("title")
            print(f"✅ English translation: {english_text}")
            
            game.language = "tamil"
            tamil_text = game.get_text("title")
            print(f"✅ Tamil translation: {tamil_text}")
            
            # Test multiple question generation
            print("\n📚 Sample Questions by Difficulty:")
            for level in [1, 3, 5, 7, 10]:
                game.level = level
                q = game.generate_question()
                print(f"   Level {level}: {q.question} (Answer: {q.answer})")
            
        finally:
            # Restore original pygame
            if original_pygame:
                sys.modules['pygame'] = original_pygame
            elif 'pygame' in sys.modules:
                del sys.modules['pygame']
        
        print("\n✅ All core components tested successfully!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

def show_game_info():
    """Display game information"""
    print("\n🎮 Snake Evolution - Game Information")
    print("="*50)
    print("📖 Description:")
    print("   Classic Snake game enhanced with educational math challenges")
    print("   Perfect for students aged 10-16 years")
    
    print("\n🎯 Educational Features:")
    print("   • Progressive difficulty (10 levels)")
    print("   • Math topics: Arithmetic, Multiplication, Squares, Square Roots")
    print("   • Multilingual support (English & Tamil)")
    print("   • Real-time performance tracking")
    print("   • Streak bonuses for consecutive correct answers")
    
    print("\n🎮 Game Features:")
    print("   • Classic Snake mechanics with modern twist")
    print("   • Retro arcade-style graphics")
    print("   • Pause/resume functionality")
    print("   • Achievement system with statistics")
    
    print("\n🛠️ Technical Details:")
    print("   • Built with Python and Pygame")
    print("   • Cross-platform compatibility")
    print("   • Minimal system requirements")
    print("   • Easy to customize and extend")

def main():
    """Main demo function"""
    print("🐍 Snake Evolution - Demo & Test")
    print("Part of EduVerse: The 10 Realms of Genius")
    print("="*60)
    
    # Test core components
    if test_game_components():
        print("\n🎉 All tests passed! The game is ready to play.")
    else:
        print("\n❌ Some tests failed. Please check the installation.")
        return
    
    # Show game information
    show_game_info()
    
    print("\n🚀 To play the full game:")
    print("   1. Run: python setup_snake_venv.py")
    print("   2. Follow the setup instructions")
    print("   3. Launch the game and enjoy learning!")
    
    print("\n📚 Educational Value:")
    print("   Snake Evolution makes math practice fun and engaging")
    print("   Students learn while playing, improving retention")
    print("   Progressive difficulty adapts to skill level")
    
    print("\n🌟 Perfect for:")
    print("   • Individual study sessions")
    print("   • Classroom activities")
    print("   • Homework supplements")
    print("   • Family learning time")

if __name__ == "__main__":
    main()
