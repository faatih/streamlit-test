def load_model(model_path):
    import joblib
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")


def preprocess_input(user_input):
    # Basic preprocessing: lowercasing and stripping whitespace
    if not isinstance(user_input, str):
        return ""
    return user_input.lower().strip()


def format_response(response):
    # Format the response for display
    if not isinstance(response, str):
        return "Invalid response."
    response = response.strip()
    if not response:
        return "No response."
    return response[0].upper() + response[1:] + ("." if not response.endswith(".") else "")