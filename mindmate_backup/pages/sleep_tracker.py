import streamlit as st
from datetime import datetime, time
import pandas as pd
import plotly.express as px
from utils.database import get_db_connection

def show_sleep_tracker_page():
    st.title("😴 Sleep Tracker")
    st.markdown("Monitor your sleep patterns and improve your sleep quality")
    
    with st.expander("Log Sleep Data"):
        col1, col2 = st.columns(2)
        with col1:
            sleep_time = st.time_input("When did you go to bed?", value=time(23, 0))
        with col2:
            wake_time = st.time_input("When did you wake up?", value=time(7, 0))
        
        sleep_quality = st.slider("Sleep Quality (1-10)", 1, 10, 7)
        notes = st.text_area("Notes about your sleep")
        submitted = st.button("Save Sleep Data")
        
        if submitted:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO sleep_data 
                (date, sleep_time, wake_time, duration, quality, notes) 
                VALUES (?, ?, ?, ?, ?, ?)""",
                (datetime.now().date(), 
                 str(sleep_time), 
                 str(wake_time),
                 (datetime.combine(datetime.today(), wake_time) - 
                  datetime.combine(datetime.today(), sleep_time)).seconds/3600,
                 sleep_quality,
                 notes)
            )
            conn.commit()
            st.success("Sleep data saved successfully!")
    
    # Sleep history visualization
    st.header("Your Sleep Patterns")
    conn = get_db_connection()
    sleep_data = pd.read_sql("SELECT * FROM sleep_data ORDER BY date DESC", conn)
    
    if not sleep_data.empty:
        # Convert to datetime for plotting
        sleep_data['date'] = pd.to_datetime(sleep_data['date'])
        sleep_data['sleep_time'] = pd.to_datetime(sleep_data['sleep_time']).dt.time
        sleep_data['wake_time'] = pd.to_datetime(sleep_data['wake_time']).dt.time
        
        # Duration vs Quality scatter plot
        fig1 = px.scatter(
            sleep_data,
            x='duration',
            y='quality',
            color='quality',
            title='Sleep Duration vs Quality',
            labels={'duration': 'Hours Slept', 'quality': 'Sleep Quality'},
            height=400
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # Sleep time distribution
        fig2 = px.histogram(
            sleep_data,
            x='sleep_time',
            title='Bedtime Distribution',
            labels={'sleep_time': 'Time Went to Bed'},
            height=400
        )
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No sleep data recorded yet. Log your first sleep above!")

if __name__ == "__main__":
    show_sleep_tracker_page()
