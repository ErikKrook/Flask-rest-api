from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
tasks = {}

@app.route('/task/<string:task_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def task(task_id):
    if request.method == 'GET':
        if task_id in tasks:
            return jsonify({task_id: tasks[task_id]}), 200
        return jsonify({"message": "Task not found"}), 404
    
    if request.method == 'POST':
        data = request.json
        if not data or "description" not in data:
            return jsonify({"message":"Missing 'description' key in request body"}), 400
        if task_id in tasks:
            return jsonify({"message":"Task already exists"}), 400
        tasks[task_id] = request.json.get("description", "")
        return jsonify({task_id: tasks[task_id]}), 201

    if request.method == 'PUT':
        if task_id not in tasks:
            return jsonify({"message":"Task not found"}), 404
        
        data = request.json
        if not data or "description" not in data:
            return jsonify({"message":"Missing 'description' key in request body"}), 400
        
        tasks[task_id] = request.json.get("description", "")
        return jsonify({"message":"Task updated successfully",
                        "task_id": task_id,
                        "description": tasks[task_id]}), 200
    
    if request.method == 'DELETE':
        if task_id in tasks:
            del tasks[task_id]
            return jsonify({"message":"Task deleted succesfully"}), 200
        return jsonify({"message":"Task not found"}), 404
        
        

if __name__ == '__main__':
    app.run(debug=True)
