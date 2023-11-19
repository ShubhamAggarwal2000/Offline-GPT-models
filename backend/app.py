# Import Flask class and other dependencies like request and jsonify
from flask import Flask, request, jsonify
from models.model_loader import load_model
from flask_cors import CORS
import os
import torch
import io
from werkzeug.utils import secure_filename
import logging

logging.basicConfig(level=logging.DEBUG) 
logger = logging.getLogger('applogger')
logger.setLevel(logging.DEBUG)


# Create an instance of the Flask app
app = Flask(__name__)
CORS(app)


# Load the model
model_path = "C:\\Users\\shubh\\OneDrive\\Desktop\\Hyperboost\\gpt-neo-125m"
model, tokenizer = load_model(model_path)

# Define a directory to save uploaded files
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', "docx"])  # Add or remove file types as needed


# Application configuration settings
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Helper function to generate response
def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    # Create an attention mask
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    max_length = len(input_text.split()) + 50  # Adjust as necessary
    output_ids = model.generate(input_ids, attention_mask=attention_mask,
                                pad_token_id=tokenizer.eos_token_id, max_length=max_length)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Route handler for /chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    """
    Chatbot query-response route
    """
    user_input = request.json['message']
    response = generate_response(user_input)
    return {"response": response}


# Route handler for /upload endpoint
@app.route('/upload', methods=['POST'])
def upload_files():
    logger.debug("Received upload request")
    if 'files[]' not in request.files:
        return jsonify({'status': 'No file part'})
    
    files = request.files.getlist('files[]')
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return jsonify({'status': 'success'})

# Route handler for /train endpoint


@app.route("/train", methods=["POST"])
def train():
    """
    Retrain chatbot route
    """
    return {"status": "success"}


# Standard boilerplate
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT not set
    app.run(port=port)