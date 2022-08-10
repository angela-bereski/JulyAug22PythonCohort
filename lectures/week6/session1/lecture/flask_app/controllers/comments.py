from flask_app import app
from flask import render_template, redirect, request, session
# from flask_app.models.user import User
from flask_app.models.comment import Comment


@app.route('/createComment/', methods=['post'])
def createComment():
    data = {
        'comment': request.form['comment'],
        'user_id': session['user_id']
    }
    Comment.save(data)
    return redirect('/dashboard/')