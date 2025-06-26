#!/bin/bash

# Quick Start Script for Snake Evolution & EduVerse
# Repository: https://github.com/aysha-dheesan-banu/eduverse-snake-evolution
# This script helps anyone quickly set up and play the games

echo "🐍 Welcome to Snake Evolution & EduVerse Setup!"
echo "Repository: https://github.com/aysha-dheesan-banu/eduverse-snake-evolution"
echo "================================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Create virtual environment
echo "📦 Setting up virtual environment..."
python3 -m venv game_env
source game_env/bin/activate

# Install requirements
echo "📥 Installing game dependencies..."
pip install --upgrade pip
pip install pygame streamlit pandas numpy

echo ""
echo "🎮 Choose how to play:"
echo "1) 🐍 Snake Evolution (Desktop Game)"
echo "2) 🌐 EduVerse Web Platform (All Games)"
echo "3) 🚀 Both!"
echo ""

read -p "Enter your choice (1, 2, or 3): " choice

case $choice in
    1)
        echo "🐍 Starting Snake Evolution..."
        python3 snake_evolution.py
        ;;
    2)
        echo "🌐 Starting EduVerse Web Platform..."
        echo "Open your browser to: http://localhost:8501"
        streamlit run eduverse_main.py
        ;;
    3)
        echo "🚀 Starting both! Snake Evolution first, then web platform..."
        python3 snake_evolution.py
        echo "Now starting web platform..."
        streamlit run eduverse_main.py
        ;;
    *)
        echo "❌ Invalid choice. Running Snake Evolution by default..."
        python3 snake_evolution.py
        ;;
esac

echo ""
echo "👋 Thanks for playing!"
echo "🌟 Don't forget to star our GitHub repository!"
