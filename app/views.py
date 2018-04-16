# -*- coding:utf-8 -*-
__author__ = u'Jiang Wen'
from flask import render_template, flash, request, abort, redirect
from app import app
from flask_login import LoginManager, login_user, login_required, logout_user


@app.route ( '/' )
@app.route ( '/index.html' )
def index():
    return render_template ( "index.html" )


@app.route ( '/login', methods=['GET', 'POST'] )
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    if request.method == 'GET':
        return render_template ( 'login.html' )
    # form = LoginForm ()
    # if form.validate_on_submit ():
    #     # Login and validate the user.
    #     # user should be an instance of your `User` class
    #     login_user ( user )
    #
    #     flash ( 'Logged in successfully.' )
    #
    #     next = request.args.get ( 'next' )
    #     # next_is_valid should check if the user has valid
    #     # permission to access the `next` url
    #     if not next_is_valid ( next ):
    #         return abort ( 400 )
    #
    #     return redirect ( next or flask.url_for ( 'index' ) )
    # return render_template ( 'login.html', form=form )


@app.route ( '/logout/' )
@login_required
def logout():
    logout_user ()  # 登出用户
    return '已经退出登录'
