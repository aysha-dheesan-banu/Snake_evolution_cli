"""
EduVerse Games Package
Contains all 10 game modules (5 Educational + 5 Fun)
"""

# Import the 10 games we created
from . import math_wizard
from . import word_master
from . import science_lab
from . import geography_quest
from . import history_hunter
from . import target_practice
from . import puzzle_master
from . import lucky_numbers
from . import memory_game
from . import quick_quiz

__all__ = [
    # Educational Games
    'math_wizard',
    'word_master', 
    'science_lab',
    'geography_quest',
    'history_hunter',
    # Fun Games
    'target_practice',
    'puzzle_master',
    'lucky_numbers',
    'memory_game',
    'quick_quiz'
]
