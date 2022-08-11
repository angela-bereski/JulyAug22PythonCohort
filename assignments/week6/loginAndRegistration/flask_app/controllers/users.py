from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('dashboard.html', user=theUser)

@app.route('/register/', methods= ['POST'])
def register():
    isValid = User.validate(request.form)
    if not isValid:
        return redirect('/')
    else:
        data = {
            'firstName' : request.form['firstName'],
            'lastName' : request.form['lastName'],
            'email' : request.form['email'],
            'password' : bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(data)
        if not id:
            flash('Something is wrong!')
            return redirect('/')
        else:
            session['user_id'] = id
            flash('You logged in!')
            return redirect('/dashboard/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data)
    if not user:
        flash('That email is not in the database. Please register.')
        redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Wrong password.')
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash('Welcome back!')
        return redirect('/dashboard/')

@app.route('/logout/')
def logout():
    session.clear()
    flash('See you next time!')
    return redirect('/')