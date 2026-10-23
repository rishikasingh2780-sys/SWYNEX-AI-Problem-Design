import os
import streamlit as st
from google import genai

st.set_page_config(page_title="AI Text Analyzer", page_icon="🤖")

st.title("🤖 AI Text Analyzer")
st.write("Analyze text sentiment using Google Gemini AI.")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API key is missing. Please configure GEMINI_API_KEY.")
    st.stop()

client = genai.Client(api_key=api_key)

text = st.text_area("Enter your text below:")

if st.button("Analyze Text"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        try:
            with st.spinner("Analyzing text..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=(
                        "Classify the sentiment of the following text as "
                        "Positive, Negative, or Neutral. "
                        "Give a short explanation.\n\n"
                        f"Text: {text}"
                    )
                )

            if response.text:
                st.subheader("Analysis Result")
                st.write(response.text)
            else:
                st.warning("The AI returned an empty response.")

        except Exception as e:
            st.error("Analysis failed. Please try again.")
            st.caption(f"Error details: {e}")

st.divider()
st.subheader("Evaluation Examples")

examples = [
    {
        "text": "I love this product. It is amazing!",
        "expected": "Positive"
    },
    {
        "text": "This is terrible. I am very disappointed.",
        "expected": "Negative"
    },
    {
        "text": "The package arrived today.",
        "expected": "Neutral"
    }
]

for example in examples:
    st.write(f"**Test text:** {example['text']}")
    st.write(f"**Expected sentiment:** {example['expected']}")
    st.divider()
