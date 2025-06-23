import streamlit as st
from chatbot import Chatbot
from datetime import datetime

def main():
    st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")
    st.title("💬 Chatbot Application")
    st.markdown(
        "<div style='color:gray; margin-bottom:16px;'>Welcome! Type your message below and chat with the bot.</div>",
        unsafe_allow_html=True
    )

    # Initialize chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Secure input for OpenAI API key in the sidebar
    with st.sidebar:
        st.markdown("---")
        api_key = st.text_input(
            label="🔑 Enter your OpenAI API Key",
            value=st.session_state.get("openai_api_key", ""),
            type="password",
            help="Your API key is only stored in your session and never sent anywhere else.",
            key="openai_api_key_input"
        )
        if api_key:
            st.session_state.openai_api_key = api_key
            st.success("API key set for this session.")
        elif "openai_api_key" in st.session_state:
            api_key = st.session_state.openai_api_key

    # Pass the API key to the chatbot if available
    chatbot = Chatbot(api_key=api_key) if api_key else Chatbot()

    # Add custom CSS for better chat bubbles and scrollbar
    st.markdown(
        """
        <style>
        .chat-bubble-user {
            background: #DCF8C6;
            padding: 10px 16px;
            border-radius: 16px 16px 4px 16px;
            margin-bottom: 4px;
            max-width: 75%;
            margin-left: auto;
            text-align: right;
            font-size: 1.05em;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }
        .chat-bubble-bot {
            background: #F1F0F0;
            padding: 10px 16px;
            border-radius: 16px 16px 16px 4px;
            margin-bottom: 12px;
            max-width: 75%;
            text-align: left;
            font-size: 1.05em;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }
        .chat-container {
            max-height: 60vh;
            overflow-y: auto;
            padding-right: 8px;
        }
        .stTextInput>div>div>input {
            font-size: 1.1em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add timestamps to chat history

    # Chat history display (chat bubbles) - show only the last 10 messages for recent chat
    chat_placeholder = st.container()
    with chat_placeholder:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for entry in st.session_state.chat_history[-10:]:
            timestamp = entry.get('timestamp', '')
            st.markdown(
                f"<div class='chat-bubble-user'><b>You:</b> {entry['user']}<br><span style='font-size:0.8em;color:#888;'>{timestamp}</span></div>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<div class='chat-bubble-bot'><b>Chatbot:</b> {entry['bot']}<br><span style='font-size:0.8em;color:#888;'>{timestamp}</span></div>",
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

    # Input area
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input("Type your message", value=st.session_state.get("input", ""), key="input", label_visibility="collapsed")
    with col2:
        send_clicked = st.button("Send", use_container_width=True)

    # Handle sending
    if send_clicked:
        if user_input.strip():
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            response = chatbot.get_response(user_input)
            st.session_state.chat_history.append({"user": user_input, "bot": response, "timestamp": now})
            st.session_state.input = ""  # Clear input
            st.experimental_rerun()
        else:
            st.warning("Please enter a message.")

    # Optional: Clear chat button
    with st.sidebar:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.session_state.input = ""
            st.experimental_rerun()
        if st.session_state.chat_history:
            if st.download_button(
                label="⬇️ Download Chat History",
                data="\n".join([
                    f"[{entry['timestamp']}] You: {entry['user']}\n[{entry['timestamp']}] Chatbot: {entry['bot']}" for entry in st.session_state.chat_history
                ]),
                file_name="chat_history.txt",
                mime="text/plain"
            ):
                st.success("Chat history downloaded!")

if __name__ == "__main__":
    main()