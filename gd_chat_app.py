import tensorflow
from tensorflow.keras.models import load_model
import streamlit as st
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import os
import gdown
from typing import List, Tuple

# https://drive.google.com/file/d/1Fgnuq3bx0OkDvZp7h-gjcs3KIEQOcYaK/view?usp=drive_link

# Google Drive File ID for model
MODEL_FILE_ID = "1Fgnuq3bx0OkDvZp7h-gjcs3KIEQOcYaK"  # Replace with your actual file ID
MODEL_PATH = "seq2seq_chatbot.h5"
TOKENIZER_PATH = "tokenizer.pkl"
MAX_LEN = 19  # Maximum sequence length

def download_model():
    """Downloads the model from Google Drive if it does not exist."""
    if not os.path.exists(MODEL_PATH):
        st.warning("Downloading the model... Please wait ⏳")
        url = f"https://drive.google.com/uc?id={MODEL_FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)
        st.success("Model downloaded successfully! ✅")

# Ensure the model is downloaded before loading
download_model()


# Load model and tokenizer
try:
    model = load_model(MODEL_PATH)
    with open(TOKENIZER_PATH, "rb") as f:
        tokenizer = pickle.load(f)
except FileNotFoundError as e:
    st.error(f"Error loading model or tokenizer: {e}. Ensure the files are present.")
    st.stop()  # Stop execution if files are missing

def generate_response(user_input: str) -> str:
    """Generates a chatbot response based on user input."""
    input_seq = tokenizer.texts_to_sequences([user_input])
    input_seq = pad_sequences(input_seq, maxlen=MAX_LEN, padding="post")

    predicted_seq = model.predict([input_seq, input_seq])
    predicted_words = [tokenizer.index_word.get(np.argmax(word), "") for word in predicted_seq[0]]

    return " ".join(predicted_words)

def main():
    """Streamlit UI for chatbot."""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.title("🤖 ChatBot")
    user_input = st.text_input("👦 Enter Your Text...")

    if st.button("Response"):
        response = generate_response(user_input)

        st.text_area("Chatbot:", value=response, height=200)

        # Update chat history
        st.session_state.chat_history.append((user_input, response))

    st.sidebar.title("Chat History")
    display_chat_history(st.session_state.chat_history)

def display_chat_history(chat_history: List[Tuple[str, str]]) -> None:
    """Display the chat history in the sidebar."""
    st.sidebar.subheader("🗂️ Chat History")
    for i, (user_msg, bot_msg) in enumerate(chat_history[-10:]):  # Show last 10 messages
        if user_msg:
            st.sidebar.markdown(f"**👤 You:** {user_msg}")
        if bot_msg:
            st.sidebar.markdown(f"**🤖 Bot:** {bot_msg}")
        if i < len(chat_history[-10:]) - 1:
            st.sidebar.markdown("---")  # Separator for readability

if __name__ == '__main__':
    main()
