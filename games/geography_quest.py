"""
Geography Quest Game - Educational Geography Game
Part of EduVerse: The 5 Educational Realms
"""

import random

class GeographyQuestGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
        
        # Geography questions database
        self.geography_data = {
            1: {  # Countries and Capitals
                "questions": [
                    {"q": "What is the capital of France?", "a": "Paris", "choices": ["London", "Paris", "Berlin", "Rome"]},
                    {"q": "What is the capital of Japan?", "a": "Tokyo", "choices": ["Tokyo", "Osaka", "Kyoto", "Hiroshima"]},
                    {"q": "What is the capital of Australia?", "a": "Canberra", "choices": ["Sydney", "Melbourne", "Canberra", "Perth"]},
                    {"q": "What is the capital of Canada?", "a": "Ottawa", "choices": ["Toronto", "Vancouver", "Montreal", "Ottawa"]},
                    {"q": "What is the capital of Brazil?", "a": "Brasília", "choices": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"]},
                    {"q": "What is the capital of Egypt?", "a": "Cairo", "choices": ["Alexandria", "Cairo", "Luxor", "Aswan"]},
                    {"q": "What is the capital of India?", "a": "New Delhi", "choices": ["Mumbai", "Kolkata", "New Delhi", "Chennai"]},
                    {"q": "What is the capital of Russia?", "a": "Moscow", "choices": ["St. Petersburg", "Moscow", "Novosibirsk", "Kazan"]}
                ]
            },
            2: {  # Continents and Oceans
                "questions": [
                    {"q": "Which is the largest continent?", "a": "Asia", "choices": ["Africa", "Asia", "North America", "Europe"]},
                    {"q": "Which is the smallest continent?", "a": "Australia", "choices": ["Europe", "Antarctica", "Australia", "South America"]},
                    {"q": "Which ocean is the largest?", "a": "Pacific", "choices": ["Atlantic", "Indian", "Pacific", "Arctic"]},
                    {"q": "How many continents are there?", "a": "7", "choices": ["5", "6", "7", "8"]},
                    {"q": "Which continent has the most countries?", "a": "Africa", "choices": ["Asia", "Europe", "Africa", "South America"]},
                    {"q": "Which ocean is the coldest?", "a": "Arctic", "choices": ["Atlantic", "Pacific", "Arctic", "Indian"]},
                    {"q": "Which continent is also a country?", "a": "Australia", "choices": ["Antarctica", "Australia", "Europe", "Asia"]},
                    {"q": "What separates Europe and Asia?", "a": "Ural Mountains", "choices": ["Himalayas", "Alps", "Ural Mountains", "Rockies"]}
                ]
            },
            3: {  # Famous Landmarks
                "questions": [
                    {"q": "In which country is the Great Wall located?", "a": "China", "choices": ["Japan", "China", "Korea", "Mongolia"]},
                    {"q": "Where is the Statue of Liberty?", "a": "USA", "choices": ["France", "USA", "Canada", "UK"]},
                    {"q": "In which country are the Pyramids of Giza?", "a": "Egypt", "choices": ["Sudan", "Libya", "Egypt", "Morocco"]},
                    {"q": "Where is Machu Picchu located?", "a": "Peru", "choices": ["Chile", "Bolivia", "Peru", "Ecuador"]},
                    {"q": "In which city is the Eiffel Tower?", "a": "Paris", "choices": ["London", "Berlin", "Paris", "Rome"]},
                    {"q": "Where is the Taj Mahal?", "a": "India", "choices": ["Pakistan", "Bangladesh", "India", "Nepal"]},
                    {"q": "In which country is Stonehenge?", "a": "England", "choices": ["Ireland", "Scotland", "Wales", "England"]},
                    {"q": "Where is Christ the Redeemer statue?", "a": "Brazil", "choices": ["Argentina", "Chile", "Brazil", "Colombia"]}
                ]
            },
            4: {  # Physical Geography
                "questions": [
                    {"q": "What is the longest river in the world?", "a": "Nile", "choices": ["Amazon", "Nile", "Mississippi", "Yangtze"]},
                    {"q": "What is the highest mountain in the world?", "a": "Mount Everest", "choices": ["K2", "Mount Everest", "Kangchenjunga", "Makalu"]},
                    {"q": "What is the largest desert in the world?", "a": "Antarctica", "choices": ["Sahara", "Gobi", "Antarctica", "Arabian"]},
                    {"q": "What is the deepest ocean trench?", "a": "Mariana Trench", "choices": ["Puerto Rico Trench", "Java Trench", "Mariana Trench", "Peru-Chile Trench"]},
                    {"q": "Which is the largest lake in the world?", "a": "Caspian Sea", "choices": ["Lake Superior", "Lake Victoria", "Caspian Sea", "Lake Baikal"]},
                    {"q": "What is the largest island in the world?", "a": "Greenland", "choices": ["Australia", "Greenland", "New Guinea", "Borneo"]},
                    {"q": "Which mountain range contains Mount Everest?", "a": "Himalayas", "choices": ["Andes", "Rockies", "Alps", "Himalayas"]},
                    {"q": "What is the largest hot desert?", "a": "Sahara", "choices": ["Sahara", "Arabian", "Kalahari", "Thar"]}
                ]
            },
            5: {  # World Cultures and Facts
                "questions": [
                    {"q": "Which country has the most time zones?", "a": "France", "choices": ["Russia", "USA", "China", "France"]},
                    {"q": "What is the most spoken language in the world?", "a": "Mandarin Chinese", "choices": ["English", "Spanish", "Mandarin Chinese", "Hindi"]},
                    {"q": "Which country has the most UNESCO World Heritage Sites?", "a": "Italy", "choices": ["China", "Spain", "Germany", "Italy"]},
                    {"q": "What is the smallest country in the world?", "a": "Vatican City", "choices": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"]},
                    {"q": "Which country spans the most time zones?", "a": "Russia", "choices": ["USA", "China", "Russia", "Canada"]},
                    {"q": "What is the most populous country?", "a": "China", "choices": ["India", "China", "USA", "Indonesia"]},
                    {"q": "Which country has the longest coastline?", "a": "Canada", "choices": ["Russia", "Australia", "Norway", "Canada"]},
                    {"q": "What currency is used in Japan?", "a": "Yen", "choices": ["Won", "Yuan", "Yen", "Rupee"]}
                ]
            }
        }
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n🌍 GEOGRAPHY QUEST - LEVEL {level}")
        print("="*35)
        
        level_descriptions = {
            1: "Countries & Capitals - Know your world capitals",
            2: "Continents & Oceans - Earth's major features",
            3: "Famous Landmarks - Iconic places around the world",
            4: "Physical Geography - Mountains, rivers, and deserts",
            5: "World Cultures - Fascinating facts about our world"
        }
        
        print(f"🗺️ {level_descriptions[level]}")
        print("Answer 5 questions to advance!")
        print("-" * 35)
        
        level_score = 0
        questions_correct = 0
        
        # Get random questions for this level
        available_questions = self.geography_data[level]["questions"].copy()
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
            print("🎉 Level Passed! Excellent world knowledge!")
            return level_score
        else:
            print("🗺️ Keep exploring! You need 3/5 to advance.")
            retry = input("Try this level again? (y/n): ").lower()
            if retry == 'y':
                return self.play_level(level)
            else:
                return level_score
    
    def get_hint(self, level, question):
        """Provide contextual hints based on the question"""
        if "capital" in question.lower():
            return "the main city of government"
        elif "continent" in question.lower():
            return "the seven large landmasses"
        elif "ocean" in question.lower():
            return "the five major bodies of water"
        elif "mountain" in question.lower() or "river" in question.lower():
            return "physical features of Earth"
        elif "country" in question.lower():
            return "nations and their characteristics"
        else:
            return "world geography and cultures"
    
    def play(self):
        """Main game loop"""
        print("\n🌍 WELCOME TO GEOGRAPHY QUEST!")
        print("🗺️ Explore the world through 5 exciting levels!")
        print("🌎 Test your knowledge of countries, landmarks, and cultures!")
        
        input("\nPress Enter to start your global adventure...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing Geography Quest!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've completed all Geography Quest levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                
                if total_score >= 2500:
                    print("🌟 WORLD EXPLORER! Outstanding global knowledge!")
                elif total_score >= 2000:
                    print("🗺️ GEOGRAPHY MASTER! Excellent world awareness!")
                elif total_score >= 1500:
                    print("🌍 WORLD SCHOLAR! Great geographical skills!")
                else:
                    print("🌎 WORLD STUDENT! Keep exploring!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
