import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Gemini LLM Applications",
    page_icon="🤖",
)

# Main Page Title
st.title("Gemini LLM Applications")

# Sidebar
st.sidebar.success("Select an application to get started.")

# Gemini Pro LLM
with st.container():
    st.header("**Gemini Pro LLM**", anchor=None)  # Optional anchor for sidebar navigation
    st.markdown("""
        This is Google Gemini Pro LLM model for text generation. It excels at:
        * Answering questions
        * Generating text
        
        Trained on a vast corpus of text from the internet.
    """)

# Gemini Pro Vision
with st.container():
    st.header("**Gemini Pro Vision LLM**", anchor=None)
    st.markdown("""
        Google Gemini Pro Vision LLM specializes in text with image generation. It's adept at:
        * Answering questions related to images
        * Describing images
        * Generating text about images
        
        This multimodal model bridges the gap between visual and textual understanding.
    """)

