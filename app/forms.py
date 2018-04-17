# 引入Form基类
from flask_wtf import FlaskForm
# 引入Form元素父类
from wtforms import StringField, PasswordField, BooleanField
# 引入Form验证父类
from wtforms.validators import DataRequired, Length

__author__ = 'JiangWen'


class LoginForm ( FlaskForm ):
    username = StringField ( "username", validators=[DataRequired ()] )
    password = PasswordField ( 'passsword', validators=[DataRequired ()], default=False )
    remember = BooleanField ( "remember", default=False )
