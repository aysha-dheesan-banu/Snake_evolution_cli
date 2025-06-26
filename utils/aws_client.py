"""
AWS Client utilities for EduVerse
Handles API calls to AWS services
"""

import requests
import json
import os
import streamlit as st
from typing import Dict, List, Any, Optional
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

class AWSClient:
    """AWS client for EduVerse game platform"""
    
    def __init__(self):
        self.api_base_url = os.environ.get('API_GATEWAY_URL', '')
        self.region = os.environ.get('AWS_REGION', 'us-east-1')
        self.environment = os.environ.get('ENVIRONMENT', 'dev')
        
        # Initialize AWS clients if credentials are available
        try:
            self.dynamodb = boto3.resource('dynamodb', region_name=self.region)
            self.bedrock = boto3.client('bedrock-runtime', region_name=self.region)
            self.rekognition = boto3.client('rekognition', region_name=self.region)
            self.aws_available = True
        except (NoCredentialsError, ClientError):
            self.aws_available = False
            st.warning("AWS services not available. Running in offline mode.")
    
    def start_game_session(self, player_id: str, game_id: int, level: int = 1) -> Optional[str]:
        """Start a new game session"""
        try:
            if not self.api_base_url:
                return self._mock_session_id()
            
            response = requests.post(
                f"{self.api_base_url}/games",
                json={
                    'action': 'start_game',
                    'player_id': player_id,
                    'game_id': str(game_id),
                    'level': level
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('session_id')
            else:
                st.error(f"Failed to start game session: {response.status_code}")
                return self._mock_session_id()
                
        except requests.RequestException as e:
            st.error(f"Network error: {e}")
            return self._mock_session_id()
    
    def submit_score(self, player_id: str, session_id: str, game_id: int, 
                    level: int, score: int, time_taken: float, 
                    level_completed: bool = True) -> bool:
        """Submit game score"""
        try:
            if not self.api_base_url:
                return self._mock_score_submission(player_id, score)
            
            response = requests.post(
                f"{self.api_base_url}/games",
                json={
                    'action': 'submit_score',
                    'player_id': player_id,
                    'session_id': session_id,
                    'game_id': str(game_id),
                    'level': level,
                    'score': score,
                    'time_taken': time_taken,
                    'level_completed': level_completed
                },
                timeout=10
            )
            
            if response.status_code == 200:
                return True
            else:
                st.error(f"Failed to submit score: {response.status_code}")
                return False
                
        except requests.RequestException as e:
            st.error(f"Network error: {e}")
            return self._mock_score_submission(player_id, score)
    
    def get_leaderboard(self, game_id: Optional[int] = None, 
                       limit: int = 10) -> List[Dict]:
        """Get leaderboard data"""
        try:
            if not self.api_base_url:
                return self._mock_leaderboard()
            
            params = {'limit': limit}
            if game_id:
                params['game_id'] = str(game_id)
            
            response = requests.get(
                f"{self.api_base_url}/leaderboard",
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('leaderboard', [])
            else:
                return self._mock_leaderboard()
                
        except requests.RequestException as e:
            st.error(f"Network error: {e}")
            return self._mock_leaderboard()
    
    def get_player_progress(self, player_id: str) -> Dict:
        """Get player progress data"""
        try:
            if not self.api_base_url:
                return self._mock_player_progress()
            
            response = requests.post(
                f"{self.api_base_url}/games",
                json={
                    'action': 'get_player_progress',
                    'player_id': player_id
                },
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return self._mock_player_progress()
                
        except requests.RequestException as e:
            st.error(f"Network error: {e}")
            return self._mock_player_progress()
    
    def generate_ai_question(self, game_id: int, level: int, 
                           language: str = 'en') -> Dict:
        """Generate AI-powered question using Bedrock"""
        try:
            if not self.api_base_url:
                return self._mock_ai_question(game_id, level, language)
            
            response = requests.post(
                f"{self.api_base_url}/games",
                json={
                    'action': 'generate_question',
                    'game_id': str(game_id),
                    'level': level,
                    'language': language
                },
                timeout=15
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return self._mock_ai_question(game_id, level, language)
                
        except requests.RequestException as e:
            st.error(f"Network error: {e}")
            return self._mock_ai_question(game_id, level, language)
    
    def analyze_image(self, image_bytes: bytes) -> Dict:
        """Analyze image using Amazon Rekognition"""
        try:
            if not self.aws_available:
                return self._mock_image_analysis()
            
            response = self.rekognition.detect_labels(
                Image={'Bytes': image_bytes},
                MaxLabels=10,
                MinConfidence=70
            )
            
            labels = []
            for label in response['Labels']:
                labels.append({
                    'name': label['Name'],
                    'confidence': label['Confidence']
                })
            
            return {'labels': labels}
            
        except ClientError as e:
            st.error(f"AWS Rekognition error: {e}")
            return self._mock_image_analysis()
    
    def save_player_data(self, player_id: str, player_data: Dict) -> bool:
        """Save player data to DynamoDB"""
        try:
            if not self.aws_available:
                return self._mock_save_data()
            
            table_name = f"eduverse-players-{self.environment}"
            table = self.dynamodb.Table(table_name)
            
            table.put_item(Item={
                'player_id': player_id,
                **player_data
            })
            
            return True
            
        except ClientError as e:
            st.error(f"Failed to save player data: {e}")
            return False
    
    def load_player_data(self, player_id: str) -> Optional[Dict]:
        """Load player data from DynamoDB"""
        try:
            if not self.aws_available:
                return None
            
            table_name = f"eduverse-players-{self.environment}"
            table = self.dynamodb.Table(table_name)
            
            response = table.get_item(Key={'player_id': player_id})
            
            if 'Item' in response:
                return response['Item']
            else:
                return None
                
        except ClientError as e:
            st.error(f"Failed to load player data: {e}")
            return None
    
    # Mock functions for offline mode
    def _mock_session_id(self) -> str:
        """Generate mock session ID"""
        import uuid
        return str(uuid.uuid4())
    
    def _mock_score_submission(self, player_id: str, score: int) -> bool:
        """Mock score submission"""
        # Update session state instead
        if 'total_score' in st.session_state:
            st.session_state.total_score += score
        return True
    
    def _mock_leaderboard(self) -> List[Dict]:
        """Mock leaderboard data"""
        return [
            {'rank': 1, 'player_name': 'Alex Chen', 'score': 9850, 'games_completed': 10},
            {'rank': 2, 'player_name': 'Priya Sharma', 'score': 9200, 'games_completed': 9},
            {'rank': 3, 'player_name': 'Mohammed Ali', 'score': 8750, 'games_completed': 8},
            {'rank': 4, 'player_name': 'Sarah Johnson', 'score': 8500, 'games_completed': 10},
            {'rank': 5, 'player_name': 'Raj Patel', 'score': 8200, 'games_completed': 7}
        ]
    
    def _mock_player_progress(self) -> Dict:
        """Mock player progress data"""
        return {
            'total_score': st.session_state.get('total_score', 0),
            'games_completed': len(st.session_state.get('player_data', {})),
            'game_progress': st.session_state.get('player_data', {}),
            'achievements': st.session_state.get('achievements', [])
        }
    
    def _mock_ai_question(self, game_id: int, level: int, language: str) -> Dict:
        """Mock AI question generation"""
        from utils.game_data import QUESTION_TEMPLATES
        import random
        
        # Simple question generation based on game and level
        questions = {
            1: {  # Math Wizard
                'en': [
                    f"What is {random.randint(1, 10 * level)} + {random.randint(1, 10 * level)}?",
                    f"Calculate {random.randint(10, 50 * level)} - {random.randint(1, 20)}",
                    f"What is {random.randint(2, level + 5)} × {random.randint(2, 8)}?"
                ],
                'ta': [
                    f"{random.randint(1, 10 * level)} + {random.randint(1, 10 * level)} என்ன?",
                    f"{random.randint(10, 50 * level)} - {random.randint(1, 20)} கணக்கிடுங்கள்",
                    f"{random.randint(2, level + 5)} × {random.randint(2, 8)} என்ன?"
                ]
            },
            2: {  # Word Master
                'en': [
                    "What is the opposite of 'hot'?",
                    "Spell the word that means 'very large'",
                    "Find a synonym for 'happy'"
                ],
                'ta': [
                    "'வெப்பம்' என்பதற்கு எதிர்ச்சொல் என்ன?",
                    "'மிகப் பெரிய' என்று அர்த்தமுள்ள வார்த்தையை எழுதுங்கள்",
                    "'மகிழ்ச்சி' என்பதற்கு ஒத்த சொல்லைக் கண்டறியவும்"
                ]
            }
        }
        
        game_questions = questions.get(game_id, {})
        lang_questions = game_questions.get(language, game_questions.get('en', ['Sample question']))
        
        return {
            'question': random.choice(lang_questions),
            'game_id': game_id,
            'level': level,
            'language': language,
            'mock': True
        }
    
    def _mock_image_analysis(self) -> Dict:
        """Mock image analysis"""
        return {
            'labels': [
                {'name': 'Tree', 'confidence': 95.5},
                {'name': 'Nature', 'confidence': 88.2},
                {'name': 'Plant', 'confidence': 82.1}
            ]
        }
    
    def _mock_save_data(self) -> bool:
        """Mock data saving"""
        return True

# Global AWS client instance
aws_client = AWSClient()
