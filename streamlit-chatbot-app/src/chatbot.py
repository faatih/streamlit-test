class Chatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I assist you today?",
            "how are you?": "I'm just a program, but thanks for asking!",
            "bye": "Goodbye! Have a great day!",
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        return self.responses.get(user_input, "I'm sorry, I don't understand that.")