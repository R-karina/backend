from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/api/data", methods=["POST"])
def save_data():
    data = request.json
    text = data.get("text", "")

    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")

    return jsonify({
        "message": "Данные успешно сохранены"
    })


if __name__ == "__main__":
    app.run(debug=True)