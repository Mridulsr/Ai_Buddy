import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")
st.title("📚 AI Study Buddy (Free via Gemini)")

# Sidebar for Gemini Key
with st.sidebar:
    api_key = st.text_input("Enter Google Gemini API Key:", type="password")
    st.info("Get a free key at: aistudio.google.com")

if not api_key:
    st.warning("Please enter your Gemini API Key in the sidebar.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    user_input = st.text_area("Paste notes here:", height=200)
    
    if st.button("Generate Study Guide"):
        if user_input:
            with st.spinner("Gemini is thinking..."):
                prompt = f"Summarize this for a student with an analogy, 3 bullet points, and a 3-question quiz: {user_input}"
                response = model.generate_content(prompt)
                st.markdown("---")
                st.write(response.text)
