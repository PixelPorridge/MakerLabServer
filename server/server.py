from flask import Flask

app = Flask(__name__)


@app.route("/items")
def items():
    return {"items": ["Sword", "Shield", "Potion"]}


if __name__ == "__main__":
    app.run(debug=True)
