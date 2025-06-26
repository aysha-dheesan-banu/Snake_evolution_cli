"""
Memory Game - Fun Memory Challenge Game
Part of EduVerse: 10-Game Arcade Platform
"""

import random
import time

class MemoryGameChallenge:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
    
    def play_sequence_memory(self, level):
        """Simon Says style sequence memory"""
        sequence_length = 3 + level
        symbols = ["🔴", "🔵", "🟡", "🟢", "🟣", "🟠"]
        
        # Generate sequence
        sequence = [random.choice(symbols) for _ in range(sequence_length)]
        
        print(f"\n🧠 SEQUENCE MEMORY")
        print(f"Memorize this sequence of {sequence_length} symbols:")
        print("(You have 3 seconds per symbol)")
        
        input("Press Enter when ready...")
        
        # Show sequence
        for i, symbol in enumerate(sequence):
            print(f"\nPosition {i+1}: {symbol}")
            time.sleep(2)  # Show each symbol for 2 seconds
        
        # Clear screen effect
        print("\n" * 10)
        print("Now repeat the sequence!")
        
        # Get user input
        user_sequence = []
        for i in range(sequence_length):
            print(f"\nPosition {i+1}:")
            print("Available symbols: " + " ".join(symbols))
            symbol = input("Enter symbol (copy/paste): ").strip()
            user_sequence.append(symbol)
        
        # Check accuracy
        correct = 0
        for i in range(sequence_length):
            if i < len(user_sequence) and user_sequence[i] == sequence[i]:
                correct += 1
        
        accuracy = correct / sequence_length
        points = int(accuracy * 150)
        
        print(f"\n📊 RESULTS:")
        print(f"Correct sequence: {' '.join(sequence)}")
        print(f"Your sequence:    {' '.join(user_sequence)}")
        print(f"Accuracy: {correct}/{sequence_length} ({accuracy*100:.1f}%)")
        
        return points
    
    def play_number_memory(self, level):
        """Remember sequences of numbers"""
        sequence_length = 4 + level
        
        # Generate number sequence
        sequence = [random.randint(0, 9) for _ in range(sequence_length)]
        
        print(f"\n🔢 NUMBER MEMORY")
        print(f"Memorize this {sequence_length}-digit number:")
        print("(You have 5 seconds)")
        
        input("Press Enter when ready...")
        
        # Show number
        number_str = ''.join(map(str, sequence))
        print(f"\n{number_str}")
        time.sleep(4)
        
        # Clear screen
        print("\n" * 10)
        print("What was the number?")
        
        user_input = input("Enter the number: ").strip()
        
        if user_input == number_str:
            points = 200
            print("🎉 Perfect! You remembered the entire number!")
        else:
            # Check partial credit
            correct_digits = 0
            min_length = min(len(user_input), len(number_str))
            for i in range(min_length):
                if user_input[i] == number_str[i]:
                    correct_digits += 1
            
            accuracy = correct_digits / sequence_length
            points = int(accuracy * 150)
            
            print(f"📊 RESULTS:")
            print(f"Correct number: {number_str}")
            print(f"Your answer:    {user_input}")
            print(f"Correct digits: {correct_digits}/{sequence_length}")
        
        return points
    
    def play_word_memory(self, level):
        """Remember lists of words"""
        word_lists = {
            1: ["cat", "dog", "bird", "fish"],
            2: ["apple", "banana", "orange", "grape", "cherry"],
            3: ["red", "blue", "green", "yellow", "purple", "orange"],
            4: ["happy", "sad", "angry", "excited", "calm", "worried", "proud"],
            5: ["mountain", "ocean", "forest", "desert", "river", "valley", "island", "canyon"]
        }
        
        words = word_lists.get(level, word_lists[5])
        num_words = len(words)
        
        print(f"\n📝 WORD MEMORY")
        print(f"Memorize these {num_words} words:")
        print("(You have 2 seconds per word)")
        
        input("Press Enter when ready...")
        
        # Show words one by one
        for i, word in enumerate(words):
            print(f"\nWord {i+1}: {word.upper()}")
            time.sleep(2)
        
        # Clear screen
        print("\n" * 10)
        print("Now list all the words you remember:")
        
        # Get user input
        user_words = []
        for i in range(num_words):
            word = input(f"Word {i+1}: ").strip().lower()
            if word:
                user_words.append(word)
        
        # Check accuracy
        correct_words = []
        for word in user_words:
            if word in [w.lower() for w in words]:
                correct_words.append(word)
        
        accuracy = len(correct_words) / num_words
        points = int(accuracy * 180)
        
        print(f"\n📊 RESULTS:")
        print(f"Original words: {', '.join(words)}")
        print(f"You remembered: {', '.join(user_words)}")
        print(f"Correct: {len(correct_words)}/{num_words} ({accuracy*100:.1f}%)")
        
        return points
    
    def play_pattern_memory(self, level):
        """Remember visual patterns"""
        grid_size = 3 + (level // 2)  # 3x3 to 5x5 grid
        num_filled = 3 + level  # Number of filled squares
        
        print(f"\n🎨 PATTERN MEMORY")
        print(f"Memorize the pattern in this {grid_size}x{grid_size} grid:")
        print("(You have 5 seconds)")
        
        # Generate pattern
        positions = []
        for _ in range(num_filled):
            while True:
                pos = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
                if pos not in positions:
                    positions.append(pos)
                    break
        
        input("Press Enter when ready...")
        
        # Show pattern
        print("\nPattern:")
        for row in range(grid_size):
            line = ""
            for col in range(grid_size):
                if (row, col) in positions:
                    line += "⬛ "
                else:
                    line += "⬜ "
            print(line)
        
        time.sleep(4)
        
        # Clear screen
        print("\n" * 10)
        print("Now recreate the pattern!")
        print("Enter the positions of the filled squares (row, col):")
        print(f"Rows and columns are numbered 1-{grid_size}")
        
        user_positions = []
        for i in range(num_filled):
            try:
                pos_input = input(f"Position {i+1} (row,col): ").strip()
                row, col = map(int, pos_input.split(','))
                user_positions.append((row-1, col-1))  # Convert to 0-based
            except:
                print("Invalid input, skipping...")
        
        # Check accuracy
        correct_positions = 0
        for pos in user_positions:
            if pos in positions:
                correct_positions += 1
        
        accuracy = correct_positions / num_filled
        points = int(accuracy * 160)
        
        print(f"\n📊 RESULTS:")
        print(f"Correct positions: {correct_positions}/{num_filled} ({accuracy*100:.1f}%)")
        
        return points
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n🌟 MEMORY GAME - LEVEL {level}")
        print("="*40)
        
        level_descriptions = {
            1: "Basic Memory - Simple sequences",
            2: "Improving Memory - Longer patterns",
            3: "Good Memory - Multiple types",
            4: "Strong Memory - Complex challenges",
            5: "Memory Master - Ultimate test"
        }
        
        print(f"🧠 {level_descriptions[level]}")
        print("Complete 4 memory challenges!")
        print("-" * 40)
        
        level_score = 0
        challenges_passed = 0
        
        # Different types of memory games
        games = ["sequence", "number", "word", "pattern"]
        random.shuffle(games)
        
        for challenge_num in range(4):
            game_type = games[challenge_num]
            print(f"\n🎮 CHALLENGE {challenge_num + 1}/4")
            
            if game_type == "sequence":
                points = self.play_sequence_memory(level)
            elif game_type == "number":
                points = self.play_number_memory(level)
            elif game_type == "word":
                points = self.play_word_memory(level)
            else:  # pattern
                points = self.play_pattern_memory(level)
            
            level_score += points
            
            if points >= 100:  # Good performance threshold
                challenges_passed += 1
                self.streak += 1
                if self.streak > 1:
                    bonus = self.streak * 20
                    level_score += bonus
                    print(f"🔥 Memory streak bonus: +{bonus} points!")
            else:
                self.streak = 0
            
            print(f"Challenge score: {points} points")
            
            if challenge_num < 3:  # Don't pause after last challenge
                input("\nPress Enter for next challenge...")
        
        print(f"\n📊 LEVEL {level} RESULTS:")
        print(f"✅ Challenges passed: {challenges_passed}/4")
        print(f"🏆 Level Score: {level_score}")
        
        # Need at least 2/4 good performances to advance
        if challenges_passed >= 2:
            print("🎉 Level Passed! Great memory skills!")
            return level_score
        else:
            print("🧠 Keep practicing! You need better performance to advance.")
            retry = input("Try this level again? (y/n): ").lower()
            if retry == 'y':
                return self.play_level(level)
            else:
                return level_score
    
    def play(self):
        """Main game loop"""
        print("\n🌟 WELCOME TO MEMORY GAME!")
        print("🧠 Challenge your memory with sequences, numbers, words, and patterns!")
        print("💭 Train your brain and improve your recall abilities!")
        
        input("\nPress Enter to start your memory training...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing Memory Game!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've completed all Memory Game levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                
                if total_score >= 3000:
                    print("🌟 MEMORY GENIUS! Photographic memory!")
                elif total_score >= 2500:
                    print("🧠 MEMORY MASTER! Incredible recall!")
                elif total_score >= 2000:
                    print("💭 MEMORY EXPERT! Excellent memory!")
                else:
                    print("🎯 MEMORY STUDENT! Keep training!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
