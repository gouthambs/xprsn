# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:50:28 2014

@author: Goutham
"""
from flask import url_for
from flask.ext.login import LoginManager
from app import flask_app
from models import User

login_manager = LoginManager()
login_manager.init_app(flask_app)

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)
    
login_manager.login_view = "auth.login"

