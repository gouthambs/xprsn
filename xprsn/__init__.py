# -*- coding: utf-8 -*-



from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

_basedir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))



app = Flask(__name__,template_folder = os.path.join(_basedir,"templates"),
            static_folder=os.path.join(_basedir,"static"),
            static_url_path="/static")

db = SQLAlchemy(app)


