"""
Game data and configuration for EduVerse
Contains all game definitions, levels, and content
"""

GAMES = {
    1: {
        'name': {
            'en': '🧮 Math Wizard',
            'ta': '🧮 கணித மந்திரவாதி'
        },
        'description': {
            'en': 'Master arithmetic operations and mathematical concepts',
            'ta': 'கணித செயல்பாடுகள் மற்றும் கருத்துகளில் வல்லுநராகுங்கள்'
        },
        'icon': '🧮',
        'levels': 10,
        'category': 'mathematics',
        'difficulty': 'progressive',
        'skills': ['arithmetic', 'algebra', 'geometry', 'problem_solving'],
        'age_group': '10-18'
    },
    2: {
        'name': {
            'en': '🔤 Word Master',
            'ta': '🔤 சொல் மாஸ்டர்'
        },
        'description': {
            'en': 'Build vocabulary and improve language skills',
            'ta': 'சொல்வளம் மற்றும் மொழித் திறன்களை மேம்படுத்துங்கள்'
        },
        'icon': '🔤',
        'levels': 10,
        'category': 'language',
        'difficulty': 'progressive',
        'skills': ['vocabulary', 'spelling', 'grammar', 'comprehension'],
        'age_group': '10-18'
    },
    3: {
        'name': {
            'en': '🧪 Science Lab',
            'ta': '🧪 அறிவியல் ஆய்வகம்'
        },
        'description': {
            'en': 'Explore scientific concepts and experiments',
            'ta': 'அறிவியல் கருத்துகள் மற்றும் சோதனைகளை ஆராயுங்கள்'
        },
        'icon': '🧪',
        'levels': 10,
        'category': 'science',
        'difficulty': 'progressive',
        'skills': ['physics', 'chemistry', 'biology', 'scientific_method'],
        'age_group': '10-18'
    },
    4: {
        'name': {
            'en': '🌍 Geography Quest',
            'ta': '🌍 புவியியல் தேடல்'
        },
        'description': {
            'en': 'Discover world geography and cultures',
            'ta': 'உலக புவியியல் மற்றும் கலாச்சாரங்களைக் கண்டறியுங்கள்'
        },
        'icon': '🌍',
        'levels': 10,
        'category': 'geography',
        'difficulty': 'progressive',
        'skills': ['world_knowledge', 'mapping', 'cultures', 'landmarks'],
        'age_group': '10-18'
    },
    5: {
        'name': {
            'en': '📚 History Hunter',
            'ta': '📚 வரலாற்று வேட்டைக்காரன்'
        },
        'description': {
            'en': 'Journey through historical events and figures',
            'ta': 'வரலாற்று நிகழ்வுகள் மற்றும் நபர்களின் வழியாக பயணம்'
        },
        'icon': '📚',
        'levels': 10,
        'category': 'history',
        'difficulty': 'progressive',
        'skills': ['chronology', 'historical_analysis', 'cause_effect', 'civilizations'],
        'age_group': '10-18'
    },
    6: {
        'name': {
            'en': '🎨 Art Creator',
            'ta': '🎨 கலை படைப்பாளி'
        },
        'description': {
            'en': 'Express creativity through art and design',
            'ta': 'கலை மற்றும் வடிவமைப்பின் மூலம் படைப்பாற்றலை வெளிப்படுத்துங்கள்'
        },
        'icon': '🎨',
        'levels': 10,
        'category': 'arts',
        'difficulty': 'progressive',
        'skills': ['color_theory', 'composition', 'art_history', 'creativity'],
        'age_group': '10-18'
    },
    7: {
        'name': {
            'en': '🎵 Music Maestro',
            'ta': '🎵 இசை மேஸ்ட்ரோ'
        },
        'description': {
            'en': 'Learn musical concepts and composition',
            'ta': 'இசைக் கருத்துகள் மற்றும் இசையமைப்பைக் கற்றுக்கொள்ளுங்கள்'
        },
        'icon': '🎵',
        'levels': 10,
        'category': 'music',
        'difficulty': 'progressive',
        'skills': ['music_theory', 'rhythm', 'melody', 'instruments'],
        'age_group': '10-18'
    },
    8: {
        'name': {
            'en': '💻 Code Ninja',
            'ta': '💻 கோட் நிஞ்ஜா'
        },
        'description': {
            'en': 'Master programming fundamentals',
            'ta': 'நிரலாக்க அடிப்படைகளில் வல்லுநராகுங்கள்'
        },
        'icon': '💻',
        'levels': 10,
        'category': 'programming',
        'difficulty': 'progressive',
        'skills': ['algorithms', 'logic', 'debugging', 'problem_solving'],
        'age_group': '12-18'
    },
    9: {
        'name': {
            'en': '🧩 Logic Puzzle',
            'ta': '🧩 தர்க்க புதிர்'
        },
        'description': {
            'en': 'Develop logical thinking and problem-solving',
            'ta': 'தர்க்கரீதியான சிந்தனை மற்றும் சிக்கல் தீர்வை வளர்க்கவும்'
        },
        'icon': '🧩',
        'levels': 10,
        'category': 'logic',
        'difficulty': 'progressive',
        'skills': ['logical_reasoning', 'pattern_recognition', 'deduction', 'analysis'],
        'age_group': '10-18'
    },
    10: {
        'name': {
            'en': '🌟 Memory Palace',
            'ta': '🌟 நினைவக அரண்மனை'
        },
        'description': {
            'en': 'Enhance memory and cognitive skills',
            'ta': 'நினைவகம் மற்றும் அறிவாற்றல் திறன்களை மேம்படுத்துங்கள்'
        },
        'icon': '🌟',
        'levels': 10,
        'category': 'memory',
        'difficulty': 'progressive',
        'skills': ['memory_techniques', 'concentration', 'recall', 'cognitive_training'],
        'age_group': '10-18'
    }
}

