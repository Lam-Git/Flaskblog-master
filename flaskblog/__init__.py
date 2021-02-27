from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "Tichmanh1."
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)  # creating the database
bcrypt = Bcrypt(app)
login_manger = LoginManager(app)
login_manger.login_view = "login"
login_manger.login_message_category = "info"

from flaskblog import routes
