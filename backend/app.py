# UPDATE THIS FILE FOR DEPLOYMENT
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db" # NAME DATABASE WITH .db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import routes # because routes.py is in the same folder and not returning anything

# CREATE DATABASE
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
    