function submitPrompt() {
    const promptInput = document.getElementById('promptInput');
    const userMessage = promptInput.value.trim();
    const responseSection = document.getElementById('responseSection');
    
    if (userMessage === '') return;

    responseSection.innerHTML = '';

    const promptBlock = document.createElement('div');
    promptBlock.classList.add('query-block');
    promptBlock.innerHTML = `<h2>Your Query:</h2><p>${userMessage}</p>`;
    responseSection.appendChild(promptBlock);

    promptInput.value = '';

    // Placeholder, mấy ông tạo 1 cái endpoint cho cái này
    const responses = [
        { type: 'text', content: 'AI something something.' },
        { type: 'image', content: 'https://via.placeholder.com/600x300', description: 'Something AI' },
        { type: 'meme', content: 'https://via.placeholder.com/300/FF0000/FFFFFF?text=RMIT+Bruh+Bruh+Lmao', description: 'Meme' },
        { type: 'video', content: 'https://www.w3schools.com/html/mov_bbb.mp4', description: 'Deepface video' },
    ];

    const responseGrid = document.createElement('div');
    responseGrid.classList.add('response-grid');

    responses.forEach(response => {
        const responseBlock = document.createElement('div');
        responseBlock.classList.add('response-block');

        if (response.type === 'text') {
            responseBlock.innerHTML = `<h2>Text Response:</h2><p>${response.content}</p>`;
        } else if (response.type === 'image' || response.type === 'meme') {
            responseBlock.innerHTML = `<h2>${response.type === 'meme' ? 'Meme Image' : 'Image'}</h2><img src="${response.content}" alt="${response.description}"><p>${response.description}</p>`;
        } else if (response.type === 'video') {
            responseBlock.innerHTML = `<h2>Video:</h2><video controls><source src="${response.content}" type="video/mp4"></video><p>${response.description}</p>`;
        }

        responseGrid.appendChild(responseBlock);
    });

    responseSection.appendChild(responseGrid);
}
