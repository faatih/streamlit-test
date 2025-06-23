import streamlit as st
from chatbot import Chatbot

def main():
    st.title("Chatbot Application")
    st.write("Welcome to the chatbot! Type your message below:")

    chatbot = Chatbot()

    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        if user_input:
            response = chatbot.get_response(user_input)
            st.text_area("Chatbot:", response, height=200)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()