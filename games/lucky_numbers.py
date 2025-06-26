"""
Lucky Numbers Game - Fun Chance & Strategy Game
Part of EduVerse: 10-Game Arcade Platform
"""

import random

class LuckyNumbersGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
        self.coins = 100  # Starting coins
    
    def play_number_guessing(self, level):
        """Number guessing mini-game"""
        if level == 1:
            max_num = 10
            attempts = 3
        elif level == 2:
            max_num = 20
            attempts = 4
        elif level == 3:
            max_num = 50
            attempts = 5
        elif level == 4:
            max_num = 100
            attempts = 6
        else:
            max_num = 200
            attempts = 7
        
        secret_number = random.randint(1, max_num)
        print(f"\n🎲 NUMBER GUESSING")
        print(f"I'm thinking of a number between 1 and {max_num}")
        print(f"You have {attempts} attempts!")
        
        for attempt in range(attempts):
            try:
                guess = int(input(f"Attempt {attempt + 1}: "))
                
                if guess == secret_number:
                    points = (attempts - attempt) * 50  # More points for fewer attempts
                    print(f"🎉 CORRECT! The number was {secret_number}")
                    print(f"✅ You earned {points} points!")
                    return points
                elif guess < secret_number:
                    print("📈 Too low!")
                else:
                    print("📉 Too high!")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
        
        print(f"💔 Out of attempts! The number was {secret_number}")
        return 0
    
    def play_dice_game(self, level):
        """Dice rolling game with betting"""
        print(f"\n🎲 DICE BETTING GAME")
        print(f"💰 You have {self.coins} coins")
        
        if self.coins <= 0:
            print("💸 No coins left! Skipping dice game.")
            return 0
        
        max_bet = min(self.coins, 20 + level * 10)
        print(f"Place your bet (1-{max_bet} coins):")
        
        try:
            bet = int(input("Bet amount: "))
            if bet < 1 or bet > max_bet:
                print("❌ Invalid bet amount!")
                return 0
        except ValueError:
            print("❌ Invalid bet!")
            return 0
        
        print("\nChoose your prediction:")
        print("1. Sum will be EVEN")
        print("2. Sum will be ODD") 
        print("3. Sum will be 7 (high payout!)")
        print("4. Sum will be doubles (same number)")
        
        try:
            choice = int(input("Your choice (1-4): "))
        except ValueError:
            print("❌ Invalid choice!")
            return 0
        
        # Roll dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        
        print(f"\n🎲 Rolling dice...")
        print(f"Die 1: {die1} | Die 2: {die2}")
        print(f"Total: {total}")
        
        won = False
        multiplier = 1
        
        if choice == 1 and total % 2 == 0:  # Even
            won = True
            multiplier = 2
        elif choice == 2 and total % 2 == 1:  # Odd
            won = True
            multiplier = 2
        elif choice == 3 and total == 7:  # Lucky 7
            won = True
            multiplier = 5
        elif choice == 4 and die1 == die2:  # Doubles
            won = True
            multiplier = 4
        
        if won:
            winnings = bet * multiplier
            self.coins += winnings - bet  # Net gain
            points = winnings
            print(f"🎉 YOU WIN! +{winnings} coins!")
            print(f"💰 Total coins: {self.coins}")
            return points
        else:
            self.coins -= bet
            print(f"💔 You lose {bet} coins")
            print(f"💰 Remaining coins: {self.coins}")
            return 0
    
    def play_lottery(self, level):
        """Simple lottery game"""
        print(f"\n🎟️ LUCKY LOTTERY")
        
        if level <= 2:
            # Pick 2 numbers from 1-10
            print("Pick 2 numbers from 1-10:")
            try:
                num1 = int(input("First number: "))
                num2 = int(input("Second number: "))
                
                if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
                    print("❌ Numbers must be between 1-10!")
                    return 0
                
                winning_nums = [random.randint(1, 10), random.randint(1, 10)]
                print(f"Winning numbers: {winning_nums}")
                
                matches = 0
                if num1 in winning_nums:
                    matches += 1
                if num2 in winning_nums:
                    matches += 1
                
                if matches == 2:
                    points = 300
                    print("🎊 JACKPOT! Both numbers match!")
                elif matches == 1:
                    points = 100
                    print("🎉 One number matches!")
                else:
                    points = 0
                    print("💔 No matches this time")
                
                return points
                
            except ValueError:
                print("❌ Invalid numbers!")
                return 0
        else:
            # Pick 3 numbers from 1-20 (harder)
            print("Pick 3 numbers from 1-20:")
            try:
                nums = []
                for i in range(3):
                    num = int(input(f"Number {i+1}: "))
                    if not (1 <= num <= 20):
                        print("❌ Numbers must be between 1-20!")
                        return 0
                    nums.append(num)
                
                winning_nums = [random.randint(1, 20) for _ in range(3)]
                print(f"Winning numbers: {winning_nums}")
                
                matches = len(set(nums) & set(winning_nums))
                
                if matches == 3:
                    points = 500
                    print("🎊 MEGA JACKPOT! All numbers match!")
                elif matches == 2:
                    points = 200
                    print("🎉 Two numbers match!")
                elif matches == 1:
                    points = 50
                    print("😊 One number matches!")
                else:
                    points = 0
                    print("💔 No matches this time")
                
                return points
                
            except ValueError:
                print("❌ Invalid numbers!")
                return 0
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n🎲 LUCKY NUMBERS - LEVEL {level}")
        print("="*40)
        
        level_descriptions = {
            1: "Beginner's Luck - Easy games",
            2: "Getting Lucky - Medium difficulty",
            3: "High Roller - Bigger risks and rewards",
            4: "Fortune Seeker - Advanced games",
            5: "Jackpot Master - Ultimate luck test"
        }
        
        print(f"🍀 {level_descriptions[level]}")
        print("Play 3 games of chance!")
        print("-" * 40)
        
        level_score = 0
        games = ["guessing", "dice", "lottery"]
        
        for game_num in range(3):
            game_type = games[game_num % 3]
            print(f"\n🎮 GAME {game_num + 1}/3")
            
            if game_type == "guessing":
                points = self.play_number_guessing(level)
            elif game_type == "dice":
                points = self.play_dice_game(level)
            else:  # lottery
                points = self.play_lottery(level)
            
            level_score += points
            
            if points > 0:
                self.streak += 1
                if self.streak > 1:
                    bonus = self.streak * 25
                    level_score += bonus
                    print(f"🔥 Lucky streak bonus: +{bonus} points!")
            else:
                self.streak = 0
            
            if game_num < 2:  # Don't pause after last game
                input("\nPress Enter for next game...")
        
        print(f"\n📊 LEVEL {level} RESULTS:")
        print(f"🏆 Level Score: {level_score}")
        print(f"💰 Coins remaining: {self.coins}")
        
        # Always pass (it's a luck game!)
        print("🎉 Level Complete! Luck is on your side!")
        return level_score
    
    def play(self):
        """Main game loop"""
        print("\n🎲 WELCOME TO LUCKY NUMBERS!")
        print("🍀 Test your luck with games of chance and strategy!")
        print("💰 Manage your coins wisely and trust your instincts!")
        
        input("\nPress Enter to try your luck...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing Lucky Numbers!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've completed all Lucky Numbers levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                print(f"💰 Final coins: {self.coins}")
                
                if total_score >= 2000:
                    print("🌟 FORTUNE'S FAVORITE! Incredible luck!")
                elif total_score >= 1500:
                    print("🍀 LUCKY CHAMPION! Great fortune!")
                elif total_score >= 1000:
                    print("🎲 LUCKY PLAYER! Good instincts!")
                else:
                    print("🎯 LUCK LEARNER! Keep trying!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
