function submitPrompt() {
    const promptInput = document.getElementById('promptInput');
    const chatWindow = document.getElementById('chatWindow');
    const userMessage = promptInput.value.trim();

    if (userMessage === '') return;

    addMessage('user', userMessage);
    promptInput.value = '';

    // Respond placeholder có gì edit cái này, theo JSON nha
    const responses = [
        { type: 'text', content: 'This is the AI text response.' },
        { type: 'image', content: 'https://via.placeholder.com/300', description: 'Sample image' },
        { type: 'meme', content: 'https://via.placeholder.com/300/FF0000/FFFFFF?text=Funny+Meme', description: 'Meme image' },
        { type: 'video', content: 'https://www.w3schools.com/html/mov_bbb.mp4', description: 'Sample video' },
    ];

    let delay = 1000; 

    responses.forEach((response) => {
        setTimeout(() => {
            addMessage('ai', response);
        }, delay);
        delay += 1500; 
    });
}

function addMessage(sender, content) {
    const chatWindow = document.getElementById('chatWindow');
    const message = document.createElement('div');
    message.className = `message ${sender}`;

    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';

    if (typeof content === 'string') {
        messageContent.textContent = content;
    } else {
        
        if (content.type === 'text') {
            messageContent.textContent = content.content;
        } else if (content.type === 'image' || content.type === 'meme') {
            const img = document.createElement('img');
            img.src = content.content;
            img.alt = content.description;
            messageContent.appendChild(img);
        } else if (content.type === 'video') {
            const video = document.createElement('video');
            video.src = content.content;
            video.controls = true;
            messageContent.appendChild(video);
        }
    }

    message.appendChild(messageContent);
    chatWindow.appendChild(message);

    chatWindow.scrollTop = chatWindow.scrollHeight;
}
