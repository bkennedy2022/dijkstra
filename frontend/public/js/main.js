// Sets the date and time displayed
function getDate() {
    date = new Date().toString();
    console.log(date);
    document.getElementById('time-container').textContent
        = date;
}

// Requests data from backend
function getGraph() {
    console.log("Getting graph data...");

    fetch("http://127.0.0.1:8080/graph", {
        method: "GET"
    })
    .then(res => res.json())
    .then(response => {
        console.log('Success getting original matrix');

        // Set current data text and update date
        getDate();
        dataDiv = document.getElementById('graph-container');
        dataDiv.innerHTML = JSON.stringify(response);
    })
    .catch(error => console.error('Error:',error))
}