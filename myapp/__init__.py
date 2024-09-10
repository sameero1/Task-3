from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.Config')  # Ensure your config is correct

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from myapp import routes
