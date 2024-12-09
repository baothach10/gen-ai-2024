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

    const response = {
        citation: [
            "https://www.example.com/citation1",
            "https://www.example.com/citation2",
            "https://www.example.com/citation3"
        ],
        imageUrl: "https://via.placeholder.com/600x300?text=Image+Placeholder",
        keywords: ["intel"],
        meme: "https://via.placeholder.com/300x200?text=Meme+Placeholder",
        query: "Tell me about latest intel",
        summary: "Placeholder summary text.",
        videoUrl: "https://www.w3schools.com/html/mov_bbb.mp4"
    };

    const summaryBlock = document.createElement('div');
    summaryBlock.classList.add('response-block');
    summaryBlock.innerHTML = `
        <h2>Summary:</h2>
        <p>${response.summary}</p>
    `;
    responseSection.appendChild(summaryBlock);

    const responseGrid = document.createElement('div');
    responseGrid.classList.add('response-grid');

    const imageBlock = document.createElement('div');
    imageBlock.classList.add('response-block');
    imageBlock.innerHTML = `
        <h2>Image:</h2>
        <img src="${response.imageUrl}" alt="Image Placeholder" />
    `;
    responseGrid.appendChild(imageBlock);

    const memeBlock = document.createElement('div');
    memeBlock.classList.add('response-block');
    memeBlock.innerHTML = `
        <h2>Meme:</h2>
        <img src="${response.meme}" alt="Meme Placeholder" />
    `;
    responseGrid.appendChild(memeBlock);

    // Video placeholder 
    const videoBlock = document.createElement('div');
    videoBlock.classList.add('response-block');
    videoBlock.innerHTML = `
        <h2>Video:</h2>
        <video controls>
            <source src="${response.videoUrl}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    `;
    responseGrid.appendChild(videoBlock);

    const citationBlock = document.createElement('div');
    citationBlock.classList.add('response-block');
    citationBlock.innerHTML = `
        <h2>Citations:</h2>
        <ul>
            ${response.citation.map(citation => `<li><a href="${citation}" target="_blank">${citation}</a></li>`).join('')}
        </ul>
    `;
    responseGrid.appendChild(citationBlock);
    responseSection.appendChild(responseGrid);
}
