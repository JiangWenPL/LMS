# -*- coding:utf-8 -*-
__author__ = u'Jiang Wen'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, DATA
import os

app = Flask ( __name__ )
app.config.from_object ( 'config' )
db = SQLAlchemy ( app )
csv_set = UploadSet ( 'CSV' )
app.config['UPLOADED_CSV_DEST'] = os.path.join ( os.path.dirname ( __file__ ), 'static', 'download_data' )
app.config['UPLOADED_CSV_ALLOW'] = DATA
configure_uploads ( app, csv_set )
lm = LoginManager ()
lm.init_app ( app )
from app import models, views
