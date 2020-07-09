from flask import Flask, jsonify, request, json
import json 

app = Flask(__name__)

todos = [
    { "label": "Vender el queso que te tengo", "done":False},
    { "label": "Lavarme las manos", "done":False},
    ]


@app.route('/todos', methods=['GET'])
def hello_world():

    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    up= jsonify(todos)
    print(request_body, decoded_object)
    return up

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    id_del = todos.pop(position)
    # del todos[position]
    up= jsonify(todos)
    print("This is the position to delete: ",position)
    return up

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
