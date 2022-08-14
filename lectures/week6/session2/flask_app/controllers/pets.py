from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.pet import Pet
from flask_app.models.user import User

@app.route('/addPet/')
def addPet():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('addPet.html', user=theUser)

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