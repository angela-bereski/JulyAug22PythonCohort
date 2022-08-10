from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.comment import Comment


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard/')
def dashboard():
    theUsers = User.getAll()
    theComments = Comment.getAll()
    return render_template('dashboard.html', users=theUsers, comments=theComments)

@app.route('/createUser/', methods=['post'])
def createUser():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/dashboard/')
