import streamlit as st
import pandas as pd
from utils.database import get_db_connection

def show_professional_help_page():
    st.title("👩‍⚕️ Professional Help")
    st.markdown("Connect with licensed mental health professionals and resources")
    
    # Professional directory section
    st.header("Find a Professional")
    
    # Sample data - in a real app this would come from a database
    professionals = pd.DataFrame([
        {
            "name": "Dr. Sarah Johnson",
            "specialty": "Clinical Psychologist",
            "modality": "Cognitive Behavioral Therapy",
            "contact": "sarah.johnson@therapy.com",
            "availability": "Mon-Fri, 9am-5pm"
        },
        {
            "name": "Dr. Michael Chen",
            "specialty": "Psychiatrist",
            "modality": "Medication Management",
            "contact": "mchen@psychiatry.org",
            "availability": "Tue-Thu, 10am-3pm"
        },
        {
            "name": "Lisa Rodriguez, LCSW",
            "specialty": "Social Worker",
            "modality": "Trauma Therapy",
            "contact": "lrodriguez@counseling.net",
            "availability": "Mon-Wed-Fri, 8am-6pm"
        }
    ])
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        specialty_filter = st.multiselect(
            "Filter by specialty",
            options=professionals['specialty'].unique(),
            default=[]
        )
    with col2:
        modality_filter = st.multiselect(
            "Filter by therapy type",
            options=professionals['modality'].unique(),
            default=[]
        )
    
    # Apply filters
    if specialty_filter:
        professionals = professionals[professionals['specialty'].isin(specialty_filter)]
    if modality_filter:
        professionals = professionals[professionals['modality'].isin(modality_filter)]
    
    # Display professionals
    if not professionals.empty:
        st.dataframe(
            professionals,
            column_config={
                "name": "Name",
                "specialty": "Specialty",
                "modality": "Therapy Type",
                "contact": "Contact",
                "availability": "Availability"
            },
            hide_index=True,
            use_container_width=True
        )
    else:
        st.info("No professionals match your filters")
    
    # Emergency resources section
    st.header("Emergency Resources")
    with st.expander("Crisis Hotlines"):
        st.markdown("""
        - **National Suicide Prevention Lifeline**: 988
        - **Crisis Text Line**: Text HOME to 741741
        - **Veterans Crisis Line**: 988 then press 1
        - **Disaster Distress Helpline**: 1-800-985-5990
        """)
    
    # Appointment booking section
    st.header("Book an Appointment")
    with st.form("appointment_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        preferred_professional = st.selectbox(
            "Preferred Professional",
            ["Any available"] + professionals['name'].tolist()
        )
        appointment_date = st.date_input("Preferred Date")
        appointment_time = st.time_input("Preferred Time")
        concerns = st.text_area("Briefly describe your concerns")
        
        submitted = st.form_submit_button("Request Appointment")
        if submitted:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO professional_requests 
                (name, email, phone, preferred_professional, appointment_date, 
                 appointment_time, concerns, status) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (name, email, phone, preferred_professional, appointment_date,
                 appointment_time, concerns, "Pending")
            )
            conn.commit()
            st.success("Appointment request submitted! A professional will contact you soon.")

if __name__ == "__main__":
    show_professional_help_page()
