document.getElementById('send-btn').addEventListener('click', function() {
    var userInput = document.getElementById('user-input');
    var message = userInput.value.trim();

    if (message) {
        // Display user's message
        displayMessage(message, 'user');
        
        // Here you will later add the code to send the message to your Flask API and get the response

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
