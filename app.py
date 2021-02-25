
from flask import Flask, request, render_template
from flask import jsonify

from cnnDepression import cnnDepression

import time

app = Flask(__name__)

# cnn= cnn_inaSpeechSegmenter()

@app.route('/', methods=['GET'])
def index():
    return "version 1.0"

@app.route('/api/<id>', methods=['GET'])
def api(id):
    print(id)
    data = jsonify(
        id= id,
        segments= [[0.2, 0.9]],
    )

    return data


@app.route('/api/depression', methods=['POST'])
def index_post():
    data= request.json
    print(data)

    filename =data['filename']
    depression= []
    try:
        depression= cnnDepression().pipeline(filename)
    except:
        print("cnnDepression error")


    st = time.time()

    elapsed = time.time() - st
    print(elapsed)

    data_res = jsonify(
        filename= filename,
        depression= depression,
        elapsed= elapsed
    )

    return data_res

app.run(host='0.0.0.0', port='8071', debug=True)

