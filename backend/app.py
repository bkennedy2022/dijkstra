from flask import Flask
from flask_cors import CORS
from algorithm import Graph
from flask_socketio import SocketIO
from flask_socketio import send, emit
from random import random
from threading import Lock
from datetime import datetime

thread = None
thread_lock = Lock()

app = Flask(__name__)
CORS(app) # enable CORS for all origins (for now...)
async_mode = None
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, cors_allowed_origins=['http://127.0.0.1:8080']) # enable CORS for all origins (for now...)
socketio = SocketIO(app, async_mode = async_mode, cors_allowed_origins="*") # enable CORS for all origins (for now...)
app.debug = True

# @socketio.on('message')
# def handle_message(message):
#     send(message)

# """
# Get current date time
# """
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")
# """
# Generate random sequence of dummy sensor values and send it to our clients
# """
def background_thread():
    print("Generating random sensor values")
    while True:
        dummy_sensor_value = round(random() * 100, 3)
        socketio.emit('updateSensorData', {'value': dummy_sensor_value, "date": get_current_datetime()})
        print("emitting data....")
        socketio.sleep(1)

@app.route("/")
def hello():
    print("boo")
    return "Hello, World!"


# """
# Decorator for disconnect
# """
@socketio.on('disconnect')
def disconnect():
    print('Client disconnected',  request.sid)

# if __name__ == '__main__':
#     socketio.run(app)

# function executed when root address receives HTTP request
@app.route("/graph", methods=["GET"]) 
def graph():
    # socketio.on('connection', (socket) => {
    # console.log('a user connected');
    # })
    print("loading sample graph data...")
    socketio.emit('news', {'data':42})
    with open("backend/graphSample4.txt", "r") as f:

        # convert text file to list
        graphList = []
        for row in f:
            graphList.append([int(x) for x in row.split()])

        # run Dijkstra
        # g = Graph(9)
        # print(graphList)
        # g.addEdges(graphList)
        # g.dijkstra(0)
        socketio.emit('updateSensorData', {'value': 30, "date": get_current_datetime()})
        print(
            "done with dijkstra!!!!!!!!"
        )

        return graphList


# """
# Decorator for connect
# """
@socketio.on('connect')
def connect():
    # global thread
    print('Client connected')
    # global thread
    # with thread_lock:
    #     if thread is None:
    #         thread = socketio.start_background_task(background_thread)


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)


# serves project locally without needing to set flask environment variables
if __name__ == "__main__":
    # app.run(port=8080)
    print("serving")
    socketio.run(app,port=5000,host='127.0.0.1',debug=True)