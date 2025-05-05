from flask import Flask, jsonify  # Добавляем импорт jsonify
from views import tasks_blueprint

app = Flask(__name__)

# Регистрируем blueprint
app.register_blueprint(tasks_blueprint)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)