#!/usr/bin/env python3
"""
Demo script for EduVerse CLI
Shows the game features and interface
"""

import os
import time
from eduverse_cli import Colors, EduVerseTranslations

def print_demo_banner():
    """Print demo banner"""
    banner = f"""
{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                🎓 EduVerse CLI Demo 🎓                       ║
║              10 Realms of Genius Terminal Edition            ║
║                                                              ║
║                    DEMO SHOWCASE                             ║
╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}
    """
    print(banner)

def demo_features():
    """Demonstrate key features"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_demo_banner()
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}🌟 KEY FEATURES DEMO 🌟{Colors.ENDC}")
    
    features = [
        ("🎮 10 Interactive Games", "Math, Words, Science, Geography, History, Art, Music, Code, Logic, Memory"),
        ("🌍 Multilingual Support", "English 🇬🇧 and Tamil 🇮🇳 with full localization"),
        ("📊 Progress Tracking", "Levels, scores, achievements, and detailed statistics"),
        ("🏆 Achievement System", "Unlock badges for streaks, perfect scores, and level completion"),
        ("⚡ Real-time Scoring", "Base points + speed bonus + streak multipliers"),
        ("💡 Hint System", "Get help when stuck (with small point penalty)"),
        ("🎯 Adaptive Difficulty", "10 levels per game with progressive challenges"),
        ("💾 Data Persistence", "Your progress is automatically saved"),
        ("🎨 Colorful Interface", "Beautiful terminal colors and emojis"),
        ("⌨️ Simple Controls", "Easy keyboard navigation and input")
    ]
    
    for i, (feature, description) in enumerate(features, 1):
        print(f"\n{Colors.OKBLUE}{i:2d}. {feature}{Colors.ENDC}")
        print(f"    {Colors.OKCYAN}{description}{Colors.ENDC}")
        time.sleep(0.5)
    
    print(f"\n{Colors.WARNING}Press Enter to see game examples...{Colors.ENDC}")
    input()

def demo_math_example():
    """Show Math Wizard example"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_demo_banner()
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}🧮 MATH WIZARD DEMO 🧮{Colors.ENDC}")
    
    examples = [
        ("Level 1-2", "Basic Arithmetic", "15 + 23 = ?", "Simple addition and subtraction"),
        ("Level 3-4", "Multiplication/Division", "7 × 8 = ?", "Times tables and division"),
        ("Level 5-6", "Mixed Operations", "156 - 89 = ?", "Larger numbers, mixed operations"),
        ("Level 7-8", "Advanced Math", "12² = ?", "Squares, percentages, fractions"),
        ("Level 9-10", "Expert Level", "25% of 240 = ?", "Complex calculations")
    ]
    
    print(f"{Colors.OKGREEN}Progressive difficulty across 10 levels:{Colors.ENDC}\n")
    
    for level, name, example, description in examples:
        print(f"{Colors.OKBLUE}{level}: {name}{Colors.ENDC}")
        print(f"   Example: {Colors.OKCYAN}{example}{Colors.ENDC}")
        print(f"   {Colors.WARNING}{description}{Colors.ENDC}\n")
        time.sleep(0.8)
    
    print(f"{Colors.HEADER}Scoring System:{Colors.ENDC}")
    print(f"{Colors.OKGREEN}• Base Score: 100 points per correct answer{Colors.ENDC}")
    print(f"{Colors.OKGREEN}• Speed Bonus: +50 points for quick answers{Colors.ENDC}")
    print(f"{Colors.OKGREEN}• Streak Bonus: +10 points per consecutive correct{Colors.ENDC}")
    print(f"{Colors.FAIL}• Penalties: -10 for hints, -25 for skips{Colors.ENDC}")
    
    print(f"\n{Colors.WARNING}Press Enter to see Word Master demo...{Colors.ENDC}")
    input()

