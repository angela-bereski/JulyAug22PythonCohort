from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.trainer import Trainer
from flask_app.models.user import User

@app.route('/trainers/')
def trainers():
    if 'user_id' not in session:
        return redirect('/')
    else:
        theTrainers = Trainer.getAll()
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('employee/trainers.html', user=theUser, trainers=theTrainers)

@app.route('/addTrainer/')
def addTrainer():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        print("the User", theUser)
        return render_template('employee/addTrainer.html', user=theUser)

@app.route('/createTrainer/', methods=['post'])
def createTrainer():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'bio': request.form['bio'],
        'user_id': request.form['user_id']
    }
    Trainer.save(data)
    print("saved data:", data)
    return redirect('/')

@app.route('/trainer/<int:trainer_id>/view/')
def viewTrainer(trainer_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        userdata = {
            'id': session['user_id']
        }
        theUser = User.getOne(userdata)
        data = {
            'id': trainer_id
        }
        theTrainer = Trainer.getOne(data)
        theCohorts = Trainer.trainerCohorts(data)
        return render_template('employee/viewTrainer.html', trainer=theTrainer, user=theUser, cohorts=theCohorts)

@app.route('/trainer/<int:trainer_id>/edit/')
def editTrainer(trainer_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        userdata = {
            'id': session['user_id']
        }
        theUser = User.getOne(userdata)
        data = {
            'id': trainer_id
        }
        return render_template('employee/editTrainer.html', trainer=Trainer.getOne(data), user=theUser)

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