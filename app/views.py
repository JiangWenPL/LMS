# -*- coding:utf-8 -*-
__author__ = u'Jiang Wen'
from flask import render_template, flash, request, abort, redirect, url_for, g
from app import app, db, lm
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import LoginForm
from flask_bootstrap import Bootstrap
from app.models import Admin

Bootstrap ( app )


@app.before_first_request
def create_db():
    # Recreate database each time for demo
    db.drop_all ()
    db.create_all ()
    admins = [Admin ( 0, 'a', 'a.name', 'admin@example.com' ), Admin ( 1, 'b', 'b.name', 'bdmin@example.com' )]
    db.session.add_all ( admins )
    db.session.commit ()


@app.before_request
def before_request():
    g.user = current_user


@app.route ( '/' )
@app.route ( '/index.html' )
def index():
    return render_template ( "index.html" )


@app.route ( '/login', methods=['GET', 'POST'] )
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    # if request.method == 'GET':
    #     return render_template ( 'login.html' )
    error = None
    if g.user is not None and g.user.is_authenticated:
        return redirect ( url_for ( 'index' ) )
    form = LoginForm ()
    if form.validate_on_submit ():
        try:
            user = Admin.query.filter_by ( id=form.username.data ).first ()
            if user is None:
                error = 'Invalid username'
            elif form.password.data != user.password:
                error = 'Invalid password'
            else:
                login_user ( user=user, remember=form.remember.data )
                flash ( 'You were logged in', category='success' )
                return redirect ( url_for ( 'index' ) )
        except Exception as e:
            flash ( e, 'danger' )

    elif request.method == 'POST':
        flash ( 'Invalid input', 'warning' )
    if error is not None:
        flash ( error, category='danger' )
    return render_template ( 'login.html', form=form, error=error )

    return redirect ( 404 )


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
    flash ( "Logout successful", category='success' )
    return redirect ( url_for ( 'index' ) )

@lm.user_loader
def load_user(id):
    return Admin.query.get ( int ( id ) )
