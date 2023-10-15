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
        var pathElement = document.getElementById('path');
        pathElement.innerHTML = ''; // clear previous path
        data.path.forEach(function(page) {
            var para = document.createElement("p");
            var node = document.createTextNode(page);
            para.appendChild(node);
            pathElement.appendChild(para);
        });
    });
});
