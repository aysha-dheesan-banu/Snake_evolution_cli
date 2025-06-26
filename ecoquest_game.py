import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import json
import boto3
from PIL import Image
import io
import base64

# Configure Streamlit page
st.set_page_config(
    page_title="EcoQuest: Planet Protectors",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize AWS clients (configure with your credentials)
@st.cache_resource
def init_aws_clients():
    try:
        # Initialize AWS clients
        bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
        rekognition = boto3.client('rekognition', region_name='us-east-1')
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        return bedrock, rekognition, dynamodb
    except Exception as e:
        st.warning(f"AWS services not configured: {e}")
        return None, None, None

# Initialize session state
def init_session_state():
    if 'player_name' not in st.session_state:
        st.session_state.player_name = ""
    if 'player_level' not in st.session_state:
        st.session_state.player_level = 1
    if 'eco_points' not in st.session_state:
        st.session_state.eco_points = 100
    if 'current_mission' not in st.session_state:
        st.session_state.current_mission = None
    if 'ecosystem_health' not in st.session_state:
        st.session_state.ecosystem_health = {
            'forest': 75,
            'ocean': 60,
            'city': 45,
            'wildlife': 70
        }
    if 'achievements' not in st.session_state:
        st.session_state.achievements = []
    if 'virtual_pets' not in st.session_state:
        st.session_state.virtual_pets = []
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False

# Game data and configurations
MISSIONS = {
    "Forest Guardian": {
        "description": "Plant 50 virtual trees to restore the Amazon rainforest",
        "target": 50,
        "reward": 200,
        "difficulty": "Easy"
    },
    "Ocean Cleaner": {
        "description": "Remove plastic waste from ocean ecosystems",
        "target": 100,
        "reward": 300,
        "difficulty": "Medium"
    },
    "City Planner": {
        "description": "Design a sustainable city with renewable energy",
        "target": 1,
        "reward": 500,
        "difficulty": "Hard"
    },
    "Species Protector": {
        "description": "Save 10 endangered species from extinction",
        "target": 10,
        "reward": 400,
        "difficulty": "Medium"
    }
}

VIRTUAL_PETS = [
    {"name": "Arctic Fox", "emoji": "🦊", "habitat": "Arctic", "status": "Vulnerable"},
    {"name": "Sea Turtle", "emoji": "🐢", "habitat": "Ocean", "status": "Endangered"},
    {"name": "Panda", "emoji": "🐼", "habitat": "Forest", "status": "Vulnerable"},
    {"name": "Polar Bear", "emoji": "🐻‍❄️", "habitat": "Arctic", "status": "Vulnerable"},
    {"name": "Whale", "emoji": "🐋", "habitat": "Ocean", "status": "Endangered"}
]

# AI-powered mission generator using Bedrock
def generate_ai_mission(bedrock_client, player_level):
    if not bedrock_client:
        return random.choice(list(MISSIONS.keys()))
    
    try:
        prompt = f"""Generate a creative environmental mission for a level {player_level} player in an eco-game. 
        The mission should be educational, age-appropriate, and focus on real environmental issues.
        Return only the mission name and description in this format:
        Mission: [Name]
        Description: [Description]"""
        
        # This is a simplified example - adjust based on your Bedrock model
        response = bedrock_client.invoke_model(
            modelId='anthropic.claude-v2',
            body=json.dumps({
                'prompt': prompt,
                'max_tokens_to_sample': 200
            })
        )
        
        result = json.loads(response['body'].read())
        return result.get('completion', 'Forest Guardian')
    except:
        return random.choice(list(MISSIONS.keys()))

# Image recognition for AR puzzles
def analyze_image_with_rekognition(rekognition_client, image_bytes):
    if not rekognition_client:
        return ["tree", "nature", "environment"]  # Mock response
    
    try:
        response = rekognition_client.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=10,
            MinConfidence=70
        )
        
        labels = [label['Name'].lower() for label in response['Labels']]
        return labels
    except Exception as e:
        st.error(f"Image analysis failed: {e}")
        return []

