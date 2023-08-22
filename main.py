from flask import Flask
from flask import request

from listToJSON import listToJSON
from User import User

app = Flask(__name__)

players = [ User('Вася', 'Пупкин', 0), User('Петя', 'Тряпкин', 1), User('Даша', 'Корйека', 2) ]

@app.route('/users', methods = ['GET'])
def users():
    return {
        'count': len(players),
        'users': players
    }

@app.route('/user/<id>', methods = ['GET', 'PUT', 'DELETE'])
def user_id(id):
    id = int(id)

    if request.method == "GET":
        return players[id]
    
    elif request.method == "PUT":
        data = request.json
        players[id] = data['name']
        return {
            'id': id,
            'name': players[id]
        }
    
    elif request.method == 'DELETE':
        buffer_name = players[id]
        players.pop(id)
        return {
            'id': id,
            'name': buffer_name
        }
    
@app.route('/user', methods = ['POST'])
def user():
    if request.method == 'POST':
        data = request.json
        players.append(data['name'])
        return {
            'id': len(players) - 1,
            'name': data['name']
        }
    
if __name__ == '__main__':
    # app.run(port=3000, debug=True)
    app.run(port=3000)