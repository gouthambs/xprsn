# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:21:39 2014

@author: Goutham
"""
from flask import render_template,Blueprint,redirect,url_for,session,g
from flask.ext.login import login_required,logout_user,current_user
from forms import LoginForm,RegisterForm
from app import TEMPLATE_FOLDER,STATIC_FOLDER,db
from models import User

auth_bp = Blueprint('auth',__name__,
                    template_folder = TEMPLATE_FOLDER,
                    static_folder = STATIC_FOLDER,
                    url_prefix = "/auth")


@auth_bp.before_request
def before_request():
    g.user = current_user

@auth_bp.route('/login',methods = ['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('/'))
    form = LoginForm()
    if form.validate_on_submit():
        session["user_id"] = form.user.id
        return redirect(url_for('index'))
    return render_template("user/login.html",form=form,title="Login")
    
    
@auth_bp.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        u = User(form.username.data,
                 form.password.data,
                 form.email.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('.login'))
    return render_template('user/register.html',form=form,title='Register')
    
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')