# Game functions
def update_ecosystem_health(action, ecosystem_type, value):
    """Update ecosystem health based on player actions"""
    current_health = st.session_state.ecosystem_health[ecosystem_type]
    new_health = max(0, min(100, current_health + value))
    st.session_state.ecosystem_health[ecosystem_type] = new_health
    
    if value > 0:
        st.session_state.eco_points += value * 2
        st.success(f"Great job! {ecosystem_type.title()} health improved by {value}%")
    else:
        st.warning(f"{ecosystem_type.title()} health decreased by {abs(value)}%")

def add_achievement(achievement_name):
    """Add achievement to player's collection"""
    if achievement_name not in st.session_state.achievements:
        st.session_state.achievements.append(achievement_name)
        st.balloons()
        st.success(f"🏆 Achievement Unlocked: {achievement_name}!")

def adopt_virtual_pet(pet):
    """Add a virtual pet to player's collection"""
    if pet not in st.session_state.virtual_pets:
        st.session_state.virtual_pets.append(pet)
        st.balloons()
        st.success(f"🎉 You adopted a {pet['name']} {pet['emoji']}!")

# Main game interface
def main_game_interface():
    st.title("🌍 EcoQuest: Planet Protectors")
    st.subheader(f"Welcome, {st.session_state.player_name}! 🌱")
    
    # Initialize AWS clients
    bedrock, rekognition, dynamodb = init_aws_clients()
    
    # Sidebar - Player Stats
    with st.sidebar:
        st.header("🎮 Player Stats")
        st.metric("Level", st.session_state.player_level)
        st.metric("Eco Points", st.session_state.eco_points)
        st.progress(st.session_state.player_level / 10)
        
        st.header("🏆 Achievements")
        if st.session_state.achievements:
            for achievement in st.session_state.achievements:
                st.write(f"🏅 {achievement}")
        else:
            st.write("No achievements yet!")
        
        st.header("🐾 Virtual Pets")
        if st.session_state.virtual_pets:
            for pet in st.session_state.virtual_pets:
                st.write(f"{pet['emoji']} {pet['name']}")
        else:
            st.write("No pets adopted yet!")
    
    # Main game tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌍 Dashboard", "🎯 Missions", "📸 AR Challenges", "🏙️ City Builder", "🌊 Ecosystem Manager"])
    
    with tab1:
        st.header("🌍 Global Ecosystem Dashboard")
        
        # Ecosystem health visualization
        col1, col2 = st.columns(2)
        
        with col1:
            # Ecosystem health chart
            ecosystems = list(st.session_state.ecosystem_health.keys())
            health_values = list(st.session_state.ecosystem_health.values())
            
            fig = px.bar(
                x=ecosystems,
                y=health_values,
                title="Ecosystem Health Status",
                color=health_values,
                color_continuous_scale="RdYlGn"
            )
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Real-time environmental data simulation
            st.subheader("🌡️ Live Environmental Data")
            
            # Simulate real-time data
            temp_data = np.random.normal(15, 5, 30)
            dates = pd.date_range(start=datetime.now() - timedelta(days=29), periods=30)
            
            fig2 = px.line(
                x=dates,
                y=temp_data,
                title="Global Temperature Trend (°C)",
                labels={'x': 'Date', 'y': 'Temperature (°C)'}
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        # Quick actions
        st.subheader("⚡ Quick Actions")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🌳 Plant Tree"):
                update_ecosystem_health("plant_tree", "forest", 5)
                if st.session_state.ecosystem_health["forest"] > 90:
                    add_achievement("Forest Guardian")
        
        with col2:
            if st.button("🌊 Clean Ocean"):
                update_ecosystem_health("clean_ocean", "ocean", 3)
                if st.session_state.ecosystem_health["ocean"] > 85:
                    add_achievement("Ocean Protector")
        
        with col3:
            if st.button("♻️ Recycle"):
                update_ecosystem_health("recycle", "city", 4)
                st.session_state.eco_points += 10
        
        with col4:
            if st.button("🐾 Protect Wildlife"):
                update_ecosystem_health("protect_wildlife", "wildlife", 6)
                if len(st.session_state.virtual_pets) == 0:
                    adopt_virtual_pet(random.choice(VIRTUAL_PETS))
    
    with tab2:
        st.header("🎯 Environmental Missions")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Available Missions")
            
            for mission_name, mission_data in MISSIONS.items():
                with st.expander(f"{mission_name} - {mission_data['difficulty']}"):
                    st.write(f"**Description:** {mission_data['description']}")
                    st.write(f"**Reward:** {mission_data['reward']} Eco Points")
                    st.write(f"**Target:** {mission_data['target']}")
                    
                    if st.button(f"Start {mission_name}", key=f"start_{mission_name}"):
                        st.session_state.current_mission = mission_name
                        st.success(f"Mission '{mission_name}' started!")
                        st.rerun()
        
        with col2:
            if st.session_state.current_mission:
                st.subheader("🎯 Current Mission")
                mission = MISSIONS[st.session_state.current_mission]
                st.write(f"**{st.session_state.current_mission}**")
                st.write(mission['description'])
                
                # Mission progress simulation
                progress = st.slider("Mission Progress", 0, mission['target'], 0)
                st.progress(progress / mission['target'])
                
                if progress >= mission['target']:
                    if st.button("Complete Mission"):
                        st.session_state.eco_points += mission['reward']
                        st.session_state.current_mission = None
                        add_achievement(f"Mission: {st.session_state.current_mission}")
                        st.rerun()
            else:
                st.info("No active mission. Select one from the left!")
    
    with tab3:
        st.header("📸 AR Environmental Challenges")
        st.write("Use your camera to identify environmental objects and earn points!")
        
        # Camera input for AR challenges
        camera_image = st.camera_input("Take a photo of something in nature!")
        
        if camera_image:
            # Display the image
            image = Image.open(camera_image)
            st.image(image, caption="Your photo", width=300)
            
            # Convert image for Rekognition
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            
            # Analyze image
            if st.button("🔍 Analyze Image"):
                with st.spinner("Analyzing your photo..."):
                    labels = analyze_image_with_rekognition(rekognition, img_byte_arr)
                    
                    st.subheader("🎯 Detected Objects:")
                    eco_points_earned = 0
                    
                    for label in labels:
                        st.write(f"• {label.title()}")
                        
                        # Award points for environmental objects
                        if any(eco_word in label.lower() for eco_word in ['tree', 'plant', 'flower', 'nature', 'water', 'sky', 'animal']):
                            eco_points_earned += 10
                    
                    if eco_points_earned > 0:
                        st.session_state.eco_points += eco_points_earned
                        st.success(f"Great photo! You earned {eco_points_earned} Eco Points!")
                        
                        if eco_points_earned >= 50:
                            add_achievement("Nature Photographer")
        
        # AR Challenge suggestions
        st.subheader("🎯 Today's AR Challenges")
        challenges = [
            "📸 Find and photograph a tree",
            "📸 Spot recyclable materials",
            "📸 Capture a water source",
            "📸 Find renewable energy (solar panels, wind turbines)",
            "📸 Photograph local wildlife"
        ]
        
        for challenge in challenges:
            st.write(f"• {challenge} - **20 points**")
    
    with tab4:
        st.header("🏙️ Sustainable City Builder")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Design Your Eco-City")
            
            # City building options
            renewable_energy = st.slider("🔋 Renewable Energy %", 0, 100, 50)
            green_spaces = st.slider("🌳 Green Spaces %", 0, 100, 30)
            public_transport = st.slider("🚌 Public Transport Coverage %", 0, 100, 40)
            recycling_rate = st.slider("♻️ Recycling Rate %", 0, 100, 60)
            
            # Calculate city sustainability score
            sustainability_score = (renewable_energy + green_spaces + public_transport + recycling_rate) / 4
            
            st.metric("🌱 City Sustainability Score", f"{sustainability_score:.1f}/100")
            
            # Visualize city stats
            city_data = {
                'Category': ['Renewable Energy', 'Green Spaces', 'Public Transport', 'Recycling'],
                'Percentage': [renewable_energy, green_spaces, public_transport, recycling_rate]
            }
            
            fig = px.radar(
                city_data,
                r='Percentage',
                theta='Category',
                title="Your Eco-City Profile"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("🎯 City Goals")
            
            if sustainability_score >= 80:
                st.success("🏆 Eco-City Master!")
                add_achievement("Eco-City Master")
            elif sustainability_score >= 60:
                st.info("🌱 Good progress! Keep improving!")
            else:
                st.warning("🔧 Your city needs more sustainable features!")
            
            if st.button("💾 Save City Design"):
                update_ecosystem_health("city_design", "city", int(sustainability_score/10))
                st.success("City design saved!")
    
    with tab5:
        st.header("🌊 Ecosystem Manager")
        
        # Interactive ecosystem management
        st.subheader("🌍 Manage Global Ecosystems")
        
        ecosystem_choice = st.selectbox(
            "Choose an ecosystem to manage:",
            ["forest", "ocean", "city", "wildlife"]
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Current {ecosystem_choice.title()} Health:** {st.session_state.ecosystem_health[ecosystem_choice]}%")
            
            # Management actions
            if ecosystem_choice == "forest":
                actions = {
                    "Plant trees": 8,
                    "Stop deforestation": 12,
                    "Create protected areas": 15,
                    "Fight forest fires": 10
                }
            elif ecosystem_choice == "ocean":
                actions = {
                    "Remove plastic waste": 10,
                    "Reduce overfishing": 8,
                    "Create marine reserves": 12,
                    "Reduce pollution": 15
                }
            elif ecosystem_choice == "city":
                actions = {
                    "Add green roofs": 6,
                    "Improve public transport": 8,
                    "Install solar panels": 10,
                    "Create bike lanes": 5
                }
            else:  # wildlife
                actions = {
                    "Create wildlife corridors": 12,
                    "Stop poaching": 15,
                    "Restore habitats": 10,
                    "Reduce human conflict": 8
                }
            
            selected_action = st.selectbox("Choose an action:", list(actions.keys()))
            
            if st.button(f"Execute: {selected_action}"):
                improvement = actions[selected_action]
                update_ecosystem_health(selected_action, ecosystem_choice, improvement)
                
                # Check for achievements
                if st.session_state.ecosystem_health[ecosystem_choice] >= 95:
                    add_achievement(f"{ecosystem_choice.title()} Master")
        
        with col2:
            # Show ecosystem health over time (simulated)
            days = list(range(1, 31))
            health_trend = [st.session_state.ecosystem_health[ecosystem_choice] + random.randint(-5, 5) for _ in days]
            
            fig = px.line(
                x=days,
                y=health_trend,
                title=f"{ecosystem_choice.title()} Health Trend (30 days)",
                labels={'x': 'Days', 'y': 'Health %'}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Global impact summary
        st.subheader("🌍 Global Impact Summary")
        total_health = sum(st.session_state.ecosystem_health.values()) / len(st.session_state.ecosystem_health)
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🌳 Forest Health", f"{st.session_state.ecosystem_health['forest']}%")
        col2.metric("🌊 Ocean Health", f"{st.session_state.ecosystem_health['ocean']}%")
        col3.metric("🏙️ City Health", f"{st.session_state.ecosystem_health['city']}%")
        col4.metric("🐾 Wildlife Health", f"{st.session_state.ecosystem_health['wildlife']}%")
        
        st.metric("🌍 Overall Planet Health", f"{total_health:.1f}%")
        
        if total_health >= 90:
            st.success("🎉 Congratulations! You're a true Planet Protector!")
            add_achievement("Planet Protector Master")

# Login/Welcome screen
def welcome_screen():
    st.title("🌍 Welcome to EcoQuest: Planet Protectors!")
    st.subheader("Join the mission to save our planet! 🌱")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("https://via.placeholder.com/400x300/4CAF50/FFFFFF?text=EcoQuest", width=400)
        
        st.write("""
        **🎮 About the Game:**
        - Manage global ecosystems and protect the environment
        - Complete exciting missions and challenges
        - Use AR technology to interact with the real world
        - Build sustainable cities and adopt virtual pets
        - Collaborate with friends to save the planet!
        """)
        
        player_name = st.text_input("Enter your Planet Protector name:", placeholder="EcoHero123")
        
        if st.button("🚀 Start Your Eco-Adventure!", type="primary"):
            if player_name:
                st.session_state.player_name = player_name
                st.session_state.game_started = True
                st.rerun()
            else:
                st.error("Please enter your name to start!")

# Main app logic
def main():
    init_session_state()
    
    if not st.session_state.game_started:
        welcome_screen()
    else:
        main_game_interface()

if __name__ == "__main__":
    main()
