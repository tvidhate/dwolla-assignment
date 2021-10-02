import flask
from flask import request, jsonify
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/v1/currentDateTime', methods=['GET'])
def home():
    return jsonify(currentTime=datetime.now().strftime("%Y-%m-%d %H:%M:%S") )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')