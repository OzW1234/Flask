import os
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host = '0.0.0.0' , port = int(os.environ.get("PORT", 5000)))
