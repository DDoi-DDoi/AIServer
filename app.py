﻿import json
import sys
from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
sys.path.append('..\\test2\\Services')
from test2.Services.OCRservice import ocrCar


# db 연동
conn = MongoClient('127.0.0.1')

# db 생성
db = conn.gps_saver

# collection 생성
collect = db.data
app = Flask(__name__)
CORS(app)

@app.route("/carNum", methods=["GET", "POST"])
def index():
    json_data = request.get_json()

    dict_data = json.dumps(json_data)
    dict_data = json.loads(dict_data)
    doc = {
        "img" : json_data["img"],
        "answer" : "None"
    }
    img = list(db.conn.gps_saver.find_one({"img" : json_data["img"]}))

    if not img:
        return jsonify(doc["answer"])
    
    result = ocrCar(dict_data)
    doc["answer"] = result
    collect.insert_one(doc)
    #img.save('test.jpg')

    return result

@app.route('/check', methods=['GET'])
def checking():
    return "ok" 

@app.route('/img/', methods=['GET'])
def list_library():
    name = request.args.get('Name', 'aaa')
    lat = request.args.get('Lat', 'bbb')
    lon = request.args.get('Lon', 'ccc')
    time = request.args.get('Time', 'ddd')

    # document 생성
    doc = {
    "Name": name,
    "Lat" : lat,
    "Lon" : lon,
    "Time" : time
    }
    # document 삽입
    collect.insert_one(doc)

    return jsonify({"code": 0, "msg": "Storage completed"})

if __name__== "__main__":
	app.run()