"""
Science Lab Game - Educational Science Game
Part of EduVerse: The 5 Educational Realms
"""

import random

class ScienceLabGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.max_level = 5
        self.streak = 0
        
        # Science questions database
        self.science_data = {
            1: {  # Basic Science
                "questions": [
                    {"q": "What do plants need to make food?", "a": "sunlight", "choices": ["sunlight", "darkness", "cold", "noise"]},
                    {"q": "How many legs does a spider have?", "a": "8", "choices": ["6", "8", "10", "4"]},
                    {"q": "What gas do we breathe in?", "a": "oxygen", "choices": ["oxygen", "carbon dioxide", "nitrogen", "helium"]},
                    {"q": "What is the center of our solar system?", "a": "sun", "choices": ["moon", "earth", "sun", "mars"]},
                    {"q": "What do we call baby frogs?", "a": "tadpoles", "choices": ["tadpoles", "puppies", "kittens", "chicks"]},
                    {"q": "Which is the largest mammal?", "a": "blue whale", "choices": ["elephant", "blue whale", "giraffe", "lion"]},
                    {"q": "What makes things fall down?", "a": "gravity", "choices": ["wind", "gravity", "magnetism", "electricity"]},
                    {"q": "How many bones are in an adult human body?", "a": "206", "choices": ["150", "206", "300", "100"]}
                ]
            },
            2: {  # Earth Science
                "questions": [
                    {"q": "What causes day and night?", "a": "earth's rotation", "choices": ["earth's rotation", "moon phases", "sun moving", "clouds"]},
                    {"q": "What is the hardest natural substance?", "a": "diamond", "choices": ["gold", "iron", "diamond", "silver"]},
                    {"q": "What type of rock is formed by cooling lava?", "a": "igneous", "choices": ["sedimentary", "metamorphic", "igneous", "limestone"]},
                    {"q": "What causes earthquakes?", "a": "tectonic plates", "choices": ["wind", "rain", "tectonic plates", "animals"]},
                    {"q": "What is the Earth's outermost layer called?", "a": "crust", "choices": ["core", "mantle", "crust", "atmosphere"]},
                    {"q": "What creates lightning?", "a": "electrical charge", "choices": ["wind", "rain", "electrical charge", "temperature"]},
                    {"q": "What is the water cycle powered by?", "a": "sun", "choices": ["moon", "wind", "sun", "gravity"]},
                    {"q": "What gas makes up most of Earth's atmosphere?", "a": "nitrogen", "choices": ["oxygen", "carbon dioxide", "nitrogen", "hydrogen"]}
                ]
            },
            3: {  # Biology
                "questions": [
                    {"q": "What is the basic unit of life?", "a": "cell", "choices": ["atom", "molecule", "cell", "tissue"]},
                    {"q": "What process do plants use to make food?", "a": "photosynthesis", "choices": ["respiration", "photosynthesis", "digestion", "circulation"]},
                    {"q": "What carries oxygen in blood?", "a": "red blood cells", "choices": ["white blood cells", "platelets", "red blood cells", "plasma"]},
                    {"q": "What is DNA?", "a": "genetic material", "choices": ["a protein", "genetic material", "a vitamin", "a mineral"]},
                    {"q": "What organ pumps blood?", "a": "heart", "choices": ["lungs", "liver", "heart", "kidney"]},
                    {"q": "What do we call animals that eat only plants?", "a": "herbivores", "choices": ["carnivores", "omnivores", "herbivores", "predators"]},
                    {"q": "What is the largest organ in the human body?", "a": "skin", "choices": ["liver", "brain", "skin", "lungs"]},
                    {"q": "What do bees collect from flowers?", "a": "nectar", "choices": ["water", "nectar", "pollen", "leaves"]}
                ]
            },
            4: {  # Chemistry
                "questions": [
                    {"q": "What is the chemical symbol for water?", "a": "H2O", "choices": ["H2O", "CO2", "O2", "NaCl"]},
                    {"q": "What is the smallest unit of matter?", "a": "atom", "choices": ["molecule", "atom", "electron", "proton"]},
                    {"q": "What gas is produced when you mix baking soda and vinegar?", "a": "carbon dioxide", "choices": ["oxygen", "hydrogen", "carbon dioxide", "nitrogen"]},
                    {"q": "What is the pH of pure water?", "a": "7", "choices": ["0", "7", "14", "1"]},
                    {"q": "What happens to water at 100°C?", "a": "it boils", "choices": ["it freezes", "it boils", "it melts", "nothing"]},
                    {"q": "What is salt's chemical name?", "a": "sodium chloride", "choices": ["sodium chloride", "calcium carbonate", "potassium iodide", "magnesium sulfate"]},
                    {"q": "What type of change is burning wood?", "a": "chemical", "choices": ["physical", "chemical", "mechanical", "electrical"]},
                    {"q": "What element has the symbol 'O'?", "a": "oxygen", "choices": ["gold", "oxygen", "osmium", "oil"]}
                ]
            },
            5: {  # Physics
                "questions": [
                    {"q": "What is the speed of light?", "a": "300,000 km/s", "choices": ["300,000 km/s", "150,000 km/s", "500,000 km/s", "100,000 km/s"]},
                    {"q": "What force keeps planets in orbit?", "a": "gravity", "choices": ["magnetism", "electricity", "gravity", "friction"]},
                    {"q": "What is energy that cannot be created or destroyed?", "a": "conservation of energy", "choices": ["kinetic energy", "potential energy", "conservation of energy", "thermal energy"]},
                    {"q": "What type of energy does a moving object have?", "a": "kinetic", "choices": ["potential", "kinetic", "thermal", "chemical"]},
                    {"q": "What happens to the volume of gas when heated?", "a": "it expands", "choices": ["it shrinks", "it expands", "stays same", "it disappears"]},
                    {"q": "What is the unit of electrical resistance?", "a": "ohm", "choices": ["volt", "amp", "ohm", "watt"]},
                    {"q": "What type of wave is sound?", "a": "longitudinal", "choices": ["transverse", "longitudinal", "electromagnetic", "circular"]},
                    {"q": "What is absolute zero?", "a": "-273°C", "choices": ["0°C", "100°C", "-273°C", "-100°C"]}
                ]
            }
        }
    
    def play_level(self, level):
        """Play a single level"""
        print(f"\n🧪 SCIENCE LAB - LEVEL {level}")
        print("="*35)
        
        level_descriptions = {
            1: "Basic Science - Fundamentals of nature",
            2: "Earth Science - Our planet and environment",
            3: "Biology - Living things and life processes",
            4: "Chemistry - Matter and chemical reactions",
            5: "Physics - Forces, energy, and motion"
        }
        
        print(f"🔬 {level_descriptions[level]}")
        print("Answer 5 questions to advance!")
        print("-" * 35)
        
        level_score = 0
        questions_correct = 0
        
        # Get random questions for this level
        available_questions = self.science_data[level]["questions"].copy()
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
            print("🎉 Level Passed! Great scientific thinking!")
            return level_score
        else:
            print("🔬 Keep experimenting! You need 3/5 to advance.")
            retry = input("Try this level again? (y/n): ").lower()
            if retry == 'y':
                return self.play_level(level)
            else:
                return level_score
    
    def get_hint(self, level, question):
        """Provide contextual hints based on the question"""
        hint_map = {
            1: "basic life processes and nature",
            2: "Earth's structure and natural phenomena", 
            3: "how living things work and function",
            4: "chemical properties and reactions",
            5: "forces, energy, and physical laws"
        }
        return hint_map.get(level, "scientific principles")
    
    def play(self):
        """Main game loop"""
        print("\n🧪 WELCOME TO SCIENCE LAB!")
        print("🔬 Explore the wonders of science through 5 exciting levels!")
        print("⚗️ Test your knowledge of biology, chemistry, physics, and more!")
        
        input("\nPress Enter to start your scientific journey...")
        
        total_score = 0
        
        for level in range(1, self.max_level + 1):
            level_score = self.play_level(level)
            total_score += level_score
            
            print(f"\n🎯 TOTAL SCORE SO FAR: {total_score}")
            
            if level < self.max_level:
                continue_game = input(f"\nReady for Level {level + 1}? (y/n): ").lower()
                if continue_game != 'y':
                    print("👋 Thanks for playing Science Lab!")
                    break
            else:
                print("\n🎊 CONGRATULATIONS! 🎊")
                print("You've completed all Science Lab levels!")
                print(f"🏆 FINAL SCORE: {total_score}")
                
                if total_score >= 2500:
                    print("🌟 SCIENCE GENIUS! Nobel Prize worthy!")
                elif total_score >= 2000:
                    print("🔬 MASTER SCIENTIST! Excellent knowledge!")
                elif total_score >= 1500:
                    print("⚗️ SCIENCE SCHOLAR! Great understanding!")
                else:
                    print("🧪 SCIENCE STUDENT! Keep exploring!")
        
        input("\nPress Enter to return to the main menu...")
        return total_score
