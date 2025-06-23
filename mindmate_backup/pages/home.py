import streamlit as st
from datetime import datetime, timedelta
from utils.database import get_journal_stats, get_meditation_stats
from utils.visualization import display_visualizations
import logging

logger = logging.getLogger(__name__)

def show_welcome_banner():
    """Display welcome banner with personalized greeting"""
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    
    st.markdown(f"""
        <div style="background-color:#f0f2f6;padding:20px;border-radius:10px;margin-bottom:20px">
            <h1 style="color:#2e86de;margin:0;">{greeting}! 👋</h1>
            <p style="color:#576574;margin:0;">Welcome to your MindMate dashboard</p>
        </div>
    """, unsafe_allow_html=True)

def show_quick_stats():
    """Display quick stats cards"""
    journal_stats = get_journal_stats()
    meditation_stats = get_meditation_stats()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div style="background-color:#ffffff;padding:15px;border-radius:10px;box-shadow:0 4px 6px rgba(0,0,0,0.1)">
                <h3 style="color:#576574;margin:0;">Journal Entries</h3>
                <p style="color:#2e86de;font-size:32px;font-weight:bold;margin:0;">{journal_stats.get('total_entries', 0)}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style="background-color:#ffffff;padding:15px;border-radius:10px;box-shadow:0 4px 6px rgba(0,0,0,0.1)">
                <h3 style="color:#576574;margin:0;">Avg Mood</h3>
                <p style="color:#2e86de;font-size:32px;font-weight:bold;margin:0;">{journal_stats.get('avg_mood', 0):.1f}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div style="background-color:#ffffff;padding:15px;border-radius:10px;box-shadow:0 4px 6px rgba(0,0,0,0.1)">
                <h3 style="color:#576574;margin:0;">Meditation Minutes</h3>
                <p style="color:#2e86de;font-size:32px;font-weight:bold;margin:0;">{meditation_stats.get('total_minutes', 0)}</p>
            </div>
        """, unsafe_allow_html=True)

def show_recent_activity():
    """Display recent activity section"""
    st.subheader("Recent Activity")
    
    # Placeholder for recent activity - would be populated from database in real implementation
    activities = [
        {"type": "journal", "time": "2 hours ago", "preview": "Today was a productive day..."},
        {"type": "meditation", "time": "Yesterday", "preview": "Completed 10 minute breathing exercise"},
        {"type": "journal", "time": "2 days ago", "preview": "Feeling a bit anxious about..."}
    ]
    
    for activity in activities:
        icon = "📔" if activity["type"] == "journal" else "🧘"
        st.markdown(f"""
            <div style="background-color:#ffffff;padding:15px;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);margin-bottom:10px">
                <div style="display:flex;align-items:center">
                    <span style="font-size:24px;margin-right:15px">{icon}</span>
                    <div>
                        <p style="color:#576574;margin:0;font-weight:bold">{activity["type"].title()} • {activity["time"]}</p>
                        <p style="color:#8395a7;margin:0">{activity["preview"]}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

def show_daily_prompt():
    """Display daily mental wellness prompt"""
    prompts = [
        "Take 5 deep breaths and notice how you feel",
        "Write down three things you're grateful for today",
        "Notice any tension in your body and gently release it",
        "Reflect on a recent challenge and what you learned",
        "Practice mindful eating during your next meal"
    ]
    
    today_prompt = prompts[datetime.now().day % len(prompts)]
    
    st.markdown(f"""
        <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;margin-top:20px">
            <h3 style="color:#2e86de;margin-top:0;">Today's Wellness Prompt</h3>
            <p style="color:#576574;font-size:18px;">{today_prompt}</p>
            <button style="background-color:#2e86de;color:white;border:none;padding:8px 16px;border-radius:5px;cursor:pointer;">
                I did this
            </button>
        </div>
    """, unsafe_allow_html=True)

def show_home():
    """Main home page function"""
    try:
        show_welcome_banner()
        show_quick_stats()
        
        st.markdown("---")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            display_visualizations()
        
        with col2:
            show_recent_activity()
            show_daily_prompt()
            
    except Exception as e:
        logger.error(f"Error displaying home page: {str(e)}")
        st.error("An error occurred while loading the dashboard")
