from groq import Groq

def test_key(api_key):
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": "Hello"}],
            model="llama-3.1-8b-instant"  # Current recommended model
        )
        print("Key works! Response:", response.choices[0].message.content)
        return True
    except Exception as e:
        print("Key verification failed:", str(e))
        return False

import os
from dotenv import load_dotenv

load_dotenv()

test_key(os.getenv("GROQ_API_KEY", ""))
