from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.enroll import Enroll
from flask_app.models.user import User
from flask_app.models.cohort import Cohort
from flask_app.models.pet import Pet

@app.route('/enrollPet/')
def enrollPet():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        thePets = User.ownerPets(data)
        theCohorts = Cohort.getAll()
        return render_template('customer/enrollPet.html', user=theUser, pets=thePets, cohorts=theCohorts)

@app.route('/createEnroll/', methods=['post'])
def createEnroll():
    data = {
        'startDate': request.form['startDate'],
        'pet_id': request.form['pet_id'],
        'cohort_id': request.form['cohort_id']
    }
    Enroll.save(data)
    return redirect('/dashboard/')