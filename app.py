import os
import streamlit as st
from google import genai

st.set_page_config(page_title="AI Text Analyzer", page_icon="🤖")

st.title("🤖 AI Text Analyzer")
st.write("Analyze your text using Google Gemini AI.")

text = st.text_area("Enter your text below:")

if st.button("Analyze Text"):
    if not text.strip():
        st.warning("Please enter some text first.")
    elif not os.getenv("GEMINI_API_KEY"):
        st.error("API key is not configured.")
    else:
        try:
            client = genai.Client(
                api_key=os.getenv("GEMINI_API_KEY")
            )

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=(
                    "Analyze the following text. Identify its sentiment, "
                    "main topic, and a brief summary:\n\n" + text
                )
            )

            st.subheader("Analysis Result")
            st.write(response.text)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
