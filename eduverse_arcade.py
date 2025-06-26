#!/usr/bin/env python3
"""
🎓 EduVerse Arcade: The 5 Educational Realms
A fun educational game platform for kids and teens
"""

import os
import sys
import json
import random
from datetime import datetime

class EduVerseArcade:
    def __init__(self):
        self.player_name = ""
        self.current_score = 0
        self.games_completed = 0
        self.player_data = self.load_player_data()
        
    def load_player_data(self):
        """Load player progress from file"""
        try:
            with open('player_data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"total_score": 0, "games_played": [], "achievements": []}
    
    def save_player_data(self):
        """Save player progress to file"""
        with open('player_data.json', 'w') as f:
            json.dump(self.player_data, f, indent=2)
    
    def display_banner(self):
        """Display the EduVerse banner"""
        print("\n" + "="*70)
        print("🎓 WELCOME TO EDUVERSE ARCADE 🎓")
        print("The Ultimate 10-Game Educational & Fun Platform")
        print("="*70)
        print("📚 EDUCATIONAL GAMES:")
        print("🧮 Math Wizard  🔤 Word Master  🧪 Science Lab  🌍 Geography  📚 History")
        print("\n🎮 FUN GAMES:")
        print("🎯 Target Practice  🧩 Puzzle Master  🎲 Lucky Numbers  🌟 Memory Game  ⚡ Quick Quiz")
        print("="*70)
    
    def main_menu(self):
        """Display main menu and handle selection"""
        while True:
            self.display_banner()
            if self.player_name:
                print(f"\n👋 Welcome back, {self.player_name}!")
                print(f"🏆 Total Score: {self.player_data.get('total_score', 0)}")
            
            print("\n🎮 EDUCATIONAL GAMES:")
            print("1. 🧮 Math Wizard - Master Numbers & Equations")
            print("2. 🔤 Word Master - Vocabulary & Language Skills") 
            print("3. 🧪 Science Lab - Explore Scientific Concepts")
            print("4. 🌍 Geography Quest - Discover the World")
            print("5. 📚 History Hunter - Journey Through Time")
            print("\n🎯 FUN GAMES:")
            print("6. 🎯 Target Practice - Test Your Aim & Reflexes")
            print("7. 🧩 Puzzle Master - Brain Teasers & Logic")
            print("8. 🎲 Lucky Numbers - Chance & Strategy")
            print("9. 🌟 Memory Game - Remember & Match")
            print("10. ⚡ Quick Quiz - Fast Facts Challenge")
            print("\n📊 Other Options:")
            print("11. 📈 View Progress & Achievements")
            print("12. ⚙️  Settings")
            print("13. 🚪 Exit")
            
            choice = input("\n🎯 Choose your adventure (1-13): ").strip()
            
            if choice == '1':
                self.play_math_wizard()
            elif choice == '2':
                self.play_word_master()
            elif choice == '3':
                self.play_science_lab()
            elif choice == '4':
                self.play_geography_quest()
            elif choice == '5':
                self.play_history_hunter()
            elif choice == '6':
                self.play_target_practice()
            elif choice == '7':
                self.play_puzzle_master()
            elif choice == '8':
                self.play_lucky_numbers()
            elif choice == '9':
                self.play_memory_game()
            elif choice == '10':
                self.play_quick_quiz()
            elif choice == '11':
                self.show_progress()
            elif choice == '12':
                self.settings_menu()
            elif choice == '13':
                self.exit_game()
                break
            else:
                print("❌ Invalid choice! Please select 1-13.")
                input("Press Enter to continue...")
    
    def get_player_name(self):
        """Get player name for personalization"""
        if not self.player_name:
            print("\n🎯 Let's get started!")
            self.player_name = input("What's your name, young scholar? ").strip()
            if self.player_name:
                print(f"🌟 Great to meet you, {self.player_name}!")
                print("🎓 Ready to embark on your educational adventure?")
                input("Press Enter to continue...")
    
    def play_math_wizard(self):
        """Launch Math Wizard game"""
        print("\n🧮 MATH WIZARD - Coming to life!")
        print("⚡ Loading mathematical challenges...")
        # Import and run the math game
        from games.math_wizard import MathWizardGame
        game = MathWizardGame()
        score = game.play()
        self.update_score(score, "Math Wizard")
    
    def play_word_master(self):
        """Launch Word Master game"""
        print("\n🔤 WORD MASTER - Activating vocabulary powers!")
        print("📚 Preparing language challenges...")
        from games.word_master import WordMasterGame
        game = WordMasterGame()
        score = game.play()
        self.update_score(score, "Word Master")
    
    def play_science_lab(self):
        """Launch Science Lab game"""
        print("\n🧪 SCIENCE LAB - Initializing experiments!")
        print("🔬 Setting up laboratory...")
        from games.science_lab import ScienceLabGame
        game = ScienceLabGame()
        score = game.play()
        self.update_score(score, "Science Lab")
    
    def play_geography_quest(self):
        """Launch Geography Quest game"""
        print("\n🌍 GEOGRAPHY QUEST - Exploring the world!")
        print("🗺️  Loading world map...")
        from games.geography_quest import GeographyQuestGame
        game = GeographyQuestGame()
        score = game.play()
        self.update_score(score, "Geography Quest")
    
    def play_history_hunter(self):
        """Launch History Hunter game"""
        print("\n📚 HISTORY HUNTER - Time travel activated!")
        print("⏰ Calibrating temporal coordinates...")
        from games.history_hunter import HistoryHunterGame
        game = HistoryHunterGame()
        score = game.play()
        self.update_score(score, "History Hunter")
    
    def play_target_practice(self):
        """Launch Target Practice game"""
        print("\n🎯 TARGET PRACTICE - Activating aim training!")
        print("🏹 Loading targets and challenges...")
        from games.target_practice import TargetPracticeGame
        game = TargetPracticeGame()
        score = game.play()
        self.update_score(score, "Target Practice")
    
    def play_puzzle_master(self):
        """Launch Puzzle Master game"""
        print("\n🧩 PUZZLE MASTER - Brain power engaged!")
        print("🧠 Preparing mind-bending challenges...")
        from games.puzzle_master import PuzzleMasterGame
        game = PuzzleMasterGame()
        score = game.play()
        self.update_score(score, "Puzzle Master")
    
    def play_lucky_numbers(self):
        """Launch Lucky Numbers game"""
        print("\n🎲 LUCKY NUMBERS - Fortune favors the bold!")
        print("🍀 Rolling the dice of destiny...")
        from games.lucky_numbers import LuckyNumbersGame
        game = LuckyNumbersGame()
        score = game.play()
        self.update_score(score, "Lucky Numbers")
    
    def play_memory_game(self):
        """Launch Memory Game"""
        print("\n🌟 MEMORY GAME - Activating neural pathways!")
        print("🧠 Preparing memory challenges...")
        from games.memory_game import MemoryGameChallenge
        game = MemoryGameChallenge()
        score = game.play()
        self.update_score(score, "Memory Game")
    
    def play_quick_quiz(self):
        """Launch Quick Quiz game"""
        print("\n⚡ QUICK QUIZ - Lightning round activated!")
        print("💨 Preparing rapid-fire questions...")
        from games.quick_quiz import QuickQuizGame
        game = QuickQuizGame()
        score = game.play()
        self.update_score(score, "Quick Quiz")
    
    def update_score(self, score, game_name):
        """Update player score and progress"""
        if score > 0:
            self.player_data['total_score'] = self.player_data.get('total_score', 0) + score
            if game_name not in self.player_data.get('games_played', []):
                self.player_data.setdefault('games_played', []).append(game_name)
            self.save_player_data()
            print(f"\n🎉 Great job! You earned {score} points in {game_name}!")
            print(f"🏆 Total Score: {self.player_data['total_score']}")
    
    def show_progress(self):
        """Display player progress and achievements"""
        print("\n📊 YOUR PROGRESS REPORT")
        print("="*40)
        print(f"👤 Player: {self.player_name or 'Anonymous'}")
        print(f"🏆 Total Score: {self.player_data.get('total_score', 0)}")
        print(f"🎮 Games Played: {len(self.player_data.get('games_played', []))}/5")
        
        games_played = self.player_data.get('games_played', [])
        if games_played:
            print("\n✅ Completed Games:")
            for game in games_played:
                print(f"   • {game}")
        
        achievements = self.player_data.get('achievements', [])
        if achievements:
            print("\n🏅 Achievements Unlocked:")
            for achievement in achievements:
                print(f"   🌟 {achievement}")
        
        input("\nPress Enter to return to main menu...")
    
    def settings_menu(self):
        """Settings and preferences"""
        print("\n⚙️  SETTINGS")
        print("="*30)
        print("1. 🔄 Reset Progress")
        print("2. 👤 Change Player Name")
        print("3. 🔙 Back to Main Menu")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == '1':
            confirm = input("⚠️  Reset all progress? (yes/no): ").lower()
            if confirm == 'yes':
                self.player_data = {"total_score": 0, "games_played": [], "achievements": []}
                self.save_player_data()
                print("✅ Progress reset successfully!")
        elif choice == '2':
            self.player_name = input("Enter new name: ").strip()
            print(f"✅ Name changed to {self.player_name}")
        
        input("Press Enter to continue...")
    
    def exit_game(self):
        """Exit the game with a nice message"""
        print("\n🎓 Thanks for playing EduVerse Arcade!")
        print("🌟 Keep learning and growing!")
        if self.player_name:
            print(f"👋 See you next time, {self.player_name}!")
        print("="*50)
    
    def run(self):
        """Main game loop"""
        self.get_player_name()
        self.main_menu()

def main():
    """Entry point for EduVerse Arcade"""
    try:
        arcade = EduVerseArcade()
        arcade.run()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for playing EduVerse Arcade!")
        print("🎓 Keep learning!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("🔧 Please try restarting the game.")

if __name__ == "__main__":
    main()
