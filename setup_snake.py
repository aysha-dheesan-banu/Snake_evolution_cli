#!/usr/bin/env python3
"""
Setup script for Snake Evolution game
Installs dependencies and provides game launcher
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("🐍 Setting up Snake Evolution...")
    print("Installing dependencies...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements_snake.txt"
        ])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_pygame():
    """Check if pygame is working"""
    try:
        import pygame
        pygame.init()
        print("✅ Pygame is working correctly!")
        pygame.quit()
        return True
    except ImportError:
        print("❌ Pygame not found. Please install it manually:")
        print("   pip install pygame")
        return False
    except Exception as e:
        print(f"❌ Pygame error: {e}")
        return False

def launch_game():
    """Launch the Snake Evolution game"""
    print("\n🚀 Launching Snake Evolution...")
    print("Game Controls:")
    print("  - Arrow Keys: Move snake")
    print("  - SPACE: Start game (from menu)")
    print("  - P: Pause/Resume")
    print("  - L: Toggle language (English/Tamil)")
    print("  - 1-4: Answer questions")
    print("  - R: Restart (game over screen)")
    print("  - Q: Quit (game over screen)")
    print("\nStarting game in 3 seconds...")
    
    import time
    time.sleep(3)
    
    try:
        import snake_evolution
        snake_evolution.main()
    except ImportError:
        print("❌ Could not import snake_evolution.py")
        print("Make sure the file is in the current directory")
    except Exception as e:
        print(f"❌ Error launching game: {e}")

def main():
    """Main setup function"""
    print("=" * 50)
    print("🐍 Snake Evolution Setup")
    print("Part of EduVerse: The 10 Realms of Genius")
    print("=" * 50)
    
    # Check if requirements file exists
    if not os.path.exists("requirements_snake.txt"):
        print("❌ requirements_snake.txt not found!")
        print("Creating requirements file...")
        with open("requirements_snake.txt", "w") as f:
            f.write("pygame==2.5.2\n")
    
    # Install dependencies
    if not install_requirements():
        print("❌ Setup failed. Please install pygame manually:")
        print("   pip install pygame")
        return
    
    # Check pygame
    if not check_pygame():
        print("❌ Pygame check failed. Please troubleshoot pygame installation.")
        return
    
    # Check if game file exists
    if not os.path.exists("snake_evolution.py"):
        print("❌ snake_evolution.py not found!")
        print("Make sure the game file is in the current directory.")
        return
    
    print("\n✅ Setup complete!")
    
    # Ask user if they want to launch the game
    response = input("\nWould you like to launch the game now? (y/n): ").lower().strip()
    if response in ['y', 'yes', '']:
        launch_game()
    else:
        print("\n🎮 To play later, run: python snake_evolution.py")
        print("Enjoy learning with Snake Evolution! 🐍📚")

if __name__ == "__main__":
    main()
