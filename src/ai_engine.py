import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)
if not api_key:
    return "❌ API key not found"
def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "⚠️ AI error. Check API key or try again."
