"""
Math Wizard Game - Educational Mathematics Game
Part of EduVerse: The 10-Game Arcade Platform
"""

import random

class MathWizardGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
    
    def generate_question(self, level):
        """Generate math questions based on level"""
        if level == 1:
            # Basic addition
            a, b = random.randint(1, 10), random.randint(1, 10)
            return f"{a} + {b}", a + b, f"Add {a} and {b}"
            
        elif level == 2:
            # Addition and subtraction
            a, b = random.randint(1, 20), random.randint(1, 20)
            if random.choice([True, False]):
                return f"{a} + {b}", a + b, f"Add {a} and {b}"
            else:
                if a < b: a, b = b, a  # Ensure positive result
                return f"{a} - {b}", a - b, f"Subtract {b} from {a}"
                
        elif level == 3:
            # Multiplication
            a, b = random.randint(1, 12), random.randint(1, 12)
            return f"{a} × {b}", a * b, f"Multiply {a} by {b}"
            
        elif level == 4:
            # Division
            b = random.randint(2, 12)
            answer = random.randint(1, 12)
            a = b * answer  # Ensure clean division
            return f"{a} ÷ {b}", answer, f"Divide {a} by {b}"
            
        else:  # level 5
            # Powers
            base = random.randint(2, 8)
            exp = random.randint(2, 3)
            return f"{base}^{exp}", base ** exp, f"{base} to the power of {exp}"
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n🧮 MATH WIZARD - LEVEL {level}")
        print("="*35)
        
        level_descriptions = {
            1: "Basic Addition (1-10)",
            2: "Addition & Subtraction (1-20)", 
            3: "Multiplication Tables (1-12)",
            4: "Division Practice (1-12)",
            5: "Powers & Exponents (2-8)"
        }
        
        print(f"📚 {level_descriptions[level]}")
        print("Answer 5 questions to advance!")
        print("-" * 35)
        
        level_score = 0
        questions_correct = 0
        
        for q in range(5):
            question, correct_answer, hint = self.generate_question(level)
            print(f"\n❓ Question {q+1}: {question} = ?")
            
            # Give player 3 attempts
            attempts = 0
            while attempts < 3:
                try:
                    user_input = input("Your answer (or 'hint' for help): ").strip()
                    
                    if user_input.lower() == 'hint':
                        print(f"💡 Hint: {hint}")
                        continue
                    
                    user_answer = float(user_input)
                    
                    if abs(user_answer - correct_answer) < 0.01:
                        points = 100 - (attempts * 20)  # Less points for more attempts
                        if self.streak > 0:
                            points += self.streak * 10  # Streak bonus
                        
                        level_score += points
                        questions_correct += 1
                        self.streak += 1
                        
                        print(f"✅ Correct! +{points} points")
                        if self.streak > 1:
                            print(f"🔥 Streak: {self.streak}!")
                        break
                    else:
                        attempts += 1
                        if attempts < 3:
                            print(f"❌ Try again! ({3-attempts} attempts left)")
                        else:
                            print(f"❌ The answer was {correct_answer}")
                            self.streak = 0
                            
                except ValueError:
                    attempts += 1
                    if attempts < 3:
                        print(f"❌ Please enter a valid number! ({3-attempts} attempts left)")
                    else:
                        print(f"❌ The answer was {correct_answer}")
                        self.streak = 0
        
        print(f"\n📊 LEVEL {level} RESULTS:")
        print(f"✅ Correct Answers: {questions_correct}/5")
        print(f"🏆 Level Score: {level_score}")
        
        # Need at least 3/5 to advance
        if questions_correct >= 3:
            print("🎉 Level Passed! Well done!")
            return level_score
        else:
            print("📚 Keep practicing! You need 3/5 to advance.")
            retry = input("Try this level again? (y/n): ").lower()
            if retry == 'y':
                return self.play_level(level)  # Retry same level
            else:
                return level_score
    
    def play(self):
        """Main game loop"""
        print("\n🧮 WELCOME TO MATH WIZARD!")
        print("🎯 Master mathematics through 5 challenging levels!")
        print("🏆 Earn points and build streaks for bonus scores!")
        
        input("\nPress Enter to begin your mathematical journey...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing Math Wizard!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've completed all Math Wizard levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                
                if total_score >= 2000:
                    print("🌟 MATH GENIUS! Perfect performance!")
                elif total_score >= 1500:
                    print("🧮 MATH MASTER! Excellent work!")
                elif total_score >= 1000:
                    print("📊 MATH SCHOLAR! Great job!")
                else:
                    print("📚 MATH STUDENT! Keep practicing!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
