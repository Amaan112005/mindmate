import streamlit as st
from mindmate.utils.animations import render_lottie, COMING_SOON_ANIMATION 

def show(user_id=None):
    st.title("🌟 Community")
    
    st.markdown("""
    <div style='text-align: center; padding: 50px;'>
        <h2>Coming Soon!</h2>
        <p style='color: #666; font-size: 1.2rem;'>We are building a safe and supportive community space for you.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if COMING_SOON_ANIMATION:
        render_lottie(COMING_SOON_ANIMATION, height=300, key="community_coming_soon")
    else:
        st.info("Stay tuned! This feature is actively under development.")
