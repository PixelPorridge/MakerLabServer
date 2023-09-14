from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/items")
def items():
    return {"items": ["Sword", "Shield", "Potion"]}
