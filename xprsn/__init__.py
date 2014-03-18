# -*- coding: utf-8 -*-



from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder = "D:\\Development\\Repository\\GitHub\\xprsn\\templates\\",
            static_folder="D:\\Development\\Repository\\GitHub\\xprsn\\static\\",
            static_url_path="/static")

db = SQLAlchemy(app)


