from flask import Flask

app = Flask(__name__)

# function executed when root address receives HTTP request
@app.route("/", methods=["GET"]) 
def users():
    print("loading sample graph data...")
    with open("graphSample.txt", "r") as f:
        data = json.load(f)
        data.append({
            "username": "user4",
            "pets": ["hamster"]
        })
        return flask.jsonify(data)

# serves project locally without needing to set flask environment variables
if __name__ == "__main__":
    app.run("localhost", 6969)