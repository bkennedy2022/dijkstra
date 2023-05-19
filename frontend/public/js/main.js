// import io from 'socket.io-client'
// const { io } = require("socket.io-client");

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

    // $(document).ready(function(){
    //     // sending a connect request to the server.
    //     var socket = io.connect('http://127.0.0.1:5000/graph');
    //     console.log("connected to socket");
    //     socket.on('news'), function(msg) {
    //         console.log('got a message ',msg)
    //     }
    //    });



    $(document).ready(function(){
            // sending a connect request to the server.
            // const socket = io('http://127.0.0.1:5000/graph');
            const socket = io.connect('http://127.0.0.1:5000');
            // const socket = io.connect('http://localhost:5000');
            console.log("connecting to socket");
            console.log(socket)

            socket.on('connect', function() {
                socket.emit('my event', {data: 'I\'m connected!'});
                });


            socket.on('news'), function(msg) {
                console.log('got a message ',msg)
            }

            //receive details from server
            socket.on("updateSensorData", function (msg) {
                console.log("Received sensorData :: " + msg.date + " :: " + msg.value);
            });
           });



    // fetch("http://127.0.0.1:5000/graph", {
    //     method: "GET"
    // })
    // .then(res => res.json())
    // .then(response => {
    //     console.log('Success getting original matrix');

    //     // Set current data text and update date
    //     getDate();
    //     dataDiv = document.getElementById('graph-container');
    //     dataDiv.innerHTML = JSON.stringify(response);
    // })
    // .catch(error => console.error('Error:',error))
}


  