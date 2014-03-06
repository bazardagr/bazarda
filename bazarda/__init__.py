from flask import Flask,render_template

app = Flask(__name__)
app.config.from_object('bazarda.config_app.DevelopmentConfig') #change this on production

from bazarda import views
