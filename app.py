from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
tasks = {
    "1": "Handla",
    "2": "Läsa",
    "3": "Prommenera",
    "4": "Städa"
}

@app.route('/task/<string:task_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def task(task_id):
    if request.method == 'GET':
        if task_id in tasks:
            return jsonify({task_id: tasks[task_id]})
        return jsonify({"message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
