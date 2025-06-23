import streamlit as st
import logging
from utils.visualization import display_visualizations

logger = logging.getLogger(__name__)

def show_analytics_page():
    """Main analytics page function"""
    try:
        st.title("Your Mental Wellness Analytics")
        display_visualizations()
        
    except Exception as e:
        logger.error(f"Error displaying analytics page: {str(e)}")
        st.error("An error occurred while loading analytics")
