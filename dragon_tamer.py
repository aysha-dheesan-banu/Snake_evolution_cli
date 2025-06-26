#!/usr/bin/env python3
"""
🐉 DRAGON TAMER ADVENTURE 🐉
A fantasy RPG where you raise and battle with dragons
"""

import random
import time
import os
import json

class Dragon:
    def __init__(self, name, dragon_type):
        self.name = name
        self.type = dragon_type
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.attack = 20
        self.defense = 15
        self.speed = 10
        self.experience = 0
        self.exp_to_next = 100
        self.happiness = 50
        self.hunger = 50
        self.energy = 100
        self.skills = []
        self.element = self.get_element()
        
        # Dragon type bonuses
        type_bonuses = {
            'Fire': {'attack': 5, 'skills': ['Flame Breath', 'Fire Shield']},
            'Ice': {'defense': 5, 'skills': ['Frost Bite', 'Ice Armor']},
            'Lightning': {'speed': 5, 'skills': ['Thunder Strike', 'Lightning Speed']},
            'Earth': {'hp': 20, 'skills': ['Rock Throw', 'Stone Skin']},
            'Shadow': {'attack': 3, 'defense': 3, 'skills': ['Shadow Strike', 'Invisibility']},
        }
        
        if dragon_type in type_bonuses:
            bonus = type_bonuses[dragon_type]
            self.attack += bonus.get('attack', 0)
            self.defense += bonus.get('defense', 0)
            self.speed += bonus.get('speed', 0)
            self.max_hp += bonus.get('hp', 0)
            self.hp = self.max_hp
            self.skills = bonus.get('skills', [])
    
    def get_element(self):
        elements = {
            'Fire': '🔥',
            'Ice': '❄️',
            'Lightning': '⚡',
            'Earth': '🌍',
            'Shadow': '🌑'
        }
        return elements.get(self.type, '🐉')
    
    def level_up(self):
        if self.experience >= self.exp_to_next:
            self.level += 1
            self.experience -= self.exp_to_next
            self.exp_to_next = int(self.exp_to_next * 1.5)
            
            # Stat increases
            self.max_hp += random.randint(10, 20)
            self.attack += random.randint(3, 7)
            self.defense += random.randint(2, 5)
            self.speed += random.randint(1, 4)
            self.hp = self.max_hp  # Full heal on level up
            
            return True
        return False
    
    def get_status(self):
        status = []
        if self.happiness > 80:
            status.append("😊 Happy")
        elif self.happiness < 30:
            status.append("😢 Sad")
        
        if self.hunger > 80:
            status.append("🍖 Hungry")
        elif self.hunger < 20:
            status.append("😋 Full")
        
        if self.energy < 30:
            status.append("😴 Tired")
        elif self.energy > 80:
            status.append("⚡ Energetic")
        
        return status if status else ["😐 Normal"]

