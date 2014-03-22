# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:57:58 2014

@author: Goutham
"""

from app import db

class Widget(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    created     = db.Column(db.DateTime)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    def __repr__(self):
        return '<Widget %r>' % (self.id)