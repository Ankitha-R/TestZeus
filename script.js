document.getElementById('test-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const userInput = document.getElementById('user-input').value;

    try {
        const response = await fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input: userInput }),
        });
        const data = await response.json();
        document.getElementById('response-content').textContent = data.output || data.error;
    } catch (err) {
        document.getElementById('response-content').textContent = 'Error: ' + err.message;
    }
});
