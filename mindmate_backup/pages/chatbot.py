import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

# System prompt defining mental health assistant role
SYSTEM_PROMPT = """You are MindMate, an empathetic and supportive mental health companion. Your role is to:
- Provide emotional support and understanding
- Listen actively and respond with empathy
- Offer constructive coping strategies and suggestions
- Encourage professional help when appropriate
- Maintain a safe and non-judgmental space
- Never provide medical diagnosis or replace professional mental health care
- Always respond in a warm, supportive manner

Remember to prioritize user safety and well-being in all interactions."""

# Mental health resources
RESOURCES = [
    {"name": "Crisis Text Line", "url": "https://www.crisistextline.org/"},
    {"name": "National Suicide Prevention Lifeline", "url": "https://988lifeline.org/"},
    {"name": "NAMI Helpline", "url": "https://www.nami.org/help"},
    {"name": "Mental Health America", "url": "https://mhanational.org/"}
]

# Conversation starters
CONVERSATION_STARTERS = [
    "I'm feeling anxious today",
    "How can I improve my sleep?",
    "I'm struggling with motivation",
    "What are some healthy coping mechanisms?",
    "How do I know if I need professional help?"
]

def show_chatbot_page():
    st.title("MindMate Chat")
    
    # Safety disclaimer
    with st.expander("Important Notice"):
        st.warning("""
        MindMate provides supportive conversations but is not a substitute for professional mental health care.
        If you're in crisis, please contact a licensed professional or emergency services immediately.
        """)
    
    # Mood tracker
    st.sidebar.subheader("How are you feeling today?")
    mood = st.sidebar.select_slider(
        "Mood scale",
        options=["😢 Very Low", "😞 Low", "😐 Neutral", "🙂 Good", "😊 Great"],
        value="😐 Neutral"
    )
    
    # Resources section
    with st.sidebar.expander("Mental Health Resources"):
        for resource in RESOURCES:
            st.markdown(f"[{resource['name']}]({resource['url']})")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.session_state.mood = mood

    # Conversation starters
    st.subheader("Need help getting started?")
    cols = st.columns(2)
    for i, starter in enumerate(CONVERSATION_STARTERS):
        if cols[i % 2].button(starter):
            st.session_state.messages.append({"role": "user", "content": starter})
            with st.chat_message("user"):
                st.markdown(starter)

    # Display chat messages (excluding system prompt)
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("How can I help you today?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": f"Mood: {mood}\n{prompt}"})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI response with full conversation history
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=st.session_state.messages,
                temperature=0.7
            )
            ai_response = response.choices[0].message.content
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            with st.chat_message("assistant"):
                st.markdown(ai_response)

        except Exception as e:
            st.error("Sorry, I'm having trouble responding right now. Please try again later.")
            st.error(str(e))
