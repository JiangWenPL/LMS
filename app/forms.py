# 引入Form基类
from flask_wtf import FlaskForm
# 引入Form元素父类
from wtforms import StringField, PasswordField, BooleanField, IntegerField, FloatField
# 引入Form验证父类
from wtforms.validators import DataRequired, Length, NumberRange
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
    year = StringField ( "year", validators=[DataRequired ()] )
    author = StringField ( "author", validators=[DataRequired ()] )
    price = IntegerField ( "price", validators=[DataRequired (), NumberRange ()] )
    stock = IntegerField ( "stock", validators=[DataRequired (), NumberRange ( min=0 )] )


class FileForm ( FlaskForm ):
    csv = FileField ( "csv", validators=[FileAllowed ( csv_set, 'Incorrect file format' ), FileRequired ()] )
