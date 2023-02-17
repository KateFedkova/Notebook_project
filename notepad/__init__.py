from flask import Flask
from flask_login import LoginManager
from environs import Env

env = Env()
env.read_env()

app = Flask(__name__)
app.secret_key = env.str("SECRET_KEY")

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

from notepad import routes

