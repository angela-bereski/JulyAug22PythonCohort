from sqlite3 import DatabaseError
from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt

from flask_app.models.wallpost import Wallpost
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/wallpost/', methods=['POST'])
def createPost():
    if 'user_id' not in session:
        return render_template('/')
    isValid = Wallpost.validate(request.form)
    if not isValid:
        return redirect('/dojowall/')
    else:
        data = {
            'user_id' : session['user_id'],
            'content' : request.form['content']
        }
        id = Wallpost.save(data)
        if not id:
            flash('Something is wrong!')
        else:
            session['user_id'] = id
            flash('You posted to the dojowall!')
        return redirect('/dojowall/')

@app.route('/deletePost/<int:id>/')
def deletePost(id):
    data = {
        'id': id
    }
    if 'user_id' not in session:
        return redirect('/')
    else:
        moreData = {
            'id': session['user_id']
        }
    Wallpost.delete(data)
    theUser = User.getOne(moreData)
    theUsers = User.getAll()
    return render_template('dojowall.html', user=theUser, users=theUsers)

