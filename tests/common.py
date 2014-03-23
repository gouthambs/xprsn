# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 14:54:13 2014

@author: Goutham
"""
from app import flask_app,db

def setup_test():
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    db.create_all()
    
def teardown_test():
    db.drop_all()