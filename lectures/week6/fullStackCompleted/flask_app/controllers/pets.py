from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.pet import Pet
from flask_app.models.user import User

@app.route('/pets/')
def pets():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        thePets = Pet.getAll()
        theOwners = User.getAll()
        return render_template('employee/pets.html', user=theUser, pets=thePets, owners=theOwners)

@app.route('/addPet/')
def addPet():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('customer/addPet.html', user=theUser)

@app.route('/createPet/', methods=['post'])
def createPet():
    data = {
        'name': request.form['name'],
        'age': request.form['age'],
        'breed': request.form['breed'],
        'user_id': request.form['user_id']
    }
    Pet.save(data)
    return redirect('/dashboard/')

@app.route('/pet/<int:pet_id>/view/')
def viewPet(pet_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        userData = {
            'id': session['user_id']
        }
        theUser = User.getOne(userData)
        data = {
            'id': pet_id
        }
        thePet = Pet.getOne(data)
        theCohorts = Pet.petCohorts(data)
        return render_template('customer/viewPet.html', user=theUser, pet=thePet, cohorts=theCohorts)

@app.route('/pet/<int:pet_id>/edit/')
def editPet(pet_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        userData = {
            'id': session['user_id']
        }
        theUser = User.getOne(userData)
        data = {
            'id': pet_id
        }
        thePet = Pet.getOne(data)
        return render_template('customer/editPet.html', user=theUser, pet=thePet)

@app.route('/pet/<int:pet_id>/update/', methods=['post'])
def updatePet(pet_id):
    data = {
        'id': pet_id,
        'name': request.form['name'],
        'age': request.form['age'],
        'breed': request.form['breed']
    }
    Pet.update(data)
    return redirect(f'/pet/{pet_id}/view/')

@app.route('/pet/<int:pet_id>/delete/')
def deletePet(pet_id):
    data = {
        'id': pet_id
    }
    Pet.delte(data)
    return redirect('/dashboard/')