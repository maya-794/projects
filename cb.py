import streamlit as st
from transformers import pipeline

# Load the model (this may take a few seconds the first time)
@st.cache_resource
def load_chatbot():
    return pipeline("text2text-generation", model="google/flan-t5-base")


chatbot = load_chatbot()

# Streamlit UI
st.title("🧠 Customer Support Chatbot")
st.markdown("Ask me anything about our services!")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if user_input:
    prompt = f"User: {user_input}\nAgent:"
    response = chatbot(prompt, max_new_tokens=50)
    bot_reply = response[0]['generated_text'].replace(prompt, "").strip()

    # Update chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_reply))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
