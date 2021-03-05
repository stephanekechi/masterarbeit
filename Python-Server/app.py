from flask import Flask, request, jsonify
from flask_cors import CORS
from routes_handler import RoutesHandler


app = Flask(__name__)
CORS(app)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

routes_handlers = RoutesHandler('models/rbmodel.pickle', 'models/nbmodel.pickle')
#routes_handlers = RoutesHandler('rbmodel.mdl', 'nbmodel.mdl')

@app.route('/test', methods=['GET'])
def test():
    resJson = {
        'username': 'Stephanekechi',
    }
    return jsonify(resJson), 200

@app.route('/add', methods=['POST'])
def add():
    postedData = request.get_json()

    resJson = {
        'message': int(postedData["x"]) + int(postedData["y"])
    }
    return jsonify(resJson), 200

@app.route('/classify', methods=['POST'])
def classify():
    postedData = request.get_json()
    print(postedData)
    classifiedData = routes_handlers.classify_news(postedData)

    #the result of the test should be false.
    return jsonify(classifiedData), 200

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')