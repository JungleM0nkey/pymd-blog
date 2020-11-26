from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import os
from pathlib import Path

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

#CWD = os.getcwd()
#file directory
basedir = os.path.abspath(os.path.dirname(__file__))
POST_DIR = Path(f'{basedir}/posts')

from app import routes, models