import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")
st.title("📚 AI Study Buddy")

# Sidebar for Setup
with st.sidebar:
    st.header("Setup")
    # Using .strip() to remove any accidental spaces in the API key
    raw_api_key = st.text_input("Enter Gemini API Key:", type="password")
    api_key = raw_api_key.strip() 
    st.info("Get a free key: [Google AI Studio](https://aistudio.google.com/)")

if not api_key:
    st.warning("Please enter your Gemini API Key to start.")
else:
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_input = st.text_area("Paste your study notes:", height=200)
        
        if st.button("✨ Generate Study Guide"):
            if user_input:
                with st.spinner("Analyzing..."):
                    prompt = f"""
                    You are a helpful student tutor.
                    1. Explain this in simple terms with an analogy.
                    2. Provide 3 key takeaways.
                    3. Create a 3-question quiz.
                    
                    Notes: {user_input}
                    """
                    # Attempt to generate content
                    response = model.generate_content(prompt)
                    
                    # Display the result
                    st.markdown("---")
                    st.markdown(response.text)
            else:
                st.error("Please paste some text first!")
                
    except Exception as e:
        # This will show you the EXACT error (e.g., API_KEY_INVALID)
        st.error(f"Something went wrong: {e}")
