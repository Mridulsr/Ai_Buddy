import streamlit as st
from openai import OpenAI

# Page setup
st.set_page_config(page_title="AI Study Buddy", page_icon="📚")

st.title("📚 AI Study Buddy")
st.write("Turn complex notes into simple summaries and quizzes.")

# Sidebar for API Key
with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Enter OpenAI API Key:", type="password")
    st.caption("Get a key at platform.openai.com")

if not api_key:
    st.info("Please enter your OpenAI API Key in the sidebar to continue.")
else:
    client = OpenAI(api_key=api_key)
    
    # User Input
    user_text = st.text_area("Paste your notes here:", height=200)
    
    if st.button("Generate Study Guide"):
        if user_text:
            with st.spinner("Processing..."):
                try:
                    prompt = f"""
                    Summarize this for a student:
                    1. Simple Explanation (with analogy)
                    2. 3 Key Bullet Points
                    3. A 3-question Multiple Choice Quiz
                    
                    Text: {user_text}
                    """
                    
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    
                    st.markdown("---")
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter some text first!")
