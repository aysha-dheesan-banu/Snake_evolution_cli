#!/usr/bin/env python3
"""
EcoQuest: Planet Protectors - Simplified Console Version
A text-based environmental education game
"""

import random
import json
import os
from datetime import datetime

class EcoQuestGame:
    def __init__(self):
        self.player_name = ""
        self.player_level = 1
        self.eco_points = 100
        self.ecosystem_health = {
            'forest': 75,
            'ocean': 60,
            'city': 45,
            'wildlife': 70
        }
        self.achievements = []
        self.virtual_pets = []
        self.current_mission = None
        
        self.missions = {
            "Forest Guardian": {
                "description": "Plant 50 virtual trees to restore the Amazon rainforest",
                "target": 50,
                "reward": 200,
                "difficulty": "Easy",
                "progress": 0
            },
            "Ocean Cleaner": {
                "description": "Remove plastic waste from ocean ecosystems",
                "target": 100,
                "reward": 300,
                "difficulty": "Medium",
                "progress": 0
            },
            "City Planner": {
                "description": "Design a sustainable city with renewable energy",
                "target": 1,
                "reward": 500,
                "difficulty": "Hard",
                "progress": 0
            },
            "Species Protector": {
                "description": "Save 10 endangered species from extinction",
                "target": 10,
                "reward": 400,
                "difficulty": "Medium",
                "progress": 0
            }
        }
        
        self.virtual_pets_available = [
            {"name": "Arctic Fox", "emoji": "🦊", "habitat": "Arctic", "status": "Vulnerable"},
            {"name": "Sea Turtle", "emoji": "🐢", "habitat": "Ocean", "status": "Endangered"},
            {"name": "Panda", "emoji": "🐼", "habitat": "Forest", "status": "Vulnerable"},
            {"name": "Polar Bear", "emoji": "🐻‍❄️", "habitat": "Arctic", "status": "Vulnerable"},
            {"name": "Whale", "emoji": "🐋", "habitat": "Ocean", "status": "Endangered"}
        ]

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_header(self):
        print("=" * 60)
        print("🌍 ECOQUEST: PLANET PROTECTORS 🌍")
        print("=" * 60)
        print(f"Player: {self.player_name} | Level: {self.player_level} | Eco Points: {self.eco_points}")
        print("-" * 60)

    def display_ecosystem_health(self):
        print("\n🌍 GLOBAL ECOSYSTEM HEALTH:")
        print("-" * 40)
        for ecosystem, health in self.ecosystem_health.items():
            bar = "█" * (health // 5) + "░" * (20 - health // 5)
            status = "🟢" if health >= 80 else "🟡" if health >= 50 else "🔴"
            print(f"{ecosystem.title():10} [{bar}] {health}% {status}")
        
        total_health = sum(self.ecosystem_health.values()) / len(self.ecosystem_health)
        print(f"\nOverall Planet Health: {total_health:.1f}%")

    def update_ecosystem_health(self, ecosystem_type, value):
        current_health = self.ecosystem_health[ecosystem_type]
        new_health = max(0, min(100, current_health + value))
        self.ecosystem_health[ecosystem_type] = new_health
        
        if value > 0:
            self.eco_points += value * 2
            print(f"✅ Great job! {ecosystem_type.title()} health improved by {value}%")
            print(f"💰 You earned {value * 2} Eco Points!")
        else:
            print(f"⚠️  {ecosystem_type.title()} health decreased by {abs(value)}%")

    def add_achievement(self, achievement_name):
        if achievement_name not in self.achievements:
            self.achievements.append(achievement_name)
            print(f"\n🏆 ACHIEVEMENT UNLOCKED: {achievement_name}! 🏆")
            self.eco_points += 100

    def adopt_virtual_pet(self, pet):
        if pet not in self.virtual_pets:
            self.virtual_pets.append(pet)
            print(f"\n🎉 You adopted a {pet['name']} {pet['emoji']}!")
            print(f"Status: {pet['status']} | Habitat: {pet['habitat']}")

    def dashboard_menu(self):
        while True:
            self.clear_screen()
            self.display_header()
            self.display_ecosystem_health()
            
            print("\n⚡ QUICK ACTIONS:")
            print("1. 🌳 Plant Tree (+5 Forest Health)")
            print("2. 🌊 Clean Ocean (+3 Ocean Health)")
            print("3. ♻️  Recycle (+4 City Health)")
            print("4. 🐾 Protect Wildlife (+6 Wildlife Health)")
            print("5. 📊 View Detailed Stats")
            print("6. 🔙 Back to Main Menu")
            
            choice = input("\nChoose an action (1-6): ").strip()
            
            if choice == '1':
                self.update_ecosystem_health("forest", 5)
                if self.ecosystem_health["forest"] > 90:
                    self.add_achievement("Forest Guardian")
                input("\nPress Enter to continue...")
                
            elif choice == '2':
                self.update_ecosystem_health("ocean", 3)
                if self.ecosystem_health["ocean"] > 85:
                    self.add_achievement("Ocean Protector")
                input("\nPress Enter to continue...")
                
            elif choice == '3':
                self.update_ecosystem_health("city", 4)
                self.eco_points += 10
                print("💰 Bonus: +10 Eco Points for recycling!")
                input("\nPress Enter to continue...")
                
            elif choice == '4':
                self.update_ecosystem_health("wildlife", 6)
                if len(self.virtual_pets) == 0:
                    pet = random.choice(self.virtual_pets_available)
                    self.adopt_virtual_pet(pet)
                input("\nPress Enter to continue...")
                
            elif choice == '5':
                self.show_detailed_stats()
                
            elif choice == '6':
                break
            else:
                print("❌ Invalid choice! Please try again.")
                input("Press Enter to continue...")

    def show_detailed_stats(self):
        self.clear_screen()
        self.display_header()
        
        print("\n📊 DETAILED PLAYER STATISTICS:")
        print("-" * 40)
        print(f"Player Level: {self.player_level}")
        print(f"Total Eco Points: {self.eco_points}")
        print(f"Achievements Earned: {len(self.achievements)}")
        print(f"Virtual Pets Adopted: {len(self.virtual_pets)}")
        
        if self.achievements:
            print("\n🏆 ACHIEVEMENTS:")
            for achievement in self.achievements:
                print(f"  🏅 {achievement}")
        
        if self.virtual_pets:
            print("\n🐾 VIRTUAL PETS:")
            for pet in self.virtual_pets:
                print(f"  {pet['emoji']} {pet['name']} ({pet['status']})")
        
        total_health = sum(self.ecosystem_health.values()) / len(self.ecosystem_health)
        if total_health >= 90:
            print("\n🌟 STATUS: Planet Protector Master!")
        elif total_health >= 70:
            print("\n🌱 STATUS: Eco Warrior")
        elif total_health >= 50:
            print("\n🌿 STATUS: Environmental Enthusiast")
        else:
            print("\n🌱 STATUS: Eco Beginner")
        
        input("\nPress Enter to continue...")

    def missions_menu(self):
        while True:
            self.clear_screen()
            self.display_header()
            
            print("\n🎯 ENVIRONMENTAL MISSIONS:")
            print("-" * 40)
            
            for i, (mission_name, mission_data) in enumerate(self.missions.items(), 1):
                status = "🎯 ACTIVE" if self.current_mission == mission_name else "📋 Available"
                progress = f"({mission_data['progress']}/{mission_data['target']})"
                print(f"{i}. {mission_name} - {mission_data['difficulty']} {status}")
                print(f"   {mission_data['description']}")
                print(f"   Progress: {progress} | Reward: {mission_data['reward']} points")
                print()
            
            print("5. 🔙 Back to Main Menu")
            
            choice = input("Choose a mission (1-5): ").strip()
            
            if choice in ['1', '2', '3', '4']:
                mission_names = list(self.missions.keys())
                selected_mission = mission_names[int(choice) - 1]
                self.play_mission(selected_mission)
            elif choice == '5':
                break
            else:
                print("❌ Invalid choice! Please try again.")
                input("Press Enter to continue...")

    def play_mission(self, mission_name):
        mission = self.missions[mission_name]
        self.current_mission = mission_name
        
        while mission['progress'] < mission['target']:
            self.clear_screen()
            self.display_header()
            
            print(f"\n🎯 ACTIVE MISSION: {mission_name}")
            print("-" * 40)
            print(f"Description: {mission['description']}")
            print(f"Difficulty: {mission['difficulty']}")
            print(f"Progress: {mission['progress']}/{mission['target']}")
            print(f"Reward: {mission['reward']} Eco Points")
            
            progress_bar = "█" * (mission['progress'] * 20 // mission['target']) + "░" * (20 - mission['progress'] * 20 // mission['target'])
            print(f"Progress: [{progress_bar}] {mission['progress'] * 100 // mission['target']}%")
            
            print("\n🎮 MISSION ACTIONS:")
            print("1. 🚀 Take Action (Advance Mission)")
            print("2. 💡 Get Hint")
            print("3. 🔙 Return to Missions Menu")
            
            choice = input("\nChoose an action (1-3): ").strip()
            
            if choice == '1':
                # Simulate mission progress
                progress_gain = random.randint(1, 5)
                mission['progress'] = min(mission['target'], mission['progress'] + progress_gain)
                
                print(f"\n✅ Great work! Mission progress: +{progress_gain}")
                
                if mission['progress'] >= mission['target']:
                    print(f"\n🎉 MISSION COMPLETED: {mission_name}!")
                    print(f"💰 You earned {mission['reward']} Eco Points!")
                    self.eco_points += mission['reward']
                    self.add_achievement(f"Mission: {mission_name}")
                    self.current_mission = None
                    input("Press Enter to continue...")
                    return
                else:
                    input("Press Enter to continue...")
                    
            elif choice == '2':
                hints = {
                    "Forest Guardian": "💡 Focus on reforestation efforts and protecting existing forests!",
                    "Ocean Cleaner": "💡 Target plastic pollution and promote marine conservation!",
                    "City Planner": "💡 Balance renewable energy, green spaces, and sustainable transport!",
                    "Species Protector": "💡 Create wildlife corridors and reduce human-wildlife conflict!"
                }
                print(f"\n{hints.get(mission_name, '💡 Keep working towards your environmental goals!')}")
                input("Press Enter to continue...")
                
            elif choice == '3':
                self.current_mission = None
                return
            else:
                print("❌ Invalid choice! Please try again.")
                input("Press Enter to continue...")

    def ar_challenges_menu(self):
        self.clear_screen()
        self.display_header()
        
        print("\n📸 AR ENVIRONMENTAL CHALLENGES:")
        print("-" * 40)
        print("🎯 Today's Challenges:")
        print("• 📸 Find and photograph a tree - 20 points")
        print("• 📸 Spot recyclable materials - 15 points")
        print("• 📸 Capture a water source - 25 points")
        print("• 📸 Find renewable energy - 30 points")
        print("• 📸 Photograph local wildlife - 35 points")
        
        print("\n🎮 SIMULATE AR CHALLENGE:")
        print("1. 🌳 Simulate Tree Photo")
        print("2. ♻️  Simulate Recycling Photo")
        print("3. 💧 Simulate Water Source Photo")
        print("4. ⚡ Simulate Renewable Energy Photo")
        print("5. 🐾 Simulate Wildlife Photo")
        print("6. 🔙 Back to Main Menu")
        
        choice = input("\nChoose a challenge (1-6): ").strip()
        
        challenges = {
            '1': ("Tree", 20, "🌳"),
            '2': ("Recyclable Materials", 15, "♻️"),
            '3': ("Water Source", 25, "💧"),
            '4': ("Renewable Energy", 30, "⚡"),
            '5': ("Wildlife", 35, "🐾")
        }
        
        if choice in challenges:
            item, points, emoji = challenges[choice]
            print(f"\n📸 *Click* - Photo taken of {item}!")
            print(f"🔍 AI Analysis: {item} detected! {emoji}")
            print(f"💰 You earned {points} Eco Points!")
            self.eco_points += points
            
            if self.eco_points >= 500:  # Arbitrary threshold for achievement
                self.add_achievement("Nature Photographer")
                
        elif choice == '6':
            return
        else:
            print("❌ Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")

    def city_builder_menu(self):
        self.clear_screen()
        self.display_header()
        
        print("\n🏙️ SUSTAINABLE CITY BUILDER:")
        print("-" * 40)
        
        print("Design your eco-friendly city by allocating resources:")
        print("You have 100 resource points to distribute.")
        
        renewable_energy = int(input("🔋 Renewable Energy (0-100): ") or "25")
        remaining = 100 - renewable_energy
        
        green_spaces = int(input(f"🌳 Green Spaces (0-{remaining}): ") or str(min(25, remaining)))
        remaining -= green_spaces
        
        public_transport = int(input(f"🚌 Public Transport (0-{remaining}): ") or str(min(25, remaining)))
        remaining -= public_transport
        
        recycling = remaining
        print(f"♻️  Recycling Programs: {recycling}")
        
        # Calculate sustainability score
        sustainability_score = (renewable_energy + green_spaces + public_transport + recycling) / 4
        
        print(f"\n🌱 CITY SUSTAINABILITY SCORE: {sustainability_score:.1f}/100")
        
        if sustainability_score >= 80:
            print("🏆 Congratulations! You've built an Eco-City Master level city!")
            self.add_achievement("Eco-City Master")
            self.update_ecosystem_health("city", 15)
        elif sustainability_score >= 60:
            print("🌱 Good job! Your city is on the right track!")
            self.update_ecosystem_health("city", 10)
        else:
            print("🔧 Your city needs more sustainable features!")
            self.update_ecosystem_health("city", 5)
        
        input("\nPress Enter to continue...")

    def ecosystem_manager_menu(self):
        while True:
            self.clear_screen()
            self.display_header()
            
            print("\n🌊 ECOSYSTEM MANAGER:")
            print("-" * 40)
            
            print("Choose an ecosystem to manage:")
            print("1. 🌳 Forest Ecosystem")
            print("2. 🌊 Ocean Ecosystem")
            print("3. 🏙️ Urban Ecosystem")
            print("4. 🐾 Wildlife Ecosystem")
            print("5. 🔙 Back to Main Menu")
            
            choice = input("\nChoose ecosystem (1-5): ").strip()
            
            ecosystems = {
                '1': 'forest',
                '2': 'ocean',
                '3': 'city',
                '4': 'wildlife'
            }
            
            if choice in ecosystems:
                self.manage_ecosystem(ecosystems[choice])
            elif choice == '5':
                break
            else:
                print("❌ Invalid choice! Please try again.")
                input("Press Enter to continue...")

    def manage_ecosystem(self, ecosystem_type):
        actions = {
            'forest': {
                "Plant trees": 8,
                "Stop deforestation": 12,
                "Create protected areas": 15,
                "Fight forest fires": 10
            },
            'ocean': {
                "Remove plastic waste": 10,
                "Reduce overfishing": 8,
                "Create marine reserves": 12,
                "Reduce pollution": 15
            },
            'city': {
                "Add green roofs": 6,
                "Improve public transport": 8,
                "Install solar panels": 10,
                "Create bike lanes": 5
            },
            'wildlife': {
                "Create wildlife corridors": 12,
                "Stop poaching": 15,
                "Restore habitats": 10,
                "Reduce human conflict": 8
            }
        }
        
        while True:
            self.clear_screen()
            self.display_header()
            
            print(f"\n🌊 MANAGING {ecosystem_type.upper()} ECOSYSTEM:")
            print("-" * 40)
            print(f"Current Health: {self.ecosystem_health[ecosystem_type]}%")
            
            ecosystem_actions = actions[ecosystem_type]
            print("\nAvailable Actions:")
            for i, (action, improvement) in enumerate(ecosystem_actions.items(), 1):
                print(f"{i}. {action} (+{improvement}% health)")
            
            print(f"{len(ecosystem_actions) + 1}. 🔙 Back to Ecosystem Menu")
            
            choice = input(f"\nChoose action (1-{len(ecosystem_actions) + 1}): ").strip()
            
            if choice.isdigit() and 1 <= int(choice) <= len(ecosystem_actions):
                action_name = list(ecosystem_actions.keys())[int(choice) - 1]
                improvement = ecosystem_actions[action_name]
                
                self.update_ecosystem_health(ecosystem_type, improvement)
                
                # Check for achievements
                if self.ecosystem_health[ecosystem_type] >= 95:
                    self.add_achievement(f"{ecosystem_type.title()} Master")
                
                input("Press Enter to continue...")
                
            elif choice == str(len(ecosystem_actions) + 1):
                break
            else:
                print("❌ Invalid choice! Please try again.")
                input("Press Enter to continue...")

    def main_menu(self):
        while True:
            self.clear_screen()
            self.display_header()
            
            print("\n🎮 MAIN MENU:")
            print("-" * 20)
            print("1. 🌍 Dashboard")
            print("2. 🎯 Missions")
            print("3. 📸 AR Challenges")
            print("4. 🏙️ City Builder")
            print("5. 🌊 Ecosystem Manager")
            print("6. 📊 Player Stats")
            print("7. 💾 Save Game")
            print("8. 🚪 Quit Game")
            
            choice = input("\nChoose option (1-8): ").strip()
            
            if choice == '1':
                self.dashboard_menu()
            elif choice == '2':
                self.missions_menu()
            elif choice == '3':
                self.ar_challenges_menu()
            elif choice == '4':
                self.city_builder_menu()
            elif choice == '5':
                self.ecosystem_manager_menu()
            elif choice == '6':
                self.show_detailed_stats()
            elif choice == '7':
                self.save_game()
            elif choice == '8':
                print("\n🌍 Thanks for playing EcoQuest: Planet Protectors!")
                print("Remember: Every small action helps save our planet! 🌱")
                break
            else:
                print("❌ Invalid choice! Please try again.")
                input("Press Enter to continue...")

    def save_game(self):
        game_data = {
            'player_name': self.player_name,
            'player_level': self.player_level,
            'eco_points': self.eco_points,
            'ecosystem_health': self.ecosystem_health,
            'achievements': self.achievements,
            'virtual_pets': self.virtual_pets,
            'missions': self.missions,
            'save_date': datetime.now().isoformat()
        }
        
        try:
            with open('ecoquest_save.json', 'w') as f:
                json.dump(game_data, f, indent=2)
            print("\n💾 Game saved successfully!")
        except Exception as e:
            print(f"\n❌ Error saving game: {e}")
        
        input("Press Enter to continue...")

    def load_game(self):
        try:
            with open('ecoquest_save.json', 'r') as f:
                game_data = json.load(f)
            
            self.player_name = game_data.get('player_name', '')
            self.player_level = game_data.get('player_level', 1)
            self.eco_points = game_data.get('eco_points', 100)
            self.ecosystem_health = game_data.get('ecosystem_health', self.ecosystem_health)
            self.achievements = game_data.get('achievements', [])
            self.virtual_pets = game_data.get('virtual_pets', [])
            self.missions = game_data.get('missions', self.missions)
            
            print("💾 Game loaded successfully!")
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"❌ Error loading game: {e}")
            return False

    def welcome_screen(self):
        self.clear_screen()
        print("=" * 60)
        print("🌍 WELCOME TO ECOQUEST: PLANET PROTECTORS! 🌍")
        print("=" * 60)
        print()
        print("🎮 About the Game:")
        print("• Manage global ecosystems and protect the environment")
        print("• Complete exciting missions and challenges")
        print("• Build sustainable cities and adopt virtual pets")
        print("• Learn real environmental science concepts")
        print("• Become a true Planet Protector!")
        print()
        
        # Check for saved game
        if os.path.exists('ecoquest_save.json'):
            load_choice = input("📁 Saved game found! Load it? (y/n): ").lower().strip()
            if load_choice == 'y':
                if self.load_game():
                    input("Press Enter to continue...")
                    return
        
        self.player_name = input("🌱 Enter your Planet Protector name: ").strip()
        if not self.player_name:
            self.player_name = "EcoHero"
        
        print(f"\n🎉 Welcome, {self.player_name}!")
        print("Your mission: Save the planet through environmental action!")
        input("\nPress Enter to start your eco-adventure...")

    def run(self):
        self.welcome_screen()
        self.main_menu()

def main():
    print("🌍 Starting EcoQuest: Planet Protectors...")
    game = EcoQuestGame()
    game.run()

if __name__ == "__main__":
    main()
