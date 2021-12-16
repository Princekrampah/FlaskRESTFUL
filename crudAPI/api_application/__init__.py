from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


# app configs
app.config["SECRET_KEY"] = '5753944b6b64e743b6b202336ea9cd25'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

db = SQLAlchemy(app)

from api_application import routes