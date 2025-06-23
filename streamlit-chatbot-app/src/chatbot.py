class Chatbot:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.responses = {
            "hi": "Hello! How can I assist you today?",
            "how are you?": "I'm just a program, but thanks for asking!",
            "bye": "Goodbye! Have a great day!",
        }

    def get_response(self, user_input):
        from utils import preprocess_input, format_response
        user_input = preprocess_input(user_input)
        response = self.responses.get(user_input, "I'm sorry, I don't understand that.")
        return format_response(response)