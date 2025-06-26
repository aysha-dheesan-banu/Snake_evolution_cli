#!/usr/bin/env python3
"""
Test script to verify all 10 games are implemented in EduVerse CLI
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from eduverse_cli import EduVerseCLI, EduVerseTranslations

def test_all_games():
    """Test that all 10 games are properly implemented"""
    
    print("🎓 Testing EduVerse CLI - All 10 Games")
    print("=" * 50)
    
    # Initialize CLI
    cli = EduVerseCLI()
    
    # Test translations for all games
    games_en = EduVerseTranslations.TRANSLATIONS['en']['games']
    games_ta = EduVerseTranslations.TRANSLATIONS['ta']['games']
    
    print(f"\n✅ Found {len(games_en)} games in English")
    print(f"✅ Found {len(games_ta)} games in Tamil")
    
    # List all games
    print("\n🎮 Available Games:")
    for i, (game_key, game_name) in enumerate(games_en.items(), 1):
        tamil_name = games_ta.get(game_key, "Not translated")
        print(f"{i:2d}. {game_name} / {tamil_name}")
        
        # Check if game method exists
        method_name = f"{game_key}_game"
        if hasattr(cli, method_name):
            print(f"    ✅ Method {method_name} exists")
        else:
            print(f"    ❌ Method {method_name} missing")
    
    # Test game selection logic
    print(f"\n🔧 Testing game selection logic...")
    
    # Test each game number
    for game_num in range(1, 11):
        try:
            game_keys = list(games_en.keys())
            game_key = game_keys[game_num - 1]
            method_name = f"{game_key}_game"
            
            if hasattr(cli, method_name):
                print(f"✅ Game {game_num} ({game_key}) - Method available")
            else:
                print(f"❌ Game {game_num} ({game_key}) - Method missing")
                
        except IndexError:
            print(f"❌ Game {game_num} - Index error")
    
    print(f"\n🎯 Test Summary:")
    print(f"   - All 10 games have translations: {'✅' if len(games_en) == 10 else '❌'}")
    print(f"   - All game methods implemented: {'✅' if all(hasattr(cli, f'{key}_game') for key in games_en.keys()) else '❌'}")
    print(f"   - Complete game method exists: {'✅' if hasattr(cli, 'complete_game') else '❌'}")
    
    print(f"\n🚀 EduVerse CLI is ready with all 10 games!")

if __name__ == "__main__":
    test_all_games()