class DragonTamer:
    def __init__(self):
        self.player_name = ""
        self.dragons = []
        self.active_dragon = None
        self.gold = 100
        self.items = {
            'Dragon Food': 5,
            'Health Potion': 3,
            'Energy Drink': 2,
            'Happiness Treat': 3
        }
        self.day = 1
        self.reputation = 0
        self.battles_won = 0
        
        # Shop items
        self.shop_items = {
            'Dragon Food': {'price': 10, 'effect': 'hunger'},
            'Health Potion': {'price': 25, 'effect': 'health'},
            'Energy Drink': {'price': 20, 'effect': 'energy'},
            'Happiness Treat': {'price': 15, 'effect': 'happiness'},
            'Dragon Egg': {'price': 200, 'effect': 'new_dragon'}
        }
        
        # Wild dragons for battles
        self.wild_dragons = [
            {'name': 'Wild Flame Drake', 'type': 'Fire', 'level': 1},
            {'name': 'Frost Wyrm', 'type': 'Ice', 'level': 2},
            {'name': 'Storm Dragon', 'type': 'Lightning', 'level': 3},
            {'name': 'Mountain Guardian', 'type': 'Earth', 'level': 4},
            {'name': 'Shadow Serpent', 'type': 'Shadow', 'level': 5},
        ]
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def create_starter_dragon(self):
        print("🐉 Welcome to Dragon Tamer Adventure! 🐉")
        self.player_name = input("Enter your name, brave tamer: ").strip()
        
        print(f"\nWelcome, {self.player_name}! Choose your starter dragon:")
        dragon_types = ['Fire', 'Ice', 'Lightning', 'Earth', 'Shadow']
        
        for i, dtype in enumerate(dragon_types, 1):
            elements = {'Fire': '🔥', 'Ice': '❄️', 'Lightning': '⚡', 'Earth': '🌍', 'Shadow': '🌑'}
            print(f"{i}. {elements[dtype]} {dtype} Dragon")
        
        while True:
            try:
                choice = int(input("\nChoose (1-5): ")) - 1
                if 0 <= choice < len(dragon_types):
                    dragon_type = dragon_types[choice]
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a number!")
        
        dragon_name = input(f"Name your {dragon_type} dragon: ").strip()
        
        starter_dragon = Dragon(dragon_name, dragon_type)
        self.dragons.append(starter_dragon)
        self.active_dragon = starter_dragon
        
        print(f"\n🎉 Congratulations! You've bonded with {dragon_name} the {dragon_type} dragon!")
        time.sleep(2)
    
    def display_dragon_stats(self, dragon):
        print(f"\n🐉 {dragon.name} the {dragon.type} Dragon {dragon.element}")
        print(f"Level: {dragon.level} | XP: {dragon.experience}/{dragon.exp_to_next}")
        print(f"HP: {dragon.hp}/{dragon.max_hp} ❤️")
        print(f"Attack: {dragon.attack} ⚔️ | Defense: {dragon.defense} 🛡️ | Speed: {dragon.speed} 💨")
        print(f"Happiness: {dragon.happiness}/100 😊")
        print(f"Hunger: {dragon.hunger}/100 🍖")
        print(f"Energy: {dragon.energy}/100 ⚡")
        print(f"Status: {', '.join(dragon.get_status())}")
        if dragon.skills:
            print(f"Skills: {', '.join(dragon.skills)}")
    
    def care_for_dragon(self):
        if not self.active_dragon:
            print("No active dragon!")
            return
        
        dragon = self.active_dragon
        
        print(f"\n🐉 Caring for {dragon.name}")
        print("1. Feed dragon 🍖")
        print("2. Play with dragon 😊")
        print("3. Let dragon rest 😴")
        print("4. Train dragon 💪")
        print("5. Use item 🎒")
        print("6. Back")
        
        choice = input("\nChoose action: ").strip()
        
        if choice == '1':
            if self.items.get('Dragon Food', 0) > 0:
                self.items['Dragon Food'] -= 1
                dragon.hunger = max(0, dragon.hunger - 30)
                dragon.happiness = min(100, dragon.happiness + 10)
                print(f"{dragon.name} enjoyed the meal! 🍖")
            else:
                print("No dragon food available!")
        
        elif choice == '2':
            if dragon.energy >= 20:
                dragon.energy -= 20
                dragon.happiness = min(100, dragon.happiness + 25)
                dragon.hunger = min(100, dragon.hunger + 10)
                print(f"{dragon.name} had fun playing! 😊")
            else:
                print(f"{dragon.name} is too tired to play!")
        
        elif choice == '3':
            dragon.energy = min(100, dragon.energy + 40)
            dragon.hunger = min(100, dragon.hunger + 15)
            print(f"{dragon.name} feels refreshed! 😴")
        
        elif choice == '4':
            if dragon.energy >= 30 and dragon.happiness >= 30:
                dragon.energy -= 30
                dragon.hunger = min(100, dragon.hunger + 20)
                dragon.experience += random.randint(10, 25)
                print(f"{dragon.name} gained experience from training! 💪")
                
                if dragon.level_up():
                    print(f"🎉 {dragon.name} leveled up to level {dragon.level}!")
            else:
                print(f"{dragon.name} is not in condition to train!")
        
        elif choice == '5':
            self.use_item()
        
        time.sleep(2)
    
    def use_item(self):
        print("\n🎒 Your Items:")
        available_items = [(item, count) for item, count in self.items.items() if count > 0]
        
        if not available_items:
            print("No items available!")
            return
        
        for i, (item, count) in enumerate(available_items, 1):
            print(f"{i}. {item} x{count}")
        
        try:
            choice = int(input("Choose item (0 to cancel): "))
            if choice == 0:
                return
            
            item_name = available_items[choice - 1][0]
            self.items[item_name] -= 1
            dragon = self.active_dragon
            
            if item_name == 'Dragon Food':
                dragon.hunger = max(0, dragon.hunger - 40)
                print(f"{dragon.name} ate the food! 🍖")
            elif item_name == 'Health Potion':
                dragon.hp = min(dragon.max_hp, dragon.hp + 50)
                print(f"{dragon.name} recovered health! ❤️")
            elif item_name == 'Energy Drink':
                dragon.energy = min(100, dragon.energy + 50)
                print(f"{dragon.name} feels energized! ⚡")
            elif item_name == 'Happiness Treat':
                dragon.happiness = min(100, dragon.happiness + 30)
                print(f"{dragon.name} is happier! 😊")
        
        except (ValueError, IndexError):
            print("Invalid choice!")
    
    def battle_system(self):
        if not self.active_dragon:
            print("No active dragon for battle!")
            return
        
        if self.active_dragon.energy < 50:
            print(f"{self.active_dragon.name} is too tired to battle!")
            return
        
        # Choose opponent
        available_opponents = [w for w in self.wild_dragons if w['level'] <= self.active_dragon.level + 2]
        opponent_data = random.choice(available_opponents)
        
        # Create opponent dragon
        opponent = Dragon(opponent_data['name'], opponent_data['type'])
        opponent.level = opponent_data['level']
        for _ in range(opponent.level - 1):
            opponent.level_up()
        
        print(f"\n⚔️ Battle begins! {self.active_dragon.name} vs {opponent.name}")
        
        player_dragon = self.active_dragon
        
        while player_dragon.hp > 0 and opponent.hp > 0:
            print(f"\n{player_dragon.name}: {player_dragon.hp}/{player_dragon.max_hp} HP")
            print(f"{opponent.name}: {opponent.hp}/{opponent.max_hp} HP")
            
            print("\n1. Attack ⚔️")
            print("2. Use Skill 🌟")
            print("3. Defend 🛡️")
            print("4. Run Away 🏃")
            
            choice = input("Choose action: ").strip()
            
            if choice == '1':
                damage = max(1, player_dragon.attack - opponent.defense + random.randint(-5, 5))
                opponent.hp -= damage
                print(f"{player_dragon.name} attacks for {damage} damage!")
            
            elif choice == '2' and player_dragon.skills:
                skill = random.choice(player_dragon.skills)
                damage = max(1, int(player_dragon.attack * 1.5) - opponent.defense)
                opponent.hp -= damage
                print(f"{player_dragon.name} uses {skill} for {damage} damage!")
            
            elif choice == '3':
                print(f"{player_dragon.name} defends!")
                damage_reduction = 0.5
            
            elif choice == '4':
                print("You ran away from battle!")
                return
            
            else:
                damage = max(1, player_dragon.attack - opponent.defense)
                opponent.hp -= damage
                print(f"{player_dragon.name} attacks for {damage} damage!")
            
            if opponent.hp <= 0:
                break
            
            # Opponent's turn
            opp_damage = max(1, opponent.attack - player_dragon.defense + random.randint(-3, 3))
            if choice == '3':
                opp_damage = int(opp_damage * 0.5)
            
            player_dragon.hp -= opp_damage
            print(f"{opponent.name} attacks for {opp_damage} damage!")
            
            time.sleep(1)
        
        # Battle results
        if player_dragon.hp <= 0:
            print(f"\n💀 {player_dragon.name} was defeated!")
            player_dragon.hp = 1  # Don't let dragon die completely
            player_dragon.happiness = max(0, player_dragon.happiness - 20)
        else:
            print(f"\n🎉 Victory! {player_dragon.name} defeated {opponent.name}!")
            exp_gained = opponent.level * 20 + random.randint(10, 30)
            gold_gained = opponent.level * 15 + random.randint(5, 20)
            
            player_dragon.experience += exp_gained
            self.gold += gold_gained
            self.battles_won += 1
            self.reputation += 5
            
            print(f"Gained {exp_gained} XP and {gold_gained} gold!")
            
            if player_dragon.level_up():
                print(f"🎉 {player_dragon.name} leveled up to level {player_dragon.level}!")
        
        player_dragon.energy -= 30
        time.sleep(3)
    
    def shop(self):
        print(f"\n🏪 Dragon Shop (Gold: {self.gold})")
        print("=" * 30)
        
        for i, (item, data) in enumerate(self.shop_items.items(), 1):
            print(f"{i}. {item} - {data['price']} gold")
        
        print("0. Leave shop")
        
        try:
            choice = int(input("\nWhat would you like to buy? "))
            if choice == 0:
                return
            
            items = list(self.shop_items.keys())
            item_name = items[choice - 1]
            price = self.shop_items[item_name]['price']
            
            if self.gold >= price:
                self.gold -= price
                
                if item_name == 'Dragon Egg':
                    self.hatch_dragon_egg()
                else:
                    self.items[item_name] = self.items.get(item_name, 0) + 1
                    print(f"Bought {item_name}!")
            else:
                print("Not enough gold!")
        
        except (ValueError, IndexError):
            print("Invalid choice!")
        
        time.sleep(2)
    
    def hatch_dragon_egg(self):
        dragon_types = ['Fire', 'Ice', 'Lightning', 'Earth', 'Shadow']
        dragon_type = random.choice(dragon_types)
        dragon_name = f"Young {dragon_type} Dragon"
        
        new_dragon = Dragon(dragon_name, dragon_type)
        self.dragons.append(new_dragon)
        
        print(f"🥚 The egg hatched! You got a {dragon_type} dragon!")
        rename = input("Would you like to rename it? (y/n): ").lower()
        if rename == 'y':
            new_name = input("Enter new name: ").strip()
            new_dragon.name = new_name
    
    def dragon_management(self):
        if not self.dragons:
            print("No dragons available!")
            return
        
        print("\n🐉 Your Dragons:")
        for i, dragon in enumerate(self.dragons, 1):
            active = " (Active)" if dragon == self.active_dragon else ""
            print(f"{i}. {dragon.name} - Level {dragon.level} {dragon.type}{active}")
        
        print("0. Back")
        
        try:
            choice = int(input("Select dragon: "))
            if choice == 0:
                return
            
            selected_dragon = self.dragons[choice - 1]
            self.active_dragon = selected_dragon
            print(f"{selected_dragon.name} is now your active dragon!")
            self.display_dragon_stats(selected_dragon)
        
        except (ValueError, IndexError):
            print("Invalid choice!")
        
        time.sleep(2)
    
    def daily_update(self):
        """Update dragon stats daily"""
        for dragon in self.dragons:
            dragon.hunger = min(100, dragon.hunger + 15)
            dragon.energy = min(100, dragon.energy + 20)
            if dragon.happiness > 20:
                dragon.happiness -= 5
        
        self.day += 1
        print(f"\n🌅 Day {self.day} begins!")
        time.sleep(1)
    
    def display_status(self):
        self.clear_screen()
        print("🐉 DRAGON TAMER ADVENTURE 🐉")
        print("=" * 40)
        print(f"Tamer: {self.player_name}")
        print(f"Day: {self.day} | Gold: {self.gold} 💰")
        print(f"Reputation: {self.reputation} ⭐")
        print(f"Battles Won: {self.battles_won} 🏆")
        
        if self.active_dragon:
            self.display_dragon_stats(self.active_dragon)
    
    def main_menu(self):
        while True:
            self.display_status()
            
            print("\n📋 What would you like to do?")
            print("1. Care for Dragon 🐉")
            print("2. Battle Wild Dragons ⚔️")
            print("3. Visit Shop 🏪")
            print("4. Manage Dragons 📝")
            print("5. Rest (Next Day) 😴")
            print("6. Quit Game 👋")
            
            choice = input("\nChoose action: ").strip()
            
            if choice == '1':
                self.care_for_dragon()
            elif choice == '2':
                self.battle_system()
            elif choice == '3':
                self.shop()
            elif choice == '4':
                self.dragon_management()
            elif choice == '5':
                self.daily_update()
            elif choice == '6':
                print("Thanks for playing Dragon Tamer Adventure! 🐉")
                break
            else:
                print("Invalid choice!")
                time.sleep(1)
    
    def game_loop(self):
        self.create_starter_dragon()
        self.main_menu()

def main():
    game = DragonTamer()
    game.game_loop()

if __name__ == "__main__":
    main()
