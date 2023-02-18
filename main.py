# imports
from flask import Flask, jsonify

# create Flask application
app = Flask(__name__)


# create route
@app.route("/")
def home():
    return "Hello Wool!"



@app.route("/data")
def data():
    data = {
        "name": "John Doe",
        "age": 25
    }
    return jsonify(data)


# run the application
if __name__ == "__main__":
    app.run(debug=True)
