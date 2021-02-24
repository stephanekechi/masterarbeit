from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Helo World Greatness"

@app.route('/add', methods=['POST'])
def add():
        postedData = request.get_json()

        retJson = {
            'message': int(postedData["x"]) + int(postedData["y"])
        }
        return jsonify(retJson), 200
        #debug=True,
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')