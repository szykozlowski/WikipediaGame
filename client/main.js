document.getElementById('wiki-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var startPage = document.getElementById('start-page').value;
    var finishPage = document.getElementById('finish-page').value;

    fetch('/find_path', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            start: startPage,
            finish: finishPage
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('path').innerHTML = data.path.join('<br>');
    });
});