# Level progression data
LEVEL_PROGRESSION = {
    'easy': {'time_limit': 60, 'questions': 5, 'score_multiplier': 1.0},
    'medium': {'time_limit': 45, 'questions': 7, 'score_multiplier': 1.5},
    'hard': {'time_limit': 30, 'questions': 10, 'score_multiplier': 2.0},
    'expert': {'time_limit': 20, 'questions': 12, 'score_multiplier': 3.0}
}

# Achievement definitions
ACHIEVEMENTS = {
    'first_steps': {
        'name': {'en': 'First Steps', 'ta': 'முதல் அடிகள்'},
        'description': {'en': 'Complete your first game', 'ta': 'உங்கள் முதல் விளையாட்டை முடிக்கவும்'},
        'icon': '👶',
        'points': 100,
        'condition': 'complete_first_game'
    },
    'quick_learner': {
        'name': {'en': 'Quick Learner', 'ta': 'விரைவு கற்பவர்'},
        'description': {'en': 'Complete a level in under 30 seconds', 'ta': '30 விநாடிகளுக்குள் ஒரு நிலையை முடிக்கவும்'},
        'icon': '⚡',
        'points': 200,
        'condition': 'complete_level_fast'
    },
    'perfectionist': {
        'name': {'en': 'Perfectionist', 'ta': 'பரிபூரணவாதி'},
        'description': {'en': 'Get 100% score in any game', 'ta': 'எந்த விளையாட்டிலும் 100% மதிப்பெண் பெறுங்கள்'},
        'icon': '💯',
        'points': 300,
        'condition': 'perfect_score'
    },
    'explorer': {
        'name': {'en': 'Explorer', 'ta': 'ஆய்வாளர்'},
        'description': {'en': 'Try all 10 games', 'ta': 'அனைத்து 10 விளையாட்டுகளையும் முயற்சிக்கவும்'},
        'icon': '🗺️',
        'points': 500,
        'condition': 'try_all_games'
    },
    'genius': {
        'name': {'en': 'Genius', 'ta': 'மேதை'},
        'description': {'en': 'Score 10,000+ total points', 'ta': 'மொத்தம் 10,000+ புள்ளிகள் பெறுங்கள்'},
        'icon': '🧠',
        'points': 1000,
        'condition': 'high_total_score'
    },
    'master': {
        'name': {'en': 'Master', 'ta': 'மாஸ்டர்'},
        'description': {'en': 'Complete all levels in 5 games', 'ta': '5 விளையாட்டுகளில் அனைத்து நிலைகளையும் முடிக்கவும்'},
        'icon': '🎓',
        'points': 1500,
        'condition': 'master_five_games'
    },
    'legend': {
        'name': {'en': 'Legend', 'ta': 'புராணம்'},
        'description': {'en': 'Complete all games with 90%+ average', 'ta': '90%+ சராசரியுடன் அனைத்து விளையாட்டுகளையும் முடிக்கவும்'},
        'icon': '👑',
        'points': 2000,
        'condition': 'complete_all_high_score'
    }
}

