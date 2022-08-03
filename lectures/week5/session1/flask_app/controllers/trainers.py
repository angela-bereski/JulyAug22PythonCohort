from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.trainer import Trainer


@app.route('/')
def trainers():
    theTrainers = Trainer.getAll()
    print("the trainers:", theTrainers)
    return render_template('index.html', trainers=theTrainers)

@app.route('/addTrainer/')
def addTrainer():
    return render_template('addTrainer.html')

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
    data = {
        'id': trainer_id
    }
    theTrainer = Trainer.getOne(data)
    return render_template('viewTrainer.html', trainer=theTrainer)

@app.route('/trainer/<int:trainer_id>/edit/')
def editTrainer(trainer_id):
    data = {
        'id': trainer_id
    }
    return render_template('editTrainer.html', trainer=Trainer.getOne(data))

@app.route('/trainer/<int:trainer_id>/update/', methods=['post'])
def updateTrainer(trainer_id):
    data = {
        'id': trainer_id,
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