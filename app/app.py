import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analyzer import analyze_code
from src.reviewer import review_code
from src.optimizer import improve_code

st.title("💻 AI Code Reviewer")

code = st.text_area("Paste your code here", height=200)

if st.button("Analyze Code"):
    if code:
        analysis = analyze_code(code)
        issues = review_code(code)
        suggestions = improve_code(code)

        st.subheader("📊 Code Analysis")
        st.write(analysis)

        st.subheader("⚠️ Issues Detected")
        for issue in issues:
            st.write(f"- {issue}")

        st.subheader("🚀 Improvements")
        for s in suggestions:
            st.write(f"- {s}")
