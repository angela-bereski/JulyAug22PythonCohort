from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.joke import Joke


@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        flash("Dude private area log in please")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    theJokes = User.userJokes(data)
    return render_template('dashboard.html', user=theUser, jokes=theJokes)

@app.route('/jokeAPI/')
def jokeAPI():
    if 'user_id' not in session:
        flash("Dude private area log in please")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    return render_template('jokeAPI.html', user=theUser)

@app.route('/createJoke/', methods=['post'])
def createJoke():
    data = {
        'question': request.form['question'],
        'punchline': request.form['punchline'],
        'user_id': session['user_id']
    }
    Joke.save(data)
    flash("Joke Saved to database")
    return redirect('/dashboard/')