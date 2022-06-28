from flask import Flask, request, json, Response
from pymongo import MongoClient
import datetime
from bson import ObjectId
from flask_jwt_extended import jwt_required


print("connecting database...")
client = MongoClient("localhost", 27017)
print("connection established with Mongo")


class MongoAPI:
    def __init__(self, document):
        cursor = client["polls"]
        self.collection = cursor[document]

    def read(self):
        documents = self.collection.find()
        output = [{item: str(data[item]) for item in data} for data in documents]
        return output

    def find_byid(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def write(self, data):
        new_document = data
        new_document["CreatedDate"] = datetime.datetime.today()
        result = self.collection.insert_one(new_document)
        return str(result.inserted_id)


app = Flask(__name__)


@app.route("/")
def base():
    return "status:up"


@app.route("/addAnswer", methods=["POST"])
@jwt_required()
def answers_post():
    data = request.json
    res = MongoAPI("answers").write(data)
    return Response(response=json.dumps(res), status=201, mimetype="application/json")


@app.route("/addPoll", methods=["POST"])
@jwt_required()
def polls_post():
    data = request.json
    res = MongoAPI("polls").write(data)
    return Response(response=json.dumps(res), status=201, mimetype="application/json")


@app.route("/getPolls", methods=["GET"])
@jwt_required()
def polls_get():
    polls = MongoAPI("polls").read()
    answers = MongoAPI("answers").read()
    for poll in polls:
        poll["answers"] = [
            answer for answer in answers if answer["poll_id"] == poll["_id"]
        ]
    return Response(response=json.dumps(polls), status=200)


if __name__ == "__main__":
    print("up")
    app.run(host="0.0.0.0", debug=True)