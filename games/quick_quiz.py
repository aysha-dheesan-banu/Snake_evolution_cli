"""
Quick Quiz Game - Fast-Paced Trivia Game
Part of EduVerse: 10-Game Arcade Platform
"""

import random
import time

class QuickQuizGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
    
    def get_quiz_questions(self, level):
        """Get questions based on level and category"""
        questions_db = {
            1: {  # General Knowledge - Easy
                "questions": [
                    {"q": "What color do you get when you mix red and blue?", "a": "purple", "choices": ["green", "purple", "orange", "yellow"]},
                    {"q": "How many days are in a week?", "a": "7", "choices": ["5", "6", "7", "8"]},
                    {"q": "What animal says 'moo'?", "a": "cow", "choices": ["pig", "sheep", "cow", "horse"]},
                    {"q": "Which season comes after winter?", "a": "spring", "choices": ["summer", "fall", "spring", "autumn"]},
                    {"q": "What do bees make?", "a": "honey", "choices": ["milk", "honey", "butter", "cheese"]},
                    {"q": "How many wheels does a bicycle have?", "a": "2", "choices": ["1", "2", "3", "4"]},
                    {"q": "What do you use to write on a blackboard?", "a": "chalk", "choices": ["pen", "pencil", "chalk", "marker"]},
                    {"q": "Which meal do you eat in the morning?", "a": "breakfast", "choices": ["lunch", "dinner", "breakfast", "snack"]}
                ]
            },
            2: {  # Science & Nature
                "questions": [
                    {"q": "What gas do plants produce?", "a": "oxygen", "choices": ["carbon dioxide", "oxygen", "nitrogen", "hydrogen"]},
                    {"q": "How many hearts does an octopus have?", "a": "3", "choices": ["1", "2", "3", "4"]},
                    {"q": "What is the fastest land animal?", "a": "cheetah", "choices": ["lion", "cheetah", "horse", "deer"]},
                    {"q": "Which planet is closest to the sun?", "a": "mercury", "choices": ["venus", "earth", "mercury", "mars"]},
                    {"q": "What do caterpillars turn into?", "a": "butterflies", "choices": ["moths", "butterflies", "beetles", "flies"]},
                    {"q": "How many bones do sharks have?", "a": "0", "choices": ["100", "50", "0", "200"]},
                    {"q": "What is the largest ocean?", "a": "pacific", "choices": ["atlantic", "indian", "pacific", "arctic"]},
                    {"q": "Which bird cannot fly?", "a": "penguin", "choices": ["eagle", "penguin", "sparrow", "robin"]}
                ]
            },
            3: {  # History & Geography
                "questions": [
                    {"q": "Which country has the most people?", "a": "china", "choices": ["india", "usa", "china", "russia"]},
                    {"q": "What is the capital of France?", "a": "paris", "choices": ["london", "berlin", "paris", "rome"]},
                    {"q": "Who was the first person on the moon?", "a": "neil armstrong", "choices": ["buzz aldrin", "neil armstrong", "john glenn", "alan shepard"]},
                    {"q": "Which continent is Egypt in?", "a": "africa", "choices": ["asia", "africa", "europe", "australia"]},
                    {"q": "What year did World War II end?", "a": "1945", "choices": ["1944", "1945", "1946", "1947"]},
                    {"q": "Which ocean is between America and Europe?", "a": "atlantic", "choices": ["pacific", "indian", "atlantic", "arctic"]},
                    {"q": "What is the smallest country in the world?", "a": "vatican city", "choices": ["monaco", "vatican city", "san marino", "liechtenstein"]},
                    {"q": "Which river is the longest in the world?", "a": "nile", "choices": ["amazon", "nile", "mississippi", "yangtze"]}
                ]
            },
            4: {  # Sports & Entertainment
                "questions": [
                    {"q": "How many players are on a basketball team on court?", "a": "5", "choices": ["4", "5", "6", "7"]},
                    {"q": "What sport is played at Wimbledon?", "a": "tennis", "choices": ["golf", "tennis", "cricket", "rugby"]},
                    {"q": "How many strings does a guitar usually have?", "a": "6", "choices": ["4", "5", "6", "7"]},
                    {"q": "What does 'www' stand for?", "a": "world wide web", "choices": ["world wide web", "world web wide", "wide world web", "web world wide"]},
                    {"q": "Which company created the iPhone?", "a": "apple", "choices": ["samsung", "google", "apple", "microsoft"]},
                    {"q": "How often are the Olympic Games held?", "a": "every 4 years", "choices": ["every 2 years", "every 3 years", "every 4 years", "every 5 years"]},
                    {"q": "What is the maximum score in ten-pin bowling?", "a": "300", "choices": ["200", "250", "300", "350"]},
                    {"q": "Which social media platform uses hashtags?", "a": "twitter", "choices": ["facebook", "twitter", "linkedin", "youtube"]}
                ]
            },
            5: {  # Mixed Challenge
                "questions": [
                    {"q": "What is the chemical symbol for gold?", "a": "au", "choices": ["go", "gd", "au", "ag"]},
                    {"q": "Which language has the most native speakers?", "a": "mandarin", "choices": ["english", "spanish", "mandarin", "hindi"]},
                    {"q": "What is the square root of 64?", "a": "8", "choices": ["6", "7", "8", "9"]},
                    {"q": "Which artist painted the Mona Lisa?", "a": "leonardo da vinci", "choices": ["michelangelo", "leonardo da vinci", "picasso", "van gogh"]},
                    {"q": "What is the hardest natural substance?", "a": "diamond", "choices": ["gold", "iron", "diamond", "platinum"]},
                    {"q": "How many minutes are in a full day?", "a": "1440", "choices": ["1440", "1400", "1480", "1420"]},
                    {"q": "Which planet has the most moons?", "a": "jupiter", "choices": ["saturn", "jupiter", "uranus", "neptune"]},
                    {"q": "What does 'HTTP' stand for?", "a": "hypertext transfer protocol", "choices": ["hypertext transfer protocol", "hypertext transport protocol", "hyperlink transfer protocol", "hyperlink transport protocol"]}
                ]
            }
        }
        
        return questions_db.get(level, questions_db[5])
    
    def play_speed_round(self, level, time_limit):
        """Play a timed speed round"""
        questions_data = self.get_quiz_questions(level)
        questions = questions_data["questions"].copy()
        random.shuffle(questions)
        
        print(f"\n⚡ SPEED ROUND - {time_limit} SECONDS!")
        print("Answer as many questions as you can!")
        print("Type the number of your choice (1-4)")
        
        input("Press Enter to start the timer...")
        
        start_time = time.time()
        questions_answered = 0
        correct_answers = 0
        
        for question in questions:
            # Check time remaining
            elapsed = time.time() - start_time
            remaining = time_limit - elapsed
            
            if remaining <= 0:
                print("\n⏰ TIME'S UP!")
                break
            
            print(f"\n⏰ Time left: {remaining:.1f}s")
            print(f"❓ {question['q']}")
            
            # Shuffle choices
            choices = question["choices"].copy()
            random.shuffle(choices)
            correct_index = choices.index(question["a"]) + 1
            
            for i, choice in enumerate(choices, 1):
                print(f"{i}. {choice}")
            
            try:
                # Quick input with timeout simulation
                answer = input("Your answer (1-4): ").strip()
                answer_num = int(answer)
                
                if 1 <= answer_num <= 4:
                    questions_answered += 1
                    if answer_num == correct_index:
                        correct_answers += 1
                        print("✅ Correct!")
                    else:
                        print(f"❌ Wrong! Answer was {correct_index}")
                else:
                    print("❌ Invalid choice!")
                    
            except ValueError:
                print("❌ Invalid input!")
            except KeyboardInterrupt:
                break
        
        # Calculate score
        if questions_answered > 0:
            accuracy = correct_answers / questions_answered
            speed_bonus = max(0, time_limit - (time.time() - start_time))
            points = int((correct_answers * 100) + (accuracy * 100) + (speed_bonus * 10))
        else:
            points = 0
        
        print(f"\n📊 SPEED ROUND RESULTS:")
        print(f"⚡ Questions answered: {questions_answered}")
        print(f"✅ Correct answers: {correct_answers}")
        print(f"📈 Accuracy: {accuracy*100:.1f}%" if questions_answered > 0 else "📈 Accuracy: 0%")
        print(f"🏆 Points earned: {points}")
        
        return points, correct_answers
    
    def play_lightning_round(self, level):
        """Super fast lightning round"""
        questions_data = self.get_quiz_questions(level)
        questions = questions_data["questions"].copy()
        random.shuffle(questions)
        
        print(f"\n⚡ LIGHTNING ROUND!")
        print("10 questions, 2 seconds each!")
        print("Just type your answer quickly!")
        
        input("Press Enter when ready...")
        
        correct = 0
        
        for i in range(min(10, len(questions))):
            question = questions[i]
            print(f"\n❓ {i+1}/10: {question['q']}")
            
            # Show choices
            choices = question["choices"].copy()
            random.shuffle(choices)
            correct_index = choices.index(question["a"]) + 1
            
            for j, choice in enumerate(choices, 1):
                print(f"{j}. {choice}")
            
            print("Quick! 2 seconds...")
            
            try:
                # Simulate quick response
                answer = input("Answer: ").strip()
                answer_num = int(answer)
                
                if answer_num == correct_index:
                    correct += 1
                    print("✅")
                else:
                    print("❌")
                    
            except:
                print("❌")
        
        points = correct * 150  # Higher points for lightning round
        
        print(f"\n⚡ LIGHTNING RESULTS:")
        print(f"✅ Correct: {correct}/10")
        print(f"🏆 Points: {points}")
        
        return points
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n⚡ QUICK QUIZ - LEVEL {level}")
        print("="*40)
        
        level_descriptions = {
            1: "General Knowledge - Easy questions",
            2: "Science & Nature - Natural world",
            3: "History & Geography - World knowledge",
            4: "Sports & Entertainment - Fun facts",
            5: "Mixed Challenge - Everything combined"
        }
        
        print(f"🧠 {level_descriptions[level]}")
        print("Complete 3 quiz rounds!")
        print("-" * 40)
        
        level_score = 0
        total_correct = 0
        
        # Round 1: Speed Round (30 seconds)
        print("\n🎮 ROUND 1: SPEED QUIZ")
        points1, correct1 = self.play_speed_round(level, 30)
        level_score += points1
        total_correct += correct1
        
        input("\nPress Enter for Round 2...")
        
        # Round 2: Speed Round (20 seconds) 
        print("\n🎮 ROUND 2: FASTER QUIZ")
        points2, correct2 = self.play_speed_round(level, 20)
        level_score += points2
        total_correct += correct2
        
        input("\nPress Enter for Round 3...")
        
        # Round 3: Lightning Round
        print("\n🎮 ROUND 3: LIGHTNING QUIZ")
        points3 = self.play_lightning_round(level)
        level_score += points3
        
        # Streak bonus
        if total_correct >= 8:  # Good performance
            self.streak += 1
            if self.streak > 1:
                bonus = self.streak * 50
                level_score += bonus
                print(f"🔥 Quiz master streak: +{bonus} points!")
        else:
            self.streak = 0
        
        print(f"\n📊 LEVEL {level} RESULTS:")
        print(f"🏆 Total Score: {level_score}")
        print(f"⚡ Quiz Performance: {'Excellent' if total_correct >= 10 else 'Good' if total_correct >= 6 else 'Keep Practicing'}")
        
        # Always pass (it's about speed and fun)
        print("🎉 Level Complete! Great quizzing!")
        return level_score
    
    def play(self):
        """Main game loop"""
        print("\n⚡ WELCOME TO QUICK QUIZ!")
        print("🧠 Test your knowledge in fast-paced trivia rounds!")
        print("💨 Speed and accuracy are key to high scores!")
        
        input("\nPress Enter to start the quiz challenge...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing Quick Quiz!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've completed all Quick Quiz levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                
                if total_score >= 4000:
                    print("🌟 QUIZ GENIUS! Lightning-fast brain!")
                elif total_score >= 3000:
                    print("⚡ QUIZ MASTER! Incredible speed and knowledge!")
                elif total_score >= 2000:
                    print("🧠 QUIZ EXPERT! Great trivia skills!")
                else:
                    print("🎯 QUIZ STUDENT! Keep practicing!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
