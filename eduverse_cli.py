#!/usr/bin/env python3
"""
🎓 EduVerse CLI: 10 Realms of Genius - DIVERSE GAME TYPES
A Terminal-Based Educational Game Platform with Unique Game Mechanics

Author: EduVerse Team
Version: 2.0.0
Age Group: 10-25 years
Languages: English 🇬🇧 / Tamil 🇮🇳

GAME TYPES:
1. 🧮 Math Wizard - Calculation & Problem Solving
2. 🔤 Word Master - Word Puzzles & Anagrams  
3. 🧪 Science Lab - Interactive Experiments
4. 🌍 Geography Quest - Map Navigation & Discovery
5. 📚 History Hunter - Timeline Building
6. 🎨 Art Creator - ASCII Art & Color Matching
7. 🎵 Music Maestro - Rhythm & Pattern Games
8. 💻 Code Ninja - Programming Logic Puzzles
9. 🧩 Logic Puzzle - Pattern Recognition & Deduction
10. 🌟 Memory Palace - Sequence & Spatial Memory
"""

import os
import sys
import json
import random
import time
import datetime
import math
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, asdict
import argparse

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Additional colors for diverse games
    PURPLE = '\033[35m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

@dataclass
class PlayerStats:
    name: str
    language: str
    total_score: int = 0
    games_played: int = 0
    correct_answers: int = 0
    total_questions: int = 0
    achievements: List[str] = None
    level_progress: Dict[str, int] = None
    game_high_scores: Dict[str, int] = None
    
    def __post_init__(self):
        if self.achievements is None:
            self.achievements = []
        if self.level_progress is None:
            self.level_progress = {}
        if self.game_high_scores is None:
            self.game_high_scores = {}

class EduVerseTranslations:
    """Multilingual support for Tamil and English"""
    
    TRANSLATIONS = {
        'en': {
            'welcome': '🎓 Welcome to EduVerse CLI: 10 Realms of Genius! 🎓',
            'select_language': 'Select Language / மொழியைத் தேர்ந்தெடுக்கவும்:',
            'enter_name': 'Enter your name: ',
            'main_menu': '🌟 MAIN MENU 🌟',
            'select_game': 'Select a game (1-10) or option:',
            'view_stats': 'View Statistics',
            'achievements': 'Achievements',
            'leaderboard': 'Leaderboard',
            'settings': 'Settings',
            'quit': 'Quit Game',
            'exit_to_menu': 'Return to Main Menu',
            'exit_game': 'Type \'exit\' to return to main menu',
            'returning_to_menu': 'Returning to main menu...',
            'current_progress': 'Current progress',
            'game_navigation': 'Game Navigation Menu',
            'quick_switch': 'Quick Game Switch',
            'continue_game': 'Continue Current Game',
            'switch_game': 'Switching to game',
            'saving_progress': 'Saving progress',
            'invalid_choice': '❌ Invalid choice! Please try again.',
            'score': 'Score',
            'level': 'Level',
            'correct': '✅ Correct!',
            'incorrect': '❌ Incorrect!',
            'game_over': '🎮 Game Over!',
            'final_score': 'Final Score',
            'play_again': 'Play again? (y/n): ',
            'loading': 'Loading...',
            'press_enter': 'Press Enter to continue...',
            'time_up': '⏰ Time\'s up!',
            'streak': 'Streak',
            'hint': 'Hint',
            'skip': 'Skip',
            'games': {
                'math_wizard': '🧮 Math Wizard',
                'word_master': '🔤 Word Master',
                'science_lab': '🧪 Science Lab',
                'geography_quest': '🌍 Geography Quest',
                'history_hunter': '📚 History Hunter',
                'art_creator': '🎨 Art Creator',
                'music_maestro': '🎵 Music Maestro',
                'code_ninja': '💻 Code Ninja',
                'logic_puzzle': '🧩 Logic Puzzle',
                'memory_palace': '🌟 Memory Palace'
            }
        },
        'ta': {
            'welcome': '🎓 EduVerse CLI: 10 மேதைகளின் உலகம்! 🎓',
            'select_language': 'Select Language / மொழியைத் தேர்ந்தெடுக்கவும்:',
            'enter_name': 'உங்கள் பெயரை உள்ளிடவும்: ',
            'main_menu': '🌟 முதன்மை மெனு 🌟',
            'select_game': 'ஒரு விளையாட்டைத் தேர்ந்தெடுக்கவும் (1-10) அல்லது விருப்பம்:',
            'view_stats': 'புள்ளிவிவரங்களைப் பார்க்கவும்',
            'achievements': 'சாதனைகள்',
            'leaderboard': 'தலைமை பலகை',
            'settings': 'அமைப்புகள்',
            'quit': 'விளையாட்டை விட்டு வெளியேறு',
            'exit_to_menu': 'முதன்மை மெனுவுக்குத் திரும்பு',
            'exit_game': 'முதன்மை மெனுவுக்குத் திரும்ப \'exit\' என்று தட்டச்சு செய்யவும்',
            'returning_to_menu': 'முதன்மை மெனுவுக்குத் திரும்புகிறது...',
            'current_progress': 'தற்போதைய முன்னேற்றம்',
            'game_navigation': 'விளையாட்டு வழிசெலுத்தல் மெனு',
            'quick_switch': 'விரைவு விளையாட்டு மாற்றம்',
            'continue_game': 'தற்போதைய விளையாட்டைத் தொடரவும்',
            'switch_game': 'விளையாட்டுக்கு மாறுகிறது',
            'saving_progress': 'முன்னேற்றத்தைச் சேமிக்கிறது',
            'invalid_choice': '❌ தவறான தேர்வு! மீண்டும் முயற்சிக்கவும்.',
            'score': 'மதிப்பெண்',
            'level': 'நிலை',
            'correct': '✅ சரி!',
            'incorrect': '❌ தவறு!',
            'game_over': '🎮 விளையாட்டு முடிந்தது!',
            'final_score': 'இறுதி மதிப்பெண்',
            'play_again': 'மீண்டும் விளையாட வேண்டுமா? (y/n): ',
            'loading': 'ஏற்றுகிறது...',
            'press_enter': 'தொடர Enter அழுத்தவும்...',
            'time_up': '⏰ நேரம் முடிந்தது!',
            'streak': 'தொடர்ச்சி',
            'hint': 'குறிப்பு',
            'skip': 'தவிர்',
            'games': {
                'math_wizard': '🧮 கணித மந்திரவாதி',
                'word_master': '🔤 சொல் மாஸ்டர்',
                'science_lab': '🧪 அறிவியல் ஆய்வகம்',
                'geography_quest': '🌍 புவியியல் தேடல்',
                'history_hunter': '📚 வரலாற்று வேட்டைக்காரன்',
                'art_creator': '🎨 கலை படைப்பாளி',
                'music_maestro': '🎵 இசை மேஸ்ட்ரோ',
                'code_ninja': '💻 கோட் நிஞ்ஜா',
                'logic_puzzle': '🧩 தர்க்க புதிர்',
                'memory_palace': '🌟 நினைவு அரண்மனை'
            }
        }
    }
    
    @classmethod
    def get(cls, key: str, lang: str = 'en') -> str:
        """Get translation for a key"""
        keys = key.split('.')
        value = cls.TRANSLATIONS.get(lang, cls.TRANSLATIONS['en'])
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                # Fallback to English if key not found
                value = cls.TRANSLATIONS['en']
                for k in keys:
                    if isinstance(value, dict) and k in value:
                        value = value[k]
                    else:
                        return key  # Return key if not found
                break
        
        return str(value)

