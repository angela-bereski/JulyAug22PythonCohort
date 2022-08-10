from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def read():
    if 'user_id' not in session:
        return redirect('/new')
    else:
        theUsers = User.get_all()
        print(theUsers)
        return render_template('index.html', users = theUsers)

@app.route('/new')
def new():
    return render_template('addNew.html')

@app.route('/create_new', methods=["POST"])
def create_new():
    isValid = User.validate(request.form)
    if not isValid:
        return redirect('/new')
    else:
        data = {
            "first_name": request.form["first_name"],
            "last_name" : request.form["last_name"],
            "email" : request.form["email"],
            "password" : bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(data)
        if not id:
            flash('Something got messed up someplace')
        else:
            session['user_id'] = id
            flash('You logged in!')
            return redirect('/')

@app.route('/user/<int:user_id>/view/')
def viewUser(user_id):
    data = {
        'id': user_id
    }
    theUser = User.getOne(data)
    return render_template('viewUser.html', user=theUser)


@app.route('/user/<int:user_id>/edit/')
def editUser(user_id):
    data = {
        'id': user_id
    }
    return render_template('editUser.html', user=User.getOne(data))

@app.route('/user/<int:user_id>/update/', methods=['post'])
def updateUser(user_id):
    data = {
        "id": user_id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.update(data)
    print("updated user controller:", data)
    return redirect(f'/user/{user_id}/view')

@app.route('/user/<int:user_id>/delete/')
def deleteUser(user_id):
    data = {
        'id': user_id
    }
    User.delete(data)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    flash("See Ya!")
    return redirect('/new')