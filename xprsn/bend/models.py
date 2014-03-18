# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 09:45:05 2014

@author: Goutham
"""

from xprsn import db

ROLE_ADMIN      = 1
ROLE_FREE_USER  = 2
ROLE_PROMO_USER = 3
ROLE_PAID_USER  = 4

class User(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    username    = db.Column(db.String(64), unique = True)
    email       = db.Column(db.String(120), unique = True)
    joined      = db.Column(db.DateTime)
    role        = db.Column(db.SmallInteger, default = ROLE_FREE_USER)
    widgets     = db.relationship('Widget', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)

class Widget(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    created     = db.Column(db.DateTime)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    def __repr__(self):
        return '<Post %r>' % (self.body)