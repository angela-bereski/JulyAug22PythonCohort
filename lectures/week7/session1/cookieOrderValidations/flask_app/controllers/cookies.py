from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.models.cookie import Cookie

@app.route('/')
def index():
    theCookies = Cookie.getAll()
    return render_template('index.html', cookies=theCookies)

@app.route('/addOrder/')
def addOrder():
    return render_template('addOrder.html')

@app.route('/createOrder/', methods=['post'])
def createOrder():
    isValid = Cookie.validate(request.form)
    if not isValid:
        return redirect('/addOrder/')
    data = {
        'name': request.form['name'],
        'type': request.form['type'],
        'number': request.form['number']
    }
    Cookie.save(data)
    return redirect('/')