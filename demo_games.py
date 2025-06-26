#!/usr/bin/env python3
"""
Demo script to showcase all 10 EduVerse CLI games
"""

import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                    🎓 EduVerse CLI Demo 🎓                   ║
║              10 Realms of Genius - All Games Ready!          ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def demo_all_games():
    """Demonstrate all 10 games"""
    
    clear_screen()
    print_banner()
    
    games = [
        ("🧮 Math Wizard", "Master mathematics from basic arithmetic to advanced algebra"),
        ("🔤 Word Master", "Expand vocabulary and language skills in English and Tamil"),
        ("🧪 Science Lab", "Explore physics, chemistry, and biology concepts"),
        ("🌍 Geography Quest", "Journey around the world learning countries and landmarks"),
        ("📚 History Hunter", "Travel through time learning about historical events"),
        ("🎨 Art Creator", "Discover famous artists, colors, and creative principles"),
        ("🎵 Music Maestro", "Learn music theory, instruments, and famous composers"),
        ("💻 Code Ninja", "Master programming concepts and computer science"),
        ("🧩 Logic Puzzle", "Challenge your brain with patterns and logical reasoning"),
        ("🌟 Memory Palace", "Train your memory with sequences and recall challenges")
    ]
    
    print("\n🎮 ALL 10 GAMES NOW AVAILABLE!")
    print("=" * 60)
    
    for i, (game_name, description) in enumerate(games, 1):
        print(f"\n{i:2d}. {game_name}")
        print(f"    {description}")
        time.sleep(0.5)
    
    print(f"\n🏆 FEATURES:")
    print(f"   ✅ Progressive difficulty (10 levels each)")
    print(f"   ✅ Multilingual support (English/Tamil)")
    print(f"   ✅ Achievement system with unlockable badges")
    print(f"   ✅ Real-time scoring with streak bonuses")
    print(f"   ✅ Comprehensive progress tracking")
    print(f"   ✅ Hint system and skip options")
    print(f"   ✅ Statistics and leaderboards")
    
    print(f"\n🚀 HOW TO START:")
    print(f"   python3 eduverse_cli.py")
    print(f"   python3 eduverse_cli.py --lang en")
    print(f"   python3 eduverse_cli.py --lang ta")
    
    print(f"\n🎯 EDUCATIONAL BENEFITS:")
    print(f"   📚 STEM Learning: Math, Science, Programming")
    print(f"   🌍 Cultural Knowledge: Geography, History, Arts")
    print(f"   🧠 Cognitive Skills: Memory, Logic, Critical Thinking")
    print(f"   🗣️ Language Development: Vocabulary, Multilingual")
    
    print(f"\n🌟 Ready to explore all 10 realms of genius?")
    print(f"   Start your educational adventure now!")

if __name__ == "__main__":
    demo_all_games()
    
    print(f"\n" + "=" * 60)
    input("Press Enter to continue...")
