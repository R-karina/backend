from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


# Версия 1.0 — сохранение данных
@app.route("/api/data", methods=["POST"])
def save_data():
    data = request.json
    text = data.get("text", "")

    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")

    return jsonify({
        "message": "Данные успешно сохранены"
    })


# Версия 2.0 — получение данных
@app.route("/api/data", methods=["GET"])
def get_data():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            content = file.read()

        return jsonify({
            "data": content
        })

    except FileNotFoundError:
        return jsonify({
            "data": ""
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)