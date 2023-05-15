from flask import Flask
from flask_cors import CORS
from algorithm import Algorithm

app = Flask(__name__)
CORS(app) # enable CORS for all origins (for now...)

@app.route("/")
def hello():
    print("boo")
    return "Hello, World!"

# function executed when root address receives HTTP request
@app.route("/graph", methods=["GET"]) 
def graph():
    print("loading sample graph data...")
    with open("backend/graphSample.txt", "r") as f:
        # print(f.read())
        # matrix = f.read()

        matrix = []
        for row in f:
            matrix.append([int(x) for x in row.split()])

        print(matrix)

        g = Algorithm(len(matrix))
        g.graph = matrix
        g.dijkstra(0)

        return matrix

# serves project locally without needing to set flask environment variables
if __name__ == "__main__":
    app.run(port=8080)