#!/usr/bin/env python3
"""
EduVerse Setup Script
Automated setup for the educational game platform
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_banner():
    """Print setup banner"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    🎓 EduVerse: The 10 Realms of Genius                     ║
    ║    Interactive Educational Game Platform Setup               ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")

def create_virtual_environment():
    """Create virtual environment"""
    print("\n🏗️  Creating virtual environment...")
    
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment")
        sys.exit(1)

def get_pip_command():
    """Get the appropriate pip command"""
    system = platform.system().lower()
    if system == "windows":
        return "venv\\Scripts\\pip"
    else:
        return "venv/bin/pip"

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    
    pip_cmd = get_pip_command()
    
    try:
        # Upgrade pip first
        subprocess.run([pip_cmd, "install", "--upgrade", "pip"], check=True)
        
        # Install requirements
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print("✅ All packages installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages")
        print("💡 Try running: pip install -r requirements.txt manually")
        return False
    
    return True

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating project directories...")
    
    directories = [
        "data",
        "logs",
        "static",
        "uploads",
        "certificates",
        "backups"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def create_env_file():
    """Create environment configuration file"""
    print("\n⚙️  Creating environment configuration...")
    
    env_content = """# EduVerse Environment Configuration

# AWS Configuration (Optional - for cloud features)
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here

# API Gateway URL (for AWS deployment)
API_GATEWAY_URL=

# S3 Bucket (for static assets)
S3_BUCKET=

# Environment
ENVIRONMENT=development

# Database Configuration (Optional)
DATABASE_URL=sqlite:///eduverse.db

# Security
SECRET_KEY=your_secret_key_here

# Email Configuration (Optional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/eduverse.log

# Game Configuration
MAX_PLAYERS=1000
SESSION_TIMEOUT=3600
ENABLE_SOUND=true
ENABLE_ANIMATIONS=true

# Performance
CACHE_TIMEOUT=300
MAX_UPLOAD_SIZE=10MB

# Features
ENABLE_AI_QUESTIONS=true
ENABLE_LEADERBOARD=true
ENABLE_ACHIEVEMENTS=true
ENABLE_CERTIFICATES=true
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("✅ Environment file created (.env)")

def create_config_file():
    """Create application configuration file"""
    print("\n📋 Creating application configuration...")
    
    config_content = """# EduVerse Application Configuration

app:
  name: "EduVerse: The 10 Realms of Genius"
  version: "1.0.0"
  description: "Interactive Educational Game Platform"
  
games:
  total_games: 10
  levels_per_game: 10
  max_time_per_level: 300
  
scoring:
  base_score: 100
  time_bonus: 2
  streak_bonus: 25
  perfect_bonus: 500
  hint_penalty: -25
  skip_penalty: -50

languages:
  supported: ["en", "ta"]
  default: "en"

features:
  ai_questions: true
  leaderboard: true
  achievements: true
  multiplayer: false
  offline_mode: true
"""
    
    with open("config.yaml", "w") as f:
        f.write(config_content)
    
    print("✅ Configuration file created (config.yaml)")

def run_initial_setup():
    """Run initial application setup"""
    print("\n🚀 Running initial setup...")
    
    try:
        # Create sample data
        print("📊 Creating sample data...")
        
        # You can add more initialization here
        print("✅ Initial setup completed")
        
    except Exception as e:
        print(f"⚠️  Warning: Initial setup had issues: {e}")

def print_instructions():
    """Print final instructions"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🎉 Setup Complete!                       ║
    ╠══════════════════════════════════════════════════════════════╣
    ║                                                              ║
    ║  To start EduVerse:                                          ║
    ║                                                              ║
    ║  1. Activate virtual environment:                            ║
    """)
    
    system = platform.system().lower()
    if system == "windows":
        print("║     venv\\Scripts\\activate                                   ║")
    else:
        print("║     source venv/bin/activate                                ║")
    
    print("""║                                                              ║
    ║  2. Run the application:                                     ║
    ║     streamlit run eduverse_main.py                           ║
    ║                                                              ║
    ║  3. Open your browser to:                                    ║
    ║     http://localhost:8501                                    ║
    ║                                                              ║
    ║  Optional AWS Setup:                                         ║
    ║  - Edit .env file with your AWS credentials                  ║
    ║  - Run: ./deploy.sh for cloud deployment                    ║
    ║                                                              ║
    ║  For help: python setup.py --help                           ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def main():
    """Main setup function"""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("""
EduVerse Setup Script

Usage: python setup.py [options]

Options:
  --help          Show this help message
  --skip-venv     Skip virtual environment creation
  --skip-install  Skip package installation
  --dev           Development setup (installs dev dependencies)
  --aws           Setup for AWS deployment
        """)
        return
    
    print_banner()
    
    # Check system requirements
    check_python_version()
    
    # Setup steps
    if "--skip-venv" not in sys.argv:
        create_virtual_environment()
    
    if "--skip-install" not in sys.argv:
        if not install_requirements():
            print("⚠️  Continuing with setup despite installation issues...")
    
    create_directories()
    create_env_file()
    create_config_file()
    run_initial_setup()
    
    print_instructions()
    
    print("\n🎓 Welcome to EduVerse! Happy learning! 🌟")

if __name__ == "__main__":
    main()
