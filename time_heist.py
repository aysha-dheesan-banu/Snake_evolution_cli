#!/usr/bin/env python3
"""
⏰ TIME HEIST CHRONICLES ⏰
A time-traveling adventure game with paradox mechanics
"""

import random
import time
import os
from datetime import datetime, timedelta
import copy

class TimeHeist:
    def __init__(self):
        self.player_name = ""
        self.current_timeline = "Prime"
        self.time_energy = 100
        self.paradox_level = 0
        self.items_stolen = []
        self.timeline_changes = {}
        self.reputation = 0
        self.heat_level = 0  # How much attention you've attracted
        self.day = 1
        
        # Time periods available
        self.time_periods = {
            "Ancient Egypt": {
                "year": -2500,
                "difficulty": 2,
                "targets": ["Golden Scarab", "Pharaoh's Crown", "Sacred Papyrus"],
                "guards": "Temple Guards",
                "description": "The land of pyramids and pharaohs"
            },
            "Medieval Castle": {
                "year": 1200,
                "difficulty": 3,
                "targets": ["Royal Sword", "Dragon's Gem", "Knight's Armor"],
                "guards": "Castle Knights",
                "description": "Age of chivalry and castles"
            },
            "Wild West": {
                "year": 1880,
                "difficulty": 2,
                "targets": ["Gold Nuggets", "Sheriff's Badge", "Outlaw's Gun"],
                "guards": "Sheriff's Posse",
                "description": "Lawless frontier towns"
            },
            "Victorian London": {
                "year": 1890,
                "difficulty": 4,
                "targets": ["Crown Jewels", "Steam Engine Plans", "Detective's Notes"],
                "guards": "Scotland Yard",
                "description": "Fog-shrouded streets of mystery"
            },
            "Future City": {
                "year": 2150,
                "difficulty": 5,
                "targets": ["Quantum Core", "AI Chip", "Plasma Weapon"],
                "guards": "Cyber Police",
                "description": "Neon-lit cyberpunk metropolis"
            }
        }
        
        # Current mission
        self.current_mission = None
        self.mission_progress = 0
        
        # Paradox effects
        self.paradox_effects = [
            "Reality glitches around you",
            "You see multiple versions of yourself",
            "Time moves in slow motion",
            "Objects phase in and out of existence",
            "You hear echoes from other timelines"
        ]
        
        # Equipment
        self.equipment = {
            "Time Watch": True,
            "Stealth Cloak": False,
            "Temporal Scanner": False,
            "Paradox Stabilizer": False,
            "Quantum Lockpick": False
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_status(self):
        self.clear_screen()
        print("⏰ TIME HEIST CHRONICLES ⏰")
        print("=" * 50)
        print(f"Agent: {self.player_name}")
        print(f"Timeline: {self.current_timeline}")
        print(f"Day: {self.day}")
        print(f"Time Energy: {self.time_energy}/100 ⚡")
        print(f"Paradox Level: {self.paradox_level}/100 🌀")
        print(f"Heat Level: {self.heat_level}/100 🚨")
        print(f"Reputation: {self.reputation} ⭐")
        
        if self.paradox_level > 0:
            effect = random.choice(self.paradox_effects)
            print(f"🌀 Paradox Effect: {effect}")
        
        if self.items_stolen:
            print(f"\n💎 Stolen Items: {len(self.items_stolen)}")
            for item in self.items_stolen[-3:]:  # Show last 3 items
                print(f"  • {item['name']} from {item['era']}")
    
    def time_travel(self):
        if self.time_energy < 20:
            print("⚡ Not enough time energy to travel!")
            return False
        
        print("\n🌀 Available Time Periods:")
        periods = list(self.time_periods.keys())
        
        for i, period in enumerate(periods, 1):
            data = self.time_periods[period]
            difficulty = "⭐" * data["difficulty"]
            print(f"{i}. {period} ({data['year']}) - {difficulty}")
            print(f"   {data['description']}")
        
        print("0. Cancel")
        
        try:
            choice = int(input("\nChoose destination: "))
            if choice == 0:
                return False
            
            period = periods[choice - 1]
            self.time_energy -= 20
            
            print(f"\n🌀 Traveling to {period}...")
            time.sleep(2)
            
            # Random time travel events
            if random.random() < 0.2:
                self.random_time_event()
            
            self.start_heist_mission(period)
            return True
            
        except (ValueError, IndexError):
            print("Invalid choice!")
            return False
    
    def random_time_event(self):
        events = [
            {
                "text": "⚡ Temporal storm detected! You arrive off-course.",
                "effect": lambda: setattr(self, 'paradox_level', min(100, self.paradox_level + 10))
            },
            {
                "text": "🌟 Smooth time travel! You feel energized.",
                "effect": lambda: setattr(self, 'time_energy', min(100, self.time_energy + 10))
            },
            {
                "text": "👁️ Someone noticed your arrival! Heat level increased.",
                "effect": lambda: setattr(self, 'heat_level', min(100, self.heat_level + 15))
            },
            {
                "text": "🔮 You glimpse another timeline and gain insight.",
                "effect": lambda: setattr(self, 'reputation', self.reputation + 5)
            }
        ]
        
        event = random.choice(events)
        print(f"\n{event['text']}")
        event['effect']()
        time.sleep(2)
    
    def start_heist_mission(self, period):
        period_data = self.time_periods[period]
        target = random.choice(period_data["targets"])
        
        self.current_mission = {
            "period": period,
            "target": target,
            "difficulty": period_data["difficulty"],
            "guards": period_data["guards"],
            "progress": 0,
            "max_progress": 100
        }
        
        print(f"\n🎯 MISSION BRIEFING")
        print(f"Location: {period}")
        print(f"Target: {target}")
        print(f"Security: {period_data['guards']}")
        print(f"Difficulty: {'⭐' * period_data['difficulty']}")
        
        self.execute_heist()
    
    def execute_heist(self):
        mission = self.current_mission
        
        while mission["progress"] < mission["max_progress"]:
            print(f"\n🏛️ {mission['period']} - Heist in Progress")
            print(f"Target: {mission['target']}")
            print(f"Progress: {mission['progress']}/{mission['max_progress']}")
            print(f"Security Alert: {self.heat_level}/100")
            
            print("\n📋 Choose your approach:")
            print("1. Stealth Approach 🥷")
            print("2. Tech Approach 💻")
            print("3. Social Engineering 🎭")
            print("4. Brute Force ⚔️")
            print("5. Use Equipment 🛠️")
            print("6. Abort Mission 🏃")
            
            choice = input("Choose action: ").strip()
            
            if choice == '1':
                self.stealth_approach()
            elif choice == '2':
                self.tech_approach()
            elif choice == '3':
                self.social_approach()
            elif choice == '4':
                self.brute_force_approach()
            elif choice == '5':
                self.use_equipment()
            elif choice == '6':
                print("Mission aborted! Returning to base...")
                self.current_mission = None
                return
            else:
                print("Invalid choice!")
                continue
            
            # Check for mission completion
            if mission["progress"] >= mission["max_progress"]:
                self.complete_heist()
                return
            
            # Random events during heist
            if random.random() < 0.3:
                self.heist_random_event()
            
            # Check if caught
            if self.heat_level >= 100:
                self.caught_by_authorities()
                return
    
    def stealth_approach(self):
        mission = self.current_mission
        success_chance = 0.7
        
        if self.equipment.get("Stealth Cloak"):
            success_chance += 0.2
        
        if random.random() < success_chance:
            progress = random.randint(15, 25)
            mission["progress"] += progress
            heat_increase = random.randint(0, 5)
            print(f"🥷 Stealth successful! Progress: +{progress}")
        else:
            heat_increase = random.randint(10, 20)
            print("🚨 You were spotted! Security increased!")
        
        self.heat_level = min(100, self.heat_level + heat_increase)
        self.time_energy -= 5
    
    def tech_approach(self):
        mission = self.current_mission
        success_chance = 0.6
        
        if self.equipment.get("Quantum Lockpick"):
            success_chance += 0.3
        if self.equipment.get("Temporal Scanner"):
            success_chance += 0.2
        
        if random.random() < success_chance:
            progress = random.randint(20, 30)
            mission["progress"] += progress
            print(f"💻 Tech hack successful! Progress: +{progress}")
            heat_increase = random.randint(0, 8)
        else:
            print("💥 Tech approach failed! Alarms triggered!")
            heat_increase = random.randint(15, 25)
        
        self.heat_level = min(100, self.heat_level + heat_increase)
        self.time_energy -= 8
    
    def social_approach(self):
        mission = self.current_mission
        success_chance = 0.5 + (self.reputation * 0.01)
        
        if random.random() < success_chance:
            progress = random.randint(10, 20)
            mission["progress"] += progress
            print(f"🎭 Social engineering worked! Progress: +{progress}")
            heat_increase = random.randint(0, 3)
        else:
            print("😤 Your cover was blown!")
            heat_increase = random.randint(8, 15)
        
        self.heat_level = min(100, self.heat_level + heat_increase)
        self.time_energy -= 3
    
    def brute_force_approach(self):
        mission = self.current_mission
        progress = random.randint(25, 35)
        mission["progress"] += progress
        heat_increase = random.randint(20, 30)
        
        print(f"⚔️ Brute force! Progress: +{progress}")
        print("🚨 But security is now on high alert!")
        
        self.heat_level = min(100, self.heat_level + heat_increase)
        self.time_energy -= 15
    
    def use_equipment(self):
        available_equipment = [item for item, owned in self.equipment.items() if owned]
        
        if not available_equipment:
            print("No equipment available!")
            return
        
        print("\n🛠️ Available Equipment:")
        for i, item in enumerate(available_equipment, 1):
            print(f"{i}. {item}")
        
        try:
            choice = int(input("Choose equipment: ")) - 1
            equipment = available_equipment[choice]
            
            if equipment == "Paradox Stabilizer":
                self.paradox_level = max(0, self.paradox_level - 20)
                print("🌀 Paradox level reduced!")
            elif equipment == "Temporal Scanner":
                mission = self.current_mission
                mission["progress"] += 15
                print("🔍 Scanner reveals hidden paths! Progress +15")
            elif equipment == "Stealth Cloak":
                self.heat_level = max(0, self.heat_level - 15)
                print("🥷 Stealth cloak activated! Heat reduced!")
            
            self.time_energy -= 5
            
        except (ValueError, IndexError):
            print("Invalid choice!")
    
    def heist_random_event(self):
        events = [
            {
                "text": "🕰️ Time distortion detected! Reality shifts around you.",
                "effect": lambda: setattr(self, 'paradox_level', min(100, self.paradox_level + 5))
            },
            {
                "text": "👮 Extra security patrol spotted!",
                "effect": lambda: setattr(self, 'heat_level', min(100, self.heat_level + 10))
            },
            {
                "text": "💎 You discover additional valuable items!",
                "effect": lambda: setattr(self, 'reputation', self.reputation + 3)
            },
            {
                "text": "⚡ Temporal energy surge! You feel recharged.",
                "effect": lambda: setattr(self, 'time_energy', min(100, self.time_energy + 15))
            },
            {
                "text": "🌀 You accidentally create a minor paradox!",
                "effect": lambda: setattr(self, 'paradox_level', min(100, self.paradox_level + 15))
            }
        ]
        
        event = random.choice(events)
        print(f"\n{event['text']}")
        event['effect']()
        time.sleep(2)
    
    def complete_heist(self):
        mission = self.current_mission
        
        print(f"\n🎉 HEIST SUCCESSFUL! 🎉")
        print(f"You successfully stole the {mission['target']}!")
        
        # Add stolen item
        stolen_item = {
            "name": mission['target'],
            "era": mission['period'],
            "value": mission['difficulty'] * 20,
            "day_stolen": self.day
        }
        self.items_stolen.append(stolen_item)
        
        # Rewards
        reputation_gain = mission['difficulty'] * 10
        self.reputation += reputation_gain
        
        print(f"Reputation gained: +{reputation_gain}")
        
        # Paradox chance based on item value
        if random.random() < (mission['difficulty'] * 0.1):
            paradox_increase = random.randint(5, 15)
            self.paradox_level = min(100, self.paradox_level + paradox_increase)
            print(f"🌀 Stealing this item created temporal ripples! Paradox +{paradox_increase}")
        
        self.current_mission = None
        time.sleep(3)
    
    def caught_by_authorities(self):
        mission = self.current_mission
        
        print(f"\n🚨 CAUGHT BY {mission['guards'].upper()}! 🚨")
        print("You've been captured and must escape!")
        
        escape_options = [
            {"name": "Time Jump Escape", "energy_cost": 30, "success_rate": 0.8},
            {"name": "Fight Your Way Out", "energy_cost": 20, "success_rate": 0.6},
            {"name": "Negotiate", "energy_cost": 10, "success_rate": 0.4},
            {"name": "Create Paradox Distraction", "energy_cost": 15, "success_rate": 0.7}
        ]
        
        print("\nEscape Options:")
        for i, option in enumerate(escape_options, 1):
            print(f"{i}. {option['name']} (Energy: {option['energy_cost']}, Success: {int(option['success_rate']*100)}%)")
        
        try:
            choice = int(input("Choose escape method: ")) - 1
            option = escape_options[choice]
            
            if self.time_energy < option['energy_cost']:
                print("Not enough energy! You're captured!")
                self.capture_consequences()
                return
            
            self.time_energy -= option['energy_cost']
            
            if random.random() < option['success_rate']:
                print(f"✅ {option['name']} successful! You escaped!")
                if option['name'] == "Create Paradox Distraction":
                    self.paradox_level = min(100, self.paradox_level + 20)
                self.heat_level = max(0, self.heat_level - 30)
            else:
                print(f"❌ {option['name']} failed! You're captured!")
                self.capture_consequences()
        
        except (ValueError, IndexError):
            print("Invalid choice! You hesitate and get captured!")
            self.capture_consequences()
        
        self.current_mission = None
    
    def capture_consequences(self):
        print("\n⛓️ CAPTURE CONSEQUENCES:")
        
        # Lose some items
        if self.items_stolen:
            lost_items = random.randint(1, min(3, len(self.items_stolen)))
            for _ in range(lost_items):
                lost_item = self.items_stolen.pop()
                print(f"Lost: {lost_item['name']}")
        
        # Reputation loss
        rep_loss = random.randint(10, 30)
        self.reputation = max(0, self.reputation - rep_loss)
        print(f"Reputation lost: -{rep_loss}")
        
        # Time energy loss
        energy_loss = random.randint(20, 40)
        self.time_energy = max(10, self.time_energy - energy_loss)
        print(f"Time energy lost: -{energy_loss}")
        
        time.sleep(3)
    
    def manage_paradoxes(self):
        if self.paradox_level == 0:
            print("No paradoxes to manage!")
            return
        
        print(f"\n🌀 Current Paradox Level: {self.paradox_level}/100")
        
        if self.paradox_level >= 80:
            print("⚠️ CRITICAL: Reality is becoming unstable!")
        elif self.paradox_level >= 50:
            print("⚠️ WARNING: Temporal distortions detected!")
        
        print("\nParadox Management Options:")
        print("1. Meditate to stabilize timeline (Energy: 10)")
        print("2. Return stolen item to reduce paradox (Lose item)")
        print("3. Use Paradox Stabilizer (Equipment)")
        print("4. Accept the chaos (Do nothing)")
        
        choice = input("Choose action: ").strip()
        
        if choice == '1':
            if self.time_energy >= 10:
                self.time_energy -= 10
                reduction = random.randint(5, 15)
                self.paradox_level = max(0, self.paradox_level - reduction)
                print(f"🧘 Meditation successful! Paradox reduced by {reduction}")
            else:
                print("Not enough energy!")
        
        elif choice == '2':
            if self.items_stolen:
                print("Choose item to return:")
                for i, item in enumerate(self.items_stolen, 1):
                    print(f"{i}. {item['name']} from {item['era']}")
                
                try:
                    item_choice = int(input("Choose item: ")) - 1
                    returned_item = self.items_stolen.pop(item_choice)
                    reduction = returned_item['value']
                    self.paradox_level = max(0, self.paradox_level - reduction)
                    print(f"Returned {returned_item['name']}. Paradox reduced by {reduction}")
                except (ValueError, IndexError):
                    print("Invalid choice!")
            else:
                print("No items to return!")
        
        elif choice == '3':
            if self.equipment.get("Paradox Stabilizer"):
                self.paradox_level = max(0, self.paradox_level - 30)
                print("🔧 Paradox Stabilizer used! Major reduction achieved!")
            else:
                print("You don't have a Paradox Stabilizer!")
        
        elif choice == '4':
            print("🌀 You embrace the chaos of the multiverse!")
            # Small chance of positive effect
            if random.random() < 0.3:
                self.reputation += 10
                print("Your reckless attitude impresses other time criminals!")
    
    def equipment_shop(self):
        shop_items = {
            "Stealth Cloak": {"price": 50, "description": "Improves stealth success rate"},
            "Temporal Scanner": {"price": 75, "description": "Reveals hidden information"},
            "Paradox Stabilizer": {"price": 100, "description": "Reduces paradox levels"},
            "Quantum Lockpick": {"price": 60, "description": "Improves tech approach success"}
        }
        
        print(f"\n🛒 TIME THIEF EQUIPMENT SHOP")
        print(f"Your Reputation: {self.reputation}")
        print("=" * 40)
        
        for i, (item, data) in enumerate(shop_items.items(), 1):
            owned = "✅" if self.equipment.get(item) else "❌"
            print(f"{i}. {item} - {data['price']} rep {owned}")
            print(f"   {data['description']}")
        
        print("0. Leave shop")
        
        try:
            choice = int(input("Choose item to buy: "))
            if choice == 0:
                return
            
            items = list(shop_items.keys())
            item_name = items[choice - 1]
            price = shop_items[item_name]['price']
            
            if self.equipment.get(item_name):
                print("You already own this item!")
            elif self.reputation >= price:
                self.reputation -= price
                self.equipment[item_name] = True
                print(f"Purchased {item_name}!")
            else:
                print("Not enough reputation!")
        
        except (ValueError, IndexError):
            print("Invalid choice!")
        
        time.sleep(2)
    
    def view_timeline_status(self):
        print("\n📊 TIMELINE STATUS REPORT")
        print("=" * 40)
        print(f"Current Timeline: {self.current_timeline}")
        print(f"Items Stolen: {len(self.items_stolen)}")
        print(f"Total Value: {sum(item['value'] for item in self.items_stolen)}")
        
        if self.items_stolen:
            print("\n💎 Stolen Artifacts:")
            for item in self.items_stolen:
                print(f"  • {item['name']} from {item['era']} (Day {item['day_stolen']})")
        
        if self.timeline_changes:
            print("\n🌀 Timeline Changes:")
            for change, effect in self.timeline_changes.items():
                print(f"  • {change}: {effect}")
        
        print(f"\n⚡ Time Energy: {self.time_energy}/100")
        print(f"🌀 Paradox Level: {self.paradox_level}/100")
        print(f"🚨 Heat Level: {self.heat_level}/100")
    
    def rest_and_recover(self):
        print("\n😴 Resting at your temporal hideout...")
        
        # Recover energy
        energy_recovery = random.randint(20, 40)
        self.time_energy = min(100, self.time_energy + energy_recovery)
        
        # Reduce heat over time
        heat_reduction = random.randint(10, 20)
        self.heat_level = max(0, self.heat_level - heat_reduction)
        
        # Small chance of paradox increase due to temporal instability
        if random.random() < 0.2:
            paradox_increase = random.randint(1, 5)
            self.paradox_level = min(100, self.paradox_level + paradox_increase)
            print(f"🌀 Temporal instability detected! Paradox +{paradox_increase}")
        
        self.day += 1
        
        print(f"⚡ Energy recovered: +{energy_recovery}")
        print(f"🚨 Heat reduced: -{heat_reduction}")
        print(f"📅 Day {self.day} begins!")
        
        time.sleep(2)
    
    def main_menu(self):
        while True:
            self.display_status()
            
            print("\n⏰ TIME HEIST OPERATIONS")
            print("1. Travel Through Time 🌀")
            print("2. Manage Paradoxes 🌀")
            print("3. Equipment Shop 🛒")
            print("4. Timeline Status 📊")
            print("5. Rest & Recover 😴")
            print("6. Quit Game 👋")
            
            choice = input("\nChoose action: ").strip()
            
            if choice == '1':
                self.time_travel()
            elif choice == '2':
                self.manage_paradoxes()
            elif choice == '3':
                self.equipment_shop()
            elif choice == '4':
                self.view_timeline_status()
                input("\nPress Enter to continue...")
            elif choice == '5':
                self.rest_and_recover()
            elif choice == '6':
                print("Thanks for playing Time Heist Chronicles! ⏰")
                break
            else:
                print("Invalid choice!")
                time.sleep(1)
    
    def game_loop(self):
        print("⏰ Welcome to TIME HEIST CHRONICLES! ⏰")
        print("You are a master thief with access to time travel technology.")
        print("Steal legendary artifacts from across history, but beware of paradoxes!")
        
        self.player_name = input("\nEnter your codename, time thief: ").strip()
        
        print(f"\nWelcome, Agent {self.player_name}!")
        print("Your mission: Steal the most valuable artifacts from across time.")
        print("But remember - every action has consequences across the timeline...")
        
        input("\nPress Enter to begin your first heist...")
        
        self.main_menu()

def main():
    game = TimeHeist()
    game.game_loop()

if __name__ == "__main__":
    main()
