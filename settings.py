from bson import ObjectId
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from connexion.apps.flask_app import FlaskJSONEncoder
import os


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['MONGO_DBNAME'] = 'NewNews'
app.config['MONGO_URI'] ='mongodb+srv://newnews_user:jOtZcR7QQrIdyMfB@newnews.uqkma.mongodb.net/NewNews?retryWrites=true&w=majority' #os.environ['DB_HOST']
mongo = PyMongo(app)

#
class CustomJSONEncoder(FlaskJSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)

        return super().default(o)

app.json_encoder = CustomJSONEncoder