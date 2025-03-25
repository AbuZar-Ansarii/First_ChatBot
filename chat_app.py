import tensorflow
from tensorflow.keras.models import load_model
import streamlit as st
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from typing import List, Tuple

# Load model and tokenizer
try:
    model = load_model("seq2seq_chatbot.h5")
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    max_len = 19
except FileNotFoundError as e:
    st.error(f"Error loading model or tokenizer: {e}. Please ensure the files are in the correct location.")
    st.stop()  # Stop execution if model or tokenizer is not found

def generate_response(user_input):
    input_seq = tokenizer.texts_to_sequences([user_input])
    input_seq = pad_sequences(input_seq, maxlen=max_len, padding="post")

    predicted_seq = model.predict([input_seq, input_seq])
    predicted_words = [tokenizer.index_word.get(np.argmax(word), "") for word in predicted_seq[0]]

    return " ".join(predicted_words)

def main():
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