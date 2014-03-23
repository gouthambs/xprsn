# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:21:39 2014

@author: Goutham
"""
from app import TEMPLATE_FOLDER,STATIC_FOLDER
from flask import render_template,Blueprint,request,redirect
from forms import LoginForm

auth_bp = Blueprint('auth',__name__,
                    template_folder = TEMPLATE_FOLDER,
                    static_folder = STATIC_FOLDER,
                    url_prefix = "/auth")


@auth_bp.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        form = request.form
        print form.username
        return redirect('/')
    form = LoginForm()
    return render_template("user/login.html",form=form,title="Login")