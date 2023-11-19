import { BASE_URL } from './config.js';

document.getElementById('send-btn').addEventListener('click', function () {
    var userInput = document.getElementById('user-input');
    var message = userInput.value.trim();

    if (message) {
        // Display user's message
        displayMessage(message, 'user');

        // Send the message to Flask API and get the response
        sendMessageToBackend(message);

        // Clear input field
        userInput.value = '';
    }
});

document.getElementById('upload-btn').addEventListener('click', function () {
    var files = document.getElementById('file-input').files;
    var formData = new FormData();
    for (var i = 0; i < files.length; i++) {
        formData.append('files[]', files[i]);
    }

    fetch(`${BASE_URL}/upload`, {  // Updated to use BASE_URL
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
});

function displayMessage(message, sender) {
    var chatBox = document.getElementById('chat-box');
    var messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.className = sender === 'user' ? 'user-message' : 'bot-message';
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}

function sendMessageToBackend(message) {
    fetch(`${BASE_URL}/chat`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
        .then(response => response.json())
        .then(data => {
            displayMessage(data.response, 'bot');
        })
        .catch((error) => {
            console.error('Error:', error);
            displayMessage('Error: Could not connect to the server', 'bot');
        });
}
