from flask import Flask, request, jsonify
from json_handler_integration import update_json, read_json, delete_json

app = Flask(__name__)

tasks = {}

@app.route('/task/<string:task_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def task(task_id):
    if request.method == 'GET':
        response = read_json(task_id)
        if response is None:
            return jsonify({"message": "Task not found"}), 404
        return jsonify(response), 200
    
    if request.method == 'POST':
        data = request.json
        if not data or "description" not in data:
            return jsonify({"message":"Missing 'description' key in request body"}), 400
        else:
            response = update_json({task_id: request.json.get("description", "")}, False)
            if response is False:
                return jsonify({"message":"Task already exists"}), 400
            else:
                return jsonify({task_id: tasks[task_id]}), 201

    if request.method == 'PUT':
        data = request.json
        if not data or "description" not in data:
            return jsonify({"message":"Missing 'description' key in request body"}), 400
        else:
            response = update_json({task_id: request.json.get("description", "")}, True)
            if response is False:
                return jsonify({"message":"Task not found"}), 404
            else:
                return jsonify({"message":"Task updated successfully",
                                "task_id": task_id,
                                "description": request.json.get("description", "")}), 200
    
    if request.method == 'DELETE':
        if task_id in tasks:
            del tasks[task_id]
            return jsonify({"message":"Task deleted succesfully"}), 200
        return jsonify({"message":"Task not found"}), 404
        
        

if __name__ == '__main__':
    app.run(debug=True)
