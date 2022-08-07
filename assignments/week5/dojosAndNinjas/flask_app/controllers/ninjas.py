from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/addNinja')
def addNinja():
    theDojos=Dojo.getAll()
    return render_template('addNinja.html', dojos=theDojos)

@app.route('/createNinja', methods=['POST'])
def createNinja():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    Ninja.save(data)
    return redirect('/dojos/<int:dojo_id>/view')

@app.route('/ninja/<int:ninja_id>/edit')
def editNinja(ninja_id):
    data = {
        'id' : ninja_id
    }
    theNinja=Ninja.getOne(data)
    return render_template('editNinja.html', ninja=theNinja)

@app.route('/ninja/<int:ninja_id>/update', methods=['post'])
def updateNinja(ninja_id):
    data = {
        'id' : ninja_id,
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
    }
    Ninja.update(data)
    return redirect('/dojos/<int:dojo_id>/view')

@app.route('/ninja/<int:ninja_id>/delete')
def deleteNinja(ninja_id):
    data = {
        'id' : ninja_id
    }
    Ninja.delete(data)
    return redirect('/dojos/<int:dojo_id>/view')
