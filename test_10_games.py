#!/usr/bin/env python3
"""
Test script for EduVerse 10-Game Arcade
Tests only the 10 games we created
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_educational_games():
    """Test the 5 educational games"""
    try:
        print("🎓 Testing Educational Games...")
        
        from games.math_wizard import MathWizardGame
        print("✅ Math Wizard imported successfully")
        
        from games.word_master import WordMasterGame
        print("✅ Word Master imported successfully")
        
        from games.science_lab import ScienceLabGame
        print("✅ Science Lab imported successfully")
        
        from games.geography_quest import GeographyQuestGame
        print("✅ Geography Quest imported successfully")
        
        from games.history_hunter import HistoryHunterGame
        print("✅ History Hunter imported successfully")
        
        print("\n🎉 All 5 educational games imported successfully!")
        return True
        
    except ImportError as e:
        print(f"❌ Educational games import error: {e}")
        return False

def test_fun_games():
    """Test the 5 fun games"""
    try:
        print("\n🎮 Testing Fun Games...")
        
        from games.target_practice import TargetPracticeGame
        print("✅ Target Practice imported successfully")
        
        from games.puzzle_master import PuzzleMasterGame
        print("✅ Puzzle Master imported successfully")
        
        from games.lucky_numbers import LuckyNumbersGame
        print("✅ Lucky Numbers imported successfully")
        
        from games.memory_game import MemoryGameChallenge
        print("✅ Memory Game imported successfully")
        
        from games.quick_quiz import QuickQuizGame
        print("✅ Quick Quiz imported successfully")
        
        print("\n🎉 All 5 fun games imported successfully!")
        return True
        
    except ImportError as e:
        print(f"❌ Fun games import error: {e}")
        return False

def test_game_creation():
    """Test if all 10 games can be created"""
    try:
        print("\n🎮 Testing Game Creation...")
        
        # Educational games
        from games.math_wizard import MathWizardGame
        from games.word_master import WordMasterGame
        from games.science_lab import ScienceLabGame
        from games.geography_quest import GeographyQuestGame
        from games.history_hunter import HistoryHunterGame
        
        # Fun games
        from games.target_practice import TargetPracticeGame
        from games.puzzle_master import PuzzleMasterGame
        from games.lucky_numbers import LuckyNumbersGame
        from games.memory_game import MemoryGameChallenge
        from games.quick_quiz import QuickQuizGame
        
        # Create instances
        games = [
            ("Math Wizard", MathWizardGame()),
            ("Word Master", WordMasterGame()),
            ("Science Lab", ScienceLabGame()),
            ("Geography Quest", GeographyQuestGame()),
            ("History Hunter", HistoryHunterGame()),
            ("Target Practice", TargetPracticeGame()),
            ("Puzzle Master", PuzzleMasterGame()),
            ("Lucky Numbers", LuckyNumbersGame()),
            ("Memory Game", MemoryGameChallenge()),
            ("Quick Quiz", QuickQuizGame())
        ]
        
        for name, game in games:
            print(f"✅ {name} created successfully")
        
        print(f"\n🎉 All 10 games created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Game creation error: {e}")
        return False

def test_main_arcade():
    """Test the main arcade"""
    try:
        print("\n🎓 Testing Main Arcade...")
        
        from eduverse_arcade import EduVerseArcade
        arcade = EduVerseArcade()
        print("✅ Main arcade created successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Main arcade error: {e}")
        return False

def main():
    """Run all tests"""
    print("🎓 EDUVERSE 10-GAME ARCADE - SYSTEM TEST")
    print("="*50)
    
    success = True
    
    # Test educational games
    if not test_educational_games():
        success = False
    
    # Test fun games
    if not test_fun_games():
        success = False
    
    # Test game creation
    if not test_game_creation():
        success = False
    
    # Test main arcade
    if not test_main_arcade():
        success = False
    
    print("\n" + "="*50)
    if success:
        print("🎉 ALL TESTS PASSED!")
        print("🚀 EduVerse 10-Game Arcade is ready to run!")
        print("\n📋 GAME LIST:")
        print("📚 EDUCATIONAL GAMES:")
        print("  1. 🧮 Math Wizard")
        print("  2. 🔤 Word Master")
        print("  3. 🧪 Science Lab")
        print("  4. 🌍 Geography Quest")
        print("  5. 📚 History Hunter")
        print("\n🎮 FUN GAMES:")
        print("  6. 🎯 Target Practice")
        print("  7. 🧩 Puzzle Master")
        print("  8. 🎲 Lucky Numbers")
        print("  9. 🌟 Memory Game")
        print(" 10. ⚡ Quick Quiz")
        print("\nTo start the arcade, run:")
        print("python3 eduverse_arcade.py")
    else:
        print("❌ SOME TESTS FAILED!")
        print("🔧 Please check the error messages above.")
    
    print("="*50)

if __name__ == "__main__":
    main()
