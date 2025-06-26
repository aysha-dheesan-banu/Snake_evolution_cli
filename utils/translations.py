"""
Multilingual translations for EduVerse
Supports English and Tamil with extensibility for more languages
"""

TRANSLATIONS = {
    'en': {
        # Main Interface
        'title': 'EduVerse: The 10 Realms of Genius',
        'subtitle': 'Master 10 Educational Realms and Become a Genius!',
        'select_language': 'Select Language',
        'player_name': 'Enter Your Name',
        'please_enter_name': 'Please enter your name to start your educational journey!',
        'choose_your_realm': 'Choose Your Educational Realm',
        'play_now': 'Play Now',
        
        # Navigation
        'main_menu': 'Main Menu',
        'leaderboard': 'Leaderboard',
        'my_progress': 'My Progress',
        'achievements': 'Achievements',
        'settings': 'Settings',
        'back_to_menu': 'Back to Menu',
        
        # Game Interface
        'level': 'Level',
        'score': 'Score',
        'time_remaining': 'Time Remaining',
        'question': 'Question',
        'answer': 'Answer',
        'submit': 'Submit',
        'next_question': 'Next Question',
        'next_level': 'Next Level',
        'game_complete': 'Game Complete!',
        'congratulations': 'Congratulations!',
        'your_score': 'Your Score',
        'time_taken': 'Time Taken',
        'correct': 'Correct!',
        'incorrect': 'Incorrect!',
        'try_again': 'Try Again',
        'hint': 'Hint',
        'skip': 'Skip',
        
        # Game Names
        'math_wizard': 'Math Wizard',
        'word_master': 'Word Master',
        'science_lab': 'Science Lab',
        'geography_quest': 'Geography Quest',
        'history_hunter': 'History Hunter',
        'art_creator': 'Art Creator',
        'music_maestro': 'Music Maestro',
        'code_ninja': 'Code Ninja',
        'logic_puzzle': 'Logic Puzzle',
        'memory_palace': 'Memory Palace',
        
        # Game Descriptions
        'math_wizard_desc': 'Master arithmetic operations and mathematical concepts',
        'word_master_desc': 'Build vocabulary and improve language skills',
        'science_lab_desc': 'Explore scientific concepts and experiments',
        'geography_quest_desc': 'Discover world geography and cultures',
        'history_hunter_desc': 'Journey through historical events and figures',
        'art_creator_desc': 'Express creativity through art and design',
        'music_maestro_desc': 'Learn musical concepts and composition',
        'code_ninja_desc': 'Master programming fundamentals',
        'logic_puzzle_desc': 'Develop logical thinking and problem-solving',
        'memory_palace_desc': 'Enhance memory and cognitive skills',
        
        # Math Wizard
        'solve_problem': 'Solve this math problem:',
        'enter_answer': 'Enter your answer:',
        'addition': 'Addition',
        'subtraction': 'Subtraction',
        'multiplication': 'Multiplication',
        'division': 'Division',
        'fractions': 'Fractions',
        'decimals': 'Decimals',
        'geometry': 'Geometry',
        'algebra': 'Algebra',
        
        # Word Master
        'spell_word': 'Spell this word:',
        'define_word': 'What does this word mean?',
        'synonym': 'Find the synonym:',
        'antonym': 'Find the antonym:',
        'complete_sentence': 'Complete the sentence:',
        'word_puzzle': 'Word Puzzle',
        'vocabulary': 'Vocabulary',
        'grammar': 'Grammar',
        
        # Science Lab
        'experiment': 'Experiment',
        'hypothesis': 'Hypothesis',
        'observation': 'Observation',
        'conclusion': 'Conclusion',
        'physics': 'Physics',
        'chemistry': 'Chemistry',
        'biology': 'Biology',
        'earth_science': 'Earth Science',
        'what_happens_when': 'What happens when...',
        'scientific_method': 'Scientific Method',
        
        # Geography Quest
        'capital_of': 'What is the capital of',
        'locate_country': 'Locate this country:',
        'continent': 'Continent',
        'ocean': 'Ocean',
        'mountain': 'Mountain',
        'river': 'River',
        'landmark': 'Landmark',
        'culture': 'Culture',
        'flag': 'Flag',
        
        # History Hunter
        'when_did': 'When did this happen?',
        'who_was': 'Who was...',
        'ancient_history': 'Ancient History',
        'medieval_period': 'Medieval Period',
        'modern_history': 'Modern History',
        'world_wars': 'World Wars',
        'independence': 'Independence',
        'civilization': 'Civilization',
        'timeline': 'Timeline',
        
        # Art Creator
        'color_theory': 'Color Theory',
        'draw_shape': 'Draw this shape:',
        'primary_colors': 'Primary Colors',
        'secondary_colors': 'Secondary Colors',
        'art_style': 'Art Style',
        'famous_artist': 'Famous Artist',
        'painting': 'Painting',
        'sculpture': 'Sculpture',
        'design': 'Design',
        
        # Music Maestro
        'note': 'Note',
        'rhythm': 'Rhythm',
        'melody': 'Melody',
        'instrument': 'Instrument',
        'composer': 'Composer',
        'music_theory': 'Music Theory',
        'beat': 'Beat',
        'tempo': 'Tempo',
        'scale': 'Scale',
        'chord': 'Chord',
        
        # Code Ninja
        'algorithm': 'Algorithm',
        'variable': 'Variable',
        'function': 'Function',
        'loop': 'Loop',
        'condition': 'Condition',
        'debug': 'Debug',
        'programming': 'Programming',
        'code': 'Code',
        'syntax': 'Syntax',
        'logic': 'Logic',
        
        # Logic Puzzle
        'pattern': 'Pattern',
        'sequence': 'Sequence',
        'next_in_series': 'What comes next in this series?',
        'logical_reasoning': 'Logical Reasoning',
        'problem_solving': 'Problem Solving',
        'critical_thinking': 'Critical Thinking',
        'deduction': 'Deduction',
        'inference': 'Inference',
        
        # Memory Palace
        'memorize': 'Memorize',
        'recall': 'Recall',
        'remember_sequence': 'Remember this sequence:',
        'memory_game': 'Memory Game',
        'concentration': 'Concentration',
        'attention': 'Attention',
        'cognitive_skill': 'Cognitive Skill',
        'brain_training': 'Brain Training',
        
        # Achievements
        'first_steps': 'First Steps',
        'quick_learner': 'Quick Learner',
        'perfectionist': 'Perfectionist',
        'speed_demon': 'Speed Demon',
        'persistent': 'Persistent',
        'explorer': 'Explorer',
        'genius': 'Genius',
        'master': 'Master',
        'champion': 'Champion',
        'legend': 'Legend',
        
        # Messages
        'well_done': 'Well done!',
        'excellent': 'Excellent!',
        'good_job': 'Good job!',
        'keep_trying': 'Keep trying!',
        'almost_there': 'Almost there!',
        'perfect_score': 'Perfect score!',
        'new_record': 'New record!',
        'level_up': 'Level up!',
        'game_over': 'Game Over',
        'play_again': 'Play Again',
        
        # Instructions
        'click_to_start': 'Click to start',
        'select_answer': 'Select your answer',
        'drag_and_drop': 'Drag and drop',
        'type_answer': 'Type your answer',
        'choose_option': 'Choose the correct option',
        'match_pairs': 'Match the pairs',
        'arrange_order': 'Arrange in correct order',
        
        # Time and Scoring
        'seconds': 'seconds',
        'minutes': 'minutes',
        'points': 'points',
        'bonus': 'Bonus',
        'streak': 'Streak',
        'multiplier': 'Multiplier',
        'total': 'Total',
        'best': 'Best',
        'average': 'Average'
    },
    
    'ta': {
        # Main Interface
        'title': 'கல்விக்கோளம்: 10 மேதைமையின் உலகங்கள்',
        'subtitle': '10 கல்வி உலகங்களில் வல்லுநராகி மேதையாகுங்கள்!',
        'select_language': 'மொழியைத் தேர்ந்தெடுக்கவும்',
        'player_name': 'உங்கள் பெயரை உள்ளிடவும்',
        'please_enter_name': 'உங்கள் கல்வி பயணத்தைத் தொடங்க உங்கள் பெயரை உள்ளிடவும்!',
        'choose_your_realm': 'உங்கள் கல்வி உலகத்தைத் தேர்ந்தெடுக்கவும்',
        'play_now': 'இப்போது விளையாடுங்கள்',
        
        # Navigation
        'main_menu': 'பிரதான மெனு',
        'leaderboard': 'தலைமை பலகை',
        'my_progress': 'என் முன்னேற்றம்',
        'achievements': 'சாதனைகள்',
        'settings': 'அமைப்புகள்',
        'back_to_menu': 'மெனுவுக்குத் திரும்பு',
        
        # Game Interface
        'level': 'நிலை',
        'score': 'மதிப்பெண்',
        'time_remaining': 'மீதமுள்ள நேரம்',
        'question': 'கேள்வி',
        'answer': 'பதில்',
        'submit': 'சமர்பிக்கவும்',
        'next_question': 'அடுத்த கேள்வி',
        'next_level': 'அடுத்த நிலை',
        'game_complete': 'விளையாட்டு முடிந்தது!',
        'congratulations': 'வாழ்த்துக்கள்!',
        'your_score': 'உங்கள் மதிப்பெண்',
        'time_taken': 'எடுத்த நேரம்',
        'correct': 'சரி!',
        'incorrect': 'தவறு!',
        'try_again': 'மீண்டும் முயற்சிக்கவும்',
        'hint': 'குறிப்பு',
        'skip': 'தவிர்க்கவும்',
        
        # Game Names
        'math_wizard': 'கணித மந்திரவாதி',
        'word_master': 'சொல் மாஸ்டர்',
        'science_lab': 'அறிவியல் ஆய்வகம்',
        'geography_quest': 'புவியியல் தேடல்',
        'history_hunter': 'வரலாற்று வேட்டைக்காரன்',
        'art_creator': 'கலை படைப்பாளி',
        'music_maestro': 'இசை மேஸ்ட்ரோ',
        'code_ninja': 'கோட் நிஞ்ஜா',
        'logic_puzzle': 'தர்க்க புதிர்',
        'memory_palace': 'நினைவக அரண்மனை',
        
        # Game Descriptions
        'math_wizard_desc': 'கணித செயல்பாடுகள் மற்றும் கருத்துகளில் வல்லுநராகுங்கள்',
        'word_master_desc': 'சொல்வளம் மற்றும் மொழித் திறன்களை மேம்படுத்துங்கள்',
        'science_lab_desc': 'அறிவியல் கருத்துகள் மற்றும் சோதனைகளை ஆராயுங்கள்',
        'geography_quest_desc': 'உலக புவியியல் மற்றும் கலாச்சாரங்களைக் கண்டறியுங்கள்',
        'history_hunter_desc': 'வரலாற்று நிகழ்வுகள் மற்றும் நபர்களின் வழியாக பயணம்',
        'art_creator_desc': 'கலை மற்றும் வடிவமைப்பின் மூலம் படைப்பாற்றலை வெளிப்படுத்துங்கள்',
        'music_maestro_desc': 'இசைக் கருத்துகள் மற்றும் இசையமைப்பைக் கற்றுக்கொள்ளுங்கள்',
        'code_ninja_desc': 'நிரலாக்க அடிப்படைகளில் வல்லுநராகுங்கள்',
        'logic_puzzle_desc': 'தர்க்கரீதியான சிந்தனை மற்றும் சிக்கல் தீர்வை வளர்க்கவும்',
        'memory_palace_desc': 'நினைவகம் மற்றும் அறிவாற்றல் திறன்களை மேம்படுத்துங்கள்',
        
        # Math Wizard
        'solve_problem': 'இந்த கணிதப் பிரச்சினையைத் தீர்க்கவும்:',
        'enter_answer': 'உங்கள் பதிலை உள்ளிடவும்:',
        'addition': 'கூட்டல்',
        'subtraction': 'கழித்தல்',
        'multiplication': 'பெருக்கல்',
        'division': 'வகுத்தல்',
        'fractions': 'பின்னங்கள்',
        'decimals': 'தசமங்கள்',
        'geometry': 'வடிவியல்',
        'algebra': 'இயற்கணிதம்',
        
        # Word Master
        'spell_word': 'இந்த வார்த்தையை எழுதுங்கள்:',
        'define_word': 'இந்த வார்த்தையின் அர்த்தம் என்ன?',
        'synonym': 'ஒத்த சொல்லைக் கண்டறியவும்:',
        'antonym': 'எதிர்ச்சொல்லைக் கண்டறியவும்:',
        'complete_sentence': 'வாக்கியத்தை முடிக்கவும்:',
        'word_puzzle': 'சொல் புதிர்',
        'vocabulary': 'சொல்வளம்',
        'grammar': 'இலக்கணம்',
        
        # Science Lab
        'experiment': 'சோதனை',
        'hypothesis': 'கருதுகோள்',
        'observation': 'கவனிப்பு',
        'conclusion': 'முடிவு',
        'physics': 'இயற்பியல்',
        'chemistry': 'வேதியியல்',
        'biology': 'உயிரியல்',
        'earth_science': 'பூமி அறிவியல்',
        'what_happens_when': 'எப்போது என்ன நடக்கும்...',
        'scientific_method': 'அறிவியல் முறை',
        
        # Geography Quest
        'capital_of': 'இதன் தலைநகரம் என்ன',
        'locate_country': 'இந்த நாட்டைக் கண்டறியவும்:',
        'continent': 'கண்டம்',
        'ocean': 'கடல்',
        'mountain': 'மலை',
        'river': 'ஆறு',
        'landmark': 'அடையாளம்',
        'culture': 'கலாச்சாரம்',
        'flag': 'கொடி',
        
        # History Hunter
        'when_did': 'இது எப்போது நடந்தது?',
        'who_was': 'யார்...',
        'ancient_history': 'பண்டைய வரலாறு',
        'medieval_period': 'இடைக்கால காலம்',
        'modern_history': 'நவீன வரலாறு',
        'world_wars': 'உலகப் போர்கள்',
        'independence': 'சுதந்திரம்',
        'civilization': 'நாகரிகம்',
        'timeline': 'காலவரிசை',
        
        # Messages
        'well_done': 'நன்றாக செய்தீர்கள்!',
        'excellent': 'சிறப்பு!',
        'good_job': 'நல்ல வேலை!',
        'keep_trying': 'தொடர்ந்து முயற்சிக்கவும்!',
        'almost_there': 'கிட்டத்தட்ட வந்துவிட்டீர்கள்!',
        'perfect_score': 'சரியான மதிப்பெண்!',
        'new_record': 'புதிய சாதனை!',
        'level_up': 'நிலை உயர்வு!',
        'game_over': 'விளையாட்டு முடிந்தது',
        'play_again': 'மீண்டும் விளையாடுங்கள்',
        
        # Time and Scoring
        'seconds': 'விநாடிகள்',
        'minutes': 'நிமிடங்கள்',
        'points': 'புள்ளிகள்',
        'bonus': 'போனஸ்',
        'streak': 'தொடர்ச்சி',
        'multiplier': 'பெருக்கி',
        'total': 'மொத்தம்',
        'best': 'சிறந்த',
        'average': 'சராசரி'
    }
}
