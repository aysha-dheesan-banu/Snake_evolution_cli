#!/usr/bin/env python3
"""
Enhanced setup script for Snake Evolution game
Handles virtual environments and provides comprehensive setup
"""

import subprocess
import sys
import os
import venv

def create_virtual_environment():
    """Create a virtual environment for the game"""
    venv_path = "snake_env"
    
    if os.path.exists(venv_path):
        print(f"✅ Virtual environment '{venv_path}' already exists")
        return venv_path
    
    print(f"🔧 Creating virtual environment '{venv_path}'...")
    try:
        venv.create(venv_path, with_pip=True)
        print(f"✅ Virtual environment created successfully!")
        return venv_path
    except Exception as e:
        print(f"❌ Error creating virtual environment: {e}")
        return None

def get_venv_python(venv_path):
    """Get the Python executable path for the virtual environment"""
    if os.name == 'nt':  # Windows
        return os.path.join(venv_path, 'Scripts', 'python.exe')
    else:  # Unix/Linux/macOS
        return os.path.join(venv_path, 'bin', 'python')

def install_requirements(venv_path):
    """Install required packages in virtual environment"""
    print("📦 Installing pygame in virtual environment...")
    
    python_exe = get_venv_python(venv_path)
    
    try:
        subprocess.check_call([
            python_exe, "-m", "pip", "install", "pygame==2.5.2"
        ])
        print("✅ Pygame installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing pygame: {e}")
        return False

def test_pygame(venv_path):
    """Test if pygame is working in the virtual environment"""
    print("🧪 Testing pygame installation...")
    
    python_exe = get_venv_python(venv_path)
    
    test_code = """
import pygame
print('Pygame version:', pygame.version.ver)
pygame.init()
print('Pygame initialized successfully!')
pygame.quit()
"""
    
    try:
        result = subprocess.run([
            python_exe, "-c", test_code
        ], capture_output=True, text=True, check=True)
        
        print("✅ Pygame test successful!")
        print(result.stdout.strip())
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Pygame test failed: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def create_launcher_script(venv_path):
    """Create a launcher script for easy game execution"""
    python_exe = get_venv_python(venv_path)
    
    if os.name == 'nt':  # Windows
        launcher_content = f"""@echo off
echo 🐍 Starting Snake Evolution...
"{python_exe}" snake_evolution.py
pause
"""
        launcher_file = "play_snake.bat"
    else:  # Unix/Linux/macOS
        launcher_content = f"""#!/bin/bash
echo "🐍 Starting Snake Evolution..."
"{python_exe}" snake_evolution.py
"""
        launcher_file = "play_snake.sh"
    
    try:
        with open(launcher_file, 'w') as f:
            f.write(launcher_content)
        
        if not os.name == 'nt':
            os.chmod(launcher_file, 0o755)  # Make executable on Unix systems
        
        print(f"✅ Launcher script created: {launcher_file}")
        return launcher_file
    except Exception as e:
        print(f"❌ Error creating launcher script: {e}")
        return None

def display_instructions(venv_path, launcher_file):
    """Display final instructions to the user"""
    python_exe = get_venv_python(venv_path)
    
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETE!")
    print("="*60)
    print("\n🎮 How to play Snake Evolution:")
    print("\nOption 1 - Use the launcher script:")
    if os.name == 'nt':
        print(f"   Double-click: {launcher_file}")
    else:
        print(f"   Run: ./{launcher_file}")
    
    print(f"\nOption 2 - Manual command:")
    print(f"   {python_exe} snake_evolution.py")
    
    print("\n🎯 Game Controls:")
    print("   Arrow Keys: Move snake")
    print("   SPACE: Start game")
    print("   P: Pause/Resume")
    print("   L: Toggle language (English/Tamil)")
    print("   1-4: Answer questions")
    print("   R: Restart (when game over)")
    print("   Q: Quit (when game over)")
    
    print("\n📚 Educational Features:")
    print("   • Progressive math difficulty (10 levels)")
    print("   • Streak bonuses for consecutive correct answers")
    print("   • Multilingual support (English & Tamil)")
    print("   • Real-time performance tracking")
    
    print("\n🐍 Enjoy learning with Snake Evolution!")
    print("="*60)

def main():
    """Main setup function"""
    print("=" * 60)
    print("🐍 Snake Evolution - Complete Setup")
    print("Part of EduVerse: The 10 Realms of Genius")
    print("=" * 60)
    
    # Check if game file exists
    if not os.path.exists("snake_evolution.py"):
        print("❌ snake_evolution.py not found!")
        print("Make sure you're running this script in the same directory as the game file.")
        return
    
    # Create virtual environment
    venv_path = create_virtual_environment()
    if not venv_path:
        print("❌ Failed to create virtual environment. Exiting.")
        return
    
    # Install requirements
    if not install_requirements(venv_path):
        print("❌ Failed to install requirements. Exiting.")
        return
    
    # Test pygame
    if not test_pygame(venv_path):
        print("❌ Pygame test failed. Please check the installation.")
        return
    
    # Create launcher script
    launcher_file = create_launcher_script(venv_path)
    
    # Display final instructions
    display_instructions(venv_path, launcher_file)
    
    # Ask if user wants to play now
    print("\n" + "-"*40)
    response = input("Would you like to start the game now? (y/n): ").lower().strip()
    
    if response in ['y', 'yes', '']:
        print("\n🚀 Launching Snake Evolution...")
        python_exe = get_venv_python(venv_path)
        try:
            subprocess.run([python_exe, "snake_evolution.py"])
        except KeyboardInterrupt:
            print("\n👋 Thanks for playing Snake Evolution!")
        except Exception as e:
            print(f"❌ Error launching game: {e}")
    else:
        print("\n👋 Setup complete! Use the launcher script to play later.")

if __name__ == "__main__":
    main()
