import os
from flask import Flask,json, jsonify, request
from flask_cors import CORS
from operation import Task
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("MY_SECRET")

app = Flask(__name__)
app.secret_key=SECRET_KEY

print(SECRET_KEY)
CORS(app)

# operations instans
task = Task()

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/alltask')
def getTask():
    res = task.ReadAllTask()
    return jsonify(res)

# Create Data Routes
@app.route('/createtask', methods=['POST'])
def addProduct(): 
    try:
        data =  json.loads(request.data)
        res = task.CreateTask(data)
        return jsonify(res)
    except Exception as e:
        return f"Error server: {e}"

# Update Data Route
@app.route('/updatetask', methods=['PUT'])
def editProduct():
    try:
        data =  json.loads(request.data)
        res = task.UpdateTask(data["id"],data)
        return jsonify(res)
    except Exception as e:
        return f"Error server: {e}"

# DELETE Data Route
@app.route('/products/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    try:
        res = task.DeleteTask(id);
        return jsonify(res)
    except Exception as e:
        return f"Error server: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=4000)