# Question templates for AI generation
QUESTION_TEMPLATES = {
    1: {  # Math Wizard
        'basic_arithmetic': [
            "What is {a} + {b}?",
            "Calculate {a} - {b}",
            "What is {a} × {b}?",
            "Divide {a} by {b}"
        ],
        'word_problems': [
            "If you have {a} apples and buy {b} more, how many do you have?",
            "A store has {a} items. If {b} are sold, how many remain?",
            "There are {a} students in each of {b} classes. How many students total?"
        ],
        'fractions': [
            "What is {a}/{b} + {c}/{d}?",
            "Simplify {a}/{b}",
            "Convert {a}/{b} to decimal"
        ]
    },
    2: {  # Word Master
        'vocabulary': [
            "What does '{word}' mean?",
            "Find a synonym for '{word}'",
            "What is the opposite of '{word}'?",
            "Use '{word}' in a sentence"
        ],
        'spelling': [
            "Spell the word that means '{definition}'",
            "Which spelling is correct: {option1} or {option2}?",
            "Complete the spelling: {partial_word}"
        ]
    },
    3: {  # Science Lab
        'physics': [
            "What happens when you mix {substance1} and {substance2}?",
            "Why does {phenomenon} occur?",
            "What is the unit of {measurement}?"
        ],
        'biology': [
            "What is the function of {organ}?",
            "Which animal group does {animal} belong to?",
            "What do plants need for photosynthesis?"
        ]
    }
}

# Scoring system
SCORING_SYSTEM = {
    'correct_answer': 100,
    'time_bonus': 50,  # per second remaining
    'streak_bonus': 25,  # per consecutive correct answer
    'perfect_level': 500,  # bonus for completing level with 100%
    'first_try': 200,  # bonus for getting answer right on first try
    'hint_penalty': -25,  # penalty for using hint
    'skip_penalty': -50   # penalty for skipping question
}

# Difficulty scaling
DIFFICULTY_SCALING = {
    1: {'multiplier': 1.0, 'time_limit': 60, 'hint_available': True},
    2: {'multiplier': 1.2, 'time_limit': 55, 'hint_available': True},
    3: {'multiplier': 1.4, 'time_limit': 50, 'hint_available': True},
    4: {'multiplier': 1.6, 'time_limit': 45, 'hint_available': True},
    5: {'multiplier': 1.8, 'time_limit': 40, 'hint_available': False},
    6: {'multiplier': 2.0, 'time_limit': 35, 'hint_available': False},
    7: {'multiplier': 2.2, 'time_limit': 30, 'hint_available': False},
    8: {'multiplier': 2.4, 'time_limit': 25, 'hint_available': False},
    9: {'multiplier': 2.6, 'time_limit': 20, 'hint_available': False},
    10: {'multiplier': 3.0, 'time_limit': 15, 'hint_available': False}
}

