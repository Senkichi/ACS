from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymongo
import time

app = Flask(__name__)

# Configure MongoDB Database
conn = 'mongodb://root:ucbmongodb@35.184.4.63:27017'
client = pymongo.MongoClient(conn)
db = client.somedb
db.someinfo.insert_one(temp_doc)



# Set up routes
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")