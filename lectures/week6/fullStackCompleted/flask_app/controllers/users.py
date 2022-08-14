from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.trainer import Trainer
from flask_app.models.cohort import Cohort
from flask_app.models.enroll import Enroll
from flask_app.models.pet import Pet

bcrypt = Bcrypt(app)

@app.route('/')
def logReg():
    if 'user_id' not in session:
        return render_template('logReg.html')
    else:
        return redirect('/dashboard/')

@app.route('/register/', methods=['post'])
def register():
    isValid = User.validate(request.form)
    if not isValid:
        return redirect('/')
    else:
        newUser = {
            'firstName': request.form['firstName'],
            'lastName': request.form['lastName'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(newUser)
        if not id:
            flash('Something went wrong')
            return redirect('/')
        else:
            session['user_id'] = id
            flash("You are now logged in")
            return redirect('/dashboard/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data) # check if the email is in the database
    if not user: # if not let them know
        flash('That email is not in our database please register')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Wrong password')
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash("You are now logged in")
        return redirect('/dashboard/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')


@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        thePets = User.ownerPets(data)
        theClasses = User.ownerPetClasses(data)
        theUser = User.getOne(data)
        if theUser.access == '9':
            print(theUser.access)
            return redirect('/trainers/')
        if theUser.id == 1:
            if theUser.access == '9':
                print(theUser.access)
                return redirect('/trainers/')
            else:
                print(theUser.access)
                User.makeEmployee(data)
                print(theUser.access)
                flash("User access updated to Employee")
                return redirect('/trainers/')
        else:
            print(theUser.access)
            return render_template('customer/dashboard.html', user=theUser, pets=thePets, classes=theClasses)

@app.route('/users/')
def users():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theUsers = User.getAll()
        return render_template('employee/users.html', user=theUser, users=theUsers)

@app.route('/user/<int:user_id>/makeCustomer/', methods=['post'])
def makeCustomer(user_id):
    data = {
        'id': user_id
    }
    User.makeCustomer(data)
    flash("You are a customer")
    return redirect('/users/')

@app.route('/user/<int:user_id>/makeEmployee/', methods=['post'])
def makeEmployee(user_id):
    data = {
        'id': user_id
    }
    User.makeEmployee(data)
    flash("You are a Employee")
    return redirect('/users/')