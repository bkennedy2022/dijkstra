console.log("in main.js")

// HTTP request object to update page with incoming data without reloading
var xhr = null;
getXmlHttpRequestObject = function () {
    if (!xhr) {
        xhr = new XMLHttpRequest();
    }
    return xhr;
};

// Updates page when response is received from backend
function dataCallback() {
    // Check response is ready and successful
    if (xhr.readyState == 4 && xhr.status == 200) {
        console.log("Graph data received!");
        getDate();
        dataDiv = document.getElementById('graph-container');
        // Set current data text
        console.log(xhr.responseText);
        dataDiv.innerHTML = xhr.responseText;
    }
}

// Sets the date and time displayed
function getDate() {
    date = new Date().toString();
    console.log(date);
    document.getElementById('time-container').textContent
        = date;
}

// Requests data from backend
function getGraph() {
    console.log("Get graph data...");
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    // xhr.open("GET", "http://localhost:6969/graph", true); // note: can pass variables in this GET request
    xhr.open("GET", "http://127.0.0.1:8080/graph", true);
    // Send the request over the network
    xhr.send();
}