class EduVerseCLI:
    """Main EduVerse CLI Game Engine with Diverse Game Types"""
    
    def __init__(self):
        self.player_stats = None
        self.current_language = 'en'
        self.data_file = '.eduverse_cli_data.json'
        self.game_session_data = {}
        self.load_player_data()
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Print game banner"""
        banner = f"""
{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                    🎓 EDUVERSE CLI 🎓                        ║
║              10 Realms of Genius - v2.0.0                   ║
║                                                              ║
║  🧮 Math Wizard      🔤 Word Master     🧪 Science Lab       ║
║  🌍 Geography Quest  📚 History Hunter  🎨 Art Creator       ║
║  🎵 Music Maestro    💻 Code Ninja      🧩 Logic Puzzle      ║
║                    🌟 Memory Palace                          ║
║                                                              ║
║              Educational Gaming Platform                     ║
║                   Ages 10-25 Years                          ║
╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}
        """
        print(banner)
    
    def select_language(self):
        """Language selection interface"""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Colors.OKCYAN}{EduVerseTranslations.get('select_language')}{Colors.ENDC}")
        print(f"{Colors.OKGREEN}1. English 🇬🇧{Colors.ENDC}")
        print(f"{Colors.OKGREEN}2. Tamil 🇮🇳{Colors.ENDC}")
        
        while True:
            try:
                choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
                if choice == '1':
                    self.current_language = 'en'
                    break
                elif choice == '2':
                    self.current_language = 'ta'
                    break
                else:
                    print(f"{Colors.FAIL}Invalid choice! Please select 1 or 2.{Colors.ENDC}")
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}Goodbye!{Colors.ENDC}")
                self.quit_game()
    
    def get_player_name(self):
        """Get player name"""
        if not self.player_stats:
            self.clear_screen()
            self.print_banner()
            
            name_prompt = EduVerseTranslations.get('enter_name', self.current_language)
            name = input(f"\n{Colors.BOLD}{name_prompt}{Colors.ENDC}").strip()
            
            if not name:
                name = "Player"
            
            self.player_stats = PlayerStats(name=name, language=self.current_language)
            self.save_player_data()
    
    def main_menu(self):
        """Display main menu with diverse game options"""
        self.clear_screen()
        self.print_banner()
        
        if self.player_stats:
            print(f"\n{Colors.OKGREEN}Welcome back, {self.player_stats.name}!{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Total Score: {self.player_stats.total_score} | Games Played: {self.player_stats.games_played}{Colors.ENDC}")
        
        print(f"\n{Colors.HEADER}{Colors.BOLD}{EduVerseTranslations.get('main_menu', self.current_language)}{Colors.ENDC}")
        
        # Display games with their unique mechanics
        games = [
            ("🧮 Math Wizard", "Calculation & Problem Solving"),
            ("🔤 Word Master", "Anagrams & Word Puzzles"),
            ("🧪 Science Lab", "Interactive Experiments"),
            ("🌍 Geography Quest", "Map Navigation & Discovery"),
            ("📚 History Hunter", "Timeline Building"),
            ("🎨 Art Creator", "ASCII Art & Color Matching"),
            ("🎵 Music Maestro", "Rhythm & Pattern Games"),
            ("💻 Code Ninja", "Programming Logic Puzzles"),
            ("🧩 Logic Puzzle", "Pattern Recognition"),
            ("🌟 Memory Palace", "Sequence & Spatial Memory")
        ]
        
        for i, (game_name, description) in enumerate(games, 1):
            print(f"{Colors.OKGREEN}{i:2d}. {game_name:<20} {Colors.OKCYAN}- {description}{Colors.ENDC}")
        
        print(f"\n{Colors.WARNING}11. {EduVerseTranslations.get('view_stats', self.current_language)}{Colors.ENDC}")
        print(f"{Colors.WARNING}12. {EduVerseTranslations.get('achievements', self.current_language)}{Colors.ENDC}")
        print(f"{Colors.WARNING}13. {EduVerseTranslations.get('settings', self.current_language)}{Colors.ENDC}")
        print(f"{Colors.FAIL}14. {EduVerseTranslations.get('quit', self.current_language)}{Colors.ENDC}")
        
        return self.get_menu_choice()
    
    def get_menu_choice(self):
        """Get user menu choice"""
        while True:
            try:
                choice = input(f"\n{Colors.BOLD}Choice (1-14): {Colors.ENDC}").strip()
                if choice.isdigit() and 1 <= int(choice) <= 14:
                    return int(choice)
                else:
                    print(f"{Colors.FAIL}{EduVerseTranslations.get('invalid_choice', self.current_language)}{Colors.ENDC}")
            except KeyboardInterrupt:
                self.quit_game()
    
    def load_player_data(self):
        """Load player data from file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.player_stats = PlayerStats(**data)
                    self.current_language = self.player_stats.language
        except Exception as e:
            print(f"Error loading player data: {e}")
            self.player_stats = None
    
    def save_player_data(self):
        """Save player data to file"""
        try:
            if self.player_stats:
                with open(self.data_file, 'w') as f:
                    json.dump(asdict(self.player_stats), f, indent=2)
        except Exception as e:
            print(f"Error saving player data: {e}")
    
    def view_statistics(self):
        """Display player statistics"""
        self.clear_screen()
        self.print_banner()
        
        if not self.player_stats:
            print(f"{Colors.WARNING}No statistics available yet!{Colors.ENDC}")
            input(f"\n{EduVerseTranslations.get('press_enter', self.current_language)}")
            return
        
        stats = self.player_stats
        accuracy = (stats.correct_answers / max(stats.total_questions, 1)) * 100
        
        print(f"\n{Colors.HEADER}{Colors.BOLD}📊 PLAYER STATISTICS 📊{Colors.ENDC}")
        print(f"\n{Colors.OKGREEN}Player Name: {stats.name}{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Language: {'English 🇬🇧' if stats.language == 'en' else 'Tamil 🇮🇳'}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Total Score: {stats.total_score:,}{Colors.ENDC}")
        print(f"{Colors.PURPLE}Games Played: {stats.games_played}{Colors.ENDC}")
        print(f"{Colors.YELLOW}Questions Answered: {stats.total_questions}{Colors.ENDC}")
        print(f"{Colors.GREEN}Correct Answers: {stats.correct_answers}{Colors.ENDC}")
        print(f"{Colors.CYAN}Accuracy: {accuracy:.1f}%{Colors.ENDC}")
        
        if stats.game_high_scores:
            print(f"\n{Colors.HEADER}🏆 HIGH SCORES BY GAME:{Colors.ENDC}")
            for game, score in stats.game_high_scores.items():
                game_name = EduVerseTranslations.get(f'games.{game}', self.current_language)
                print(f"{Colors.OKGREEN}{game_name}: {score:,}{Colors.ENDC}")
        
        input(f"\n{EduVerseTranslations.get('press_enter', self.current_language)}")
    
    def view_achievements(self):
        """Display player achievements"""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Colors.HEADER}{Colors.BOLD}🏆 ACHIEVEMENTS 🏆{Colors.ENDC}")
        
        if not self.player_stats or not self.player_stats.achievements:
            print(f"\n{Colors.WARNING}No achievements unlocked yet!{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Play games to unlock achievements!{Colors.ENDC}")
        else:
            for achievement in self.player_stats.achievements:
                print(f"{Colors.OKGREEN}✅ {achievement}{Colors.ENDC}")
        
        input(f"\n{EduVerseTranslations.get('press_enter', self.current_language)}")
    
    def settings_menu(self):
        """Settings menu"""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Colors.HEADER}{Colors.BOLD}⚙️ SETTINGS ⚙️{Colors.ENDC}")
        print(f"\n{Colors.OKGREEN}1. Change Language{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Reset Progress{Colors.ENDC}")
        print(f"{Colors.FAIL}3. Back to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-3): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.select_language()
            if self.player_stats:
                self.player_stats.language = self.current_language
                self.save_player_data()
        elif choice == '2':
            confirm = input(f"{Colors.WARNING}Are you sure? This will delete all progress! (y/N): {Colors.ENDC}").strip().lower()
            if confirm == 'y':
                if os.path.exists(self.data_file):
                    os.remove(self.data_file)
                self.player_stats = None
                print(f"{Colors.OKGREEN}Progress reset successfully!{Colors.ENDC}")
                time.sleep(2)
    
    def quit_game(self):
        """Quit the game"""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Colors.OKCYAN}Thank you for playing EduVerse CLI!{Colors.ENDC}")
        print(f"{Colors.OKGREEN}Keep learning and growing! 🌟{Colors.ENDC}")
        
        if self.player_stats:
            print(f"\n{Colors.BOLD}Final Stats:{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Total Score: {self.player_stats.total_score:,}{Colors.ENDC}")
            print(f"{Colors.OKGREEN}Games Played: {self.player_stats.games_played}{Colors.ENDC}")
        
        sys.exit(0)
    
    def run(self):
        """Main game loop"""
        try:
            self.select_language()
            self.get_player_name()
            
            while True:
                choice = self.main_menu()
                
                if 1 <= choice <= 10:
                    self.play_game(choice)
                elif choice == 11:
                    self.view_statistics()
                elif choice == 12:
                    self.view_achievements()
                elif choice == 13:
                    self.settings_menu()
                elif choice == 14:
                    self.quit_game()
                    
        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}Game interrupted by user.{Colors.ENDC}")
            self.quit_game()
        except Exception as e:
            print(f"\n{Colors.FAIL}An error occurred: {e}{Colors.ENDC}")
            self.quit_game()
    
    def play_game(self, game_number):
        """Play selected game with unique mechanics"""
        game_methods = {
            1: self.math_wizard_game,
            2: self.word_master_game,
            3: self.science_lab_game,
            4: self.geography_quest_game,
            5: self.history_hunter_game,
            6: self.art_creator_game,
            7: self.music_maestro_game,
            8: self.code_ninja_game,
            9: self.logic_puzzle_game,
            10: self.memory_palace_game
        }
        
        if game_number in game_methods:
            game_methods[game_number]()
        else:
            self.placeholder_game(game_number)
    
    # ==================== GAME 1: MATH WIZARD ====================
    def math_wizard_game(self):
        """Math Wizard - Interactive Calculation Game"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.math_wizard', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - Interactive Calculator{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}🧮 Solve mathematical challenges step by step!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}📊 Build equations, solve puzzles, and master arithmetic!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start Math Challenge{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_math_wizard()
    
    def run_math_wizard(self):
        """Run the Math Wizard game with progressive difficulty"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}🧮 MATH WIZARD - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            # Generate math problem based on level
            if level <= 3:
                # Basic arithmetic
                a, b = random.randint(1, 20), random.randint(1, 20)
                operations = ['+', '-', '*']
                op = random.choice(operations)
                
                if op == '+':
                    answer = a + b
                    problem = f"{a} + {b}"
                elif op == '-':
                    if a < b:
                        a, b = b, a  # Ensure positive result
                    answer = a - b
                    problem = f"{a} - {b}"
                else:  # multiplication
                    answer = a * b
                    problem = f"{a} × {b}"
                    
            elif level <= 6:
                # Intermediate problems
                if random.choice([True, False]):
                    # Multi-step arithmetic
                    a, b, c = random.randint(1, 15), random.randint(1, 15), random.randint(1, 15)
                    if random.choice([True, False]):
                        answer = a + b * c
                        problem = f"{a} + {b} × {c}"
                    else:
                        answer = (a + b) * c
                        problem = f"({a} + {b}) × {c}"
                else:
                    # Division problems
                    b = random.randint(2, 12)
                    answer = random.randint(2, 15)
                    a = answer * b
                    problem = f"{a} ÷ {b}"
                    
            else:
                # Advanced problems
                problem_type = random.choice(['quadratic', 'percentage', 'fraction'])
                
                if problem_type == 'quadratic':
                    # Simple quadratic: x² = n, find x
                    x = random.randint(2, 12)
                    n = x * x
                    answer = x
                    problem = f"If x² = {n}, what is x? (positive value)"
                    
                elif problem_type == 'percentage':
                    # Percentage problems
                    base = random.randint(20, 200)
                    percent = random.choice([10, 20, 25, 50, 75])
                    answer = int(base * percent / 100)
                    problem = f"What is {percent}% of {base}?"
                    
                else:  # fraction
                    # Simple fraction addition
                    # Same denominator for simplicity
                    denom = random.choice([2, 3, 4, 5, 6])
                    num1 = random.randint(1, denom-1)
                    num2 = random.randint(1, denom-1)
                    
                    # Ensure result is less than 1
                    if num1 + num2 >= denom:
                        num2 = denom - num1 - 1
                        if num2 <= 0:
                            num2 = 1
                            num1 = denom - 2
                    
                    # Present as decimal
                    result = (num1 + num2) / denom
                    answer = round(result, 2)
                    problem = f"{num1}/{denom} + {num2}/{denom} = ? (as decimal, rounded to 2 places)"
            
            print(f"\n{Colors.OKGREEN}Problem: {problem}{Colors.ENDC}")
            
            # Interactive solving process
            if level >= 4:
                print(f"{Colors.OKCYAN}💡 Hint available! Type 'hint' for help{Colors.ENDC}")
            print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
            
            user_input = input(f"\n{Colors.BOLD}Your answer (or 'hint'/'skip'/'exit'/'nav'): {Colors.ENDC}").strip()
            
            # Handle navigation commands
            nav_result = self.handle_game_navigation(user_input, "Math Wizard", level, score)
            if nav_result == 'main_menu':
                return
            elif nav_result == 'switched':
                return
            elif nav_result == 'continue':
                continue  # Skip this iteration and continue with the game
            
            # Handle exit command
            if user_input.lower() == 'exit':
                print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                time.sleep(1)
                return  # Exit the game and return to main menu
            
            total_questions += 1
            
            if user_input.lower() == 'hint' and level >= 4:
                self.show_math_hint(problem, level)
                user_input = input(f"\n{Colors.BOLD}Your answer (or 'exit' to quit): {Colors.ENDC}").strip()
                
                # Check for exit again after hint
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
            
            if user_input.lower() == 'skip':
                print(f"{Colors.WARNING}⏭️ Skipped! The answer was: {answer}{Colors.ENDC}")
                streak = 0
                score -= 25  # Penalty for skipping
            else:
                try:
                    user_answer = float(user_input)
                    if abs(user_answer - answer) < 0.01:  # Allow small floating point errors
                        print(f"{Colors.OKGREEN}✅ Correct! +100 points{Colors.ENDC}")
                        score += 100
                        correct_answers += 1
                        streak += 1
                        max_streak = max(max_streak, streak)
                        
                        # Streak bonus
                        if streak >= 3:
                            bonus = streak * 25
                            score += bonus
                            print(f"{Colors.YELLOW}🔥 Streak Bonus: +{bonus} points!{Colors.ENDC}")
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! The answer was: {answer}{Colors.ENDC}")
                        streak = 0
                        
                except ValueError:
                    print(f"{Colors.FAIL}❌ Invalid input! The answer was: {answer}{Colors.ENDC}")
                    streak = 0
            
            time.sleep(2)
            level += 1
        
        self.complete_game('math_wizard', game_name, score, correct_answers, total_questions, max_streak)
    
    def show_math_hint(self, problem, level):
        """Show contextual hints for math problems"""
        hints = {
            1: "Break down the problem step by step",
            2: "Remember order of operations: PEMDAS",
            3: "For division, think: what number times the divisor gives the dividend?",
            4: "For quadratics, find the square root",
            5: "For percentages, multiply by the percentage and divide by 100",
            6: "For fractions, add numerators when denominators are the same"
        }
        
        hint_level = min(level // 2 + 1, 6)
        print(f"{Colors.YELLOW}💡 Hint: {hints[hint_level]}{Colors.ENDC}")
    
    # ==================== GAME 2: WORD MASTER ====================
    def word_master_game(self):
        """Word Master - Anagram and Word Puzzle Game"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.word_master', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - Word Puzzles & Anagrams{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}🔤 Unscramble letters, solve anagrams, and build words!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}📝 Challenge your vocabulary and word-building skills!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start Word Challenge{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_word_master()
    
    def run_word_master(self):
        """Run the Word Master game with anagrams and word puzzles"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        # Word lists by difficulty
        word_lists = {
            'easy': ['cat', 'dog', 'sun', 'moon', 'tree', 'book', 'fish', 'bird', 'star', 'home'],
            'medium': ['computer', 'elephant', 'rainbow', 'mountain', 'library', 'garden', 'kitchen', 'window', 'pencil', 'flower'],
            'hard': ['adventure', 'mysterious', 'beautiful', 'dangerous', 'incredible', 'magnificent', 'wonderful', 'fantastic', 'brilliant', 'excellent']
        }
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}🔤 WORD MASTER - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            # Select difficulty based on level
            if level <= 3:
                difficulty = 'easy'
                word_list = word_lists['easy']
            elif level <= 7:
                difficulty = 'medium'
                word_list = word_lists['medium']
            else:
                difficulty = 'hard'
                word_list = word_lists['hard']
            
            # Choose game type
            game_types = ['anagram', 'word_building', 'missing_letters']
            game_type = random.choice(game_types)
            
            if game_type == 'anagram':
                # Anagram challenge
                target_word = random.choice(word_list)
                scrambled = self.scramble_word(target_word)
                
                print(f"\n{Colors.OKGREEN}🔀 ANAGRAM CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Unscramble these letters: {Colors.BOLD}{scrambled.upper()}{Colors.ENDC}")
                print(f"{Colors.YELLOW}💡 Hint: It's a {len(target_word)}-letter word{Colors.ENDC}")
                
                user_input = input(f"\n{Colors.BOLD}Your answer: {Colors.ENDC}").strip().lower()
                
                if user_input == target_word:
                    print(f"{Colors.OKGREEN}✅ Correct! The word was '{target_word.upper()}'!{Colors.ENDC}")
                    score += 150
                    correct_answers += 1
                    streak += 1
                else:
                    print(f"{Colors.FAIL}❌ Incorrect! The word was '{target_word.upper()}'!{Colors.ENDC}")
                    streak = 0
                    
            elif game_type == 'word_building':
                # Word building from letters
                base_letters = random.choice(['AEIOU', 'BCDFG', 'HJKLM', 'NPQRS', 'TVWXY'])
                extra_letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
                available_letters = base_letters + extra_letters
                
                print(f"\n{Colors.OKGREEN}🏗️ WORD BUILDING CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Use these letters to make a word: {Colors.BOLD}{available_letters}{Colors.ENDC}")
                print(f"{Colors.YELLOW}💡 You can use each letter only once{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                
                user_input = input(f"\n{Colors.BOLD}Your word (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Word Master", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue  # Skip this iteration and continue with the game
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                user_input = user_input.upper()
                
                if self.is_valid_word_from_letters(user_input, available_letters):
                    word_score = len(user_input) * 20
                    print(f"{Colors.OKGREEN}✅ Great word! '{user_input}' (+{word_score} points){Colors.ENDC}")
                    score += word_score
                    correct_answers += 1
                    streak += 1
                else:
                    print(f"{Colors.FAIL}❌ Invalid word or uses unavailable letters!{Colors.ENDC}")
                    streak = 0
                    
            else:  # missing_letters
                # Fill in missing letters
                target_word = random.choice(word_list)
                missing_positions = random.sample(range(len(target_word)), min(2, len(target_word)//2))
                display_word = list(target_word)
                
                for pos in missing_positions:
                    display_word[pos] = '_'
                
                display_str = ''.join(display_word).upper()
                
                print(f"\n{Colors.OKGREEN}🔍 MISSING LETTERS CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Complete this word: {Colors.BOLD}{display_str}{Colors.ENDC}")
                print(f"{Colors.YELLOW}💡 Fill in the missing letters{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                
                user_input = input(f"\n{Colors.BOLD}Complete word (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Word Master", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue  # Skip this iteration and continue with the game
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                user_input = user_input.lower()
                
                if user_input == target_word:
                    print(f"{Colors.OKGREEN}✅ Perfect! The word was '{target_word.upper()}'!{Colors.ENDC}")
                    score += 120
                    correct_answers += 1
                    streak += 1
                else:
                    print(f"{Colors.FAIL}❌ Incorrect! The word was '{target_word.upper()}'!{Colors.ENDC}")
                    streak = 0
            
            total_questions += 1
            max_streak = max(max_streak, streak)
            
            # Streak bonus
            if streak >= 3:
                bonus = streak * 30
                score += bonus
                print(f"{Colors.YELLOW}🔥 Word Streak Bonus: +{bonus} points!{Colors.ENDC}")
            
            time.sleep(2.5)
            level += 1
        
        self.complete_game('word_master', game_name, score, correct_answers, total_questions, max_streak)
    
    def scramble_word(self, word):
        """Scramble letters of a word"""
        letters = list(word)
        random.shuffle(letters)
        scrambled = ''.join(letters)
        
        # Ensure it's actually scrambled
        if scrambled == word and len(word) > 2:
            return self.scramble_word(word)
        return scrambled
    
    def is_valid_word_from_letters(self, word, available_letters):
        """Check if word can be made from available letters"""
        if len(word) < 3:  # Minimum word length
            return False
        
        available = list(available_letters)
        for letter in word:
            if letter in available:
                available.remove(letter)
            else:
                return False
        return True
    
    # ==================== GAME 3: SCIENCE LAB ====================
    def science_lab_game(self):
        """Science Lab - Interactive Experiment Simulation"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.science_lab', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - Interactive Experiments{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}🧪 Conduct virtual experiments and discover scientific principles!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}⚗️ Mix chemicals, observe reactions, and learn through discovery!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start Science Experiments{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_science_lab()
    
    def run_science_lab(self):
        """Run interactive science experiments"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        experiments = [
            {
                'name': 'Chemical Reactions',
                'description': 'Mix chemicals and predict the result',
                'type': 'chemistry'
            },
            {
                'name': 'Physics Forces',
                'description': 'Calculate forces and motion',
                'type': 'physics'
            },
            {
                'name': 'Biology Classification',
                'description': 'Classify living organisms',
                'type': 'biology'
            }
        ]
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}🧪 SCIENCE LAB - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            experiment = random.choice(experiments)
            print(f"\n{Colors.OKGREEN}🔬 EXPERIMENT: {experiment['name']}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}{experiment['description']}{Colors.ENDC}")
            
            if experiment['type'] == 'chemistry':
                # Chemistry experiment simulation
                reactions = [
                    {'reactants': ['H2', 'O2'], 'product': 'H2O', 'name': 'Water Formation'},
                    {'reactants': ['Na', 'Cl'], 'product': 'NaCl', 'name': 'Salt Formation'},
                    {'reactants': ['C', 'O2'], 'product': 'CO2', 'name': 'Carbon Dioxide'},
                    {'reactants': ['Fe', 'O2'], 'product': 'Fe2O3', 'name': 'Rust Formation'}
                ]
                
                reaction = random.choice(reactions)
                reactants_str = ' + '.join(reaction['reactants'])
                
                print(f"\n{Colors.YELLOW}⚗️ Mixing: {reactants_str}{Colors.ENDC}")
                print(f"{Colors.OKCYAN}What product will be formed?{Colors.ENDC}")
                
                # Show options
                options = [reaction['product']]
                # Add wrong options
                wrong_options = ['H2SO4', 'NH3', 'CH4', 'CaCO3']
                options.extend(random.sample(wrong_options, 3))
                random.shuffle(options)
                
                for i, option in enumerate(options, 1):
                    print(f"{Colors.OKGREEN}{i}. {option}{Colors.ENDC}")
                
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-4): {Colors.ENDC}").strip()
                
                try:
                    choice_idx = int(user_choice) - 1
                    if 0 <= choice_idx < len(options) and options[choice_idx] == reaction['product']:
                        print(f"{Colors.OKGREEN}✅ Correct! You created {reaction['name']}!{Colors.ENDC}")
                        score += 120
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! The product is {reaction['product']} ({reaction['name']}){Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
                    
            elif experiment['type'] == 'physics':
                # Physics calculation
                mass = random.randint(5, 50)
                acceleration = random.randint(2, 10)
                force = mass * acceleration
                
                print(f"\n{Colors.YELLOW}⚖️ Object mass: {mass} kg{Colors.ENDC}")
                print(f"{Colors.YELLOW}🏃 Acceleration: {acceleration} m/s²{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Calculate the force (F = ma):{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                
                user_input = input(f"\n{Colors.BOLD}Force in Newtons (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Science Lab", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue  # Skip this iteration and continue with the game
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_force = int(user_input)
                    if user_force == force:
                        print(f"{Colors.OKGREEN}✅ Correct! Force = {force} N{Colors.ENDC}")
                        score += 100
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! Force = {force} N{Colors.ENDC}")
                        streak = 0
                except ValueError:
                    print(f"{Colors.FAIL}❌ Invalid input! Force = {force} N{Colors.ENDC}")
                    streak = 0
                    
            else:  # biology
                # Biology classification
                organisms = [
                    {'name': 'Lion', 'kingdom': 'Animal', 'class': 'Mammal'},
                    {'name': 'Eagle', 'kingdom': 'Animal', 'class': 'Bird'},
                    {'name': 'Oak Tree', 'kingdom': 'Plant', 'class': 'Tree'},
                    {'name': 'Mushroom', 'kingdom': 'Fungi', 'class': 'Fungus'},
                    {'name': 'Shark', 'kingdom': 'Animal', 'class': 'Fish'}
                ]
                
                organism = random.choice(organisms)
                
                print(f"\n{Colors.YELLOW}🦁 Organism: {organism['name']}{Colors.ENDC}")
                print(f"{Colors.OKCYAN}What kingdom does this belong to?{Colors.ENDC}")
                
                kingdoms = ['Animal', 'Plant', 'Fungi', 'Bacteria']
                random.shuffle(kingdoms)
                
                for i, kingdom in enumerate(kingdoms, 1):
                    print(f"{Colors.OKGREEN}{i}. {kingdom}{Colors.ENDC}")
                
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-4): {Colors.ENDC}").strip()
                
                try:
                    choice_idx = int(user_choice) - 1
                    if 0 <= choice_idx < len(kingdoms) and kingdoms[choice_idx] == organism['kingdom']:
                        print(f"{Colors.OKGREEN}✅ Correct! {organism['name']} is in the {organism['kingdom']} kingdom!{Colors.ENDC}")
                        score += 110
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! {organism['name']} belongs to {organism['kingdom']} kingdom{Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
            
            total_questions += 1
            max_streak = max(max_streak, streak)
            
            # Streak bonus
            if streak >= 3:
                bonus = streak * 35
                score += bonus
                print(f"{Colors.YELLOW}🔥 Science Streak: +{bonus} points!{Colors.ENDC}")
            
            time.sleep(2.5)
            level += 1
        
        self.complete_game('science_lab', game_name, score, correct_answers, total_questions, max_streak)
    
    # ==================== GAME 4: GEOGRAPHY QUEST ====================
    def geography_quest_game(self):
        """Geography Quest - Map Navigation and Discovery"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.geography_quest', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - Map Navigation & Discovery{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}🌍 Explore the world through interactive map challenges!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}🗺️ Navigate continents, discover countries, and learn geography!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start Geography Adventure{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_geography_quest()
    
    def run_geography_quest(self):
        """Run geography navigation challenges"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        # Geography data
        continents = {
            'Asia': ['China', 'India', 'Japan', 'Thailand', 'Indonesia'],
            'Europe': ['France', 'Germany', 'Italy', 'Spain', 'United Kingdom'],
            'Africa': ['Egypt', 'Nigeria', 'South Africa', 'Kenya', 'Morocco'],
            'North America': ['United States', 'Canada', 'Mexico', 'Guatemala', 'Cuba'],
            'South America': ['Brazil', 'Argentina', 'Chile', 'Peru', 'Colombia'],
            'Oceania': ['Australia', 'New Zealand', 'Fiji', 'Papua New Guinea', 'Samoa']
        }
        
        capitals = {
            'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome',
            'Japan': 'Tokyo', 'China': 'Beijing', 'India': 'New Delhi',
            'Brazil': 'Brasília', 'Australia': 'Canberra', 'Canada': 'Ottawa',
            'Egypt': 'Cairo', 'Nigeria': 'Abuja', 'Mexico': 'Mexico City'
        }
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}🌍 GEOGRAPHY QUEST - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            # Choose challenge type
            challenge_types = ['continent_match', 'capital_city', 'map_navigation']
            challenge = random.choice(challenge_types)
            
            if challenge == 'continent_match':
                # Match country to continent
                continent = random.choice(list(continents.keys()))
                country = random.choice(continents[continent])
                
                print(f"\n{Colors.OKGREEN}🗺️ CONTINENT CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Which continent is {Colors.BOLD}{country}{Colors.ENDC}{Colors.OKCYAN} located in?{Colors.ENDC}")
                
                # Create options
                options = [continent]
                other_continents = [c for c in continents.keys() if c != continent]
                options.extend(random.sample(other_continents, 3))
                random.shuffle(options)
                
                for i, option in enumerate(options, 1):
                    print(f"{Colors.OKGREEN}{i}. {option}{Colors.ENDC}")
                
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-4, 'exit', 'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_choice, "Geography Quest", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_choice.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    choice_idx = int(user_choice) - 1
                    if 0 <= choice_idx < len(options) and options[choice_idx] == continent:
                        print(f"{Colors.OKGREEN}✅ Correct! {country} is in {continent}!{Colors.ENDC}")
                        score += 100
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! {country} is in {continent}!{Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
                    
            elif challenge == 'capital_city':
                # Capital city challenge
                country = random.choice(list(capitals.keys()))
                capital = capitals[country]
                
                print(f"\n{Colors.OKGREEN}🏛️ CAPITAL CITY CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}What is the capital of {Colors.BOLD}{country}{Colors.ENDC}{Colors.OKCYAN}?{Colors.ENDC}")
                
                # Create options
                options = [capital]
                other_capitals = [c for c in capitals.values() if c != capital]
                options.extend(random.sample(other_capitals, min(3, len(other_capitals))))
                random.shuffle(options)
                
                for i, option in enumerate(options, 1):
                    print(f"{Colors.OKGREEN}{i}. {option}{Colors.ENDC}")
                
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-{len(options)}, 'exit', 'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_choice, "Geography Quest", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_choice.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    choice_idx = int(user_choice) - 1
                    if 0 <= choice_idx < len(options) and options[choice_idx] == capital:
                        print(f"{Colors.OKGREEN}✅ Correct! The capital of {country} is {capital}!{Colors.ENDC}")
                        score += 120
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! The capital of {country} is {capital}!{Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
                    
            else:  # map_navigation
                # ASCII map navigation
                print(f"\n{Colors.OKGREEN}🧭 MAP NAVIGATION CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}You are at position (2,2) on this grid:{Colors.ENDC}")
                
                # Simple ASCII map
                map_grid = [
                    "🌊🌊🌊🌊🌊",
                    "🌊🏔️🌲🏛️🌊",
                    "🌊🌲🏠🌲🌊",
                    "🌊🏛️🌲🏔️🌊",
                    "🌊🌊🌊🌊🌊"
                ]
                
                for i, row in enumerate(map_grid):
                    if i == 2:  # Current position row
                        row_display = row[:4] + '👤' + row[5:]  # Replace house with player
                        print(f"{Colors.YELLOW}{row_display}{Colors.ENDC}")
                    else:
                        print(f"{Colors.CYAN}{row}{Colors.ENDC}")
                
                print(f"\n{Colors.OKCYAN}Legend: 🌊=Water 🏔️=Mountain 🌲=Forest 🏛️=City 👤=You{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Which direction should you go to reach a city?{Colors.ENDC}")
                
                directions = ['North (Up)', 'South (Down)', 'East (Right)', 'West (Left)']
                for i, direction in enumerate(directions, 1):
                    print(f"{Colors.OKGREEN}{i}. {direction}{Colors.ENDC}")
                
                # Correct answers: North (1,3) or South (3,1) both have cities
                correct_directions = [1, 2]  # North or South
                
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-4, 'exit', 'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_choice, "Geography Quest", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_choice.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    choice_idx = int(user_choice)
                    if choice_idx in correct_directions:
                        direction_name = directions[choice_idx-1]
                        print(f"{Colors.OKGREEN}✅ Correct! Going {direction_name} leads to a city!{Colors.ENDC}")
                        score += 90
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! That direction doesn't lead to a city.{Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
            
            total_questions += 1
            max_streak = max(max_streak, streak)
            
            # Streak bonus
            if streak >= 3:
                bonus = streak * 30
                score += bonus
                print(f"{Colors.YELLOW}🔥 Explorer Streak: +{bonus} points!{Colors.ENDC}")
            
            time.sleep(2.5)
            level += 1
        
        self.complete_game('geography_quest', game_name, score, correct_answers, total_questions, max_streak)
    
    # ==================== GAME 5: HISTORY HUNTER ====================
    def history_hunter_game(self):
        """History Hunter - Timeline Building Game"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.history_hunter', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - Timeline Building{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}📚 Build historical timelines and discover the past!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}⏳ Arrange events chronologically and learn history!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start History Adventure{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_history_hunter()
    
    def run_history_hunter(self):
        """Run timeline building challenges"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        # Historical events with years
        historical_events = [
            {'event': 'World War II ended', 'year': 1945},
            {'event': 'Moon landing', 'year': 1969},
            {'event': 'Berlin Wall fell', 'year': 1989},
            {'event': 'Internet was invented', 'year': 1989},
            {'event': 'First iPhone released', 'year': 2007},
            {'event': 'World War I began', 'year': 1914},
            {'event': 'Titanic sank', 'year': 1912},
            {'event': 'American Civil War ended', 'year': 1865},
            {'event': 'Declaration of Independence', 'year': 1776},
            {'event': 'Columbus reached America', 'year': 1492}
        ]
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}📚 HISTORY HUNTER - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            if level <= 5:
                # Simple year guessing
                event = random.choice(historical_events)
                
                print(f"\n{Colors.OKGREEN}📅 YEAR CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}In what year did this happen?{Colors.ENDC}")
                print(f"{Colors.BOLD}{event['event']}{Colors.ENDC}")
                
                # Create year options
                correct_year = event['year']
                options = [correct_year]
                
                # Add nearby years as wrong options
                for _ in range(3):
                    wrong_year = correct_year + random.randint(-20, 20)
                    if wrong_year not in options and wrong_year > 1000:
                        options.append(wrong_year)
                
                while len(options) < 4:
                    wrong_year = random.randint(1800, 2020)
                    if wrong_year not in options:
                        options.append(wrong_year)
                
                options.sort()
                
                for i, year in enumerate(options, 1):
                    print(f"{Colors.OKGREEN}{i}. {year}{Colors.ENDC}")
                
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-4, 'exit', 'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_choice, "History Hunter", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_choice.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    choice_idx = int(user_choice) - 1
                    if 0 <= choice_idx < len(options) and options[choice_idx] == correct_year:
                        print(f"{Colors.OKGREEN}✅ Correct! {event['event']} in {correct_year}!{Colors.ENDC}")
                        score += 100
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! {event['event']} in {correct_year}!{Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
                
                # Shuffle for display
                display_events = selected_events.copy()
                random.shuffle(display_events)
                
                print(f"\n{Colors.OKGREEN}⏳ TIMELINE CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Arrange these events in chronological order (earliest first):{Colors.ENDC}")
                
                for i, event in enumerate(display_events, 1):
                    print(f"{Colors.YELLOW}{i}. {event['event']}{Colors.ENDC}")
                
                print(f"\n{Colors.OKCYAN}Enter the correct order (e.g., '2,1,3'):{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_input = input(f"{Colors.BOLD}Order (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "History Hunter", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_order = [int(x.strip()) - 1 for x in user_input.split(',')]
                    
                    # Check if the order is correct
                    user_events = [display_events[i] for i in user_order]
                    user_years = [event['year'] for event in user_events]
                    correct_years = [event['year'] for event in selected_events]
                    
                    if user_years == correct_years:
                        print(f"{Colors.OKGREEN}✅ Perfect timeline! Events in correct chronological order!{Colors.ENDC}")
                        score += 150
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect order!{Colors.ENDC}")
                        print(f"{Colors.OKCYAN}Correct timeline:{Colors.ENDC}")
                        for event in selected_events:
                            print(f"{Colors.OKGREEN}{event['year']}: {event['event']}{Colors.ENDC}")
                        streak = 0
                        
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid input format!{Colors.ENDC}")
                    streak = 0
            
            total_questions += 1
            max_streak = max(max_streak, streak)
            
            # Streak bonus
            if streak >= 3:
                bonus = streak * 40
                score += bonus
                print(f"{Colors.YELLOW}🔥 History Streak: +{bonus} points!{Colors.ENDC}")
            
            time.sleep(2.5)
            level += 1
        
        self.complete_game('history_hunter', game_name, score, correct_answers, total_questions, max_streak)
    
    # ==================== GAME 6: ART CREATOR ====================
    def art_creator_game(self):
        """Art Creator - ASCII Art and Color Matching"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.art_creator', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - ASCII Art & Color Matching{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}🎨 Create ASCII art and match colors creatively!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}🖌️ Express your artistic side through terminal art!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start Art Challenge{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_art_creator()
    
    def run_art_creator(self):
        """Run ASCII art and color challenges"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        # ASCII art patterns
        ascii_patterns = {
            'heart': [
                "  ♥♥   ♥♥  ",
                " ♥♥♥♥ ♥♥♥♥ ",
                "♥♥♥♥♥♥♥♥♥♥♥",
                " ♥♥♥♥♥♥♥♥♥ ",
                "  ♥♥♥♥♥♥♥  ",
                "   ♥♥♥♥♥   ",
                "    ♥♥♥    ",
                "     ♥     "
            ],
            'star': [
                "    ★    ",
                "   ★★★   ",
                "  ★★★★★  ",
                " ★★★★★★★ ",
                "★★★★★★★★★",
                " ★★★★★★★ ",
                "  ★★★★★  ",
                "   ★★★   ",
                "    ★    "
            ],
            'tree': [
                "    🌲    ",
                "   🌲🌲🌲   ",
                "  🌲🌲🌲🌲🌲  ",
                " 🌲🌲🌲🌲🌲🌲🌲 ",
                "🌲🌲🌲🌲🌲🌲🌲🌲🌲",
                "    |||    ",
                "    |||    "
            ]
        }
        
        color_combinations = {
            'sunset': [Colors.RED, Colors.YELLOW, Colors.PURPLE],
            'ocean': [Colors.BLUE, Colors.CYAN, Colors.WHITE],
            'forest': [Colors.GREEN, Colors.YELLOW, Colors.BLUE],
            'fire': [Colors.RED, Colors.YELLOW, Colors.WHITE]
        }
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}🎨 ART CREATOR - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            if level <= 5:
                # ASCII pattern completion
                pattern_name = random.choice(list(ascii_patterns.keys()))
                pattern = ascii_patterns[pattern_name]
                
                # Remove a random line for user to complete
                missing_line_idx = random.randint(1, len(pattern) - 2)
                missing_line = pattern[missing_line_idx]
                
                print(f"\n{Colors.OKGREEN}🖼️ ASCII ART COMPLETION{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Complete this {pattern_name} pattern:{Colors.ENDC}")
                
                for i, line in enumerate(pattern):
                    if i == missing_line_idx:
                        print(f"{Colors.YELLOW}{'_' * len(line)}{Colors.ENDC}")
                    else:
                        print(f"{Colors.GREEN}{line}{Colors.ENDC}")
                
                print(f"\n{Colors.OKCYAN}What should the missing line be?{Colors.ENDC}")
                
                # Create options
                options = [missing_line]
                
                # Generate wrong options
                for _ in range(3):
                    wrong_line = ''.join(random.choices(['♥', '★', '🌲', ' '], k=len(missing_line)))
                    if wrong_line not in options:
                        options.append(wrong_line)
                
                random.shuffle(options)
                
                for i, option in enumerate(options, 1):
                    print(f"{Colors.OKGREEN}{i}. {option}{Colors.ENDC}")
                
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-4, 'exit', 'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_choice, "Art Creator", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_choice.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    choice_idx = int(user_choice) - 1
                    if 0 <= choice_idx < len(options) and options[choice_idx] == missing_line:
                        print(f"{Colors.OKGREEN}✅ Perfect! You completed the {pattern_name}!{Colors.ENDC}")
                        score += 120
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Not quite right! The correct line was: {missing_line}{Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
                    
            else:
                # Color harmony challenge
                theme_name = random.choice(list(color_combinations.keys()))
                theme_colors = color_combinations[theme_name]
                
                print(f"\n{Colors.OKGREEN}🌈 COLOR HARMONY CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Create a {theme_name} color palette!{Colors.ENDC}")
                
                # Show a sample with one color
                sample_color = random.choice(theme_colors)
                print(f"\n{Colors.OKCYAN}Starting color:{Colors.ENDC}")
                print(f"{sample_color}████████{Colors.ENDC}")
                
                print(f"\n{Colors.OKCYAN}Which colors would complete this {theme_name} theme?{Colors.ENDC}")
                
                # Create color options
                all_colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW, 
                             Colors.PURPLE, Colors.CYAN, Colors.WHITE, Colors.MAGENTA]
                
                correct_colors = [c for c in theme_colors if c != sample_color]
                wrong_colors = [c for c in all_colors if c not in theme_colors]
                
                options = correct_colors + random.sample(wrong_colors, 2)
                random.shuffle(options)
                
                for i, color in enumerate(options, 1):
                    print(f"{color}{i}. Color Sample ████{Colors.ENDC}")
                
                print(f"\n{Colors.OKCYAN}Select TWO colors that match the theme (e.g., '1,3'):{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_input = input(f"{Colors.BOLD}Your choices (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Art Creator", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_choices = [int(x.strip()) - 1 for x in user_input.split(',')]
                    user_colors = [options[i] for i in user_choices if 0 <= i < len(options)]
                    
                    if len(user_colors) == 2 and all(color in correct_colors for color in user_colors):
                        print(f"{Colors.OKGREEN}✅ Beautiful {theme_name} palette! Perfect color harmony!{Colors.ENDC}")
                        score += 140
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Not quite the right harmony for {theme_name}!{Colors.ENDC}")
                        streak = 0
                        
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid input format!{Colors.ENDC}")
                    streak = 0
            
            total_questions += 1
            max_streak = max(max_streak, streak)
            
            # Streak bonus
            if streak >= 3:
                bonus = streak * 35
                score += bonus
                print(f"{Colors.YELLOW}🔥 Artistic Streak: +{bonus} points!{Colors.ENDC}")
            
            time.sleep(2.5)
            level += 1
        
        self.complete_game('art_creator', game_name, score, correct_answers, total_questions, max_streak)
    
    # ==================== GAME 7: MUSIC MAESTRO ====================
    def music_maestro_game(self):
        """Music Maestro - Rhythm and Pattern Games"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.music_maestro', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - Rhythm & Pattern Games{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}🎵 Feel the rhythm and create musical patterns!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}🎼 Challenge your musical memory and timing!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start Music Challenge{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_music_maestro()
    
    def run_music_maestro(self):
        """Run rhythm and musical pattern challenges"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        # Musical notes and patterns
        notes = ['🎵', '🎶', '♪', '♫', '🎼']
        rhythm_symbols = ['👏', '🥁', '🎺', '🎸', '🎹']
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}🎵 MUSIC MAESTRO - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            if level <= 4:
                # Rhythm pattern repetition
                pattern_length = min(3 + level // 2, 6)
                rhythm_pattern = [random.choice(rhythm_symbols) for _ in range(pattern_length)]
                
                print(f"\n{Colors.OKGREEN}🥁 RHYTHM PATTERN CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Memorize and repeat this rhythm pattern:{Colors.ENDC}")
                
                # Display pattern
                pattern_str = ' '.join(rhythm_pattern)
                print(f"\n{Colors.YELLOW}{pattern_str}{Colors.ENDC}")
                
                input(f"\n{Colors.BOLD}Press Enter when ready to repeat...{Colors.ENDC}")
                
                self.clear_screen()
                print(f"\n{Colors.HEADER}{Colors.BOLD}🎵 MUSIC MAESTRO - LEVEL {level}{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Now repeat the rhythm pattern:{Colors.ENDC}")
                
                # Show available symbols
                print(f"\n{Colors.OKCYAN}Available symbols:{Colors.ENDC}")
                for i, symbol in enumerate(rhythm_symbols, 1):
                    print(f"{Colors.OKGREEN}{i}. {symbol}{Colors.ENDC}")
                
                print(f"\n{Colors.OKCYAN}Enter the pattern (e.g., '1,2,3' for {rhythm_symbols[0]} {rhythm_symbols[1]} {rhythm_symbols[2]}):{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_input = input(f"{Colors.BOLD}Pattern (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Music Maestro", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_indices = [int(x.strip()) - 1 for x in user_input.split(',')]
                    user_pattern = [rhythm_symbols[i] for i in user_indices if 0 <= i < len(rhythm_symbols)]
                    
                    if user_pattern == rhythm_pattern:
                        print(f"{Colors.OKGREEN}✅ Perfect rhythm! You nailed the pattern!{Colors.ENDC}")
                        score += 100
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Not quite right!{Colors.ENDC}")
                        print(f"{Colors.OKCYAN}Correct pattern was: {' '.join(rhythm_pattern)}{Colors.ENDC}")
                        streak = 0
                        
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid input format!{Colors.ENDC}")
                    streak = 0
                    
            elif level <= 7:
                # Musical scale completion
                scales = {
                    'C Major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                    'G Major': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
                    'F Major': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
                }
                
                scale_name = random.choice(list(scales.keys()))
                scale_notes = scales[scale_name]
                
                # Remove 2 notes for user to complete
                missing_indices = random.sample(range(len(scale_notes)), 2)
                display_scale = scale_notes.copy()
                
                for idx in missing_indices:
                    display_scale[idx] = '?'
                
                print(f"\n{Colors.OKGREEN}🎼 MUSICAL SCALE CHALLENGE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Complete the {scale_name} scale:{Colors.ENDC}")
                
                scale_display = ' - '.join(display_scale)
                print(f"\n{Colors.YELLOW}{scale_display}{Colors.ENDC}")
                
                missing_notes = [scale_notes[i] for i in missing_indices]
                
                print(f"\n{Colors.OKCYAN}What are the missing notes? (in order, e.g., 'C,E'):{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_input = input(f"{Colors.BOLD}Missing notes (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Music Maestro", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_notes = [note.strip() for note in user_input.split(',')]
                    
                    if user_notes == missing_notes:
                        print(f"{Colors.OKGREEN}✅ Excellent! You completed the {scale_name} scale!{Colors.ENDC}")
                        score += 130
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Not quite right!{Colors.ENDC}")
                        print(f"{Colors.OKCYAN}Missing notes were: {', '.join(missing_notes)}{Colors.ENDC}")
                        streak = 0
                        
                except:
                    print(f"{Colors.FAIL}❌ Invalid input format!{Colors.ENDC}")
                    streak = 0
                    
            else:
                # Chord identification
                chords = {
                    'C Major': ['C', 'E', 'G'],
                    'D Minor': ['D', 'F', 'A'],
                    'G Major': ['G', 'B', 'D'],
                    'A Minor': ['A', 'C', 'E'],
                    'F Major': ['F', 'A', 'C']
                }
                
                chord_name = random.choice(list(chords.keys()))
                chord_notes = chords[chord_name]
                
                print(f"\n{Colors.OKGREEN}🎹 CHORD IDENTIFICATION{Colors.ENDC}")
                print(f"{Colors.OKCYAN}What chord is formed by these notes?{Colors.ENDC}")
                
                notes_display = ' + '.join(chord_notes)
                print(f"\n{Colors.YELLOW}{notes_display}{Colors.ENDC}")
                
                # Create options
                options = [chord_name]
                other_chords = [name for name in chords.keys() if name != chord_name]
                options.extend(random.sample(other_chords, 3))
                random.shuffle(options)
                
                for i, option in enumerate(options, 1):
                    print(f"{Colors.OKGREEN}{i}. {option}{Colors.ENDC}")
                
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-4): {Colors.ENDC}").strip()
                
                try:
                    choice_idx = int(user_choice) - 1
                    if 0 <= choice_idx < len(options) and options[choice_idx] == chord_name:
                        print(f"{Colors.OKGREEN}✅ Bravo! That's a {chord_name} chord!{Colors.ENDC}")
                        score += 150
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! That was a {chord_name} chord!{Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
            
            total_questions += 1
            max_streak = max(max_streak, streak)
            
            # Streak bonus
            if streak >= 3:
                bonus = streak * 40
                score += bonus
                print(f"{Colors.YELLOW}🔥 Musical Streak: +{bonus} points!{Colors.ENDC}")
            
            time.sleep(2.5)
            level += 1
        
        self.complete_game('music_maestro', game_name, score, correct_answers, total_questions, max_streak)
    
    # ==================== GAME 8: CODE NINJA ====================
    def code_ninja_game(self):
        """Code Ninja - Programming Logic Puzzles"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.code_ninja', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - Programming Logic Puzzles{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}💻 Solve coding challenges and debug programs!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}🐛 Master algorithms and logical thinking!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start Coding Challenge{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_code_ninja()
    
    def run_code_ninja(self):
        """Run programming logic challenges"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}💻 CODE NINJA - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            if level <= 3:
                # Basic algorithm tracing
                numbers = [random.randint(1, 20) for _ in range(4)]
                
                print(f"\n{Colors.OKGREEN}🔍 ALGORITHM TRACING{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Trace through this simple algorithm:{Colors.ENDC}")
                print(f"\n{Colors.YELLOW}numbers = {numbers}{Colors.ENDC}")
                print(f"{Colors.YELLOW}result = 0{Colors.ENDC}")
                print(f"{Colors.YELLOW}for num in numbers:{Colors.ENDC}")
                print(f"{Colors.YELLOW}    result = result + num{Colors.ENDC}")
                print(f"{Colors.YELLOW}print(result){Colors.ENDC}")
                
                correct_result = sum(numbers)
                
                print(f"\n{Colors.OKCYAN}What will this program output?{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_input = input(f"{Colors.BOLD}Output (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Code Ninja", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_result = int(user_input)
                    if user_result == correct_result:
                        print(f"{Colors.OKGREEN}✅ Correct! The sum is {correct_result}!{Colors.ENDC}")
                        score += 100
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! The output is {correct_result}!{Colors.ENDC}")
                        streak = 0
                except ValueError:
                    print(f"{Colors.FAIL}❌ Invalid input! The output is {correct_result}!{Colors.ENDC}")
                    streak = 0
                    
            elif level <= 6:
                # Loop and condition logic
                start = random.randint(1, 5)
                end = start + random.randint(3, 7)
                
                print(f"\n{Colors.OKGREEN}🔄 LOOP LOGIC{Colors.ENDC}")
                print(f"{Colors.OKCYAN}What will this loop print?{Colors.ENDC}")
                print(f"\n{Colors.YELLOW}for i in range({start}, {end}):{Colors.ENDC}")
                print(f"{Colors.YELLOW}    if i % 2 == 0:{Colors.ENDC}")
                print(f"{Colors.YELLOW}        print(i){Colors.ENDC}")
                
                # Calculate correct output
                correct_output = [str(i) for i in range(start, end) if i % 2 == 0]
                
                print(f"\n{Colors.OKCYAN}Enter the numbers that will be printed (comma-separated):{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_input = input(f"{Colors.BOLD}Numbers (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Code Ninja", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_output = [x.strip() for x in user_input.split(',') if x.strip()]
                    if user_output == correct_output:
                        print(f"{Colors.OKGREEN}✅ Perfect! You traced the loop correctly!{Colors.ENDC}")
                        score += 120
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! The output is: {', '.join(correct_output)}{Colors.ENDC}")
                        streak = 0
                except:
                    print(f"{Colors.FAIL}❌ Invalid format! The output is: {', '.join(correct_output)}{Colors.ENDC}")
                    streak = 0
                    
            else:
                # Bug finding
                bugs = [
                    {
                        'code': [
                            "def find_max(numbers):",
                            "    max_num = 0",  # Bug: should be numbers[0] or -infinity
                            "    for num in numbers:",
                            "        if num > max_num:",
                            "            max_num = num",
                            "    return max_num"
                        ],
                        'bug_line': 1,
                        'explanation': "max_num should be initialized to numbers[0] or negative infinity"
                    },
                    {
                        'code': [
                            "def count_vowels(text):",
                            "    vowels = 'aeiou'",
                            "    count = 0",
                            "    for char in text:",
                            "        if char in vowels:",  # Bug: should handle uppercase
                            "            count += 1",
                            "    return count"
                        ],
                        'bug_line': 4,
                        'explanation': "Should check char.lower() to handle uppercase vowels"
                    }
                ]
                
                bug_example = random.choice(bugs)
                
                print(f"\n{Colors.OKGREEN}🐛 BUG HUNTING{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Find the bug in this code:{Colors.ENDC}")
                
                for i, line in enumerate(bug_example['code']):
                    print(f"{Colors.YELLOW}{i+1:2d}: {line}{Colors.ENDC}")
                
                print(f"\n{Colors.OKCYAN}Which line contains the bug? (Enter line number):{Colors.ENDC}")
                user_input = input(f"{Colors.BOLD}Line number: {Colors.ENDC}").strip()
                
                try:
                    user_line = int(user_input) - 1
                    if user_line == bug_example['bug_line']:
                        print(f"{Colors.OKGREEN}✅ Great debugging! You found the bug!{Colors.ENDC}")
                        print(f"{Colors.OKCYAN}Explanation: {bug_example['explanation']}{Colors.ENDC}")
                        score += 150
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Not quite! The bug is on line {bug_example['bug_line'] + 1}{Colors.ENDC}")
                        print(f"{Colors.OKCYAN}Explanation: {bug_example['explanation']}{Colors.ENDC}")
                        streak = 0
                except ValueError:
                    print(f"{Colors.FAIL}❌ Invalid input! The bug is on line {bug_example['bug_line'] + 1}{Colors.ENDC}")
                    streak = 0
            
            total_questions += 1
            max_streak = max(max_streak, streak)
            
            # Streak bonus
            if streak >= 3:
                bonus = streak * 45
                score += bonus
                print(f"{Colors.YELLOW}🔥 Coding Streak: +{bonus} points!{Colors.ENDC}")
            
            time.sleep(2.5)
            level += 1
        
        self.complete_game('code_ninja', game_name, score, correct_answers, total_questions, max_streak)
    
    # ==================== GAME 9: LOGIC PUZZLE ====================
    def logic_puzzle_game(self):
        """Logic Puzzle - Pattern Recognition and Deduction"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.logic_puzzle', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - Pattern Recognition{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}🧩 Solve logical puzzles and recognize patterns!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}🔍 Challenge your deductive reasoning skills!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start Logic Challenge{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_logic_puzzle()
    
    def run_logic_puzzle(self):
        """Run pattern recognition and logic challenges"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}🧩 LOGIC PUZZLE - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            if level <= 3:
                # Number sequence patterns
                patterns = [
                    {'sequence': [2, 4, 6, 8], 'next': 10, 'rule': 'add 2'},
                    {'sequence': [1, 3, 9, 27], 'next': 81, 'rule': 'multiply by 3'},
                    {'sequence': [1, 4, 7, 10], 'next': 13, 'rule': 'add 3'},
                    {'sequence': [2, 6, 18, 54], 'next': 162, 'rule': 'multiply by 3'},
                    {'sequence': [1, 1, 2, 3, 5], 'next': 8, 'rule': 'Fibonacci'}
                ]
                
                pattern = random.choice(patterns)
                
                print(f"\n{Colors.OKGREEN}🔢 NUMBER SEQUENCE{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Find the pattern and next number:{Colors.ENDC}")
                
                sequence_str = ', '.join(map(str, pattern['sequence']))
                print(f"\n{Colors.YELLOW}{sequence_str}, ?{Colors.ENDC}")
                
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_input = input(f"\n{Colors.BOLD}Next number (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Logic Puzzle", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_number = int(user_input)
                    if user_number == pattern['next']:
                        print(f"{Colors.OKGREEN}✅ Correct! The pattern is: {pattern['rule']}!{Colors.ENDC}")
                        score += 100
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! The next number is {pattern['next']} ({pattern['rule']}){Colors.ENDC}")
                        streak = 0
                except ValueError:
                    print(f"{Colors.FAIL}❌ Invalid input! The next number is {pattern['next']}{Colors.ENDC}")
                    streak = 0
                    
            elif level <= 6:
                # Shape pattern logic
                shapes = ['○', '□', '△', '◇', '★']
                
                # Create a simple pattern
                base_shape = random.choice(shapes)
                pattern_length = 3
                
                if level <= 4:
                    # Simple alternating pattern
                    other_shape = random.choice([s for s in shapes if s != base_shape])
                    pattern_sequence = [base_shape, other_shape] * pattern_length
                    next_shape = base_shape
                else:
                    # Three-shape rotation
                    shape_set = random.sample(shapes, 3)
                    pattern_sequence = shape_set * 2
                    next_shape = shape_set[0]
                
                print(f"\n{Colors.OKGREEN}🔷 SHAPE PATTERN{Colors.ENDC}")
                print(f"{Colors.OKCYAN}What comes next in this pattern?{Colors.ENDC}")
                
                pattern_str = ' '.join(pattern_sequence)
                print(f"\n{Colors.YELLOW}{pattern_str} ?{Colors.ENDC}")
                
                # Show options
                options = [next_shape]
                options.extend(random.sample([s for s in shapes if s != next_shape], 3))
                random.shuffle(options)
                
                for i, shape in enumerate(options, 1):
                    print(f"{Colors.OKGREEN}{i}. {shape}{Colors.ENDC}")
                
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-4, 'exit', 'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_choice, "Logic Puzzle", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_choice.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    choice_idx = int(user_choice) - 1
                    if 0 <= choice_idx < len(options) and options[choice_idx] == next_shape:
                        print(f"{Colors.OKGREEN}✅ Perfect pattern recognition!{Colors.ENDC}")
                        score += 120
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Incorrect! The next shape is {next_shape}{Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
                    
            else:
                # Logic grid puzzles
                print(f"\n{Colors.OKGREEN}🎯 LOGIC DEDUCTION{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Solve this logic puzzle:{Colors.ENDC}")
                
                # Simple logic puzzle
                people = ['Alice', 'Bob', 'Carol']
                colors = ['Red', 'Blue', 'Green']
                
                # Create a simple scenario
                person = random.choice(people)
                color = random.choice(colors)
                
                other_people = [p for p in people if p != person]
                other_colors = [c for c in colors if c != color]
                
                print(f"\n{Colors.YELLOW}Three people (Alice, Bob, Carol) each like a different color (Red, Blue, Green).{Colors.ENDC}")
                print(f"{Colors.YELLOW}Clues:{Colors.ENDC}")
                print(f"{Colors.YELLOW}1. {person} likes {color}{Colors.ENDC}")
                print(f"{Colors.YELLOW}2. {other_people[0]} does not like {other_colors[0]}{Colors.ENDC}")
                
                # Determine the solution
                remaining_person = other_people[1]
                remaining_color = other_colors[1] if other_people[0] != remaining_person else other_colors[0]
                
                print(f"\n{Colors.OKCYAN}What color does {remaining_person} like?{Colors.ENDC}")
                
                for i, c in enumerate(colors, 1):
                    print(f"{Colors.OKGREEN}{i}. {c}{Colors.ENDC}")
                
                user_choice = input(f"\n{Colors.BOLD}Your choice (1-3): {Colors.ENDC}").strip()
                
                try:
                    choice_idx = int(user_choice) - 1
                    if 0 <= choice_idx < len(colors):
                        user_color = colors[choice_idx]
                        
                        # Check logic
                        if user_color != color and user_color != other_colors[0]:
                            print(f"{Colors.OKGREEN}✅ Excellent deduction! {remaining_person} likes {user_color}!{Colors.ENDC}")
                            score += 150
                            correct_answers += 1
                            streak += 1
                        else:
                            print(f"{Colors.FAIL}❌ Incorrect! Check the clues again.{Colors.ENDC}")
                            streak = 0
                    else:
                        print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                        streak = 0
                except (ValueError, IndexError):
                    print(f"{Colors.FAIL}❌ Invalid choice!{Colors.ENDC}")
                    streak = 0
            
            total_questions += 1
            max_streak = max(max_streak, streak)
            
            # Streak bonus
            if streak >= 3:
                bonus = streak * 40
                score += bonus
                print(f"{Colors.YELLOW}🔥 Logic Streak: +{bonus} points!{Colors.ENDC}")
            
            time.sleep(2.5)
            level += 1
        
        self.complete_game('logic_puzzle', game_name, score, correct_answers, total_questions, max_streak)
    
    # ==================== GAME 10: MEMORY PALACE ====================
    def memory_palace_game(self):
        """Memory Palace - Sequence and Spatial Memory"""
        self.clear_screen()
        self.print_banner()
        
        game_name = EduVerseTranslations.get('games.memory_palace', self.current_language)
        print(f"\n{Colors.HEADER}{Colors.BOLD}{game_name} - Sequence & Spatial Memory{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}🌟 Train your memory with sequences and spatial patterns!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}🧠 Build your mental palace and enhance recall!{Colors.ENDC}")
        
        print(f"\n{Colors.OKGREEN}1. Start Memory Training{Colors.ENDC}")
        print(f"{Colors.WARNING}2. Return to Main Menu{Colors.ENDC}")
        
        choice = input(f"\n{Colors.BOLD}Choice (1-2): {Colors.ENDC}").strip()
        
        if choice == '1':
            self.run_memory_palace()
    
    def run_memory_palace(self):
        """Run memory training challenges"""
        score = 0
        level = 1
        correct_answers = 0
        total_questions = 0
        streak = 0
        max_streak = 0
        
        while level <= 10:
            self.clear_screen()
            print(f"\n{Colors.HEADER}{Colors.BOLD}🌟 MEMORY PALACE - LEVEL {level}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Score: {score} | Streak: {streak} | Level: {level}/10{Colors.ENDC}")
            
            if level <= 4:
                # Number sequence memory
                sequence_length = min(3 + level, 8)
                number_sequence = [random.randint(1, 9) for _ in range(sequence_length)]
                
                print(f"\n{Colors.OKGREEN}🔢 NUMBER SEQUENCE MEMORY{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Memorize this sequence of numbers:{Colors.ENDC}")
                
                sequence_str = ' '.join(map(str, number_sequence))
                print(f"\n{Colors.YELLOW}{sequence_str}{Colors.ENDC}")
                
                # Display time based on difficulty
                display_time = max(2, 5 - level // 2)
                for i in range(display_time, 0, -1):
                    print(f"\r{Colors.WARNING}Memorizing... {i} seconds left{Colors.ENDC}", end='', flush=True)
                    time.sleep(1)
                
                self.clear_screen()
                print(f"\n{Colors.HEADER}{Colors.BOLD}🌟 MEMORY PALACE - LEVEL {level}{Colors.ENDC}")
                print(f"\n{Colors.OKCYAN}Now enter the sequence you memorized:{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                
                user_input = input(f"{Colors.BOLD}Sequence (space-separated, or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Memory Palace", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_sequence = [int(x) for x in user_input.split()]
                    if user_sequence == number_sequence:
                        print(f"{Colors.OKGREEN}✅ Perfect memory! You got it exactly right!{Colors.ENDC}")
                        score += 100 + (sequence_length * 10)
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Not quite right!{Colors.ENDC}")
                        print(f"{Colors.OKCYAN}Correct sequence was: {' '.join(map(str, number_sequence))}{Colors.ENDC}")
                        streak = 0
                except ValueError:
                    print(f"{Colors.FAIL}❌ Invalid format!{Colors.ENDC}")
                    streak = 0
                    
            elif level <= 7:
                # Color pattern memory
                colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW, Colors.PURPLE, Colors.CYAN]
                color_names = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'PURPLE', 'CYAN']
                
                pattern_length = min(4 + (level - 4), 7)
                color_pattern = random.choices(list(zip(colors, color_names)), k=pattern_length)
                
                print(f"\n{Colors.OKGREEN}🌈 COLOR PATTERN MEMORY{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Memorize this color sequence:{Colors.ENDC}")
                
                print(f"\n", end='')
                for color, name in color_pattern:
                    print(f"{color}██{Colors.ENDC} ", end='')
                print()
                
                display_time = max(3, 6 - level // 3)
                for i in range(display_time, 0, -1):
                    print(f"\r{Colors.WARNING}Memorizing... {i} seconds left{Colors.ENDC}", end='', flush=True)
                    time.sleep(1)
                
                self.clear_screen()
                print(f"\n{Colors.HEADER}{Colors.BOLD}🌟 MEMORY PALACE - LEVEL {level}{Colors.ENDC}")
                print(f"\n{Colors.OKCYAN}Enter the color sequence (e.g., 'RED,BLUE,GREEN'):{Colors.ENDC}")
                print(f"{Colors.WARNING}Commands: 'exit' (main menu) | 'nav' (game menu){Colors.ENDC}")
                
                user_input = input(f"{Colors.BOLD}Colors (or 'exit'/'nav'): {Colors.ENDC}").strip()
                
                # Handle navigation commands
                nav_result = self.handle_game_navigation(user_input, "Memory Palace", level, score)
                if nav_result == 'main_menu':
                    return
                elif nav_result == 'switched':
                    return
                elif nav_result == 'continue':
                    continue
                
                # Handle exit command
                if user_input.lower() == 'exit':
                    print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
                    time.sleep(1)
                    return
                
                try:
                    user_colors = [c.strip() for c in user_input.upper().split(',')]
                    correct_colors = [name for _, name in color_pattern]
                    
                    if user_colors == correct_colors:
                        print(f"{Colors.OKGREEN}✅ Brilliant color memory!{Colors.ENDC}")
                        score += 120 + (pattern_length * 15)
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Not quite right!{Colors.ENDC}")
                        print(f"{Colors.OKCYAN}Correct sequence was: {', '.join(correct_colors)}{Colors.ENDC}")
                        streak = 0
                except:
                    print(f"{Colors.FAIL}❌ Invalid format!{Colors.ENDC}")
                    streak = 0
                    
            else:
                # Spatial memory grid
                grid_size = 4
                num_positions = min(3 + (level - 7), 6)
                
                # Generate random positions
                positions = random.sample([(i, j) for i in range(grid_size) for j in range(grid_size)], num_positions)
                
                print(f"\n{Colors.OKGREEN}🗺️ SPATIAL MEMORY GRID{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Memorize the positions of the stars:{Colors.ENDC}")
                
                # Display grid with stars
                print()
                for i in range(grid_size):
                    for j in range(grid_size):
                        if (i, j) in positions:
                            print(f"{Colors.YELLOW}★{Colors.ENDC} ", end='')
                        else:
                            print(f"{Colors.CYAN}·{Colors.ENDC} ", end='')
                    print()
                
                display_time = max(4, 8 - level // 2)
                for i in range(display_time, 0, -1):
                    print(f"\r{Colors.WARNING}Memorizing... {i} seconds left{Colors.ENDC}", end='', flush=True)
                    time.sleep(1)
                
                self.clear_screen()
                print(f"\n{Colors.HEADER}{Colors.BOLD}🌟 MEMORY PALACE - LEVEL {level}{Colors.ENDC}")
                print(f"\n{Colors.OKCYAN}Now mark where the stars were:{Colors.ENDC}")
                
                # Display empty grid with coordinates
                print(f"\n{Colors.OKCYAN}Grid coordinates (row,col):{Colors.ENDC}")
                print("  0 1 2 3")
                for i in range(grid_size):
                    print(f"{i} ", end='')
                    for j in range(grid_size):
                        print(f"{Colors.CYAN}·{Colors.ENDC} ", end='')
                    print()
                
                print(f"\n{Colors.OKCYAN}Enter star positions (e.g., '0,1 2,3 1,0'):{Colors.ENDC}")
                user_input = input(f"{Colors.BOLD}Positions: {Colors.ENDC}").strip()
                
                try:
                    user_positions = []
                    for pos_str in user_input.split():
                        row, col = map(int, pos_str.split(','))
                        user_positions.append((row, col))
                    
                    if set(user_positions) == set(positions):
                        print(f"{Colors.OKGREEN}✅ Amazing spatial memory! Perfect recall!{Colors.ENDC}")
                        score += 150 + (num_positions * 20)
                        correct_answers += 1
                        streak += 1
                    else:
                        print(f"{Colors.FAIL}❌ Not quite right!{Colors.ENDC}")
                        print(f"{Colors.OKCYAN}Correct positions were: {positions}{Colors.ENDC}")
                        streak = 0
                except:
                    print(f"{Colors.FAIL}❌ Invalid format!{Colors.ENDC}")
                    streak = 0
            
            total_questions += 1
            max_streak = max(max_streak, streak)
            
            # Streak bonus
            if streak >= 3:
                bonus = streak * 50
                score += bonus
                print(f"{Colors.YELLOW}🔥 Memory Streak: +{bonus} points!{Colors.ENDC}")
            
            time.sleep(2.5)
            level += 1
        
        self.complete_game('memory_palace', game_name, score, correct_answers, total_questions, max_streak)
    
    # ==================== GAME COMPLETION ====================
    def show_game_navigation_menu(self, current_game_name, level, score):
        """Show in-game navigation menu"""
        print(f"\n{Colors.HEADER}🎮 GAME NAVIGATION MENU 🎮{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Current Game: {current_game_name}{Colors.ENDC}")
        print(f"{Colors.YELLOW}Progress: Level {level}, Score: {score}{Colors.ENDC}")
        
        print(f"\n{Colors.HEADER}Quick Game Switch:{Colors.ENDC}")
        print(f"{Colors.OKGREEN}1. 🧮 Math Wizard{Colors.ENDC}")
        print(f"{Colors.OKGREEN}2. 🔤 Word Master{Colors.ENDC}")
        print(f"{Colors.OKGREEN}3. 🧪 Science Lab{Colors.ENDC}")
        print(f"{Colors.OKGREEN}4. 🌍 Geography Quest{Colors.ENDC}")
        print(f"{Colors.OKGREEN}5. 📚 History Hunter{Colors.ENDC}")
        print(f"{Colors.OKGREEN}6. 🎨 Art Creator{Colors.ENDC}")
        print(f"{Colors.OKGREEN}7. 🎵 Music Maestro{Colors.ENDC}")
        print(f"{Colors.OKGREEN}8. 💻 Code Ninja{Colors.ENDC}")
        print(f"{Colors.OKGREEN}9. 🧩 Logic Puzzle{Colors.ENDC}")
        print(f"{Colors.OKGREEN}10. 🌟 Memory Palace{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}11. Continue Current Game{Colors.ENDC}")
        print(f"{Colors.WARNING}12. Return to Main Menu{Colors.ENDC}")
        print(f"{Colors.FAIL}13. Quit EduVerse{Colors.ENDC}")
        
        while True:
            try:
                choice = input(f"\n{Colors.BOLD}Choice (1-13): {Colors.ENDC}").strip()
                if choice.isdigit() and 1 <= int(choice) <= 13:
                    return int(choice)
                else:
                    print(f"{Colors.FAIL}Invalid choice! Please select 1-13.{Colors.ENDC}")
            except KeyboardInterrupt:
                return 12  # Return to main menu on Ctrl+C
    
    def handle_game_navigation(self, user_input, current_game_name, level, score):
        """Handle navigation commands during gameplay"""
        if user_input.lower() == 'nav' or user_input.lower() == 'menu':
            choice = self.show_game_navigation_menu(current_game_name, level, score)
            
            if choice == 11:  # Continue current game
                return 'continue'
            elif choice == 12:  # Return to main menu
                return 'main_menu'
            elif choice == 13:  # Quit
                self.quit_game()
            elif 1 <= choice <= 10:  # Switch to another game
                print(f"\n{Colors.OKCYAN}Switching to game {choice}...{Colors.ENDC}")
                print(f"{Colors.YELLOW}Saving progress: {current_game_name} - Level {level}, Score: {score}{Colors.ENDC}")
                time.sleep(1)
                self.play_game(choice)
                return 'switched'
        
        return 'normal'  # Normal input processing
    
    def handle_game_exit(self, level, score):
        """Handle exit from game with current progress display"""
        print(f"\n{Colors.OKCYAN}Returning to main menu...{Colors.ENDC}")
        print(f"{Colors.YELLOW}Current progress: Level {level}, Score: {score}{Colors.ENDC}")
        time.sleep(1)
        return True  # Indicates game should exit
    
    def get_game_input_with_exit(self, prompt, level, score):
        """Get user input with exit handling"""
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            self.handle_game_exit(level, score)
            return None  # Indicates exit was requested
        return user_input
    
    def complete_game(self, game_key, game_name, score, correct_answers, total_questions, max_streak):
        """Complete game and update stats"""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Colors.HEADER}{Colors.BOLD}🎮 GAME COMPLETE! 🎮{Colors.ENDC}")
        print(f"\n{Colors.OKGREEN}Game: {game_name}{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Final Score: {score:,} points{Colors.ENDC}")
        print(f"{Colors.YELLOW}Correct Answers: {correct_answers}/{total_questions}{Colors.ENDC}")
        
        if total_questions > 0:
            accuracy = (correct_answers / total_questions) * 100
            print(f"{Colors.PURPLE}Accuracy: {accuracy:.1f}%{Colors.ENDC}")
        
        print(f"{Colors.CYAN}Max Streak: {max_streak}{Colors.ENDC}")
        
        # Update player stats
        if self.player_stats:
            self.player_stats.total_score += score
            self.player_stats.games_played += 1
            self.player_stats.correct_answers += correct_answers
            self.player_stats.total_questions += total_questions
            
            # Update high score for this game
            if game_key not in self.player_stats.game_high_scores or score > self.player_stats.game_high_scores[game_key]:
                self.player_stats.game_high_scores[game_key] = score
                print(f"\n{Colors.YELLOW}🏆 NEW HIGH SCORE for {game_name}!{Colors.ENDC}")
            
            # Check for achievements
            self.check_achievements(game_key, score, accuracy if total_questions > 0 else 0, max_streak)
            
            self.save_player_data()
        
        # Performance feedback
        if total_questions > 0:
            if accuracy >= 90:
                print(f"\n{Colors.OKGREEN}🌟 EXCELLENT PERFORMANCE! 🌟{Colors.ENDC}")
            elif accuracy >= 75:
                print(f"\n{Colors.OKCYAN}👍 GREAT JOB! 👍{Colors.ENDC}")
            elif accuracy >= 60:
                print(f"\n{Colors.YELLOW}📈 GOOD EFFORT! 📈{Colors.ENDC}")
            else:
                print(f"\n{Colors.WARNING}💪 KEEP PRACTICING! 💪{Colors.ENDC}")
        
        # Improved post-game options
        print(f"\n{Colors.HEADER}What would you like to do next?{Colors.ENDC}")
        print(f"{Colors.OKGREEN}1. Play this game again{Colors.ENDC}")
        print(f"{Colors.OKCYAN}2. Return to Main Menu{Colors.ENDC}")
        print(f"{Colors.WARNING}3. View Statistics{Colors.ENDC}")
        print(f"{Colors.FAIL}4. Quit EduVerse{Colors.ENDC}")
        
        while True:
            try:
                choice = input(f"\n{Colors.BOLD}Choice (1-4): {Colors.ENDC}").strip()
                if choice == '1':
                    self.play_game(self.get_game_number_by_key(game_key))
                    break
                elif choice == '2':
                    return  # Return to main menu
                elif choice == '3':
                    self.view_statistics()
                    return  # Return to main menu after viewing stats
                elif choice == '4':
                    self.quit_game()
                else:
                    print(f"{Colors.FAIL}Invalid choice! Please select 1-4.{Colors.ENDC}")
            except KeyboardInterrupt:
                return  # Return to main menu on Ctrl+C
    
    def get_game_number_by_key(self, game_key):
        """Get game number from game key"""
        game_keys = ['math_wizard', 'word_master', 'science_lab', 'geography_quest', 
                    'history_hunter', 'art_creator', 'music_maestro', 'code_ninja', 
                    'logic_puzzle', 'memory_palace']
        try:
            return game_keys.index(game_key) + 1
        except ValueError:
            return 1
    
    def check_achievements(self, game_key, score, accuracy, max_streak):
        """Check and award achievements"""
        if not self.player_stats:
            return
        
        achievements = []
        
        # Score-based achievements
        if score >= 1000:
            achievements.append("🏆 High Scorer - Scored 1000+ points in a game")
        if score >= 1500:
            achievements.append("💎 Master Player - Scored 1500+ points in a game")
        
        # Accuracy achievements
        if accuracy >= 90:
            achievements.append("🎯 Sharpshooter - 90%+ accuracy in a game")
        if accuracy == 100:
            achievements.append("🌟 Perfect Game - 100% accuracy")
        
        # Streak achievements
        if max_streak >= 5:
            achievements.append("🔥 Streak Master - 5+ answer streak")
        if max_streak >= 10:
            achievements.append("⚡ Lightning Round - 10+ answer streak")
        
        # Game-specific achievements
        game_achievements = {
            'math_wizard': "🧮 Math Genius - Completed Math Wizard",
            'word_master': "📝 Word Wizard - Completed Word Master",
            'science_lab': "🧪 Mad Scientist - Completed Science Lab",
            'geography_quest': "🌍 World Explorer - Completed Geography Quest",
            'history_hunter': "📚 Time Traveler - Completed History Hunter",
            'art_creator': "🎨 Creative Genius - Completed Art Creator",
            'music_maestro': "🎵 Music Master - Completed Music Maestro",
            'code_ninja': "💻 Code Warrior - Completed Code Ninja",
            'logic_puzzle': "🧩 Logic Master - Completed Logic Puzzle",
            'memory_palace': "🧠 Memory Champion - Completed Memory Palace"
        }
        
        if game_key in game_achievements:
            achievements.append(game_achievements[game_key])
        
        # Total games achievement
        if self.player_stats.games_played >= 10:
            achievements.append("🎮 Game Veteran - Played 10+ games")
        if self.player_stats.games_played >= 25:
            achievements.append("🏅 Game Master - Played 25+ games")
        
        # Add new achievements
        new_achievements = [ach for ach in achievements if ach not in self.player_stats.achievements]
        
        if new_achievements:
            print(f"\n{Colors.HEADER}🏆 NEW ACHIEVEMENTS UNLOCKED! 🏆{Colors.ENDC}")
            for achievement in new_achievements:
                print(f"{Colors.OKGREEN}✨ {achievement}{Colors.ENDC}")
                self.player_stats.achievements.append(achievement)
    
    def placeholder_game(self, game_number):
        """Placeholder for any missing games"""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Colors.WARNING}🚧 Game {game_number} is under construction! 🚧{Colors.ENDC}")
        print(f"{Colors.OKCYAN}This game will be available in a future update.{Colors.ENDC}")
        print(f"{Colors.OKGREEN}Try one of the other amazing games!{Colors.ENDC}")
        
        input(f"\n{EduVerseTranslations.get('press_enter', self.current_language)}")


# ==================== MAIN ENTRY POINT ====================
def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='EduVerse CLI: 10 Realms of Genius - Diverse Game Types')
    parser.add_argument('--version', action='version', version='EduVerse CLI 2.0.0')
    parser.add_argument('--lang', choices=['en', 'ta'], help='Set default language')
    
    args = parser.parse_args()
    
    try:
        game = EduVerseCLI()
        if args.lang:
            game.current_language = args.lang
        game.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Thanks for playing EduVerse CLI!{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.FAIL}An unexpected error occurred: {e}{Colors.ENDC}")
        sys.exit(1)


if __name__ == "__main__":
    main()
