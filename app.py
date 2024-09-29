from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Путь к файлу с данными
DATA_FILE = 'data.json'

# Загружаем данные из файла
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'count': 0}

# Сохраняем данные в файл
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

# Получаем текущее количество кликов
@app.route('/get_count', methods=['GET'])
def get_count():
    data = load_data()
    return jsonify(data)

# Обновляем количество кликов
@app.route('/update', methods=['POST'])
def update_count():
    data = request.get_json()
    save_data(data)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
