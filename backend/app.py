import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, origins="*")
CORS(app)

@app.route('/api/getMyInfo')
def getMyInfo():
    value = {
        "name": "Jorge",
        "lastname": "Silva",
        "socialMedia":
        {
            "facebookUser": "jrsz",
            "instagramUser": "jrsz",
            "xUser": "jorgesilva",
            "linkedin": "https://www.linkedin.com/in/jsilvazuniga/",
            "githubUser": "jsilvazuniga"
        },
        "blog": "https://github.com/jsilvazuniga",
        "author": "Jorge Silva"
    }
    return json.dumps(value)