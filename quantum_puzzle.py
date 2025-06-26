#!/usr/bin/env python3
"""
🔮 QUANTUM PUZZLE MASTER 🔮
A mind-bending puzzle game with quantum mechanics simulation
"""

import random
import time
import os
import copy

class QuantumPuzzle:
    def __init__(self):
        self.grid_size = 4
        self.grid = []
        self.quantum_states = []  # Superposition states
        self.entangled_pairs = []  # Quantum entanglement
        self.score = 0
        self.moves = 0
        self.level = 1
        self.target_pattern = []
        self.quantum_energy = 100
        self.collapse_probability = 0.3
        
        # Quantum symbols
        self.symbols = {
            0: '⚫',  # Empty/void
            1: '🔵',  # Electron
            2: '🔴',  # Proton
            3: '🟡',  # Neutron
            4: '🟢',  # Photon
            5: '🟣',  # Quantum state
            6: '⚡',  # Energy
            7: '🌟',  # Entangled
        }
        
        self.colors = {
            'quantum': '\033[95m',
            'entangled': '\033[93m',
            'stable': '\033[92m',
            'unstable': '\033[91m',
            'reset': '\033[0m'
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def initialize_grid(self):
        """Initialize the quantum grid with random particles"""
        self.grid = [[random.randint(0, 4) for _ in range(self.grid_size)] 
                     for _ in range(self.grid_size)]
        
        # Create quantum superposition states
        self.quantum_states = []
        for _ in range(2 + self.level):
            x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            self.quantum_states.append({
                'pos': (x, y),
                'states': [random.randint(1, 4), random.randint(1, 4)],
                'collapsed': False
            })
        
        # Create entangled pairs
        self.entangled_pairs = []
        for _ in range(1 + self.level // 2):
            pos1 = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
            pos2 = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
            if pos1 != pos2:
                self.entangled_pairs.append([pos1, pos2])
        
        # Generate target pattern
        self.generate_target_pattern()
    
    def generate_target_pattern(self):
        """Generate the target pattern to achieve"""
        self.target_pattern = []
        pattern_type = random.choice(['line', 'square', 'cross', 'diagonal'])
        
        if pattern_type == 'line':
            # Horizontal or vertical line
            if random.choice([True, False]):
                row = random.randint(0, self.grid_size-1)
                self.target_pattern = [(i, row) for i in range(self.grid_size)]
            else:
                col = random.randint(0, self.grid_size-1)
                self.target_pattern = [(col, i) for i in range(self.grid_size)]
        
        elif pattern_type == 'square':
            # 2x2 square
            start_x, start_y = random.randint(0, self.grid_size-2), random.randint(0, self.grid_size-2)
            self.target_pattern = [(start_x+i, start_y+j) for i in range(2) for j in range(2)]
        
        elif pattern_type == 'cross':
            # Cross pattern
            center = self.grid_size // 2
            self.target_pattern = [(center, i) for i in range(self.grid_size)]
            self.target_pattern += [(i, center) for i in range(self.grid_size)]
            self.target_pattern = list(set(self.target_pattern))
        
        elif pattern_type == 'diagonal':
            # Diagonal line
            self.target_pattern = [(i, i) for i in range(self.grid_size)]
    
    def draw_grid(self):
        """Draw the quantum grid with special effects"""
        self.clear_screen()
        
        print(f"{self.colors['quantum']}🔮 QUANTUM PUZZLE MASTER 🔮{self.colors['reset']}")
        print("=" * 50)
        
        # Draw grid
        for y in range(self.grid_size):
            row = ""
            for x in range(self.grid_size):
                pos = (x, y)
                cell_value = self.grid[y][x]
                
                # Check if position is in quantum superposition
                quantum_state = next((qs for qs in self.quantum_states if qs['pos'] == pos), None)
                if quantum_state and not quantum_state['collapsed']:
                    if random.random() < 0.5:  # Flickering effect
                        symbol = self.symbols[quantum_state['states'][0]]
                    else:
                        symbol = self.symbols[quantum_state['states'][1]]
                    row += f"{self.colors['quantum']}{symbol}{self.colors['reset']} "
                
                # Check if position is entangled
                elif any(pos in pair for pair in self.entangled_pairs):
                    symbol = self.symbols[cell_value]
                    row += f"{self.colors['entangled']}{symbol}{self.colors['reset']} "
                
                # Check if position is part of target pattern
                elif pos in self.target_pattern:
                    symbol = self.symbols[cell_value]
                    if cell_value == 4:  # Correct particle in target
                        row += f"{self.colors['stable']}{symbol}{self.colors['reset']} "
                    else:
                        row += f"{self.colors['unstable']}{symbol}{self.colors['reset']} "
                
                else:
                    row += f"{self.symbols[cell_value]} "
            
            print(f"  {row}")
        
        print("=" * 50)
        print(f"Score: {self.score} | Moves: {self.moves} | Level: {self.level}")
        print(f"Quantum Energy: {self.quantum_energy}")
        print(f"Target: Fill pattern with {self.symbols[4]} (Photons)")
        
        # Show quantum states
        if self.quantum_states:
            print(f"\n{self.colors['quantum']}Quantum Superpositions:{self.colors['reset']}")
            for i, qs in enumerate(self.quantum_states):
                if not qs['collapsed']:
                    x, y = qs['pos']
                    states = [self.symbols[s] for s in qs['states']]
                    print(f"  Position ({x},{y}): {states[0]}|{states[1]}")
        
        # Show entangled pairs
        if self.entangled_pairs:
            print(f"\n{self.colors['entangled']}Entangled Pairs:{self.colors['reset']}")
            for i, pair in enumerate(self.entangled_pairs):
                print(f"  Pair {i+1}: {pair[0]} ↔ {pair[1]}")
    
    def make_move(self, x, y, action):
        """Make a quantum move"""
        if not (0 <= x < self.grid_size and 0 <= y < self.grid_size):
            return False
        
        self.moves += 1
        pos = (x, y)
        
        if action == 'rotate':
            # Rotate particle type
            self.grid[y][x] = (self.grid[y][x] + 1) % 5
            self.quantum_energy -= 5
        
        elif action == 'collapse':
            # Collapse quantum superposition
            quantum_state = next((qs for qs in self.quantum_states if qs['pos'] == pos), None)
            if quantum_state and not quantum_state['collapsed']:
                chosen_state = random.choice(quantum_state['states'])
                self.grid[y][x] = chosen_state
                quantum_state['collapsed'] = True
                self.quantum_energy -= 15
                self.score += 20
        
        elif action == 'entangle':
            # Create quantum entanglement effect
            for pair in self.entangled_pairs:
                if pos in pair:
                    other_pos = pair[1] if pair[0] == pos else pair[0]
                    ox, oy = other_pos
                    # Synchronize entangled particles
                    self.grid[oy][ox] = self.grid[y][x]
                    self.quantum_energy -= 10
                    self.score += 15
        
        elif action == 'teleport':
            # Quantum teleportation
            if self.quantum_energy >= 25:
                target_x = random.randint(0, self.grid_size-1)
                target_y = random.randint(0, self.grid_size-1)
                self.grid[target_y][target_x], self.grid[y][x] = self.grid[y][x], self.grid[target_y][target_x]
                self.quantum_energy -= 25
                self.score += 10
        
        # Random quantum fluctuations
        if random.random() < self.collapse_probability:
            self.quantum_fluctuation()
        
        return True
    
    def quantum_fluctuation(self):
        """Random quantum events"""
        event = random.choice(['collapse', 'entangle', 'energy'])
        
        if event == 'collapse':
            # Random collapse
            uncollapsed = [qs for qs in self.quantum_states if not qs['collapsed']]
            if uncollapsed:
                qs = random.choice(uncollapsed)
                x, y = qs['pos']
                self.grid[y][x] = random.choice(qs['states'])
                qs['collapsed'] = True
        
        elif event == 'entangle':
            # Create new entanglement
            if len(self.entangled_pairs) < 3:
                pos1 = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
                pos2 = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
                if pos1 != pos2:
                    self.entangled_pairs.append([pos1, pos2])
        
        elif event == 'energy':
            # Energy fluctuation
            self.quantum_energy += random.randint(-10, 15)
            self.quantum_energy = max(0, min(100, self.quantum_energy))
    
    def check_win_condition(self):
        """Check if target pattern is achieved"""
        for x, y in self.target_pattern:
            if self.grid[y][x] != 4:  # Not a photon
                return False
        return True
    
    def next_level(self):
        """Advance to next level"""
        self.level += 1
        self.grid_size = min(6, self.grid_size + 1)
        self.quantum_energy = 100
        self.collapse_probability += 0.05
        self.score += 100 * self.level
        self.initialize_grid()
    
    def show_help(self):
        """Show game help"""
        print(f"\n{self.colors['quantum']}QUANTUM MECHANICS:{self.colors['reset']}")
        print("• Rotate (r): Change particle type")
        print("• Collapse (c): Collapse quantum superposition")
        print("• Entangle (e): Activate entanglement effects")
        print("• Teleport (t): Quantum teleportation")
        print("• Help (h): Show this help")
        print("• Quit (q): Exit game")
        print(f"\n{self.colors['stable']}Goal: Fill the target pattern with Photons {self.symbols[4]}{self.colors['reset']}")
        input("\nPress Enter to continue...")
    
    def game_loop(self):
        """Main game loop"""
        print(f"{self.colors['quantum']}🔮 Welcome to QUANTUM PUZZLE MASTER! 🔮{self.colors['reset']}")
        print("Manipulate quantum particles to solve puzzles!")
        print("Press Enter to start...")
        input()
        
        self.initialize_grid()
        
        while self.quantum_energy > 0:
            self.draw_grid()
            
            if self.check_win_condition():
                print(f"\n{self.colors['stable']}🎉 QUANTUM PUZZLE SOLVED! 🎉{self.colors['reset']}")
                print(f"Level {self.level} completed!")
                time.sleep(2)
                self.next_level()
                continue
            
            print(f"\nEnter command (format: x y action) or 'h' for help: ", end="")
            try:
                command = input().strip().lower()
                
                if command == 'h':
                    self.show_help()
                elif command == 'q':
                    break
                else:
                    parts = command.split()
                    if len(parts) == 3:
                        try:
                            x, y = int(parts[0]), int(parts[1])
                            action = parts[2]
                            if action in ['r', 'rotate']:
                                action = 'rotate'
                            elif action in ['c', 'collapse']:
                                action = 'collapse'
                            elif action in ['e', 'entangle']:
                                action = 'entangle'
                            elif action in ['t', 'teleport']:
                                action = 'teleport'
                            
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
        print(f"{self.colors['quantum']}🔮 QUANTUM GAME OVER! 🔮{self.colors['reset']}")
        print(f"Final Score: {self.score}")
        print(f"Levels Completed: {self.level - 1}")
        print("Thanks for exploring the quantum realm!")

def main():
    game = QuantumPuzzle()
    game.game_loop()

if __name__ == "__main__":
    main()
