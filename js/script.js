document.getElementById('queryForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const query = document.getElementById('userQuery').value;
    
    fetch('http://localhost:5000/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseContainer').innerText = data.response;
    })
    .catch(error => console.error('Error:', error));
});
