from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('bazarda.config_app.DevelopmentConfig') #change this on production

db = SQLAlchemy(app)
Session = db.session

from bazarda import views
