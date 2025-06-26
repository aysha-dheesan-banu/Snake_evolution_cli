"""
Puzzle Master Game - Fun Brain Teaser Game
Part of EduVerse: 10-Game Arcade Platform
"""

import random

class PuzzleMasterGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
    
    def generate_number_sequence(self, level):
        """Generate number sequence puzzles"""
        if level == 1:
            # Simple arithmetic sequences
            start = random.randint(1, 10)
            step = random.randint(1, 5)
            sequence = [start + i * step for i in range(4)]
            answer = start + 4 * step
            hint = f"Add {step} each time"
        elif level == 2:
            # Multiplication sequences
            start = random.randint(2, 5)
            multiplier = random.randint(2, 3)
            sequence = [start * (multiplier ** i) for i in range(4)]
            answer = start * (multiplier ** 4)
            hint = f"Multiply by {multiplier} each time"
        else:
            # Mixed sequences
            patterns = [
                ("fibonacci", [1, 1, 2, 3], 5, "Add the two previous numbers"),
                ("squares", [1, 4, 9, 16], 25, "Perfect squares: 1², 2², 3², 4²"),
                ("double+1", [1, 3, 7, 15], 31, "Double and add 1 each time")
            ]
            pattern_type, sequence, answer, hint = random.choice(patterns)
        
        return sequence, answer, hint
    
    def generate_word_puzzle(self, level):
        """Generate word-based puzzles"""
        puzzles = [
            {
                "type": "anagram",
                "scrambled": "TRACE",
                "answer": "CRATE",
                "hint": "Rearrange letters to make a word for a wooden box"
            },
            {
                "type": "anagram", 
                "scrambled": "LISTEN",
                "answer": "SILENT",
                "hint": "Rearrange to make a word meaning 'quiet'"
            },
            {
                "type": "riddle",
                "question": "I have keys but no locks. I have space but no room. What am I?",
                "answer": "KEYBOARD",
                "hint": "Think about computer parts"
            },
            {
                "type": "riddle",
                "question": "What gets wet while drying?",
                "answer": "TOWEL",
                "hint": "Something you use after a shower"
            },
            {
                "type": "word_chain",
                "start": "CAT",
                "clue": "Change one letter to make an animal that flies",
                "answer": "BAT",
                "hint": "Change the first letter"
            }
        ]
        return random.choice(puzzles)
    
    def generate_logic_puzzle(self, level):
        """Generate logic puzzles"""
        puzzles = [
            {
                "type": "pattern",
                "sequence": "🔴🔵🔴🔵🔴",
                "question": "What comes next?",
                "answer": "🔵",
                "choices": ["🔴", "🔵", "🟡", "🟢"],
                "hint": "Look for the alternating pattern"
            },
            {
                "type": "pattern",
                "sequence": "⭐⭐🌙⭐⭐🌙⭐⭐",
                "question": "What comes next?",
                "answer": "🌙",
                "choices": ["⭐", "🌙", "☀️", "🌟"],
                "hint": "Count the stars between moons"
            },
            {
                "type": "logic",
                "question": "If all roses are flowers, and some flowers are red, can we say all roses are red?",
                "answer": "NO",
                "choices": ["YES", "NO", "MAYBE", "UNKNOWN"],
                "hint": "Think carefully about the logic"
            }
        ]
        return random.choice(puzzles)
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n🧩 PUZZLE MASTER - LEVEL {level}")
        print("="*40)
        
        level_descriptions = {
            1: "Number Patterns - Find the sequence",
            2: "Word Puzzles - Anagrams and riddles", 
            3: "Logic Challenges - Think outside the box",
            4: "Mixed Puzzles - Variety pack",
            5: "Master Level - Ultimate brain teasers"
        }
        
        print(f"🧠 {level_descriptions[level]}")
        print("Solve 5 puzzles to advance!")
        print("-" * 40)
        
        level_score = 0
        puzzles_solved = 0
        
        puzzle_types = ["number", "word", "logic"]
        if level == 1:
            puzzle_types = ["number"] * 3 + ["word"] * 2
        elif level == 2:
            puzzle_types = ["word"] * 3 + ["number"] * 2
        elif level == 3:
            puzzle_types = ["logic"] * 3 + ["number", "word"]
        else:
            puzzle_types = ["number", "word", "logic", "number", "word"]
        
        random.shuffle(puzzle_types)
        
        for p in range(5):
            puzzle_type = puzzle_types[p]
            print(f"\n🧩 PUZZLE {p+1}/5")
            
            if puzzle_type == "number":
                sequence, answer, hint = self.generate_number_sequence(level)
                print(f"Number Sequence: {', '.join(map(str, sequence))}, ?")
                print("What number comes next?")
                
                user_input = input("Your answer: ").strip()
                try:
                    user_answer = int(user_input)
                    if user_answer == answer:
                        points = 120 + (self.streak * 15)
                        level_score += points
                        puzzles_solved += 1
                        self.streak += 1
                        print(f"✅ Correct! +{points} points")
                        if self.streak > 1:
                            print(f"🔥 Streak: {self.streak}!")
                    else:
                        print(f"❌ Wrong! The answer was {answer}")
                        print(f"💡 Hint: {hint}")
                        self.streak = 0
                except ValueError:
                    print(f"❌ Invalid input! The answer was {answer}")
                    self.streak = 0
            
            elif puzzle_type == "word":
                puzzle = self.generate_word_puzzle(level)
                
                if puzzle["type"] == "anagram":
                    print(f"Anagram: Unscramble '{puzzle['scrambled']}'")
                elif puzzle["type"] == "riddle":
                    print(f"Riddle: {puzzle['question']}")
                elif puzzle["type"] == "word_chain":
                    print(f"Word Chain: Start with '{puzzle['start']}'")
                    print(puzzle["clue"])
                
                user_answer = input("Your answer: ").strip().upper()
                
                if user_answer == puzzle["answer"]:
                    points = 120 + (self.streak * 15)
                    level_score += points
                    puzzles_solved += 1
                    self.streak += 1
                    print(f"✅ Correct! +{points} points")
                    if self.streak > 1:
                        print(f"🔥 Streak: {self.streak}!")
                else:
                    print(f"❌ Wrong! The answer was {puzzle['answer']}")
                    print(f"💡 Hint: {puzzle['hint']}")
                    self.streak = 0
            
            else:  # logic puzzle
                puzzle = self.generate_logic_puzzle(level)
                
                if puzzle["type"] == "pattern":
                    print(f"Pattern: {puzzle['sequence']}")
                    print(puzzle["question"])
                    
                    print("\nChoices:")
                    for i, choice in enumerate(puzzle["choices"], 1):
                        print(f"{i}. {choice}")
                    
                    try:
                        choice_num = int(input("Your choice (1-4): "))
                        if 1 <= choice_num <= 4:
                            user_answer = puzzle["choices"][choice_num - 1]
                            if user_answer == puzzle["answer"]:
                                points = 120 + (self.streak * 15)
                                level_score += points
                                puzzles_solved += 1
                                self.streak += 1
                                print(f"✅ Correct! +{points} points")
                                if self.streak > 1:
                                    print(f"🔥 Streak: {self.streak}!")
                            else:
                                print(f"❌ Wrong! The answer was {puzzle['answer']}")
                                print(f"💡 Hint: {puzzle['hint']}")
                                self.streak = 0
                        else:
                            print("❌ Invalid choice!")
                            self.streak = 0
                    except ValueError:
                        print("❌ Invalid input!")
                        self.streak = 0
                
                elif puzzle["type"] == "logic":
                    print(f"Logic: {puzzle['question']}")
                    
                    print("\nChoices:")
                    for i, choice in enumerate(puzzle["choices"], 1):
                        print(f"{i}. {choice}")
                    
                    try:
                        choice_num = int(input("Your choice (1-4): "))
                        if 1 <= choice_num <= 4:
                            user_answer = puzzle["choices"][choice_num - 1]
                            if user_answer == puzzle["answer"]:
                                points = 120 + (self.streak * 15)
                                level_score += points
                                puzzles_solved += 1
                                self.streak += 1
                                print(f"✅ Correct! +{points} points")
                                if self.streak > 1:
                                    print(f"🔥 Streak: {self.streak}!")
                            else:
                                print(f"❌ Wrong! The answer was {puzzle['answer']}")
                                print(f"💡 Hint: {puzzle['hint']}")
                                self.streak = 0
                        else:
                            print("❌ Invalid choice!")
                            self.streak = 0
                    except ValueError:
                        print("❌ Invalid input!")
                        self.streak = 0
        
        print(f"\n📊 LEVEL {level} RESULTS:")
        print(f"✅ Puzzles Solved: {puzzles_solved}/5")
        print(f"🏆 Level Score: {level_score}")
        
        # Need at least 3/5 to advance
        if puzzles_solved >= 3:
            print("🎉 Level Passed! Brilliant puzzle solving!")
            return level_score
        else:
            print("🧩 Keep thinking! You need 3/5 to advance.")
            retry = input("Try this level again? (y/n): ").lower()
            if retry == 'y':
                return self.play_level(level)
            else:
                return level_score
    
    def play(self):
        """Main game loop"""
        print("\n🧩 WELCOME TO PUZZLE MASTER!")
        print("🧠 Challenge your mind with brain teasers and logic puzzles!")
        print("🎯 Test your pattern recognition and problem-solving skills!")
        
        input("\nPress Enter to start your puzzle adventure...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing Puzzle Master!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've completed all Puzzle Master levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                
                if total_score >= 2500:
                    print("🌟 PUZZLE GENIUS! Your brain is incredible!")
                elif total_score >= 2000:
                    print("🧩 PUZZLE MASTER! Excellent problem solving!")
                elif total_score >= 1500:
                    print("🧠 PUZZLE SOLVER! Great logical thinking!")
                else:
                    print("🎯 PUZZLE STUDENT! Keep challenging yourself!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
