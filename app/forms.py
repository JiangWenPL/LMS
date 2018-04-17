# 引入Form基类
from flask_wtf import FlaskForm
# 引入Form元素父类
from wtforms import StringField, PasswordField, BooleanField, IntegerField, FloatField, SelectField
# 引入Form验证父类
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from flask_wtf.file import FileAllowed, FileRequired, FileField
from app import csv_set

__author__ = 'JiangWen'


class LoginForm ( FlaskForm ):
    username = StringField ( "username", validators=[DataRequired ()] )
    password = PasswordField ( 'passsword', validators=[DataRequired ()], default=False )
    remember = BooleanField ( "remember", default=False )


class CheckInForm ( FlaskForm ):
    bookID = IntegerField ( "bookID", validators=[DataRequired (), NumberRange ()] )
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
    bookID = IntegerField ( "bookID", validators=[Optional ()] )
    category = StringField ( "category", validators=[Optional ()] )
    book_name = StringField ( "book_name", validators=[Optional ()] )
    press = StringField ( "press", validators=[Optional ()] )
    year_from = StringField ( "year_from", validators=[Optional ()] )
    year_to = StringField ( "year_to", validators=[Optional ()] )
    author = StringField ( "author", validators=[Optional ()] )
    price_from = IntegerField ( "price_from", validators=[Optional ()] )
    price_to = IntegerField ( "price_to", validators=[Optional ()] )
    stock = IntegerField ( "stock", validators=[Optional ()] )
    order_by = StringField ( "order_by" )
