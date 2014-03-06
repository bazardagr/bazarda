from bazarda import app
from flask import render_template as render

@app.route('/')
def hello():
    return render('hello.html')

