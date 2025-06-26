#!/usr/bin/env python3
"""
🌈 NEON MAZE RUNNER 🌈
Navigate through procedurally generated mazes with neon effects
"""

import random
import time
import os
from collections import deque

class NeonMaze:
    def __init__(self, width=25, height=15):
        self.width = width
        self.height = height
        self.maze = []
        self.player_pos = [1, 1]
        self.exit_pos = [width-2, height-2]
        self.collectibles = []
        self.score = 0
        self.time_left = 60
        self.level = 1
        self.trail = deque(maxlen=5)  # Player trail effect
        self.power_mode = False
        self.power_timer = 0
        
        # Neon colors (ANSI codes)
        self.colors = {
            'wall': '\033[95m█\033[0m',      # Magenta
            'path': '\033[90m \033[0m',      # Dark gray
            'player': '\033[96m●\033[0m',    # Cyan
            'exit': '\033[92m★\033[0m',      # Green
            'gem': '\033[93m◆\033[0m',       # Yellow
            'power': '\033[91m⚡\033[0m',     # Red
            'trail': '\033[94m·\033[0m',     # Blue
            'neon_wall': '\033[95m▓\033[0m', # Neon wall
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def generate_maze(self):
        # Initialize maze with walls
        self.maze = [['█' for _ in range(self.width)] for _ in range(self.height)]
        
        # Recursive backtracking maze generation
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
        
        # Add some random openings for complexity
        for _ in range(self.level * 2):
            x, y = random.randint(1, self.width-2), random.randint(1, self.height-2)
            if self.maze[y][x] == '█':
                neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
                if sum(1 for nx, ny in neighbors if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == ' ') >= 2:
                    self.maze[y][x] = ' '
        
        # Place collectibles
        self.place_collectibles()
    
    def place_collectibles(self):
        self.collectibles = []
        gem_count = 5 + self.level
        power_count = 2
        
        for _ in range(gem_count):
            while True:
                x, y = random.randint(1, self.width-2), random.randint(1, self.height-2)
                if (self.maze[y][x] == ' ' and [x, y] != self.player_pos and 
                    [x, y] != self.exit_pos):
                    self.collectibles.append({'pos': [x, y], 'type': 'gem', 'value': 10})
                    break
        
        for _ in range(power_count):
            while True:
                x, y = random.randint(1, self.width-2), random.randint(1, self.height-2)
                if (self.maze[y][x] == ' ' and [x, y] != self.player_pos and 
                    [x, y] != self.exit_pos and 
                    not any(c['pos'] == [x, y] for c in self.collectibles)):
                    self.collectibles.append({'pos': [x, y], 'type': 'power', 'value': 50})
                    break
    
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
            # Add current position to trail
            self.trail.append(self.player_pos.copy())
            self.player_pos = new_pos
            
            # Check for collectibles
            for collectible in self.collectibles[:]:
                if collectible['pos'] == self.player_pos:
                    self.score += collectible['value']
                    if collectible['type'] == 'power':
                        self.power_mode = True
                        self.power_timer = 10
                    self.collectibles.remove(collectible)
    
    def update_game(self):
        self.time_left -= 0.1
        if self.power_timer > 0:
            self.power_timer -= 0.1
            if self.power_timer <= 0:
                self.power_mode = False
    
    def draw_maze(self):
        self.clear_screen()
        
        # Draw title with neon effect
        print("\033[95m" + "="*50 + "\033[0m")
        print("\033[96m🌈 NEON MAZE RUNNER 🌈\033[0m")
        print("\033[95m" + "="*50 + "\033[0m")
        
        # Draw maze
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                pos = [x, y]
                
                if pos == self.player_pos:
                    if self.power_mode:
                        row += '\033[91m●\033[0m'  # Red when powered
                    else:
                        row += self.colors['player']
                elif pos == self.exit_pos:
                    row += self.colors['exit']
                elif pos in [c['pos'] for c in self.collectibles]:
                    collectible = next(c for c in self.collectibles if c['pos'] == pos)
                    if collectible['type'] == 'gem':
                        row += self.colors['gem']
                    else:
                        row += self.colors['power']
                elif pos in list(self.trail):
                    row += self.colors['trail']
                elif self.maze[y][x] == '█':
                    # Neon wall effect
                    if random.random() < 0.1:
                        row += self.colors['neon_wall']
                    else:
                        row += self.colors['wall']
                else:
                    row += self.colors['path']
            print(row)
        
        # Draw UI
        print("\033[95m" + "="*50 + "\033[0m")
        print(f"\033[93mScore: {self.score}\033[0m | \033[92mTime: {self.time_left:.1f}s\033[0m | \033[96mLevel: {self.level}\033[0m")
        
        if self.power_mode:
            print(f"\033[91m⚡ POWER MODE: {self.power_timer:.1f}s ⚡\033[0m")
        
        print("\033[94mControls: W/A/S/D - Move, Q - Quit\033[0m")
        print(f"\033[95mCollect all gems (◆) and reach the star (★)!\033[0m")
        print(f"\033[93mGems remaining: {len([c for c in self.collectibles if c['type'] == 'gem'])}\033[0m")
    
    def check_win_condition(self):
        # Win if player reaches exit and collected all gems
        gems_remaining = len([c for c in self.collectibles if c['type'] == 'gem'])
        return self.player_pos == self.exit_pos and gems_remaining == 0
    
    def next_level(self):
        self.level += 1
        self.time_left += 30  # Bonus time
        self.width = min(35, self.width + 2)
        self.height = min(25, self.height + 2)
        self.player_pos = [1, 1]
        self.exit_pos = [self.width-2, self.height-2]
        self.trail.clear()
        self.generate_maze()
    
    def game_loop(self):
        print("\033[96m🌈 Welcome to NEON MAZE RUNNER! 🌈\033[0m")
        print("Navigate through the glowing maze and collect all gems!")
        print("Press Enter to start...")
        input()
        
        self.generate_maze()
        
        while self.time_left > 0:
            self.draw_maze()
            
            if self.check_win_condition():
                print("\033[92m🎉 LEVEL COMPLETE! 🎉\033[0m")
                print(f"Bonus points: {int(self.time_left * 10)}")
                self.score += int(self.time_left * 10)
                time.sleep(2)
                self.next_level()
                continue
            
            print("\nEnter move (w/a/s/d/q): ", end="")
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
                
                self.update_game()
                
            except KeyboardInterrupt:
                break
        
        self.clear_screen()
        print("\033[95m" + "="*50 + "\033[0m")
        print("\033[96m🌈 GAME OVER! 🌈\033[0m")
        print(f"\033[93mFinal Score: {self.score}\033[0m")
        print(f"\033[92mLevels Completed: {self.level - 1}\033[0m")
        print("\033[95m" + "="*50 + "\033[0m")

def main():
    game = NeonMaze()
    game.game_loop()

if __name__ == "__main__":
    main()
