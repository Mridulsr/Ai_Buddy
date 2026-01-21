import streamlit as st
from openai import OpenAI
import os

# Page Config
st.set_page_config(page_title="AI Study Buddy", page_icon="📚")

st.title("📚 AI Study Buddy")
st.markdown("Convert complex lecture notes into simple explanations and instant quizzes.")

# Initialize client using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Input Area
user_input = st.text_area(
    "Paste your study material or lecture notes here:",
    height=250,
    placeholder="e.g., The mitochondria is the powerhouse of the cell..."
)

col1, col2 = st.columns(2)

with col1:
    if st.button("✨ Simplify & Summarize"):
        if user_input:
            with st.spinner("Breaking it down..."):
                prompt = (
                    f"Simplify the following text for a student. "
                    f"Use a relatable analogy and then provide 3 key bullet points:\n\n{user_input}"
                )
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful tutor."},
                        {"role": "user", "content": prompt}
                    ]
                )
                st.subheader("Simplified Explanation")
                st.write(response.choices[0].message["content"])
        else:
            st.error("Please paste text first.")

with col2:
    if st.button("📝 Generate Quiz"):
        if user_input:
            with st.spinner("Creating questions..."):
                prompt = (
                    f"Based on this text, create 3 Multiple Choice Questions "
                    f"with answers at the bottom:\n\n{user_input}"
                )
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a quiz generator."},
                        {"role": "user", "content": prompt}
                    ]
                )
                st.subheader("Quick Quiz")
                st.write(response.choices[0].message["content"])
        else:
            st.error("Please paste text first.")
