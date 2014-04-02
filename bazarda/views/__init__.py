from flask import render_template as render
from bazarda import Session 
from bazarda import app
from bazarda.model.user import User

@app.route('/')
def hello():
    user = Session.query(User).get(1)
    n = 'boboss'
    v= user.username
    return render('hello.html',name=v)

