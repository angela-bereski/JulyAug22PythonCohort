from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.trainer import Trainer


@app.route('/dashboard/')
def trainers():
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        theTrainers = Trainer.getAll()
        print("the trainers:", theTrainers)
        return render_template('index.html', trainers=theTrainers, user=theUser)

@app.route('/addTrainer/')
def addTrainer():
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        return render_template('addTrainer.html', user=theUser)

@app.route('/createTrainer/', methods=['post'])
def createTrainer():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'bio': request.form['bio']
    }
    Trainer.save(data)
    print("saved data:", data)
    return redirect('/')

@app.route('/trainer/<int:trainer_id>/view/')
def viewTrainer(trainer_id):
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        data = {
            'id': trainer_id
        }
        theTrainer = Trainer.getOne(data)
        return render_template('viewTrainer.html', trainer=theTrainer, user=theUser)

@app.route('/trainer/<int:trainer_id>/edit/')
def editTrainer(trainer_id):
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        data = {
            'id': trainer_id
        }
        return render_template('editTrainer.html', trainer=Trainer.getOne(data), user=theUser)

@app.route('/trainer/<int:trainer_id>/update/', methods=['post'])
def updateTrainer(trainer_id):
    data = {
        # 'id': trainer_id,
        'id': request.form['id'],
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'bio': request.form['bio']
    }
    Trainer.update(data)
    print("updated trainer controller:", data)
    return redirect(f'/trainer/{trainer_id}/view')

@app.route('/trainer/<int:trainer_id>/delete/')
def deleteTrainer(trainer_id):
    data = {
        'id': trainer_id
    }
    Trainer.delete(data)
    return redirect('/')