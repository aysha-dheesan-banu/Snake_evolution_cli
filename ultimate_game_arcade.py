#!/usr/bin/env python3
"""
🎮 ULTIMATE GAME ARCADE 🎮
All 5 innovative games in one unified launcher!
"""

import random
import time
import os
import sys
from collections import deque
import copy
import json

class GameLauncher:
    def __init__(self):
        self.player_name = ""
        self.total_score = 0
        self.games_played = 0
        self.achievements = []
        self.game_stats = {
            'cosmic_defender': {'played': 0, 'high_score': 0},
            'neon_maze': {'played': 0, 'high_score': 0},
            'quantum_puzzle': {'played': 0, 'high_score': 0},
            'dragon_tamer': {'played': 0, 'high_score': 0},
            'time_heist': {'played': 0, 'high_score': 0}
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_main_menu(self):
        self.clear_screen()
        print("🎮" + "="*60 + "🎮")
        print("🌟           ULTIMATE GAME ARCADE           🌟")
        print("🎮" + "="*60 + "🎮")
        
        if self.player_name:
            print(f"👤 Player: {self.player_name}")
            print(f"🏆 Total Score: {self.total_score}")
            print(f"🎯 Games Played: {self.games_played}")
        
        print("\n🎮 AVAILABLE GAMES:")
        print("1. 🚀 Cosmic Defender - Space Shooter")
        print("2. 🌈 Neon Maze Runner - Puzzle Adventure")
        print("3. 🔮 Quantum Puzzle Master - Mind Bender")
        print("4. 🐉 Dragon Tamer Adventure - Fantasy RPG")
        print("5. ⏰ Time Heist Chronicles - Time Travel")
        print("\n📊 ARCADE FEATURES:")
        print("6. 🏆 View Statistics")
        print("7. 🎖️ Achievements")
        print("8. ⚙️ Settings")
        print("9. ❓ Help")
        print("0. 👋 Exit Arcade")
    
    def setup_player(self):
        if not self.player_name:
            print("🎮 Welcome to the Ultimate Game Arcade! 🎮")
            self.player_name = input("Enter your gamer tag: ").strip()
            print(f"Welcome, {self.player_name}! Ready to play some amazing games?")
            time.sleep(2)
    
    def launch_game(self, game_choice):
        self.games_played += 1
        
        if game_choice == 1:
            score = self.launch_cosmic_defender()
            self.update_stats('cosmic_defender', score)
        elif game_choice == 2:
            score = self.launch_neon_maze()
            self.update_stats('neon_maze', score)
        elif game_choice == 3:
            score = self.launch_quantum_puzzle()
            self.update_stats('quantum_puzzle', score)
        elif game_choice == 4:
            score = self.launch_dragon_tamer()
            self.update_stats('dragon_tamer', score)
        elif game_choice == 5:
            score = self.launch_time_heist()
            self.update_stats('time_heist', score)
    
    def update_stats(self, game_name, score):
        self.game_stats[game_name]['played'] += 1
        if score > self.game_stats[game_name]['high_score']:
            self.game_stats[game_name]['high_score'] = score
            print(f"🎉 NEW HIGH SCORE in {game_name.replace('_', ' ').title()}!")
        
        self.total_score += score
        self.check_achievements()
    
    def check_achievements(self):
        new_achievements = []
        
        # First game achievement
        if self.games_played == 1 and "First Game" not in self.achievements:
            new_achievements.append("First Game")
        
        # Score achievements
        if self.total_score >= 1000 and "Score Master" not in self.achievements:
            new_achievements.append("Score Master")
        
        # Game variety achievement
        games_with_scores = sum(1 for stats in self.game_stats.values() if stats['played'] > 0)
        if games_with_scores >= 3 and "Game Explorer" not in self.achievements:
            new_achievements.append("Game Explorer")
        
        if games_with_scores == 5 and "Arcade Master" not in self.achievements:
            new_achievements.append("Arcade Master")
        
        # Add new achievements
        for achievement in new_achievements:
            self.achievements.append(achievement)
            print(f"🏆 ACHIEVEMENT UNLOCKED: {achievement}!")
            time.sleep(1)
    
    def view_statistics(self):
        self.clear_screen()
        print("📊 PLAYER STATISTICS 📊")
        print("="*40)
        print(f"Player: {self.player_name}")
        print(f"Total Score: {self.total_score}")
        print(f"Games Played: {self.games_played}")
        print(f"Achievements: {len(self.achievements)}")
        
        print("\n🎮 GAME STATISTICS:")
        for game, stats in self.game_stats.items():
            game_name = game.replace('_', ' ').title()
            print(f"{game_name}:")
            print(f"  Played: {stats['played']} times")
            print(f"  High Score: {stats['high_score']}")
        
        input("\nPress Enter to continue...")
    
    def view_achievements(self):
        self.clear_screen()
        print("🏆 ACHIEVEMENTS 🏆")
        print("="*30)
        
        all_achievements = {
            "First Game": "Play your first game",
            "Score Master": "Reach 1000 total points",
            "Game Explorer": "Play 3 different games",
            "Arcade Master": "Play all 5 games",
            "High Scorer": "Get 500+ in any single game",
            "Persistent Player": "Play 10 games total"
        }
        
        for achievement, description in all_achievements.items():
            status = "✅" if achievement in self.achievements else "❌"
            print(f"{status} {achievement}: {description}")
        
        print(f"\nUnlocked: {len(self.achievements)}/{len(all_achievements)}")
        input("\nPress Enter to continue...")
    
    def main_loop(self):
        self.setup_player()
        
        while True:
            self.display_main_menu()
            
            try:
                choice = int(input("\nChoose an option: "))
                
                if choice == 0:
                    print(f"Thanks for playing, {self.player_name}! 👋")
                    break
                elif 1 <= choice <= 5:
                    self.launch_game(choice)
                elif choice == 6:
                    self.view_statistics()
                elif choice == 7:
                    self.view_achievements()
                elif choice == 8:
                    self.settings_menu()
                elif choice == 9:
                    self.help_menu()
                else:
                    print("Invalid choice!")
                    time.sleep(1)
            
            except ValueError:
                print("Please enter a number!")
                time.sleep(1)
            except KeyboardInterrupt:
                print(f"\nThanks for playing, {self.player_name}! 👋")
                break
    
    def settings_menu(self):
        print("\n⚙️ Settings menu - Coming soon!")
        time.sleep(1)
    
    def help_menu(self):
        self.clear_screen()
        print("❓ HELP & GAME DESCRIPTIONS ❓")
        print("="*50)
        
        games_help = {
            "🚀 Cosmic Defender": "Space shooter - Defend Earth from aliens!",
            "🌈 Neon Maze Runner": "Navigate glowing mazes and collect gems",
            "🔮 Quantum Puzzle Master": "Manipulate quantum particles to solve puzzles",
            "🐉 Dragon Tamer Adventure": "Raise and battle with magical dragons",
            "⏰ Time Heist Chronicles": "Steal artifacts across different time periods"
        }
        
        for game, description in games_help.items():
            print(f"{game}")
            print(f"  {description}")
            print()
        
        print("Controls vary by game - each game has its own help system!")
        input("\nPress Enter to continue...")
    
    def launch_cosmic_defender(self):
        game = CosmicDefender()
        return game.play()
    
    def launch_neon_maze(self):
        game = NeonMaze()
        return game.play()
    
    def launch_quantum_puzzle(self):
        game = QuantumPuzzle()
        return game.play()
    
    def launch_dragon_tamer(self):
        game = DragonTamer()
        return game.play()
    
    def launch_time_heist(self):
        game = TimeHeist()
        return game.play()

# COSMIC DEFENDER GAME CLASS
class CosmicDefender:
    def __init__(self):
        self.width = 60
        self.height = 15
        self.player_pos = self.width // 2
        self.player_char = "🚀"
        self.bullets = []
        self.enemies = []
        self.powerups = []
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def spawn_enemy(self):
        if random.random() < 0.4 + (self.level * 0.1):
            enemy_type = random.choice(['👾', '🛸', '💀', '⚡'])
            self.enemies.append({
                'x': random.randint(0, self.width-1),
                'y': 0,
                'char': enemy_type,
                'health': 1 if enemy_type != '🛸' else 2
            })
    
    def spawn_powerup(self):
        if random.random() < 0.08:
            powerup_type = random.choice(['💊', '⚡', '🛡️', '💥'])
            self.powerups.append({
                'x': random.randint(0, self.width-1),
                'y': 0,
                'char': powerup_type,
                'type': powerup_type
            })
    
    def move_player(self, direction):
        if direction == 'left' and self.player_pos > 0:
            self.player_pos -= 2
        elif direction == 'right' and self.player_pos < self.width - 1:
            self.player_pos += 2
    
    def shoot(self):
        self.bullets.append({'x': self.player_pos, 'y': self.height - 2})
    
    def update_game(self):
        # Update bullets
        self.bullets = [b for b in self.bullets if b['y'] > 0]
        for bullet in self.bullets:
            bullet['y'] -= 1
        
        # Update enemies
        for enemy in self.enemies[:]:
            enemy['y'] += 1
            if enemy['y'] >= self.height:
                self.enemies.remove(enemy)
                self.lives -= 1
        
        # Update powerups
        for powerup in self.powerups[:]:
            powerup['y'] += 1
            if powerup['y'] >= self.height:
                self.powerups.remove(powerup)
        
        # Check collisions
        self.check_collisions()
    
    def check_collisions(self):
        # Bullet-Enemy collisions
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if abs(bullet['x'] - enemy['x']) <= 1 and bullet['y'] == enemy['y']:
                    self.bullets.remove(bullet)
                    enemy['health'] -= 1
                    if enemy['health'] <= 0:
                        self.enemies.remove(enemy)
                        self.score += 10
                    break
        
        # Player-Powerup collisions
        for powerup in self.powerups[:]:
            if abs(self.player_pos - powerup['x']) <= 1 and powerup['y'] >= self.height - 2:
                self.powerups.remove(powerup)
                self.apply_powerup(powerup['type'])
        
        # Player-Enemy collisions
        for enemy in self.enemies[:]:
            if abs(self.player_pos - enemy['x']) <= 1 and enemy['y'] >= self.height - 2:
                self.enemies.remove(enemy)
                self.lives -= 1
    
    def apply_powerup(self, powerup_type):
        if powerup_type == '💊':
            self.lives += 1
        elif powerup_type == '⚡':
            for i in range(3):
                self.bullets.append({'x': self.player_pos + i - 1, 'y': self.height - 2})
        elif powerup_type == '🛡️':
            self.lives += 2
        elif powerup_type == '💥':
            self.score += len(self.enemies) * 5
            self.enemies.clear()
    
    def draw_game(self):
        self.clear_screen()
        
        # Create game field
        field = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Place player
        if self.player_pos < self.width:
            field[self.height-1][self.player_pos] = self.player_char
        
        # Place bullets
        for bullet in self.bullets:
            if 0 <= bullet['x'] < self.width and 0 <= bullet['y'] < self.height:
                field[bullet['y']][bullet['x']] = '|'
        
        # Place enemies
        for enemy in self.enemies:
            if 0 <= enemy['x'] < self.width and 0 <= enemy['y'] < self.height:
                field[enemy['y']][enemy['x']] = enemy['char']
        
        # Place powerups
        for powerup in self.powerups:
            if 0 <= powerup['x'] < self.width and 0 <= powerup['y'] < self.height:
                field[powerup['y']][powerup['x']] = powerup['char']
        
        # Draw field
        print("🚀 COSMIC DEFENDER 🚀")
        print("=" * (self.width + 2))
        for row in field:
            print("|" + "".join(row) + "|")
        print("=" * (self.width + 2))
        
        # Draw UI
        print(f"Score: {self.score} | Lives: {'❤️ ' * self.lives} | Level: {self.level}")
        print("A/D - Move, SPACE - Shoot, Q - Quit")
    
    def play(self):
        print("🚀 COSMIC DEFENDER 🚀")
        print("Defend Earth from alien invasion!")
        print("Press Enter to start...")
        input()
        
        turns = 0
        
        while not self.game_over and self.lives > 0:
            self.draw_game()
            
            # Auto-spawn enemies and powerups
            if turns % 3 == 0:
                self.spawn_enemy()
            if turns % 15 == 0:
                self.spawn_powerup()
            
            # Get player input
            print("Enter command (a/d/space/q): ", end="")
            try:
                command = input().lower().strip()
                if command == 'a':
                    self.move_player('left')
                elif command == 'd':
                    self.move_player('right')
                elif command == ' ' or command == 'space':
                    self.shoot()
                elif command == 'q':
                    break
                
                self.update_game()
                
                # Level progression
                if self.score > 0 and self.score % 100 == 0 and turns % 50 == 0:
                    self.level += 1
                
                turns += 1
                
            except KeyboardInterrupt:
                break
        
        self.clear_screen()
        if self.lives <= 0:
            print("💥 GAME OVER! 💥")
        else:
            print("👋 Thanks for playing!")
        
        print(f"Final Score: {self.score}")
        return self.score

# NEON MAZE RUNNER GAME CLASS
class NeonMaze:
    def __init__(self, width=21, height=13):
        self.width = width
        self.height = height
        self.maze = []
        self.player_pos = [1, 1]
        self.exit_pos = [width-2, height-2]
        self.collectibles = []
        self.score = 0
        self.time_left = 45
        self.level = 1
        self.trail = deque(maxlen=3)
        
        # Neon colors (simplified for compatibility)
        self.symbols = {
            'wall': '█',
            'path': ' ',
            'player': '●',
            'exit': '★',
            'gem': '◆',
            'power': '⚡',
            'trail': '·',
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def generate_maze(self):
        # Initialize maze with walls
        self.maze = [['█' for _ in range(self.width)] for _ in range(self.height)]
        
        # Simple maze generation
        def carve_path(x, y):
            self.maze[y][x] = ' '
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (1 <= nx < self.width-1 and 1 <= ny < self.height-1 and 
                    self.maze[ny][nx] == '█'):
                    self.maze[y + dy//2][x + dx//2] = ' '
                    carve_path(nx, ny)
        
        carve_path(1, 1)
        self.place_collectibles()
    
    def place_collectibles(self):
        self.collectibles = []
        gem_count = 3 + self.level
        
        for _ in range(gem_count):
            attempts = 0
            while attempts < 20:
                x, y = random.randint(1, self.width-2), random.randint(1, self.height-2)
                if (self.maze[y][x] == ' ' and [x, y] != self.player_pos and 
                    [x, y] != self.exit_pos):
                    self.collectibles.append({'pos': [x, y], 'type': 'gem', 'value': 10})
                    break
                attempts += 1
        
        # Add power-up
        attempts = 0
        while attempts < 10:
            x, y = random.randint(1, self.width-2), random.randint(1, self.height-2)
            if (self.maze[y][x] == ' ' and [x, y] != self.player_pos and 
                [x, y] != self.exit_pos and 
                not any(c['pos'] == [x, y] for c in self.collectibles)):
                self.collectibles.append({'pos': [x, y], 'type': 'power', 'value': 25})
                break
            attempts += 1
    
    def move_player(self, direction):
        x, y = self.player_pos
        new_pos = [x, y]
        
        if direction == 'up' and y > 0:
            new_pos[1] -= 1
        elif direction == 'down' and y < self.height - 1:
            new_pos[1] += 1
        elif direction == 'left' and x > 0:
            new_pos[0] -= 1
        elif direction == 'right' and x < self.width - 1:
            new_pos[0] += 1
        
        # Check if move is valid
        if self.maze[new_pos[1]][new_pos[0]] != '█':
            self.trail.append(self.player_pos.copy())
            self.player_pos = new_pos
            
            # Check for collectibles
            for collectible in self.collectibles[:]:
                if collectible['pos'] == self.player_pos:
                    self.score += collectible['value']
                    if collectible['type'] == 'power':
                        self.time_left += 15
                    self.collectibles.remove(collectible)
    
    def draw_maze(self):
        self.clear_screen()
        
        print("🌈 NEON MAZE RUNNER 🌈")
        print("=" * 40)
        
        # Draw maze
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                pos = [x, y]
                
                if pos == self.player_pos:
                    row += self.symbols['player']
                elif pos == self.exit_pos:
                    row += self.symbols['exit']
                elif pos in [c['pos'] for c in self.collectibles]:
                    collectible = next(c for c in self.collectibles if c['pos'] == pos)
                    if collectible['type'] == 'gem':
                        row += self.symbols['gem']
                    else:
                        row += self.symbols['power']
                elif pos in list(self.trail):
                    row += self.symbols['trail']
                elif self.maze[y][x] == '█':
                    row += self.symbols['wall']
                else:
                    row += self.symbols['path']
            print(row)
        
        print("=" * 40)
        print(f"Score: {self.score} | Time: {self.time_left:.1f}s | Level: {self.level}")
        print("W/A/S/D - Move, Q - Quit")
        print(f"Gems remaining: {len([c for c in self.collectibles if c['type'] == 'gem'])}")
    
    def check_win_condition(self):
        gems_remaining = len([c for c in self.collectibles if c['type'] == 'gem'])
        return self.player_pos == self.exit_pos and gems_remaining == 0
    
    def next_level(self):
        self.level += 1
        self.time_left += 20
        self.width = min(25, self.width + 2)
        self.height = min(17, self.height + 2)
        self.player_pos = [1, 1]
        self.exit_pos = [self.width-2, self.height-2]
        self.trail.clear()
        self.generate_maze()
    
    def play(self):
        print("🌈 Welcome to NEON MAZE RUNNER! 🌈")
        print("Navigate through the maze and collect all gems!")
        print("Press Enter to start...")
        input()
        
        self.generate_maze()
        
        while self.time_left > 0:
            self.draw_maze()
            
            if self.check_win_condition():
                print("🎉 LEVEL COMPLETE! 🎉")
                bonus = int(self.time_left * 5)
                self.score += bonus
                print(f"Time bonus: {bonus}")
                time.sleep(2)
                self.next_level()
                continue
            
            print("Enter move (w/a/s/d/q): ", end="")
            try:
                move = input().lower().strip()
                if move == 'w':
                    self.move_player('up')
                elif move == 's':
                    self.move_player('down')
                elif move == 'a':
                    self.move_player('left')
                elif move == 'd':
                    self.move_player('right')
                elif move == 'q':
                    break
                
                self.time_left -= 0.5
                
            except KeyboardInterrupt:
                break
        
        self.clear_screen()
        print("🌈 MAZE GAME OVER! 🌈")
        print(f"Final Score: {self.score}")
        print(f"Levels Completed: {self.level - 1}")
        return self.score

# QUANTUM PUZZLE MASTER GAME CLASS
class QuantumPuzzle:
    def __init__(self):
        self.grid_size = 4
        self.grid = []
        self.quantum_states = []
        self.score = 0
        self.moves = 0
        self.level = 1
        self.target_pattern = []
        self.quantum_energy = 100
        
        # Quantum symbols
        self.symbols = {
            0: '⚫', 1: '🔵', 2: '🔴', 3: '🟡', 4: '🟢', 5: '🟣'
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def initialize_grid(self):
        self.grid = [[random.randint(0, 3) for _ in range(self.grid_size)] 
                     for _ in range(self.grid_size)]
        
        # Create quantum superposition states
        self.quantum_states = []
        for _ in range(1 + self.level // 2):
            x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            self.quantum_states.append({
                'pos': (x, y),
                'states': [random.randint(1, 3), random.randint(1, 3)],
                'collapsed': False
            })
        
        # Generate target pattern (make all cells value 4)
        self.target_pattern = []
        pattern_size = min(3, self.grid_size)
        start_x = random.randint(0, self.grid_size - pattern_size)
        start_y = random.randint(0, self.grid_size - pattern_size)
        
        for i in range(pattern_size):
            for j in range(pattern_size):
                self.target_pattern.append((start_x + i, start_y + j))
    
    def draw_grid(self):
        self.clear_screen()
        
        print("🔮 QUANTUM PUZZLE MASTER 🔮")
        print("=" * 40)
        
        # Draw grid
        for y in range(self.grid_size):
            row = ""
            for x in range(self.grid_size):
                pos = (x, y)
                cell_value = self.grid[y][x]
                
                # Check if position is in quantum superposition
                quantum_state = next((qs for qs in self.quantum_states if qs['pos'] == pos), None)
                if quantum_state and not quantum_state['collapsed']:
                    # Show flickering quantum state
                    if random.random() < 0.5:
                        symbol = self.symbols[quantum_state['states'][0]]
                    else:
                        symbol = self.symbols[quantum_state['states'][1]]
                    row += f"{symbol} "
                elif pos in self.target_pattern:
                    # Highlight target positions
                    if cell_value == 4:
                        row += "🌟 "  # Correct
                    else:
                        row += f"{self.symbols[cell_value]} "
                else:
                    row += f"{self.symbols[cell_value]} "
            print(f"  {row}")
        
        print("=" * 40)
        print(f"Score: {self.score} | Moves: {self.moves} | Level: {self.level}")
        print(f"Quantum Energy: {self.quantum_energy}")
        print("Goal: Fill target pattern with green particles (🟢)")
        
        # Show quantum states
        if self.quantum_states:
            uncollapsed = [qs for qs in self.quantum_states if not qs['collapsed']]
            if uncollapsed:
                print(f"Quantum Superpositions: {len(uncollapsed)}")
    
    def make_move(self, x, y, action):
        if not (0 <= x < self.grid_size and 0 <= y < self.grid_size):
            return False
        
        self.moves += 1
        pos = (x, y)
        
        if action == 'rotate':
            self.grid[y][x] = (self.grid[y][x] + 1) % 5
            self.quantum_energy -= 5
        
        elif action == 'collapse':
            quantum_state = next((qs for qs in self.quantum_states if qs['pos'] == pos), None)
            if quantum_state and not quantum_state['collapsed']:
                chosen_state = random.choice(quantum_state['states'])
                self.grid[y][x] = chosen_state
                quantum_state['collapsed'] = True
                self.quantum_energy -= 15
                self.score += 20
        
        elif action == 'quantum':
            if self.quantum_energy >= 20:
                # Quantum manipulation - set to target value
                self.grid[y][x] = 4
                self.quantum_energy -= 20
                self.score += 10
        
        # Random quantum fluctuations
        if random.random() < 0.2:
            self.quantum_fluctuation()
        
        return True
    
    def quantum_fluctuation(self):
        # Random quantum events
        if random.random() < 0.5 and self.quantum_states:
            uncollapsed = [qs for qs in self.quantum_states if not qs['collapsed']]
            if uncollapsed:
                qs = random.choice(uncollapsed)
                x, y = qs['pos']
                self.grid[y][x] = random.choice(qs['states'])
                qs['collapsed'] = True
    
    def check_win_condition(self):
        for x, y in self.target_pattern:
            if self.grid[y][x] != 4:
                return False
        return True
    
    def next_level(self):
        self.level += 1
        if self.level % 3 == 0:
            self.grid_size = min(6, self.grid_size + 1)
        self.quantum_energy = 100
        self.score += 100 * self.level
        self.initialize_grid()
    
    def play(self):
        print("🔮 Welcome to QUANTUM PUZZLE MASTER! 🔮")
        print("Manipulate quantum particles to solve puzzles!")
        print("Commands: x y r (rotate), x y c (collapse), x y q (quantum)")
        print("Press Enter to start...")
        input()
        
        self.initialize_grid()
        
        while self.quantum_energy > 0:
            self.draw_grid()
            
            if self.check_win_condition():
                print("🎉 QUANTUM PUZZLE SOLVED! 🎉")
                print(f"Level {self.level} completed!")
                time.sleep(2)
                self.next_level()
                continue
            
            print("Enter command (x y action) or 'q' to quit: ", end="")
            try:
                command = input().strip().lower()
                
                if command == 'q':
                    break
                
                parts = command.split()
                if len(parts) == 3:
                    try:
                        x, y = int(parts[0]), int(parts[1])
                        action = parts[2]
                        
                        if action in ['r', 'rotate']:
                            action = 'rotate'
                        elif action in ['c', 'collapse']:
                            action = 'collapse'
                        elif action in ['q', 'quantum']:
                            action = 'quantum'
                        
                        if not self.make_move(x, y, action):
                            print("Invalid move!")
                            time.sleep(1)
                    except ValueError:
                        print("Invalid format! Use: x y action")
                        time.sleep(1)
                else:
                    print("Invalid format! Use: x y action (e.g., '1 2 r')")
                    time.sleep(1)
            
            except KeyboardInterrupt:
                break
        
        self.clear_screen()
        print("🔮 QUANTUM GAME OVER! 🔮")
        print(f"Final Score: {self.score}")
        print(f"Levels Completed: {self.level - 1}")
        return self.score

# DRAGON TAMER ADVENTURE GAME CLASS
class DragonTamer:
    def __init__(self):
        self.dragon = None
        self.score = 0
        self.day = 1
        self.battles_won = 0
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def create_dragon(self):
        dragon_types = ['Fire', 'Ice', 'Lightning', 'Earth', 'Shadow']
        elements = {'Fire': '🔥', 'Ice': '❄️', 'Lightning': '⚡', 'Earth': '🌍', 'Shadow': '🌑'}
        
        print("🐉 Choose your dragon type:")
        for i, dtype in enumerate(dragon_types, 1):
            print(f"{i}. {elements[dtype]} {dtype} Dragon")
        
        while True:
            try:
                choice = int(input("Choose (1-5): ")) - 1
                if 0 <= choice < len(dragon_types):
                    dragon_type = dragon_types[choice]
                    break
            except ValueError:
                pass
            print("Invalid choice!")
        
        dragon_name = input(f"Name your {dragon_type} dragon: ").strip()
        
        self.dragon = {
            'name': dragon_name,
            'type': dragon_type,
            'element': elements[dragon_type],
            'level': 1,
            'hp': 100,
            'max_hp': 100,
            'attack': 20,
            'defense': 15,
            'happiness': 50,
            'hunger': 50,
            'energy': 100,
            'experience': 0
        }
        
        print(f"🎉 {dragon_name} the {dragon_type} dragon is ready!")
        time.sleep(2)
    
    def display_dragon_stats(self):
        d = self.dragon
        print(f"\n🐉 {d['name']} the {d['type']} Dragon {d['element']}")
        print(f"Level: {d['level']} | HP: {d['hp']}/{d['max_hp']}")
        print(f"Attack: {d['attack']} | Defense: {d['defense']}")
        print(f"Happiness: {d['happiness']}/100 😊")
        print(f"Hunger: {d['hunger']}/100 🍖")
        print(f"Energy: {d['energy']}/100 ⚡")
        print(f"Experience: {d['experience']}")
    
    def care_for_dragon(self):
        print("\n🐉 Dragon Care Options:")
        print("1. Feed dragon 🍖")
        print("2. Play with dragon 😊")
        print("3. Let dragon rest 😴")
        print("4. Train dragon 💪")
        
        choice = input("Choose action (1-4): ").strip()
        
        if choice == '1':
            self.dragon['hunger'] = max(0, self.dragon['hunger'] - 30)
            self.dragon['happiness'] = min(100, self.dragon['happiness'] + 10)
            print(f"{self.dragon['name']} enjoyed the meal! 🍖")
            self.score += 5
        
        elif choice == '2':
            if self.dragon['energy'] >= 20:
                self.dragon['energy'] -= 20
                self.dragon['happiness'] = min(100, self.dragon['happiness'] + 25)
                print(f"{self.dragon['name']} had fun playing! 😊")
                self.score += 10
            else:
                print(f"{self.dragon['name']} is too tired to play!")
        
        elif choice == '3':
            self.dragon['energy'] = min(100, self.dragon['energy'] + 40)
            print(f"{self.dragon['name']} feels refreshed! 😴")
            self.score += 5
        
        elif choice == '4':
            if self.dragon['energy'] >= 30 and self.dragon['happiness'] >= 30:
                self.dragon['energy'] -= 30
                self.dragon['experience'] += random.randint(15, 30)
                print(f"{self.dragon['name']} gained experience! 💪")
                self.score += 15
                
                # Level up check
                if self.dragon['experience'] >= self.dragon['level'] * 50:
                    self.level_up_dragon()
            else:
                print(f"{self.dragon['name']} is not ready to train!")
    
    def level_up_dragon(self):
        self.dragon['level'] += 1
        self.dragon['max_hp'] += 20
        self.dragon['hp'] = self.dragon['max_hp']
        self.dragon['attack'] += 5
        self.dragon['defense'] += 3
        self.dragon['experience'] = 0
        
        print(f"🎉 {self.dragon['name']} leveled up to level {self.dragon['level']}!")
        self.score += 50
    
    def battle_system(self):
        if self.dragon['energy'] < 30:
            print(f"{self.dragon['name']} is too tired to battle!")
            return
        
        # Create opponent
        enemy_types = ['Wild Drake', 'Forest Wyrm', 'Mountain Dragon', 'Shadow Beast']
        enemy_name = random.choice(enemy_types)
        enemy_level = max(1, self.dragon['level'] + random.randint(-1, 2))
        
        enemy = {
            'name': enemy_name,
            'level': enemy_level,
            'hp': 80 + (enemy_level * 20),
            'attack': 15 + (enemy_level * 5),
            'defense': 10 + (enemy_level * 3)
        }
        
        print(f"\n⚔️ Battle: {self.dragon['name']} vs {enemy['name']} (Level {enemy_level})")
        
        while self.dragon['hp'] > 0 and enemy['hp'] > 0:
            print(f"\n{self.dragon['name']}: {self.dragon['hp']}/{self.dragon['max_hp']} HP")
            print(f"{enemy['name']}: {enemy['hp']} HP")
            
            print("1. Attack ⚔️")
            print("2. Defend 🛡️")
            print("3. Special Attack 🌟")
            
            choice = input("Choose action: ").strip()
            
            # Player turn
            if choice == '1':
                damage = max(1, self.dragon['attack'] - enemy['defense'] + random.randint(-3, 3))
                enemy['hp'] -= damage
                print(f"{self.dragon['name']} attacks for {damage} damage!")
            
            elif choice == '2':
                print(f"{self.dragon['name']} defends!")
                damage_reduction = 0.5
            
            elif choice == '3':
                damage = max(1, int(self.dragon['attack'] * 1.5) - enemy['defense'])
                enemy['hp'] -= damage
                print(f"{self.dragon['name']} uses special attack for {damage} damage!")
            
            else:
                damage = max(1, self.dragon['attack'] - enemy['defense'])
                enemy['hp'] -= damage
                print(f"{self.dragon['name']} attacks for {damage} damage!")
            
            if enemy['hp'] <= 0:
                break
            
            # Enemy turn
            enemy_damage = max(1, enemy['attack'] - self.dragon['defense'] + random.randint(-2, 2))
            if choice == '2':
                enemy_damage = int(enemy_damage * 0.5)
            
            self.dragon['hp'] -= enemy_damage
            print(f"{enemy['name']} attacks for {enemy_damage} damage!")
            
            time.sleep(1)
        
        # Battle results
        if self.dragon['hp'] <= 0:
            print(f"\n💀 {self.dragon['name']} was defeated!")
            self.dragon['hp'] = 10
            self.dragon['happiness'] = max(0, self.dragon['happiness'] - 20)
        else:
            print(f"\n🎉 Victory! {self.dragon['name']} defeated {enemy['name']}!")
            exp_gained = enemy_level * 25
            self.dragon['experience'] += exp_gained
            self.battles_won += 1
            self.score += enemy_level * 30
            
            print(f"Gained {exp_gained} experience!")
            
            if self.dragon['experience'] >= self.dragon['level'] * 50:
                self.level_up_dragon()
        
        self.dragon['energy'] -= 30
    
    def daily_update(self):
        self.dragon['hunger'] = min(100, self.dragon['hunger'] + 15)
        self.dragon['energy'] = min(100, self.dragon['energy'] + 20)
        if self.dragon['happiness'] > 10:
            self.dragon['happiness'] -= 5
        
        self.day += 1
        print(f"🌅 Day {self.day} begins!")
    
    def play(self):
        print("🐉 Welcome to DRAGON TAMER ADVENTURE! 🐉")
        print("Raise and battle with your dragon companion!")
        print("Press Enter to start...")
        input()
        
        self.create_dragon()
        
        while True:
            self.clear_screen()
            print("🐉 DRAGON TAMER ADVENTURE 🐉")
            print(f"Day: {self.day} | Score: {self.score} | Battles Won: {self.battles_won}")
            
            self.display_dragon_stats()
            
            print("\n📋 What would you like to do?")
            print("1. Care for Dragon 🐉")
            print("2. Battle Wild Dragons ⚔️")
            print("3. Rest (Next Day) 😴")
            print("4. Quit Game 👋")
            
            choice = input("Choose action: ").strip()
            
            if choice == '1':
                self.care_for_dragon()
                time.sleep(2)
            elif choice == '2':
                self.battle_system()
                time.sleep(2)
            elif choice == '3':
                self.daily_update()
                time.sleep(1)
            elif choice == '4':
                break
            else:
                print("Invalid choice!")
                time.sleep(1)
        
        print(f"Final Score: {self.score}")
        print(f"Days Survived: {self.day}")
        print(f"Battles Won: {self.battles_won}")
        return self.score

# TIME HEIST CHRONICLES GAME CLASS
class TimeHeist:
    def __init__(self):
        self.time_energy = 100
        self.score = 0
        self.items_stolen = []
        self.heat_level = 0
        self.day = 1
        
        # Time periods
        self.time_periods = {
            "Ancient Egypt": {"difficulty": 2, "targets": ["Golden Scarab", "Pharaoh's Crown"]},
            "Medieval Castle": {"difficulty": 3, "targets": ["Royal Sword", "Dragon's Gem"]},
            "Wild West": {"difficulty": 2, "targets": ["Gold Nuggets", "Sheriff's Badge"]},
            "Future City": {"difficulty": 4, "targets": ["Quantum Core", "AI Chip"]}
        }
        
        self.current_mission = None
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_status(self):
        self.clear_screen()
        print("⏰ TIME HEIST CHRONICLES ⏰")
        print("=" * 40)
        print(f"Day: {self.day}")
        print(f"Time Energy: {self.time_energy}/100 ⚡")
        print(f"Heat Level: {self.heat_level}/100 🚨")
        print(f"Score: {self.score} ⭐")
        print(f"Items Stolen: {len(self.items_stolen)}")
        
        if self.items_stolen:
            print("Recent Heists:")
            for item in self.items_stolen[-3:]:
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
            print(f"{i}. {period} - {difficulty}")
        
        try:
            choice = int(input("Choose destination (0 to cancel): "))
            if choice == 0:
                return False
            
            period = periods[choice - 1]
            self.time_energy -= 20
            
            print(f"\n🌀 Traveling to {period}...")
            time.sleep(1)
            
            self.start_heist_mission(period)
            return True
            
        except (ValueError, IndexError):
            print("Invalid choice!")
            return False
    
    def start_heist_mission(self, period):
        period_data = self.time_periods[period]
        target = random.choice(period_data["targets"])
        
        self.current_mission = {
            "period": period,
            "target": target,
            "difficulty": period_data["difficulty"],
            "progress": 0,
            "max_progress": 100
        }
        
        print(f"\n🎯 MISSION: Steal {target} from {period}")
        self.execute_heist()
    
    def execute_heist(self):
        mission = self.current_mission
        
        while mission["progress"] < mission["max_progress"]:
            print(f"\n🏛️ {mission['period']} - Heist Progress: {mission['progress']}/100")
            print(f"Target: {mission['target']}")
            print(f"Heat Level: {self.heat_level}/100")
            
            print("\n📋 Choose approach:")
            print("1. Stealth Approach 🥷")
            print("2. Tech Approach 💻")
            print("3. Social Engineering 🎭")
            print("4. Abort Mission 🏃")
            
            choice = input("Choose action: ").strip()
            
            if choice == '1':
                self.stealth_approach()
            elif choice == '2':
                self.tech_approach()
            elif choice == '3':
                self.social_approach()
            elif choice == '4':
                print("Mission aborted!")
                self.current_mission = None
                return
            else:
                print("Invalid choice!")
                continue
            
            if mission["progress"] >= mission["max_progress"]:
                self.complete_heist()
                return
            
            if self.heat_level >= 100:
                self.caught_by_authorities()
                return
    
    def stealth_approach(self):
        mission = self.current_mission
        success_chance = 0.7
        
        if random.random() < success_chance:
            progress = random.randint(20, 35)
            mission["progress"] += progress
            heat_increase = random.randint(0, 10)
            print(f"🥷 Stealth successful! Progress: +{progress}")
        else:
            heat_increase = random.randint(15, 25)
            print("🚨 You were spotted! Security increased!")
        
        self.heat_level = min(100, self.heat_level + heat_increase)
        self.time_energy -= 5
    
    def tech_approach(self):
        mission = self.current_mission
        success_chance = 0.6
        
        if random.random() < success_chance:
            progress = random.randint(25, 40)
            mission["progress"] += progress
            print(f"💻 Tech hack successful! Progress: +{progress}")
            heat_increase = random.randint(5, 15)
        else:
            print("💥 Tech approach failed! Alarms triggered!")
            heat_increase = random.randint(20, 30)
        
        self.heat_level = min(100, self.heat_level + heat_increase)
        self.time_energy -= 10
    
    def social_approach(self):
        mission = self.current_mission
        success_chance = 0.5
        
        if random.random() < success_chance:
            progress = random.randint(15, 25)
            mission["progress"] += progress
            print(f"🎭 Social engineering worked! Progress: +{progress}")
            heat_increase = random.randint(0, 8)
        else:
            print("😤 Your cover was blown!")
            heat_increase = random.randint(10, 20)
        
        self.heat_level = min(100, self.heat_level + heat_increase)
        self.time_energy -= 3
    
    def complete_heist(self):
        mission = self.current_mission
        
        print(f"\n🎉 HEIST SUCCESSFUL! 🎉")
        print(f"You stole the {mission['target']}!")
        
        # Add stolen item
        stolen_item = {
            "name": mission['target'],
            "era": mission['period'],
            "value": mission['difficulty'] * 25
        }
        self.items_stolen.append(stolen_item)
        
        # Calculate score
        score_gain = mission['difficulty'] * 50
        self.score += score_gain
        
        print(f"Score gained: +{score_gain}")
        self.current_mission = None
        time.sleep(2)
    
    def caught_by_authorities(self):
        print(f"\n🚨 CAUGHT BY AUTHORITIES! 🚨")
        print("You must escape or face consequences!")
        
        print("Escape options:")
        print("1. Time Jump Escape (30 energy)")
        print("2. Fight Your Way Out (20 energy)")
        print("3. Surrender")
        
        choice = input("Choose escape method: ").strip()
        
        if choice == '1' and self.time_energy >= 30:
            self.time_energy -= 30
            if random.random() < 0.8:
                print("✅ Time jump successful! You escaped!")
                self.heat_level = max(0, self.heat_level - 40)
            else:
                print("❌ Time jump failed! Captured!")
                self.capture_consequences()
        
        elif choice == '2' and self.time_energy >= 20:
            self.time_energy -= 20
            if random.random() < 0.6:
                print("✅ You fought your way out!")
                self.heat_level = max(0, self.heat_level - 30)
            else:
                print("❌ Fighting failed! Captured!")
                self.capture_consequences()
        
        else:
            print("You surrender or lack energy!")
            self.capture_consequences()
        
        self.current_mission = None
    
    def capture_consequences(self):
        print("\n⛓️ CAPTURE CONSEQUENCES:")
        
        # Lose some items
        if self.items_stolen:
            lost_count = min(2, len(self.items_stolen))
            for _ in range(lost_count):
                lost_item = self.items_stolen.pop()
                print(f"Lost: {lost_item['name']}")
        
        # Score penalty
        score_loss = min(100, self.score // 4)
        self.score = max(0, self.score - score_loss)
        print(f"Score penalty: -{score_loss}")
        
        # Energy loss
        self.time_energy = max(20, self.time_energy - 30)
        print(f"Energy drained!")
        
        time.sleep(2)
    
    def rest_and_recover(self):
        print("\n😴 Resting at temporal hideout...")
        
        # Recover energy
        energy_recovery = random.randint(25, 40)
        self.time_energy = min(100, self.time_energy + energy_recovery)
        
        # Reduce heat
        heat_reduction = random.randint(15, 25)
        self.heat_level = max(0, self.heat_level - heat_reduction)
        
        self.day += 1
        
        print(f"⚡ Energy recovered: +{energy_recovery}")
        print(f"🚨 Heat reduced: -{heat_reduction}")
        print(f"📅 Day {self.day} begins!")
        
        time.sleep(2)
    
    def play(self):
        print("⏰ Welcome to TIME HEIST CHRONICLES! ⏰")
        print("Steal legendary artifacts across time!")
        print("Press Enter to start...")
        input()
        
        while True:
            self.display_status()
            
            print("\n⏰ TIME HEIST OPERATIONS")
            print("1. Travel Through Time 🌀")
            print("2. Rest & Recover 😴")
            print("3. View Stolen Items 💎")
            print("4. Quit Game 👋")
            
            choice = input("Choose action: ").strip()
            
            if choice == '1':
                self.time_travel()
            elif choice == '2':
                self.rest_and_recover()
            elif choice == '3':
                self.view_stolen_items()
            elif choice == '4':
                break
            else:
                print("Invalid choice!")
                time.sleep(1)
        
        print(f"Final Score: {self.score}")
        print(f"Items Stolen: {len(self.items_stolen)}")
        print(f"Days Active: {self.day}")
        return self.score
    
    def view_stolen_items(self):
        if not self.items_stolen:
            print("No items stolen yet!")
        else:
            print("\n💎 STOLEN ARTIFACTS:")
            total_value = 0
            for item in self.items_stolen:
                print(f"• {item['name']} from {item['era']} (Value: {item['value']})")
                total_value += item['value']
            print(f"Total Value: {total_value}")
        
        input("Press Enter to continue...")

# MAIN EXECUTION
def main():
    arcade = GameLauncher()
    arcade.main_loop()

if __name__ == "__main__":
    main()
