# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:43:08 2014

@author: Goutham
"""
from datetime import datetime 
from app import db
from werkzeug.security import generate_password_hash, \
     check_password_hash



class User(db.Model):
    ROLE_ADMIN      = 1
    ROLE_FREE_USER  = 2
    ROLE_PROMO_USER = 3
    ROLE_PAID_USER  = 4
    ''' Generic User. Doesn't have custom code or relationships'''
    id          = db.Column(db.Integer, primary_key = True)
    username    = db.Column(db.String(64), unique = True)
    password    = db.Column(db.String(64)) # hashed password
    email       = db.Column(db.String(120), unique = True)
    joined      = db.Column(db.DateTime)
    role        = db.Column(db.SmallInteger, default = ROLE_FREE_USER)
    widgets = db.relationship('Widget', backref = 'author', lazy = 'dynamic')
    
    def __init__(self , username ,password , email,
                 role=ROLE_FREE_USER):
        self.username = username
        self.password = self.hash_password(password)
        self.email = email
        self.joined = datetime.utcnow() 
        
        
    
    def __repr__(self):
        return '<User %r>' % (self.username)
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
        
    # Required for administrative interface
    def __unicode__(self):
        return self.username
    
    
    @classmethod
    def hash_password(cls,password):
        return generate_password_hash(password)
        
    def valid_authentication(self,username,password):
        auth = False
        if (self.username == username) and (check_password_hash(self.password,password)):
            auth = True
        return auth
       
    @classmethod   
    def get(cls,userid):
        u = User.query.filter_by(id = int(userid)).first()
        return u
        
    
