def load_model(model_path):
    import joblib
    model = joblib.load(model_path)
    return model

def preprocess_input(user_input):
    # Basic preprocessing: lowercasing and stripping whitespace
    return user_input.lower().strip()

def format_response(response):
    # Format the response for display
    return response.capitalize() + '.' if not response.endswith('.') else response.capitalize()