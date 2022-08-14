from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.cohort import Cohort
from flask_app.models.trainer import Trainer
from flask_app.models.user import User
from flask_app.models.pet import Pet

@app.route('/cohorts/')
def cohorts():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theCohorts = Cohort.getAll()
        print(theCohorts)
        theTrainers = Trainer.getAll()
        return render_template('employee/cohorts.html', user=theUser, cohorts=theCohorts, trainers=theTrainers)
    
@app.route('/addCohort/')
def addCohort():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theTrainers = Trainer.getAll()
        return render_template('employee/addCohort.html', user=theUser, trainers=theTrainers)

@app.route('/createCohort/', methods=['post'])
def createCohort():
    data = {
        'name': request.form['name'],
        'topic': request.form['topic'],
        'length': request.form['length'],
        'trainer_id': request.form['trainer_id']
    }
    Cohort.save(data)
    return redirect('/cohorts/')

@app.route('/cohort/<int:cohort_id>/view/')
def viewCohort(cohort_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        userdata = {
            'id': session['user_id']
        }
        theUser = User.getOne(userdata)
        data = {
            'id': cohort_id
        }
        theCohort = Cohort.getOne(data)
        theTrainers = Trainer.getAll()
        thePets = Cohort.cohortPets(data)
        return render_template('employee/viewCohort.html', cohort=theCohort, user=theUser, trainers=theTrainers, pets=thePets)

@app.route('/cohort/<int:cohort_id>/edit/')
def editCohort(cohort_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        userdata = {
            'id': session['user_id']
        }
        theUser = User.getOne(userdata)
        data = {
            'id': cohort_id
        }
        theTrainers = Trainer.getAll()
        return render_template('employee/editCohort.html', cohort=Cohort.getOne(data), user=theUser, trainers=theTrainers)

@app.route('/cohort/<int:cohort_id>/update/', methods=['post'])
def updateCohort(cohort_id):
    data = {
        'id': cohort_id,
        # 'id': request.form['id'],
        'name': request.form['name'],
        'topic': request.form['topic'],
        'length': request.form['length'],
        'trainer_id': request.form['trainer_id']
    }
    Cohort.update(data)
    print("updated cohort controller:", data)
    return redirect(f'/cohort/{cohort_id}/view')

@app.route('/cohort/<int:cohort_id>/delete/')
def deleteCohort(cohort_id):
    data = {
        'id': cohort_id
    }
    Cohort.delete(data)
    return redirect('/cohorts/')