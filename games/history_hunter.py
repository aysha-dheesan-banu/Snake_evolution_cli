"""
History Hunter Game - Educational History Game
Part of EduVerse: The 5 Educational Realms
"""

import random

class HistoryHunterGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
        
        # History questions database
        self.history_data = {
            1: {  # Ancient History
                "questions": [
                    {"q": "Which ancient wonder was in Egypt?", "a": "Great Pyramid", "choices": ["Colossus of Rhodes", "Great Pyramid", "Hanging Gardens", "Lighthouse"]},
                    {"q": "Who was the first emperor of Rome?", "a": "Augustus", "choices": ["Julius Caesar", "Augustus", "Nero", "Trajan"]},
                    {"q": "Which civilization built Machu Picchu?", "a": "Inca", "choices": ["Maya", "Aztec", "Inca", "Olmec"]},
                    {"q": "What was the ancient Greek city-state known for warriors?", "a": "Sparta", "choices": ["Athens", "Sparta", "Corinth", "Thebes"]},
                    {"q": "Who was the famous Egyptian queen?", "a": "Cleopatra", "choices": ["Nefertiti", "Hatshepsut", "Cleopatra", "Ankhesenamun"]},
                    {"q": "Which empire was ruled by Cyrus the Great?", "a": "Persian", "choices": ["Babylonian", "Assyrian", "Persian", "Macedonian"]},
                    {"q": "What did ancient Egyptians use to write?", "a": "Hieroglyphs", "choices": ["Cuneiform", "Hieroglyphs", "Alphabet", "Pictographs"]},
                    {"q": "Who was the Greek god of the sea?", "a": "Poseidon", "choices": ["Zeus", "Hades", "Poseidon", "Apollo"]}
                ]
            },
            2: {  # Medieval Times
                "questions": [
                    {"q": "What were medieval warriors on horseback called?", "a": "Knights", "choices": ["Samurai", "Knights", "Vikings", "Crusaders"]},
                    {"q": "Who was the legendary king of Camelot?", "a": "Arthur", "choices": ["Arthur", "Charlemagne", "Alfred", "William"]},
                    {"q": "What was the Black Death?", "a": "Plague", "choices": ["War", "Famine", "Plague", "Earthquake"]},
                    {"q": "Which empire was centered in Constantinople?", "a": "Byzantine", "choices": ["Roman", "Ottoman", "Byzantine", "Persian"]},
                    {"q": "What were the religious wars called?", "a": "Crusades", "choices": ["Crusades", "Jihads", "Inquisition", "Reformation"]},
                    {"q": "Who was the Mongol leader?", "a": "Genghis Khan", "choices": ["Kublai Khan", "Genghis Khan", "Tamerlane", "Attila"]},
                    {"q": "What system bound peasants to land?", "a": "Feudalism", "choices": ["Capitalism", "Feudalism", "Socialism", "Mercantilism"]},
                    {"q": "Which explorer reached the Americas in 1492?", "a": "Columbus", "choices": ["Magellan", "Columbus", "Vasco da Gama", "Marco Polo"]}
                ]
            },
            3: {  # Renaissance & Exploration
                "questions": [
                    {"q": "Who painted the Mona Lisa?", "a": "Leonardo da Vinci", "choices": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"]},
                    {"q": "Which explorer circumnavigated the globe first?", "a": "Magellan's crew", "choices": ["Columbus", "Vasco da Gama", "Magellan's crew", "Drake"]},
                    {"q": "Who invented the printing press?", "a": "Gutenberg", "choices": ["Galileo", "Newton", "Gutenberg", "Copernicus"]},
                    {"q": "Which scientist said Earth orbits the Sun?", "a": "Copernicus", "choices": ["Galileo", "Kepler", "Copernicus", "Newton"]},
                    {"q": "Who wrote Romeo and Juliet?", "a": "Shakespeare", "choices": ["Marlowe", "Shakespeare", "Chaucer", "Dante"]},
                    {"q": "Which city was the center of the Renaissance?", "a": "Florence", "choices": ["Rome", "Venice", "Florence", "Milan"]},
                    {"q": "Who sculpted the statue of David?", "a": "Michelangelo", "choices": ["Leonardo", "Michelangelo", "Donatello", "Bernini"]},
                    {"q": "Which empire did Cortés conquer?", "a": "Aztec", "choices": ["Inca", "Maya", "Aztec", "Olmec"]}
                ]
            },
            4: {  # Modern History (1600-1900)
                "questions": [
                    {"q": "When did the American Revolution begin?", "a": "1775", "choices": ["1765", "1775", "1783", "1789"]},
                    {"q": "Who was the first US President?", "a": "Washington", "choices": ["Adams", "Jefferson", "Washington", "Franklin"]},
                    {"q": "Which revolution began in 1789?", "a": "French", "choices": ["American", "French", "Industrial", "Russian"]},
                    {"q": "Who was Napoleon?", "a": "French Emperor", "choices": ["French King", "French Emperor", "British General", "Spanish King"]},
                    {"q": "When did the American Civil War end?", "a": "1865", "choices": ["1863", "1865", "1867", "1869"]},
                    {"q": "Who invented the steam engine?", "a": "James Watt", "choices": ["Thomas Edison", "James Watt", "Alexander Bell", "Nikola Tesla"]},
                    {"q": "Which country had the Industrial Revolution first?", "a": "Britain", "choices": ["France", "Germany", "Britain", "USA"]},
                    {"q": "Who wrote the Declaration of Independence?", "a": "Jefferson", "choices": ["Washington", "Adams", "Franklin", "Jefferson"]}
                ]
            },
            5: {  # 20th Century
                "questions": [
                    {"q": "When did World War I begin?", "a": "1914", "choices": ["1912", "1914", "1916", "1918"]},
                    {"q": "Who was the first person to fly?", "a": "Wright Brothers", "choices": ["Lindbergh", "Wright Brothers", "Earhart", "Yeager"]},
                    {"q": "When did World War II end?", "a": "1945", "choices": ["1943", "1944", "1945", "1946"]},
                    {"q": "Who was the first person on the moon?", "a": "Neil Armstrong", "choices": ["Buzz Aldrin", "Neil Armstrong", "John Glenn", "Alan Shepard"]},
                    {"q": "When did the Berlin Wall fall?", "a": "1989", "choices": ["1987", "1989", "1991", "1993"]},
                    {"q": "Who led the civil rights movement?", "a": "Martin Luther King Jr.", "choices": ["Malcolm X", "Martin Luther King Jr.", "Rosa Parks", "Jesse Jackson"]},
                    {"q": "When did the Cold War end?", "a": "1991", "choices": ["1989", "1990", "1991", "1992"]},
                    {"q": "Who was the first female Prime Minister of Britain?", "a": "Margaret Thatcher", "choices": ["Margaret Thatcher", "Theresa May", "Elizabeth II", "Diana Spencer"]}
                ]
            }
        }
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n📚 HISTORY HUNTER - LEVEL {level}")
        print("="*35)
        
        level_descriptions = {
            1: "Ancient History - Civilizations of the past",
            2: "Medieval Times - Knights, castles, and kingdoms",
            3: "Renaissance & Exploration - Art, science, and discovery",
            4: "Modern History - Revolutions and nations (1600-1900)",
            5: "20th Century - Wars, technology, and change"
        }
        
        print(f"⏰ {level_descriptions[level]}")
        print("Answer 5 questions to advance!")
        print("-" * 35)
        
        level_score = 0
        questions_correct = 0
        
        # Get random questions for this level
        available_questions = self.history_data[level]["questions"].copy()
        random.shuffle(available_questions)
        
        for q in range(5):
            question_data = available_questions[q]
            question = question_data["q"]
            correct_answer = question_data["a"]
            choices = question_data["choices"].copy()
            random.shuffle(choices)
            
            print(f"\n❓ Question {q+1}: {question}")
            print("\nChoices:")
            for i, choice in enumerate(choices, 1):
                print(f"{i}. {choice}")
            
            # Give player 2 attempts
            attempts = 0
            while attempts < 2:
                try:
                    user_input = input("Your choice (1-4) or 'hint' for help: ").strip()
                    
                    if user_input.lower() == 'hint':
                        print(f"💡 Hint: Think about {self.get_hint(level, question)}")
                        continue
                    
                    answer_index = int(user_input) - 1
                    
                    if 0 <= answer_index < 4 and choices[answer_index] == correct_answer:
                        points = 120 - (attempts * 20)  # Less points for more attempts
                        if self.streak > 0:
                            points += self.streak * 15  # Streak bonus
                        
                        level_score += points
                        questions_correct += 1
                        self.streak += 1
                        
                        print(f"✅ Correct! +{points} points")
                        if self.streak > 1:
                            print(f"🔥 Streak: {self.streak}!")
                        break
                    else:
                        attempts += 1
                        if attempts < 2:
                            print(f"❌ Try again! (1 attempt left)")
                        else:
                            print(f"❌ The answer was '{correct_answer}'")
                            self.streak = 0
                            
                except (ValueError, IndexError):
                    attempts += 1
                    if attempts < 2:
                        print(f"❌ Please enter 1, 2, 3, or 4! (1 attempt left)")
                    else:
                        print(f"❌ The answer was '{correct_answer}'")
                        self.streak = 0
        
        print(f"\n📊 LEVEL {level} RESULTS:")
        print(f"✅ Correct Answers: {questions_correct}/5")
        print(f"🏆 Level Score: {level_score}")
        
        # Need at least 3/5 to advance
        if questions_correct >= 3:
            print("🎉 Level Passed! Great historical knowledge!")
            return level_score
        else:
            print("📖 Keep studying! You need 3/5 to advance.")
            retry = input("Try this level again? (y/n): ").lower()
            if retry == 'y':
                return self.play_level(level)
            else:
                return level_score
    
    def get_hint(self, level, question):
        """Provide contextual hints based on the question"""
        hint_map = {
            1: "ancient civilizations and their achievements",
            2: "medieval life, knights, and kingdoms",
            3: "Renaissance art, science, and exploration",
            4: "revolutions and the birth of modern nations",
            5: "major events of the 1900s"
        }
        return hint_map.get(level, "historical events and people")
    
    def play(self):
        """Main game loop"""
        print("\n📚 WELCOME TO HISTORY HUNTER!")
        print("⏰ Journey through time across 5 historical periods!")
        print("🏛️ Test your knowledge of civilizations, wars, and great figures!")
        
        input("\nPress Enter to start your time-traveling adventure...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing History Hunter!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've completed all History Hunter levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                
                if total_score >= 2500:
                    print("🌟 HISTORY GENIUS! You know the past like a master!")
                elif total_score >= 2000:
                    print("📚 HISTORY MASTER! Excellent historical knowledge!")
                elif total_score >= 1500:
                    print("⏰ HISTORY SCHOLAR! Great understanding of the past!")
                else:
                    print("📖 HISTORY STUDENT! Keep learning about our past!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
