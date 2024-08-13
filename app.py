import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# Configure the API key

genai.configure(api_key=GOOGLE_API_KEY)
# Streamlit UI
st.title("Generative AI: Text Generator")

# Input box for the user to enter the text prompt
text_prompt = st.text_input("Enter your text prompt")

# Button to trigger content generation
if st.button("Generate Content"):
    # Generate the text content using the model
    text_model = genai.GenerativeModel('gemini-pro')
    text_response = text_model.generate_content(text_prompt)
    
    # Display the generated text
    st.subheader("Generated text")
    st.write(text_response.text)