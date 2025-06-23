import streamlit as st
from pages import home, journal, meditation, resources, analytics, chatbot, mood_tracker, sleep_tracker, goals, professional_help, community
import os
import logging
from utils.database import init_db
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Debug output for environment variables
print("Loaded GROQ_API_KEY:", os.getenv('GROQ_API_KEY') is not None)
print("Loaded DATABASE_PATH:", os.getenv('DATABASE_PATH'))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize database
init_db()

# Page configuration
st.set_page_config(
    page_title="MindMate",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
PAGES = {
    "Home": home,
    "Journal": journal,
    "Meditation": meditation,
    "Analytics": analytics,
    "Resources": resources,
    "Chatbot": chatbot,
    "Mood Tracker": mood_tracker,
    "Sleep Tracker": sleep_tracker,
    "Wellness Goals": goals,
    "Professional Help": professional_help,
    "Community": community
}

def main():
    # Remove sidebar title to avoid duplication
    # st.sidebar.title("MindMate")
    st.sidebar.markdown("Your mental wellness companion")
    
    selection = st.sidebar.radio("", list(PAGES.keys()))
    page = PAGES[selection]
    
    try:
        # Handle different page function names
        if hasattr(page, 'show_home'):
            page.show_home()
        elif hasattr(page, 'show_journal_page'):
            page.show_journal_page()
        elif hasattr(page, 'show_analytics_page'):
            page.show_analytics_page()
        elif hasattr(page, 'show_meditation_page'):
            page.show_meditation_page()
        elif hasattr(page, 'show_resources_page'):
            page.show_resources_page()
        elif hasattr(page, 'show_chatbot_page'):
            page.show_chatbot_page()
        elif hasattr(page, 'show_mood_tracker_page'):
            page.show_mood_tracker_page()
        elif hasattr(page, 'show_sleep_tracker_page'):
            page.show_sleep_tracker_page()
        elif hasattr(page, 'show_goals_page'):
            page.show_goals_page()
        elif hasattr(page, 'show_professional_help_page'):
            page.show_professional_help_page()
        elif hasattr(page, 'show_community_page'):
            page.show_community_page()
        elif hasattr(page, 'show_page'):
            page.show_page()
        else:
            raise AttributeError(f"Page {selection} has no valid show function")
    except Exception as e:
        logger.error(f"Error loading page {selection}: {str(e)}")
        st.error(f"An error occurred while loading the {selection} page")

if __name__ == "__main__":
    main()
