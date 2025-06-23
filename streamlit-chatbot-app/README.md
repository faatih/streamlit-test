# 💬 Streamlit Chatbot Application

A modern, secure, and user-friendly chatbot app built with Streamlit. This app supports OpenAI API integration, chat history, message timestamps, and data export.

## Features
- Beautiful chat UI with chat bubbles and scrollable history
- Secure OpenAI API key input (never stored or logged)
- Chat history with timestamps (last 10 messages shown)
- Download chat history as a text file
- Clear chat with one click
- Responsive and accessible design

## Getting Started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd streamlit-chatbot-app/src
```

### 2. Install dependencies
```bash
pip install -r ../requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

### 4. Open in your browser
Go to the URL shown in the terminal (usually http://localhost:8501).

## Usage
- Enter your OpenAI API key in the sidebar (it is only stored in your session).
- Type your message and click **Send**.
- View the conversation in chat bubbles, with timestamps.
- Use **Clear Chat** to reset the conversation.
- Use **Download Chat History** to export your chat as a text file.

## Security
- The OpenAI API key is never stored on disk or sent anywhere except to the OpenAI API.
- All sensitive data is kept in Streamlit's session state.

## Customization
- You can modify the UI, add avatars, or extend the chatbot logic in `src/app.py` and `src/chatbot.py`.

## Requirements
- Python 3.8+
- Streamlit
- OpenAI (if using OpenAI API)

## File Structure
```
streamlit-chatbot-app/
├── README.md
├── requirements.txt
└── src/
    ├── app.py
    ├── chatbot.py
    └── utils.py
```

## License
MIT