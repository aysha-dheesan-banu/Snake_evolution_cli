#!/bin/bash

# Snake Evolution Game Launcher
# Part of EduVerse: The 10 Realms of Genius

echo "🐍 Starting Snake Evolution with Category Selection..."
echo "Part of EduVerse: The 10 Realms of Genius"
echo ""

# Check if snake environment exists
if [ ! -d "snake_env" ]; then
    echo "❌ Snake environment not found!"
    echo "Please run: python3 setup_snake.py"
    exit 1
fi

# Activate the snake environment and run the game
source snake_env/bin/activate
python snake_evolution.py

echo ""
echo "👋 Thanks for playing Snake Evolution!"
echo "🎓 Part of EduVerse: Where Education Meets Adventure!"
