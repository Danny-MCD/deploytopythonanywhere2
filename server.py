from flask import Flask, jsonify, request, abort
from ActorDAO import ActorDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/actors"
@app.route('/actors')
def getAll():
    #print("in getall")
    results = ActorDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/actors/2"
@app.route('/actors/<int:id>')
def findById(id):
    foundActor = actorDAO.findByID(id)

    return jsonify(foundActor)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"filmography\":\"Russia4ever\",\"name\":\"Liya Silver\",\"age\":21}" http://127.0.0.1:5000/actors
@app.route('/actors', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    actor = {
        "filmography": request.json['filmography'],
        "name": request.json['name'],
        "age": request.json['age'],
    }
    addedactor = ActorDAODAO.create(actor)
    
    return jsonify(addedactor)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"filmography\":\"Russia4ever\",\"name\":\"Liya Silver\",\"age\":21}" http://127.0.0.1:5000/actors/1
@app.route('/actors/<int:id>', methods=['PUT'])
def update(id):
    foundActor = ActorDAO.findByID(id)
    if not foundActor:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'age' in reqJson and type(reqJson['age']) is not int:
        abort(400)

    if 'filmography' in reqJson:
        foundActor['filmography'] = reqJson['filmography']
    if 'name' in reqJson:
        foundActor['name'] = reqJson['name']
    if 'age' in reqJson:
        foundActor['age'] = reqJson['age']
    ActorDAODAO.update(id,foundActor)
    return jsonify(foundActor)
        

    

@app.route('/actors/<int:id>' , methods=['DELETE'])
def delete(id):
    ActorDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)
