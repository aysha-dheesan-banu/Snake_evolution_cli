#!/usr/bin/env python3
"""
Demo script to showcase Snake Evolution with Category Selection
"""

import time
import sys

def print_banner():
    """Print a nice banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                    🐍 SNAKE EVOLUTION 🐍                     ║
║                  Category Selection Update                   ║
║              Part of EduVerse: 10 Realms of Genius          ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def demonstrate_features():
    """Demonstrate the new features"""
    print("🎯 NEW FEATURES DEMONSTRATION")
    print("=" * 60)
    
    features = [
        ("🎓 Educational Games Category", [
            "🧮 Math Wizard - Arithmetic, algebra, geometry",
            "🧪 Science Lab - Physics, chemistry, biology", 
            "🌍 Geography Quest - Countries, capitals, landmarks",
            "📚 History Hunter - Historical events and figures",
            "🔤 Word Master - Vocabulary, grammar, language"
        ]),
        ("🐍 Python Games Category", [
            "⭕ Tic-Tac-Toe - Game logic and algorithms",
            "🚀 Space Shooter - Collision detection and physics",
            "🏎️ Car Racing - Movement controls and mechanics",
            "🎮 2D Platformer - Jump mechanics and collision",
            "🎯 3D Adventure - 3D coordinates and rendering"
        ])
    ]
    
    for category, games in features:
        print(f"\n{category}")
        print("-" * 40)
        for game in games:
            print(f"  • {game}")
            time.sleep(0.3)
    
    print("\n🌟 ENHANCED GAMEPLAY FLOW")
    print("=" * 60)
    
    steps = [
        "1. 🎮 Start the game with SPACE",
        "2. 🕹️  Control snake with arrow keys", 
        "3. 🍎 Navigate to the pulsing question mark food",
        "4. 📚 Choose category: Press 1 (Education) or 2 (Python)",
        "5. 🤔 Answer the question by pressing 1-4",
        "6. 🏆 Correct answers grow snake and increase score",
        "7. 📈 Level up every 5 correct answers"
    ]
    
    for step in steps:
        print(f"   {step}")
        time.sleep(0.5)

def show_sample_questions():
    """Show sample questions from each category"""
    print("\n🎯 SAMPLE QUESTIONS")
    print("=" * 60)
    
    samples = {
        "🎓 Educational Games": [
            ("🧮 Math", "What is 15 × 8?", ["120", "125", "130", "115"]),
            ("🧪 Science", "What is H2O?", ["Water", "Hydrogen", "Oxygen", "Salt"]),
            ("🌍 Geography", "Capital of France?", ["Paris", "London", "Berlin", "Madrid"]),
            ("📚 History", "First US President?", ["Washington", "Jefferson", "Lincoln", "Adams"]),
            ("🔤 Language", "Opposite of 'hot'?", ["Cold", "Warm", "Cool", "Mild"])
        ],
        "🐍 Python Games": [
            ("⭕ Tic-Tac-Toe", "What checks win condition?", ["Algorithm", "Variable", "Loop", "Function"]),
            ("🚀 Space Shooter", "What detects collisions?", ["Collision detection", "Movement", "Rendering", "Input"]),
            ("🏎️ Car Racing", "What controls speed?", ["Velocity", "Position", "Color", "Size"]),
            ("🎮 2D Platformer", "What makes character jump?", ["Physics", "Graphics", "Sound", "Menu"]),
            ("🎯 3D Adventure", "What represents position?", ["Coordinates", "Texture", "Model", "Camera"])
        ]
    }
    
    for category, questions in samples.items():
        print(f"\n{category}")
        print("-" * 50)
        for subject, question, options in questions:
            print(f"  {subject}: {question}")
            for i, option in enumerate(options, 1):
                print(f"    {i}. {option}")
            print()
            time.sleep(0.8)

def show_multilingual_support():
    """Show multilingual support"""
    print("\n🌐 MULTILINGUAL SUPPORT")
    print("=" * 60)
    
    translations = [
        ("English", "Choose Game Category", "Educational Games", "Python Games"),
        ("Tamil", "விளையாட்டு வகையை தேர்ந்தெடுக்கவும்", "கல்வி விளையாட்டுகள்", "பைதான் விளையாட்டுகள்")
    ]
    
    for lang, category_text, edu_text, python_text in translations:
        print(f"\n🗣️  {lang}:")
        print(f"   Category Selection: {category_text}")
        print(f"   Educational: {edu_text}")
        print(f"   Python Games: {python_text}")
        time.sleep(0.5)

def show_scoring_system():
    """Show the scoring system"""
    print("\n🏆 SCORING SYSTEM")
    print("=" * 60)
    
    scoring = [
        "📊 Base Points: 10 points per correct answer",
        "🔥 Streak Bonus: +2 points per consecutive correct (max +20)",
        "⚡ Speed Bonus: Faster answers get bonus points",
        "📈 Level Up: Every 5 correct answers increases difficulty",
        "🎯 Accuracy Tracking: Percentage of correct answers",
        "🏅 Best Streak: Track longest streak of correct answers"
    ]
    
    for item in scoring:
        print(f"   {item}")
        time.sleep(0.4)

def show_controls():
    """Show game controls"""
    print("\n🎮 GAME CONTROLS")
    print("=" * 60)
    
    controls = [
        "SPACE - Start the game",
        "Arrow Keys - Control snake movement", 
        "1 - Select Educational Games category",
        "2 - Select Python Games category",
        "1-4 - Select answer options",
        "L - Toggle language (English/Tamil)",
        "P - Pause/Resume game",
        "R - Restart after game over",
        "Q - Quit game"
    ]
    
    for control in controls:
        print(f"   🔹 {control}")
        time.sleep(0.3)

def main():
    """Main demo function"""
    print_banner()
    
    try:
        demonstrate_features()
        show_sample_questions()
        show_multilingual_support()
        show_scoring_system()
        show_controls()
        
        print("\n" + "=" * 60)
        print("🚀 READY TO PLAY!")
        print("=" * 60)
        print("To start the game:")
        print("1. Activate environment: source snake_env/bin/activate")
        print("2. Run game: python snake_evolution.py")
        print("3. Press SPACE to start playing!")
        print("\n🎓 Part of EduVerse: The 10 Realms of Genius")
        print("   Where Education Meets Adventure! 🌟")
        
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Thanks for watching!")
        sys.exit(0)

if __name__ == "__main__":
    main()
