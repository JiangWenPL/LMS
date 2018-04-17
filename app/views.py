# -*- coding:utf-8 -*-
__author__ = u'Jiang Wen'
from flask import render_template, flash, request, abort, redirect, url_for, g
from app import app, db, lm, csv_set
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import LoginForm, CheckInForm, FileForm
from flask_bootstrap import Bootstrap
from app.models import Admin, Book
import csv

Bootstrap ( app )


@app.before_first_request
def init_view():
    # recreate database every time
    db.drop_all ()
    db.create_all ()
    admins = [Admin ( 0, 'a', 'a.name', 'admin@example.com' ), Admin ( 1, 'b', 'b.name', 'bdmin@example.com' )]
    db.session.add_all ( admins )
    db.session.commit ()
    # Add login guider
    lm.login_view = url_for ( 'login' )
    lm.login_message = "Please login"
    lm.login_message_category = 'info'


@app.before_request
def before_request():
    g.user = current_user


@app.route ( '/' )
@app.route ( '/index.html' )
def index():
    return render_template ( "index.html" )


@app.route ( '/check_in', methods=['GET', 'POST'] )
@login_required
def check_in():
    single_form = CheckInForm ()
    group_form = FileForm ()
    if request.method == 'POST' and request.form['kinds'] == 'single':
        if single_form.validate_on_submit ():
            try:
                book = Book ( bookID=single_form.bookID.data, category=single_form.category.data,
                              book_name=single_form.book_name.data,
                              press=single_form.press.data, year=single_form.year.data, author=single_form.author.data,
                              price=single_form.price.data,
                              stock=single_form.stock.data )
                db.session.add ( book )
                db.session.commit ()
                flash ( Book.query.all (), 'success' )
                flash ( 'Check in book success', 'success' )
            except Exception as e:
                flash ( e, 'danger' )
        elif request.method == 'POST':
            flash ( 'Invalid input', 'warning' )
    elif request.method == 'POST' and request.form['kinds'] == 'group':
        if group_form.validate_on_submit ():
            try:
                csv_name = csv_set.save ( request.files['csv'] )
                flash ( 'Upload file success', 'info' )
                books = []
                with open ( app.config['UPLOADED_CSV_DEST'] + '/' + csv_name ) as csv_file:
                    reader = csv.reader ( csv_file )
                    for line in reader:
                        assert len ( line ) == Book.length, "Not match col size"
                        books.append (
                            Book ( bookID=line[0], category=line[1], book_name=line[2], press=line[3], year=line[4],
                                   author=line[5], price=line[6], stock=line[7] ) )
                    db.session.add_all ( books )
                    db.session.commit ()
            except Exception as e:
                flash ( e, 'danger' )
            else:
                flash ( 'Success load into database', 'success' )
        elif request.method == 'POST':
            flash ( 'Invalid file', 'warning' )

    return render_template ( "check_in.html", single_form=single_form, group_form=group_form )


@app.route ( '/login', methods=['GET', 'POST'] )
def login():
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


@app.route ( '/search' )
def search():
    return render_template ( 'search.html' )


@app.route ( '/borrow' )
@login_required
def borrow():
    return render_template ( 'borrow.html' )


@app.route ( '/return_book' )
@login_required
def return_book():
    return render_template ( 'return_book.html' )


@app.route ( '/card' )
@login_required
def card():
    return render_template ( 'card.html' )


@app.route ( '/about' )
def about():
    return render_template ( 'about.html' )


@app.route ( '/logout/' )
@login_required
def logout():
    logout_user ()  # 登出用户
    flash ( "Logout successful", category='success' )
    return redirect ( url_for ( 'index' ) )


@lm.user_loader
def load_user(id):
    return Admin.query.get ( int ( id ) )
