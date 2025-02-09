from pyexpat.errors import messages

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/simple')
def hello_simple():
    return jsonify(message='Hello, Simple World!!!')

@app.route('/not_found')
def not_found():
    return jsonify(error='This route was not found'),404

@app.route('/parameters')
def parameters():
    name = request.args.get('name', '')
    age = int(request.args.get('age', 0))
    if age > 21:
        return jsonify(message=f"Welcome, {name}!!!")
    else:
        return jsonify(message=f"Sorry {name}, you are not old enough to access this API.")

@app.route('/api_variables', defaults={'name':'John', 'age':0})
@app.route('/api_variables/<string:name>', defaults={'age':0})
@app.route('/api_variables/<string:name>/<int:age>')
def api_variables(name:str, age:int):
    if age > 20:
        return jsonify(message=f"Welcome, {name}!")
    else:
        return jsonify(messae=f"Sorry {name}, you are not old enoughg to access this API!")

if __name__ == '__main__':
    app.run()