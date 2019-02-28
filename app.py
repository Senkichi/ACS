from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from random import sample
import time

app = Flask(__name__)

# # Configure MongoDB Database
app.config['MONGO_DBNAME'] = 'ACS'
app.config['MONGO_URI'] = 'mongodb://root:ucbmongodb@35.184.4.63:27017/ACS'

mongo = PyMongo(app)

# conn = 'mongodb://root:ucbmongodb@35.184.4.63:27017'
# client = pymongo.MongoClient(conn)
# db = client.somedb
# db.someinfo.insert_one(temp_doc)



# Set up routes
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    acs = mongo.db.acs

    result = acs.find_all({'County'})

    return jsonify({'results': result['County']})


if __name__ == '__main__':
    app.run(debug=True)