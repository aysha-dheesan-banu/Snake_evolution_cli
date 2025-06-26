#!/usr/bin/env python3
"""
🚀 COSMIC DEFENDER 🚀
A space shooter game with ASCII graphics and power-ups
"""

import random
import time
import os
import sys
from threading import Thread
import keyboard

class CosmicDefender:
    def __init__(self):
        self.width = 80
        self.height = 20
        self.player_pos = self.width // 2
        self.player_char = "🚀"
        self.bullets = []
        self.enemies = []
        self.powerups = []
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False
        self.paused = False
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def spawn_enemy(self):
        if random.random() < 0.3 + (self.level * 0.1):
            enemy_type = random.choice(['👾', '🛸', '💀', '⚡'])
            self.enemies.append({
                'x': random.randint(0, self.width-1),
                'y': 0,
                'char': enemy_type,
                'health': 1 if enemy_type != '🛸' else 2
            })
    
    def spawn_powerup(self):
        if random.random() < 0.05:
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
    
    def update_bullets(self):
        self.bullets = [b for b in self.bullets if b['y'] > 0]
        for bullet in self.bullets:
            bullet['y'] -= 1
    
    def update_enemies(self):
        for enemy in self.enemies[:]:
            enemy['y'] += 1
            if enemy['y'] >= self.height:
                self.enemies.remove(enemy)
                self.lives -= 1
    
    def update_powerups(self):
        for powerup in self.powerups[:]:
            powerup['y'] += 1
            if powerup['y'] >= self.height:
                self.powerups.remove(powerup)
    
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
            # Multi-shot for next 10 shots
            for i in range(3):
                self.bullets.append({'x': self.player_pos + i - 1, 'y': self.height - 2})
        elif powerup_type == '🛡️':
            self.lives += 2
        elif powerup_type == '💥':
            # Clear all enemies
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
        print("=" * (self.width + 2))
        for row in field:
            print("|" + "".join(row) + "|")
        print("=" * (self.width + 2))
        
        # Draw UI
        print(f"Score: {self.score} | Lives: {'❤️ ' * self.lives} | Level: {self.level}")
        print("Controls: A/D - Move, SPACE - Shoot, P - Pause, Q - Quit")
        
        if self.paused:
            print("\n*** GAME PAUSED - Press P to continue ***")
    
    def game_loop(self):
        print("🚀 COSMIC DEFENDER 🚀")
        print("Defend Earth from alien invasion!")
        print("Press any key to start...")
        input()
        
        frame_count = 0
        
        while not self.game_over and self.lives > 0:
            if not self.paused:
                # Game logic
                self.spawn_enemy()
                self.spawn_powerup()
                self.update_bullets()
                self.update_enemies()
                self.update_powerups()
                self.check_collisions()
                
                # Level progression
                if self.score > 0 and self.score % 100 == 0 and frame_count % 60 == 0:
                    self.level += 1
                
                frame_count += 1
            
            self.draw_game()
            
            # Simple input handling (non-blocking simulation)
            print("\nEnter command (a/d/space/p/q): ", end="")
            try:
                # Simulate real-time input with timeout
                import select
                import sys
                
                if select.select([sys.stdin], [], [], 0.1)[0]:
                    command = input().lower().strip()
                    if command == 'a':
                        self.move_player('left')
                    elif command == 'd':
                        self.move_player('right')
                    elif command == ' ' or command == 'space':
                        self.shoot()
                    elif command == 'p':
                        self.paused = not self.paused
                    elif command == 'q':
                        self.game_over = True
            except:
                # Fallback for systems without select
                time.sleep(0.2)
            
            time.sleep(0.1)
        
        self.clear_screen()
        if self.lives <= 0:
            print("💥 GAME OVER! 💥")
        else:
            print("👋 Thanks for playing!")
        
        print(f"Final Score: {self.score}")
        print(f"Level Reached: {self.level}")

def main():
    game = CosmicDefender()
    game.game_loop()

if __name__ == "__main__":
    main()
