from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ['TODO_SECRET_KEY']
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['TODO_DATABASE_URI']
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  from flaskr.views import bp
  app.register_blueprint(bp)
  db.init_app(app)
  migrate.init_app(app, db)
  return app