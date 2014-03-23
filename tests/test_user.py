# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 06:41:43 2014

@author: Goutham
"""
from app import db
import app.models as mod
from nose.tools import with_setup
from common import setup_test,teardown_test


@with_setup(setup_test,teardown_test)
def test_user_insert():
    ud = {"name":"test1","pass":"password","email":"user@email.com"}
    u = mod.User(ud["name"],ud["pass"],ud["email"])
    db.session.add(u)
    db.session.commit()
    #check only one user exists
    users = mod.User.query.all() 
    assert(len(users) == 1)
    u = users[0]
    assert(u.username == ud["name"])
    assert(u.password != ud["pass"]) # assert we don't store raw passwords
    assert(u.email == ud["email"]) 
    assert(u.role == mod.User.ROLE_FREE_USER)
        
    #assert(u.widgets==None)
    
        
        
        
@with_setup(setup_test,teardown_test)
def test_user_authentication():
    ud = {"name":"test1","pass":"password","email":"user@email.com"}
    u = mod.User(ud["name"],ud["pass"],ud["email"])
    db.session.add(u)
    db.session.commit()
    user = mod.User.query.filter((mod.User.username ==ud["name"])).first()
    assert(user.valid_authentication(ud["name"],ud["pass"])==True)
    assert(user.valid_authentication(ud["name"],ud["pass"]+"randowm")==False)
    
    

    
    
    