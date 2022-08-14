from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.score import Scores
from flask_app.models.user import User


@app.route('/addGame/')
def addGame():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('addGame.html', user=theUser)

@app.route('/createGame/', methods=['post'])
def createGame():
    data = {
        'teamOne': request.form['teamOne'],
        'teamTwo': request.form['teamTwo'],
        'finalScore': request.form['finalScore'],
        'info': request.form['info'],
        'gameDate': request.form['gameDate'],
        'user_id': request.form['user_id'],
    }
    Scores.save(data)
    return redirect('/dashboard/')

@app.route('/game/<int:scores_id>/view/')
def viewGame(scores_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        gameData = {
            'id': scores_id
        }
        theUser = User.getOne(data)
        theGame = Scores.getOne(gameData)
        theUsers = User.getAll()
        return render_template('viewGame.html', user=theUser, game=theGame, users=theUsers)

@app.route('/game/<int:scores_id>/edit/')
def editGame(scores_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        gameData = {
            'id': scores_id
        }
        theGame = Scores.getOne(gameData)
        return render_template('editGame.html', user=theUser, game=theGame)

@app.route('/game/<int:scores_id>/update/', methods=['post'])
def updateGame(scores_id):
    data = {
        'id': scores_id,
        'teamOne': request.form['teamOne'],
        'teamTwo': request.form['teamTwo'],
        'finalScore': request.form['finalScore'],
        'info': request.form['info'],
        'gameDate': request.form['gameDate']
    }
    Scores.update(data)
    return redirect(f'/game/{scores_id}/view/')

@app.route('/game/<int:scores_id>/delete/')
def deleteGame(scores_id):
    data = {
        'id': scores_id
    }
    Scores.delete(data)
    return redirect('/dashboard/')