import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analyzer import analyze_code
from src.reviewer import review_code
from src.optimizer import improve_code
from src.ai_engine import generate_response
st.title("💻 AI Code Reviewer")

code = st.text_area("Paste your code here", height=200)

if st.button("Analyze Code"):
    if code:

        st.subheader("📖 Code Explanation")
        explanation_prompt = f"Explain this code in simple terms:\n{code}"
        st.write(generate_response(explanation_prompt))

        st.subheader("⚠️ Issues Detected")
        issue_prompt = f"Find issues or bad practices in this code:\n{code}"
        st.write(generate_response(issue_prompt))

        st.subheader("🚀 Improvements")
        improve_prompt = f"Suggest improvements for this code:\n{code}"
        st.write(generate_response(improve_prompt))
