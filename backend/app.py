# Import Flask class and other dependencies like request and jsonify
from flask import Flask, request, jsonify

# Create an instance of the Flask app
# __name__ allows Flask to locate resources like templates relative to the app
app = Flask(__name__)

# Application configuration settings
# Set debug mode to True for auto-reload when code changes
app.config['DEBUG'] = True

# Disable sorting JSON keys alphabetically and use dict insert order instead
# This allows control over the response structure
app.config['JSON_SORT_KEYS'] = False

# Add other config values as needed

# Route handler for /chat endpoint
# POST method allows sending data in request body


@app.route("/chat", methods=["POST"])
def chat():
    """
    Chatbot query-response route

    This route handles queries sent to the chatbot
    and returns the bot's response
    """
    return {"response": "Hello!"}  # Logic to be added later


# Route handler for /train endpoint
# POST method allows sending training data
@app.route("/train", methods=["POST"])
def train():
    """
    Retrain chatbot route

    This route allows retraining the chatbot 
    model on new data
    """
    return {"status": "success"}   # Logic to be added later


# Standard boilerplate
# Runs the Flask app when executed directly
if __name__ == "__main__":
    app.run()
