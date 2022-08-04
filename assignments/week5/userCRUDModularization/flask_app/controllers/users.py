from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.user import User


@app.route('/')
def read():
    theUsers = User.get_all()
    print(theUsers)
    return render_template('index.html', users = theUsers)

@app.route('/new')
def new():
    return render_template('addNew.html')

@app.route('/create_new', methods=["POST"])
def create_new():

    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    User.save(data)
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