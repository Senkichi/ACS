from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure Database
# TODO: replace placeholder 'xxx' with DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'xxx'
# db = SQLAlchemy(app)


# Set up routes
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")