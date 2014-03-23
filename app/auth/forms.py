# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:33:43 2014

@author: Goutham
"""

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required

class LoginForm(Form):
    username = TextField('Username',validators= [Required()])
    password = PasswordField('Password' , validators=[Required()])
