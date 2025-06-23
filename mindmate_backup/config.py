import os

# Groq API Configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY')  # Loaded from .env file

# Database Configuration
DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'mindmate.db')

# Application Settings
DEBUG = True
LOG_LEVEL = 'INFO'

# Mood Analysis Settings
MOOD_ANALYSIS_THRESHOLD = 0.5
