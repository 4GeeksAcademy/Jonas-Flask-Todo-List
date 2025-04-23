from flask import Flask, jsonify, request

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)

    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    print("Incoming request with the following body", request_body)

    # Validación mínima
    if not request_body or "label" not in request_body or "done" not in request_body:
        return jsonify({ "error": "Missing 'label' or 'done'" }), 400

    todos.append(request_body)

    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
        # Comprobamos que la posición sea válida
    if 0 <= position < len(todos):
        del todos[position]  # Eliminar la tarea en la posición dada
        return jsonify(todos), 200  # Retornar la lista actualizada con estado 200
    else:
        return jsonify({"error": "Position not found"}), 404  # Retornar error si la posición no es válida

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)