def demo_word_example():
    """Show Word Master example"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_demo_banner()
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}🔤 WORD MASTER DEMO 🔤{Colors.ENDC}")
    
    print(f"{Colors.OKGREEN}Multilingual vocabulary building:{Colors.ENDC}\n")
    
    # English example
    print(f"{Colors.OKBLUE}English Example (Level 2):{Colors.ENDC}")
    print(f"Definition: {Colors.OKCYAN}A large mammal with a trunk{Colors.ENDC}")
    print(f"Options:")
    print(f"  1. tiger")
    print(f"  2. {Colors.OKGREEN}elephant{Colors.ENDC} ✓")
    print(f"  3. lion")
    print(f"  4. bear")
    
    time.sleep(1)
    
    # Tamil example
    print(f"\n{Colors.OKBLUE}Tamil Example (Level 2):{Colors.ENDC}")
    print(f"Definition: {Colors.OKCYAN}துதிக்கையுடன் கூடிய பெரிய விலங்கு{Colors.ENDC}")
    print(f"Options:")
    print(f"  1. புலி")
    print(f"  2. {Colors.OKGREEN}யானை{Colors.ENDC} ✓")
    print(f"  3. சிங்கம்")
    print(f"  4. கரடி")
    
    time.sleep(1)
    
    print(f"\n{Colors.HEADER}Level Progression:{Colors.ENDC}")
    levels = [
        ("Level 1-2", "Basic vocabulary (cat, book, sun)"),
        ("Level 3-4", "Intermediate words (elephant, computer)"),
        ("Level 5+", "Advanced vocabulary (magnificent, mysterious)")
    ]
    
    for level, description in levels:
        print(f"{Colors.OKBLUE}{level}: {Colors.OKCYAN}{description}{Colors.ENDC}")
        time.sleep(0.5)
    
    print(f"\n{Colors.WARNING}Press Enter to see achievements demo...{Colors.ENDC}")
    input()

def demo_achievements():
    """Show achievements system"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_demo_banner()
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}🏆 ACHIEVEMENT SYSTEM DEMO 🏆{Colors.ENDC}")
    
    achievements = [
        ("🎯 Level Achievements", "Math Wizard Level 5", "Complete game levels"),
        ("🔥 Streak Masters", "Math Streak Master", "5+ consecutive correct answers"),
        ("⭐ Perfect Scores", "Word Perfect Score", "100% accuracy in a game"),
        ("⚡ Speed Demons", "Lightning Fast", "Quick completion bonuses"),
        ("🎮 Game Masters", "All Games Played", "Try every game type"),
        ("📈 Progress Milestones", "100 Questions Answered", "Dedication rewards"),
        ("🌟 Special Badges", "Multilingual Master", "Play in both languages"),
        ("🏅 Score Achievements", "High Scorer", "Reach score milestones")
    ]
    
    print(f"{Colors.OKGREEN}Unlock achievements as you play:{Colors.ENDC}\n")
    
    for category, example, description in achievements:
        print(f"{Colors.OKBLUE}{category}{Colors.ENDC}")
        print(f"   Example: {Colors.OKCYAN}{example}{Colors.ENDC}")
        print(f"   {Colors.WARNING}{description}{Colors.ENDC}\n")
        time.sleep(0.7)
    
    print(f"\n{Colors.WARNING}Press Enter to see statistics demo...{Colors.ENDC}")
    input()

def demo_statistics():
    """Show statistics tracking"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_demo_banner()
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}📊 STATISTICS TRACKING DEMO 📊{Colors.ENDC}")
    
    print(f"{Colors.OKGREEN}Comprehensive progress tracking:{Colors.ENDC}\n")
    
    # Sample statistics
    stats = [
        ("Player Name", "Young Genius"),
        ("Language", "English 🇬🇧"),
        ("Total Score", "2,450 points"),
        ("Games Played", "15 sessions"),
        ("Questions Answered", "150 questions"),
        ("Correct Answers", "127 correct"),
        ("Accuracy", "84.7%"),
        ("", ""),
        ("🎮 GAME PROGRESS", ""),
        ("🧮 Math Wizard", "Level 4"),
        ("🔤 Word Master", "Level 3"),
        ("🧪 Science Lab", "Level 1"),
        ("🌍 Geography Quest", "Level 1")
    ]
    
    for label, value in stats:
        if label == "":
            print()
        elif label.startswith("🎮"):
            print(f"{Colors.HEADER}{label}:{Colors.ENDC}")
        elif label.startswith(("🧮", "🔤", "🧪", "🌍")):
            print(f"{Colors.OKBLUE}{label}: {Colors.OKCYAN}{value}{Colors.ENDC}")
        else:
            print(f"{Colors.OKGREEN}{label}: {Colors.OKCYAN}{value}{Colors.ENDC}")
        time.sleep(0.3)
    
    print(f"\n{Colors.WARNING}Press Enter to finish demo...{Colors.ENDC}")
    input()

def demo_conclusion():
    """Show conclusion"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_demo_banner()
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}🎉 READY TO START LEARNING? 🎉{Colors.ENDC}")
    
    print(f"\n{Colors.OKGREEN}To start playing EduVerse CLI:{Colors.ENDC}")
    print(f"{Colors.OKCYAN}   python3 eduverse_cli.py{Colors.ENDC}")
    print(f"{Colors.OKCYAN}   or{Colors.ENDC}")
    print(f"{Colors.OKCYAN}   ./eduverse{Colors.ENDC}")
    
    print(f"\n{Colors.OKGREEN}Command line options:{Colors.ENDC}")
    print(f"{Colors.OKCYAN}   --lang en    {Colors.WARNING}# Start in English{Colors.ENDC}")
    print(f"{Colors.OKCYAN}   --lang ta    {Colors.WARNING}# Start in Tamil{Colors.ENDC}")
    print(f"{Colors.OKCYAN}   --version    {Colors.WARNING}# Show version info{Colors.ENDC}")
    
    print(f"\n{Colors.HEADER}🎯 Perfect for ages 10-25!{Colors.ENDC}")
    print(f"{Colors.OKGREEN}✨ Learn while having fun{Colors.ENDC}")
    print(f"{Colors.OKGREEN}🌍 Practice in multiple languages{Colors.ENDC}")
    print(f"{Colors.OKGREEN}🏆 Unlock achievements{Colors.ENDC}")
    print(f"{Colors.OKGREEN}📈 Track your progress{Colors.ENDC}")
    
    print(f"\n{Colors.BOLD}{Colors.HEADER}Happy Learning! 🎓✨{Colors.ENDC}")

def run_demo():
    """Run the complete demo"""
    try:
        demo_features()
        demo_math_example()
        demo_word_example()
        demo_achievements()
        demo_statistics()
        demo_conclusion()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.OKGREEN}Demo ended. Thanks for watching!{Colors.ENDC}")

if __name__ == "__main__":
    run_demo()
