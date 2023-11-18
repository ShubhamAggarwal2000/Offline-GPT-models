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


function displayMessage(message, sender) {
    var chatBox = document.getElementById('chat-box');
    var messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.className = sender === 'user' ? 'user-message' : 'bot-message';
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}



// This function sends a POST request to your Flask backend(/chat route) with the user's message.
// When it receives a response, it displays the message returned by the backend.

function sendMessageToBackend(message) {
    fetch('http://localhost:5000/chat', {  // Make sure to use your Flask server's URL
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
