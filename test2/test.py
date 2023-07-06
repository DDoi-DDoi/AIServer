from flask import Flask, jsonify, request
from pymongo import MongoClient

# db 연동
conn = MongoClient('127.0.0.1')

# db 생성
db = conn.gps_saver

# collection 생성
collect = db.data

app = Flask(__name__)


@app.route('/', methods=['GET'])
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


if __name__ == '__main__':
    app.run()