"""
Target Practice Game - Fun Arcade Game
Part of EduVerse: 10-Game Arcade Platform
"""

import random
import time

class TargetPracticeGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
        self.total_shots = 0
        self.hits = 0
    
    def generate_target(self, level):
        """Generate target based on difficulty level"""
        if level == 1:
            # Large targets, easy to hit
            target_size = random.randint(8, 10)
            target_distance = random.randint(1, 3)
            wind_factor = 0
        elif level == 2:
            # Medium targets
            target_size = random.randint(6, 8)
            target_distance = random.randint(2, 4)
            wind_factor = random.randint(-1, 1)
        elif level == 3:
            # Small targets
            target_size = random.randint(4, 6)
            target_distance = random.randint(3, 5)
            wind_factor = random.randint(-2, 2)
        elif level == 4:
            # Moving targets
            target_size = random.randint(3, 5)
            target_distance = random.randint(4, 6)
            wind_factor = random.randint(-3, 3)
            moving = True
        else:  # level 5
            # Expert level - small, far, windy, moving
            target_size = random.randint(2, 4)
            target_distance = random.randint(5, 8)
            wind_factor = random.randint(-4, 4)
            moving = True
        
        return {
            'size': target_size,
            'distance': target_distance,
            'wind': wind_factor,
            'moving': level >= 4,
            'position': random.randint(1, 10)
        }
    
    def display_target(self, target):
        """Display the target visually"""
        print("\n" + "="*50)
        print("🎯 TARGET RANGE")
        print("="*50)
        
        # Show target info
        print(f"📏 Target Size: {target['size']}/10")
        print(f"📐 Distance: {target['distance']} units")
        if target['wind'] != 0:
            wind_dir = "➡️" if target['wind'] > 0 else "⬅️"
            print(f"💨 Wind: {wind_dir} {abs(target['wind'])} mph")
        if target['moving']:
            print("🏃 Target is MOVING!")
        
        # Visual representation
        print("\n🎯 TARGET FIELD:")
        field = [" "] * 20
        
        # Place target
        target_pos = target['position']
        target_char = "🎯" if target['size'] >= 6 else "🔴" if target['size'] >= 4 else "⚫"
        
        if target_pos < len(field):
            field[target_pos] = target_char
        
        print("".join(field))
        print("1234567890123456789")  # Position markers
        print("="*50)
    
    def calculate_hit(self, aim_position, target, shot_power):
        """Calculate if shot hits target"""
        target_pos = target['position']
        target_size = target['size']
        wind_effect = target['wind'] * 0.3
        distance_effect = target['distance'] * 0.1
        
        # Adjust aim for wind and distance
        actual_position = aim_position + wind_effect + distance_effect
        
        # Check if hit
        hit_range = target_size / 2
        distance_from_target = abs(actual_position - target_pos)
        
        if distance_from_target <= hit_range:
            # Calculate hit quality
            if distance_from_target <= hit_range * 0.3:
                return "bullseye", 150  # Perfect hit
            elif distance_from_target <= hit_range * 0.6:
                return "hit", 100      # Good hit
            else:
                return "graze", 50     # Grazing hit
        else:
            return "miss", 0
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n🎯 TARGET PRACTICE - LEVEL {level}")
        print("="*40)
        
        level_descriptions = {
            1: "Basic Training - Large stationary targets",
            2: "Intermediate - Medium targets with light wind",
            3: "Advanced - Small targets with wind",
            4: "Expert - Moving targets with strong wind",
            5: "Master - Ultimate challenge!"
        }
        
        print(f"🏹 {level_descriptions[level]}")
        print("Hit 5 targets to advance!")
        print("-" * 40)
        
        level_score = 0
        targets_hit = 0
        shots_taken = 0
        
        for shot in range(5):
            target = self.generate_target(level)
            self.display_target(target)
            
            print(f"\n🏹 SHOT {shot + 1}/5")
            
            # Get player input
            try:
                print("Aim your shot:")
                aim_pos = float(input("Position (1-10): "))
                power = int(input("Power (1-10): "))
                
                if not (1 <= aim_pos <= 10) or not (1 <= power <= 10):
                    print("❌ Invalid input! Shot goes wide!")
                    result, points = "miss", 0
                else:
                    result, points = self.calculate_hit(aim_pos, target, power)
                
                shots_taken += 1
                self.total_shots += 1
                
                # Display result
                if result == "bullseye":
                    print("🎯 BULLSEYE! Perfect shot!")
                    targets_hit += 1
                    self.hits += 1
                    self.streak += 1
                    if self.streak > 1:
                        points += self.streak * 10
                        print(f"🔥 Streak bonus: +{self.streak * 10}")
                elif result == "hit":
                    print("✅ HIT! Nice shooting!")
                    targets_hit += 1
                    self.hits += 1
                    self.streak += 1
                elif result == "graze":
                    print("😐 Grazed the target!")
                    self.streak = 0
                else:
                    print("❌ MISS! Better luck next time!")
                    self.streak = 0
                
                level_score += points
                print(f"Points earned: {points}")
                
            except ValueError:
                print("❌ Invalid input! Shot goes wild!")
                shots_taken += 1
                self.total_shots += 1
                self.streak = 0
            
            if shot < 4:  # Don't pause after last shot
                input("\nPress Enter for next shot...")
        
        # Level results
        accuracy = (targets_hit / shots_taken * 100) if shots_taken > 0 else 0
        print(f"\n📊 LEVEL {level} RESULTS:")
        print(f"🎯 Targets Hit: {targets_hit}/5")
        print(f"📈 Accuracy: {accuracy:.1f}%")
        print(f"🏆 Level Score: {level_score}")
        
        # Need at least 3/5 hits to advance
        if targets_hit >= 3:
            print("🎉 Level Passed! Great shooting!")
            return level_score
        else:
            print("🎯 Keep practicing! You need 3/5 hits to advance.")
            retry = input("Try this level again? (y/n): ").lower()
            if retry == 'y':
                return self.play_level(level)
            else:
                return level_score
    
    def play(self):
        """Main game loop"""
        print("\n🎯 WELCOME TO TARGET PRACTICE!")
        print("🏹 Test your aim and reflexes across 5 challenging levels!")
        print("🎯 Account for wind, distance, and moving targets!")
        
        input("\nPress Enter to enter the shooting range...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing Target Practice!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've completed all Target Practice levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                
                overall_accuracy = (self.hits / self.total_shots * 100) if self.total_shots > 0 else 0
                print(f"🎯 Overall Accuracy: {overall_accuracy:.1f}%")
                
                if overall_accuracy >= 90:
                    print("🌟 SHARPSHOOTER! Incredible accuracy!")
                elif overall_accuracy >= 75:
                    print("🎯 MARKSMAN! Excellent shooting!")
                elif overall_accuracy >= 60:
                    print("🏹 ARCHER! Good aim!")
                else:
                    print("🎯 TRAINEE! Keep practicing!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
