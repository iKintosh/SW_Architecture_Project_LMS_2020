from LMS.model import models
from LMS.controller import routes
from LMS.controller.login import api as login_ns
from LMS.controller.signup import API as signup_ns
from LMS.controller.user import API as user_ns
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
api = Api(app)


api.add_namespace(user_ns, path="/user")
api.add_namespace(signup_ns, path="/signup")
api.add_namespace(login_ns, path="/login")
