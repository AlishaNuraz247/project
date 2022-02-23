#import flask from flask module
#import SQLALCHEMY CLASS FROM SQLALCHEMY MODULE
# import OS
#importt getenv from OS

#create instance of flask and store it in app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" 
app.config['SECRET_KEY'] = "my-secret"

db = SQLAlchemy(app)


from application import routes


#create and store enviornment variables

#import routes