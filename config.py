# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))
# The database will be stored in the project folder as "app.db"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
