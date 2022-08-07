from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def read():
    theDojos = Dojo.getAll()
    print(theDojos)
    return render_template('index.html', dojos = theDojos)

@app.route('/dojos', methods=['POST'])
def createDojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>/view')
def showDojo(dojo_id):
    data = {
        'id' : dojo_id
    }
    theNinjas=Dojo.dojoNinjas(data)
    print(theNinjas)
    return render_template('showDojo.html', dojo=theNinjas)
