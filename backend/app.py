# Import Flask class and other dependencies like request and jsonify
from flask import Flask, request, jsonify
from models.model_loader import load_model

# Create an instance of the Flask app
app = Flask(__name__)

# Load the model
model_path = "C:\\Users\\shubh\\OneDrive\\Desktop\\Hyperboost\\gpt-neo-125m"
model, tokenizer = load_model(model_path)

# Application configuration settings
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

# Helper function to generate response


def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    max_length = len(input_text.split()) + 50
    output_ids = model.generate(input_ids, max_length=max_length)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Route handler for /chat endpoint


@app.route("/chat", methods=["POST"])
def chat():
    """
    Chatbot query-response route
    """
    user_input = request.json['message']
    response = generate_response(user_input)
    return {"response": response}

# Route handler for /train endpoint


@app.route("/train", methods=["POST"])
def train():
    """
    Retrain chatbot route
    """
    return {"status": "success"}


# Standard boilerplate
if __name__ == "__main__":
    app.run()
