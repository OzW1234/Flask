import os
from flask import Flask
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

json=[]
@app.route('/webhook', methods=['POST'])
def addOne():
    new_message = request.get_json()
    json.append(new_message)
    return jsonify({'json' : json})

@app.route('/webhook', methods=['PUT'])
def editOne(name):
    new_json = request.get_json()
    for i,q in enumerate(json):
      if q['name'] == name:
        json[i] = new_json
    qs = request.get_json()
    return jsonify({'json' : json})

if __name__ == "__main__":
    app.run(host = '0.0.0.0' , port = int(os.environ.get("PORT", 5000)))
