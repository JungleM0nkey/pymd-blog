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

CWD = os.getcwd()
APP_DIR = str(Path(CWD))
POST_DIR = f'{APP_DIR}\\app\\posts'

from app import routes, models