Project Name: Offline GPT Model POC
Description
This project is a proof of concept for an offline chat system utilizing open-source Large Language Models (LLM), specifically GPT-Neo. It's designed to facilitate chat-like interactions in an offline environment, with a focus on modularity, scalability, and ease of integration with different LLMs.

Features
Offline Chat Capability: Leverages GPT-Neo for generating conversational responses without needing an internet connection.
Scalable Architecture: Designed with scalability in mind, allowing for easy upgrades and integration with different or more advanced models.
User-Friendly Interface: Includes a simple and intuitive frontend for user interactions.
RESTful API Backend: A Flask backend that handles chat requests and model interactions.


Installation & Setup

Prerequisites
Before you start, ensure you have the following prerequisites installed on your system:

      Python 3.6 or higher (Python 3.8 recommended)
      pip (Python package installer)
      git (for cloning the repository)


Setting up the Environment

Clone the GPT-Neo Model Repository:
The GPT-Neo model can be cloned from its repository. Open a terminal and run:

            git clone https://github.com/EleutherAI/gpt-neo-125m.git
            
Specify the Model Path:

After cloning, note the path where the GPT-Neo model is stored.
This path needs to be specified in your backend application where the model is loaded.

Clone the Repository:

    git clone https://github.com/ShubhamAggarwal2000/Offline-GPT-models.git
    cd Offline-GPT-models


Create a Virtual Environment:

  For Windows:
  
        python -m venv env
        env\Scripts\activate
        
  For macOS/Linux:

        python3 -m venv env
        source env/bin/activate


Install Dependencies:
Inside the activated virtual environment, install the required Python packages:        

      pip install -r backend/requirements.txt


Running the Application

  Start the Flask Server:
  Navigate to the backend directory:
          
      cd backend
  Run the Flask application:

      python app.py

  The server will start on http://127.0.0.1:5000 by default.

Frontend

Accessing the Frontend Interface:
Open the index.html file located in the frontend folder with a web browser.
Ensure the Flask server is running in the background as the frontend interacts with the backend.

Testing the Application
Once the Flask server is running and the frontend is opened in a browser, you can test the chat functionality by typing messages and checking the responses from the GPT-Neo model.

Acknowledgements
Credits to any third-party assets, libraries, or code used in the project.
