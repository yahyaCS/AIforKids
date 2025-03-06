import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="API_KEY")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get kid-friendly answers
def ask_kid_friendly_ai(question):
    prompt = f"""
    Answer the following question in a way that a 5 to 10-year-old child can easily understand.
    Use simple words, short sentences, and relatable examples.

    Question: {question}
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="AI for Kids", page_icon="🧒", layout="centered")

st.title("🤖 AI FOR KIDS")
st.write("Ask me anything 😊")

user_input = st.text_input("Enter your question:", "")

if st.button("Get Answer"):
    if user_input.strip():
        answer = ask_kid_friendly_ai(user_input)
        st.write("👦 **Answer:**")
        st.info(answer)
    else:
        st.warning("Please enter a question!")

