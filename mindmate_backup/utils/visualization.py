import logging
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List, Optional
from datetime import datetime
from utils.mood_analysis import get_mood_trends, get_mood_distribution, get_keyword_frequency

logger = logging.getLogger(__name__)

def plot_mood_trend(mood_data: Dict) -> Optional[go.Figure]:
    """Create a line chart showing mood trends over time"""
    try:
        if not mood_data.get("mood_trends"):
            return None

        df = pd.DataFrame(mood_data["mood_trends"])
        df['date'] = pd.to_datetime(df['date'])
        
        # Create figure
        fig = px.line(
            df,
            x='date',
            y='mood',
            title='Mood Trend Over Time',
            labels={'mood': 'Mood Score', 'date': 'Date'},
            markers=True
        )
        
        # Customize layout
        fig.update_layout(
            xaxis_title='Date',
            yaxis_title='Mood Score',
            yaxis_range=[-1, 1],
            hovermode='x unified',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        # Add reference lines for mood ranges
        fig.add_hline(y=0.2, line_dash="dot", line_color="green", 
                     annotation_text="Positive Threshold", annotation_position="bottom right")
        fig.add_hline(y=-0.2, line_dash="dot", line_color="red", 
                     annotation_text="Negative Threshold", annotation_position="bottom right")
        
        return fig
        
    except Exception as e:
        logger.error(f"Failed to create mood trend chart: {str(e)}")
        return None

def plot_mood_distribution(mood_dist: Dict) -> Optional[go.Figure]:
    """Create a pie chart showing mood distribution"""
    try:
        if not mood_dist:
            return None

        labels = ['Positive', 'Neutral', 'Negative']
        values = [mood_dist['positive'], mood_dist['neutral'], mood_dist['negative']]
        colors = ['#2ecc71', '#f39c12', '#e74c3c']
        
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            marker_colors=colors,
            hole=0.3,
            textinfo='percent+label'
        )])
        
        fig.update_layout(
            title='Mood Distribution',
            showlegend=False,
            margin=dict(t=50, b=0, l=0, r=0)
        )
        
        return fig
        
    except Exception as e:
        logger.error(f"Failed to create mood distribution chart: {str(e)}")
        return None

def plot_keyword_frequency(keywords: List[Dict]) -> Optional[go.Figure]:
    """Create a bar chart showing most frequent mood keywords"""
    try:
        if not keywords:
            return None

        df = pd.DataFrame(keywords)
        
        fig = px.bar(
            df,
            x='keyword',
            y='count',
            title='Most Frequent Mood Keywords',
            labels={'keyword': 'Keyword', 'count': 'Frequency'},
            color='count',
            color_continuous_scale='Blues'
        )
        
        fig.update_layout(
            xaxis_title='Keyword',
            yaxis_title='Frequency',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            coloraxis_showscale=False
        )
        
        return fig
        
    except Exception as e:
        logger.error(f"Failed to create keyword frequency chart: {str(e)}")
        return None

def plot_meditation_progress(sessions_data: List[Dict]) -> Optional[go.Figure]:
    """Create a bar chart showing meditation minutes over time"""
    try:
        if not sessions_data:
            return None

        df = pd.DataFrame(sessions_data)
        df['date'] = pd.to_datetime(df['date'])
        
        fig = px.bar(
            df,
            x='date',
            y='minutes',
            title='Meditation Minutes Over Time',
            labels={'date': 'Date', 'minutes': 'Minutes'},
            color='minutes',
            color_continuous_scale='Greens'
        )
        
        fig.update_layout(
            xaxis_title='Date',
            yaxis_title='Minutes',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            coloraxis_showscale=False
        )
        
        return fig
        
    except Exception as e:
        logger.error(f"Failed to create meditation progress chart: {str(e)}")
        return None

def display_visualizations(user_id: str = "default_user") -> None:
    """Display all visualizations in Streamlit"""
    try:
        st.header("Your Mental Wellness Insights")
        
        # Mood trends section
        st.subheader("Mood Trends")
        mood_trends = get_mood_trends(user_id)
        trend_fig = plot_mood_trend(mood_trends)
        if trend_fig:
            st.plotly_chart(trend_fig, use_container_width=True)
        else:
            st.info("No mood data available yet. Start journaling to see your trends!")
        
        # Mood distribution section
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Mood Distribution")
            mood_dist = get_mood_distribution(user_id)
            dist_fig = plot_mood_distribution(mood_dist)
            if dist_fig:
                st.plotly_chart(dist_fig, use_container_width=True)
            else:
                st.info("No mood distribution data available")
        
        # Keyword frequency section
        with col2:
            st.subheader("Common Mood Keywords")
            keywords = get_keyword_frequency(user_id)
            keyword_fig = plot_keyword_frequency(keywords)
            if keyword_fig:
                st.plotly_chart(keyword_fig, use_container_width=True)
            else:
                st.info("No keyword data available yet")
        
        # Add spacing
        st.markdown("---")
        
    except Exception as e:
        logger.error(f"Failed to display visualizations: {str(e)}")
        st.error("An error occurred while generating visualizations")
