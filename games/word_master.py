"""
Word Master Game - Educational Language Arts Game
Part of EduVerse: The 5 Educational Realms
"""

import random

class WordMasterGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
        
        # Word databases for different levels
        self.word_data = {
            1: {  # Basic vocabulary
                "words": ["cat", "dog", "sun", "moon", "tree", "book", "car", "house", "water", "fire"],
                "definitions": {
                    "cat": "a small furry pet animal",
                    "dog": "a loyal pet animal that barks",
                    "sun": "the bright star in our sky",
                    "moon": "the bright object in the night sky",
                    "tree": "a tall plant with leaves and branches",
                    "book": "something you read with pages",
                    "car": "a vehicle with four wheels",
                    "house": "a building where people live",
                    "water": "a clear liquid we drink",
                    "fire": "hot flames that give light and heat"
                }
            },
            2: {  # Intermediate vocabulary
                "words": ["elephant", "butterfly", "mountain", "ocean", "library", "computer", "telephone", "bicycle", "rainbow", "thunder"],
                "definitions": {
                    "elephant": "a large gray animal with a trunk",
                    "butterfly": "a colorful insect with wings",
                    "mountain": "a very tall hill or peak",
                    "ocean": "a very large body of salt water",
                    "library": "a place with many books to read",
                    "computer": "an electronic device for work and games",
                    "telephone": "a device used to talk to people far away",
                    "bicycle": "a two-wheeled vehicle you pedal",
                    "rainbow": "colorful arc in the sky after rain",
                    "thunder": "the loud sound that follows lightning"
                }
            },
            3: {  # Advanced vocabulary
                "words": ["magnificent", "adventure", "mysterious", "celebration", "imagination", "friendship", "discovery", "courage", "wisdom", "harmony"],
                "definitions": {
                    "magnificent": "extremely beautiful or impressive",
                    "adventure": "an exciting and unusual experience",
                    "mysterious": "difficult to understand or explain",
                    "celebration": "a special event or party",
                    "imagination": "the ability to create ideas in your mind",
                    "friendship": "a close relationship between friends",
                    "discovery": "finding something new or unknown",
                    "courage": "bravery in facing danger or difficulty",
                    "wisdom": "knowledge gained through experience",
                    "harmony": "a pleasing combination or agreement"
                }
            },
            4: {  # Synonyms and antonyms
                "words": ["happy", "big", "fast", "hot", "bright", "easy", "strong", "quiet", "clean", "new"],
                "synonyms": {
                    "happy": ["joyful", "cheerful", "glad"],
                    "big": ["large", "huge", "enormous"],
                    "fast": ["quick", "rapid", "speedy"],
                    "hot": ["warm", "burning", "heated"],
                    "bright": ["shiny", "brilliant", "glowing"],
                    "easy": ["simple", "effortless", "basic"],
                    "strong": ["powerful", "mighty", "tough"],
                    "quiet": ["silent", "peaceful", "calm"],
                    "clean": ["spotless", "pure", "tidy"],
                    "new": ["fresh", "recent", "modern"]
                },
                "antonyms": {
                    "happy": ["sad", "unhappy", "miserable"],
                    "big": ["small", "tiny", "little"],
                    "fast": ["slow", "sluggish", "gradual"],
                    "hot": ["cold", "cool", "freezing"],
                    "bright": ["dark", "dim", "dull"],
                    "easy": ["hard", "difficult", "challenging"],
                    "strong": ["weak", "fragile", "feeble"],
                    "quiet": ["loud", "noisy", "boisterous"],
                    "clean": ["dirty", "messy", "filthy"],
                    "new": ["old", "ancient", "outdated"]
                }
            },
            5: {  # Spelling challenge
                "words": ["necessary", "beautiful", "different", "important", "interesting", "wonderful", "excellent", "fantastic", "incredible", "magnificent"],
                "scrambled": True
            }
        }
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n🔤 WORD MASTER - LEVEL {level}")
        print("="*35)
        
        level_descriptions = {
            1: "Basic Vocabulary - Match words to definitions",
            2: "Intermediate Words - Learn new vocabulary",
            3: "Advanced Vocabulary - Complex meanings",
            4: "Synonyms & Antonyms - Word relationships",
            5: "Spelling Challenge - Unscramble words"
        }
        
        print(f"📚 {level_descriptions[level]}")
        print("Answer 5 questions to advance!")
        print("-" * 35)
        
        level_score = 0
        questions_correct = 0
        
        for q in range(5):
            if level <= 3:
                # Definition matching
                word, definition = self.generate_definition_question(level)
                print(f"\n❓ Question {q+1}: What does '{word}' mean?")
                print(f"Definition: {definition}")
                
                # Multiple choice
                correct_word = word
                choices = self.get_word_choices(level, correct_word)
                
                print("\nChoices:")
                for i, choice in enumerate(choices, 1):
                    print(f"{i}. {choice}")
                
                try:
                    answer = int(input("Your choice (1-4): "))
                    if 1 <= answer <= 4 and choices[answer-1] == correct_word:
                        points = 100 + (self.streak * 10)
                        level_score += points
                        questions_correct += 1
                        self.streak += 1
                        print(f"✅ Correct! +{points} points")
                        if self.streak > 1:
                            print(f"🔥 Streak: {self.streak}!")
                    else:
                        print(f"❌ Wrong! The answer was '{correct_word}'")
                        self.streak = 0
                except ValueError:
                    print(f"❌ Invalid input! The answer was '{correct_word}'")
                    self.streak = 0
                    
            elif level == 4:
                # Synonyms and antonyms
                word, relationship, correct_answer = self.generate_synonym_antonym_question()
                print(f"\n❓ Question {q+1}: Find a {relationship} for '{word}'")
                
                choices = self.get_synonym_antonym_choices(word, relationship, correct_answer)
                
                print("\nChoices:")
                for i, choice in enumerate(choices, 1):
                    print(f"{i}. {choice}")
                
                try:
                    answer = int(input("Your choice (1-4): "))
                    if 1 <= answer <= 4 and choices[answer-1] == correct_answer:
                        points = 100 + (self.streak * 10)
                        level_score += points
                        questions_correct += 1
                        self.streak += 1
                        print(f"✅ Correct! +{points} points")
                        if self.streak > 1:
                            print(f"🔥 Streak: {self.streak}!")
                    else:
                        print(f"❌ Wrong! The answer was '{correct_answer}'")
                        self.streak = 0
                except ValueError:
                    print(f"❌ Invalid input! The answer was '{correct_answer}'")
                    self.streak = 0
                    
            else:  # level 5 - Spelling
                scrambled_word, correct_word = self.generate_spelling_question()
                print(f"\n❓ Question {q+1}: Unscramble this word: '{scrambled_word}'")
                
                user_answer = input("Your answer: ").strip().lower()
                
                if user_answer == correct_word.lower():
                    points = 150 + (self.streak * 15)  # Higher points for spelling
                    level_score += points
                    questions_correct += 1
                    self.streak += 1
                    print(f"✅ Correct! +{points} points")
                    if self.streak > 1:
                        print(f"🔥 Streak: {self.streak}!")
                else:
                    print(f"❌ Wrong! The word was '{correct_word}'")
                    self.streak = 0
        
        print(f"\n📊 LEVEL {level} RESULTS:")
        print(f"✅ Correct Answers: {questions_correct}/5")
        print(f"🏆 Level Score: {level_score}")
        
        # Need at least 3/5 to advance
        if questions_correct >= 3:
            print("🎉 Level Passed! Excellent vocabulary skills!")
            return level_score
        else:
            print("📚 Keep studying! You need 3/5 to advance.")
            retry = input("Try this level again? (y/n): ").lower()
            if retry == 'y':
                return self.play_level(level)
            else:
                return level_score
    
    def generate_definition_question(self, level):
        """Generate a definition matching question"""
        word_list = self.word_data[level]["words"]
        definitions = self.word_data[level]["definitions"]
        
        word = random.choice(word_list)
        definition = definitions[word]
        
        return word, definition
    
    def get_word_choices(self, level, correct_word):
        """Get multiple choice options for word questions"""
        word_list = self.word_data[level]["words"]
        choices = [correct_word]
        
        while len(choices) < 4:
            word = random.choice(word_list)
            if word not in choices:
                choices.append(word)
        
        random.shuffle(choices)
        return choices
    
    def generate_synonym_antonym_question(self):
        """Generate synonym or antonym question"""
        word_list = self.word_data[4]["words"]
        word = random.choice(word_list)
        relationship = random.choice(["synonym", "antonym"])
        
        if relationship == "synonym":
            correct_answer = random.choice(self.word_data[4]["synonyms"][word])
        else:
            correct_answer = random.choice(self.word_data[4]["antonyms"][word])
        
        return word, relationship, correct_answer
    
    def get_synonym_antonym_choices(self, word, relationship, correct_answer):
        """Get choices for synonym/antonym questions"""
        choices = [correct_answer]
        
        # Add wrong choices from other words
        other_words = [w for w in self.word_data[4]["words"] if w != word]
        
        while len(choices) < 4:
            other_word = random.choice(other_words)
            if relationship == "synonym":
                wrong_choice = random.choice(self.word_data[4]["synonyms"][other_word])
            else:
                wrong_choice = random.choice(self.word_data[4]["antonyms"][other_word])
            
            if wrong_choice not in choices:
                choices.append(wrong_choice)
        
        random.shuffle(choices)
        return choices
    
    def generate_spelling_question(self):
        """Generate a scrambled word for spelling"""
        word_list = self.word_data[5]["words"]
        word = random.choice(word_list)
        
        # Scramble the word
        letters = list(word)
        random.shuffle(letters)
        scrambled = ''.join(letters)
        
        # Make sure it's actually scrambled
        while scrambled == word:
            random.shuffle(letters)
            scrambled = ''.join(letters)
        
        return scrambled, word
    
    def play(self):
        """Main game loop"""
        print("\n🔤 WELCOME TO WORD MASTER!")
        print("🎯 Expand your vocabulary through 5 challenging levels!")
        print("📚 Learn definitions, synonyms, antonyms, and spelling!")
        
        input("\nPress Enter to begin your word adventure...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing Word Master!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've mastered all Word Master levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                
                if total_score >= 2500:
                    print("🌟 VOCABULARY GENIUS! Outstanding!")
                elif total_score >= 2000:
                    print("📚 WORD MASTER! Excellent vocabulary!")
                elif total_score >= 1500:
                    print("🔤 WORD SCHOLAR! Great job!")
                else:
                    print("📖 WORD STUDENT! Keep reading!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
