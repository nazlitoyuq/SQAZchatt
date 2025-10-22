# backend.py
from flask import Flask, request, jsonify, send_from_directory
import random
import os

app = Flask(__name__, static_folder="frontend")

# === Подготовленные ответы (1000) ===
responses = {
    "привет": "Привет!",
    "как дела": "Отлично, спасибо!",
    "что делаешь": "Помогаю тебе учиться и развлекаться.",
    "как тебя зовут": "Я SQAZchat, твой виртуальный помощник.",
    "пока": "До встречи!",
    "ты умеешь шутить": "Конечно! Почему компьютер не умеет плавать? Потому что боится вирусов 😄",
    "какая сегодня погода": "Я не знаю погоду, но могу поддержать беседу!",
    "спасибо": "Пожалуйста!",
    "ты человек": "Нет, я искусственный интеллект.",
    "что ты можешь": "Могу отвечать на вопросы, считать и генерировать примеры."
}

# Автозаполнение до 1000 случайными фразами
for i in range(10, 1000):
    responses[f"вопрос{i}"] = f"Это ответ на вопрос {i}"


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()

    # ищем точный ответ
    answer = responses.get(user_message)

    # если нет точного совпадения, возвращаем случайный ответ
    if not answer:
        answer = random.choice(list(responses.values()))

    return jsonify({"reply": answer})


# === Статические файлы фронтенда ===
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    if path != "" and os.path.exists(f"frontend/{path}"):
        return send_from_directory("frontend", path)
    else:
        return send_from_directory("frontend", "index.html")


if __name__ == "__main__":
    app.run(debug=True)
