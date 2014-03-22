# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 20:53:10 2014

@author: Goutham
"""

import os
from flask import Flask,render_template
#from .database import db

#############################################
# Some paths and globals used is set here   #
#############################################
_BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))


flask_app = Flask(__name__,
            template_folder = os.path.join(_BASEDIR,"templates"),
            static_folder   = os.path.join(_BASEDIR,"static"),
            static_url_path = "/static")
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(flask_app)
import models
#db.init_app(flask_app)



# Sample HTTP error handling
@flask_app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404





db.create_all()