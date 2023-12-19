from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
db = PyMongo(app).db

@app.route('/')
def hello_world():
    db.new_doc.insert_one({"a": 1})
    return 'Hello, World!'

app.run(debug=True)