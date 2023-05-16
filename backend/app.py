from flask import Flask
from flask_cors import CORS
from algorithm import Graph

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
    with open("backend/graphSample4.txt", "r") as f:

        # convert text file to list
        graphList = []
        for row in f:
            graphList.append([int(x) for x in row.split()])

        # run Dijkstra
        g = Graph(9)
        print(graphList)
        g.addEdges(graphList)
        g.dijkstra(0)

        return graphList

# serves project locally without needing to set flask environment variables
if __name__ == "__main__":
    app.run(port=8080)