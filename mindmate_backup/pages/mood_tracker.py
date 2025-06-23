import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
from utils.database import get_db_connection
from utils.mood_analysis import (
    analyze_mood_from_text,
    detect_keywords,
    get_mood_trends,
    get_mood_distribution,
    get_keyword_frequency
)

def show_mood_tracker_page():
    st.title("😊 Mood Tracker")
    st.markdown("Track your emotional patterns and gain insights into your mental wellbeing")
    
    # Mood input section
    with st.expander("Log Your Mood"):
        col1, col2 = st.columns(2)
        with col1:
            mood = st.select_slider(
                "How are you feeling?",
                options=["😢 Terrible", "😞 Sad", "😐 Neutral", "🙂 Good", "😁 Excellent"],
                value="😐 Neutral"
            )
        with col2:
            notes = st.text_area("Optional notes about your mood")
            submitted = st.button("Save Mood Entry")
            
        if submitted:
            # Analyze mood from text notes if provided
            mood_score = 3.0  # Default neutral
            keywords = []
            if notes:
                try:
                    mood_score = analyze_mood_from_text(notes)
                    keywords = detect_keywords(notes)
                except Exception as e:
                    st.error(f"Error analyzing mood: {str(e)}")
                    return
            
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute(
                    """INSERT INTO mood_entries 
                    (timestamp, mood, notes, mood_score, keywords) 
                    VALUES (?, ?, ?, ?, ?)""",
                    (datetime.now(), mood, notes, mood_score, ",".join(keywords))
                )
                conn.commit()
                st.success("Mood entry saved successfully!")
            except Exception as e:
                st.error(f"Failed to save mood entry: {str(e)}")
    
    # Mood history and analysis
    st.header("Your Mood History")
    try:
        conn = get_db_connection()
        mood_data = pd.read_sql("SELECT * FROM mood_entries ORDER BY timestamp DESC", conn)
    
    except Exception as e:
        st.error(f"Error loading mood data: {str(e)}")
        return
        
    if not mood_data.empty:
        # Convert mood to numeric scale for analysis
        mood_scale = {
            "😢 Terrible": 1,
            "😞 Sad": 2,
            "😐 Neutral": 3,
            "🙂 Good": 4,
            "😁 Excellent": 5
        }
        mood_data['mood_value'] = mood_data['mood'].map(mood_scale)
        
        # Show interactive chart
        fig = px.line(
            mood_data,
            x='timestamp',
            y='mood_value',
            title='Your Mood Trend',
            labels={'mood_value': 'Mood Level', 'timestamp': 'Date'},
            height=400,
            template='plotly_white',
            line_shape='spline'
        )
        fig.update_traces(line=dict(width=3))
        fig.update_layout(hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)
        
        # Mood analysis
        st.header("Insights")
        
        # Show mood distribution
        dist_data = get_mood_distribution()
        st.subheader("Mood Distribution")
        dist_df = pd.DataFrame({
            "Mood": ["Positive", "Neutral", "Negative"],
            "Count": [dist_data["positive"], dist_data["neutral"], dist_data["negative"]]
        })
        fig = px.pie(
            dist_df,
            names="Mood",
            values="Count",
            color="Mood",
            color_discrete_map={
                "Positive": "green",
                "Neutral": "blue",
                "Negative": "red"
            }
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Show frequent keywords
        keywords = get_keyword_frequency(limit=10)
        if keywords:
            st.subheader("Frequent Mood Keywords")
            kw_df = pd.DataFrame(keywords)
            fig = px.bar(
                kw_df,
                x="keyword",
                y="count",
                labels={"keyword": "Keyword", "count": "Frequency"}
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No mood entries yet. Log your first mood above!")

if __name__ == "__main__":
    show_mood_tracker_page()
