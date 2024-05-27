from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
db = PyMongo(app).db

from user.routes import routes
routes(app)

app.run(debug=True)