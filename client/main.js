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
        var ul = document.createElement('ul');
        data.path.forEach(function(page) {
            var li = document.createElement("li");
            var a = document.createElement("a");
            a.href = page;
            a.textContent = decodeURIComponent(page);
            li.appendChild(a);
            ul.appendChild(li);
        });
        pathElement.appendChild(ul);
    });
});
