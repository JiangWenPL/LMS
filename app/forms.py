# 引入Form基类
from flask_wtf import FlaskForm
# 引入Form元素父类
from wtforms import StringField, PasswordField, BooleanField, IntegerField, FloatField, SelectField
# 引入Form验证父类
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from flask_wtf.file import FileAllowed, FileRequired, FileField
from app import csv_set
from app.models import Book

__author__ = 'JiangWen'


class LoginForm ( FlaskForm ):
    username = StringField ( "username", validators=[DataRequired ()] )
    password = PasswordField ( 'passsword', validators=[DataRequired ()], default=False )
    remember = BooleanField ( "remember", default=False )


class CheckInForm ( FlaskForm ):
    bookID = StringField ( "bookID", validators=[DataRequired ()] )
    category = StringField ( "category", validators=[DataRequired ()] )
    book_name = StringField ( "book_name", validators=[DataRequired ()] )
    press = StringField ( "press", validators=[DataRequired ()] )
    year = IntegerField ( "year", validators=[DataRequired (), NumberRange ( 0, 10000 )] )
    author = StringField ( "author", validators=[DataRequired ()] )
    price = IntegerField ( "price", validators=[DataRequired (), NumberRange ()] )
    stock = IntegerField ( "stock", validators=[DataRequired (), NumberRange ( min=0 )] )


class FileForm ( FlaskForm ):
    csv = FileField ( "csv", validators=[FileAllowed ( csv_set, 'Incorrect file format' ), FileRequired ()] )


class SearchForm ( FlaskForm ):
    bookID = StringField ( "bookID", validators=[Optional ()] )
    category = StringField ( "category", validators=[Optional ()] )
    book_name = StringField ( "book_name", validators=[Optional ()] )
    press = StringField ( "press", validators=[Optional ()] )
    year_from = IntegerField ( "year_from", validators=[Optional ()] )
    year_to = IntegerField ( "year_to", validators=[Optional ()] )
    author = StringField ( "author", validators=[Optional ()] )
    price_from = FloatField ( "price_from", validators=[Optional ()] )
    price_to = FloatField ( "price_to", validators=[Optional ()] )
    stock = IntegerField ( "stock", validators=[Optional ()] )
    order_by = SelectField ( "order_by",
                             choices=[("book_name", 'book_name'), ("category", "category"), ("bookID", "bookID"),
                                      ("press", "press"), ("year", "year"), ("author", "author"), ("price", "price"),
                                      ("stock", "stock"), ("amount", "amount")] )
    # order_by = StringField ( "order_by" )


order_object = {"book_name": Book.book_name, "category": Book.category, "bookID": Book.bookID,
                "press": Book.press, "year": Book.year, "author": Book.author, "price": Book.price,
                "stock": Book.stock, "amount": Book.amount}