# Game-specific content
GAME_CONTENT = {
    1: {  # Math Wizard
        'topics': {
            1: 'Basic Addition',
            2: 'Basic Subtraction', 
            3: 'Multiplication Tables',
            4: 'Division Basics',
            5: 'Mixed Operations',
            6: 'Fractions',
            7: 'Decimals',
            8: 'Percentages',
            9: 'Basic Algebra',
            10: 'Geometry'
        }
    },
    2: {  # Word Master
        'topics': {
            1: 'Common Words',
            2: 'Synonyms',
            3: 'Antonyms',
            4: 'Spelling',
            5: 'Grammar',
            6: 'Sentence Structure',
            7: 'Reading Comprehension',
            8: 'Vocabulary Building',
            9: 'Advanced Grammar',
            10: 'Creative Writing'
        }
    },
    3: {  # Science Lab
        'topics': {
            1: 'Basic Physics',
            2: 'Simple Chemistry',
            3: 'Human Body',
            4: 'Plants and Animals',
            5: 'Earth Science',
            6: 'Weather and Climate',
            7: 'Space and Astronomy',
            8: 'Energy and Motion',
            9: 'Chemical Reactions',
            10: 'Advanced Concepts'
        }
    },
    4: {  # Geography Quest
        'topics': {
            1: 'World Continents',
            2: 'Country Capitals',
            3: 'Major Rivers',
            4: 'Mountain Ranges',
            5: 'Oceans and Seas',
            6: 'Famous Landmarks',
            7: 'World Cultures',
            8: 'Climate Zones',
            9: 'Natural Resources',
            10: 'Global Issues'
        }
    },
    5: {  # History Hunter
        'topics': {
            1: 'Ancient Civilizations',
            2: 'Medieval Period',
            3: 'Age of Exploration',
            4: 'Industrial Revolution',
            5: 'World War I',
            6: 'World War II',
            7: 'Modern History',
            8: 'Independence Movements',
            9: 'Cultural History',
            10: 'Contemporary Events'
        }
    }
}

# Leaderboard categories
LEADERBOARD_CATEGORIES = {
    'global': 'Global Champions',
    'daily': 'Today\'s Leaders',
    'weekly': 'This Week\'s Best',
    'monthly': 'Monthly Masters',
    'game_specific': 'Game Champions',
    'level_specific': 'Level Leaders'
}

# Power-ups and special items
POWER_UPS = {
    'time_freeze': {
        'name': {'en': 'Time Freeze', 'ta': 'நேர நிறுத்தம்'},
        'description': {'en': 'Freeze time for 10 seconds', 'ta': '10 விநாடிகளுக்கு நேரத்தை நிறுத்துங்கள்'},
        'icon': '⏰',
        'cost': 100,
        'effect': 'freeze_timer'
    },
    'double_score': {
        'name': {'en': 'Double Score', 'ta': 'இரட்டை மதிப்பெண்'},
        'description': {'en': 'Double points for next question', 'ta': 'அடுத்த கேள்விக்கு இரட்டை புள்ளிகள்'},
        'icon': '2️⃣',
        'cost': 150,
        'effect': 'double_points'
    },
    'hint_master': {
        'name': {'en': 'Hint Master', 'ta': 'குறிப்பு மாஸ்டர்'},
        'description': {'en': 'Get detailed hint for any question', 'ta': 'எந்த கேள்விக்கும் விரிவான குறிப்பு பெறுங்கள்'},
        'icon': '💡',
        'cost': 75,
        'effect': 'enhanced_hint'
    },
    'skip_free': {
        'name': {'en': 'Free Skip', 'ta': 'இலவச தவிர்ப்பு'},
        'description': {'en': 'Skip question without penalty', 'ta': 'அபராதம் இல்லாமல் கேள்வியைத் தவிர்க்கவும்'},
        'icon': '⏭️',
        'cost': 50,
        'effect': 'penalty_free_skip'
    }
}
