from dataclasses import dataclass
from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt

from flask_app.models.order import Order

bcrypt = Bcrypt(app)

@app.route('/')
def read():
    theOrders = Order.getAll()
    print(theOrders)
    return render_template('index.html', orders = theOrders)

@app.route('/new')
def new():
    return render_template('new_order.html')

@app.route('/create_new', methods = ['POST'])
def createNew():
    isValid = Order.validate(request.form)
    if not isValid:
        return redirect('/new')
    else:
        data = {
            'customerName' : request.form['customerName'],
            'cookie' : request.form['cookie'],
            'num_boxes' : request.form['num_boxes'],
        }
        Order.save(data)
        print('saved order', data)
        return redirect('/')


@app.route('/order/<int:order_id>/edit/')
def editOrder(order_id):
    data = {
        'id' : order_id
    }
    return render_template('edit_order.html', order=Order.getOne(data))

@app.route('/order/<int:order_id>/update', methods=['POST'])
def updateOrder(order_id):
    isValid = Order.validate(request.form)
    if not isValid:
        return redirect(f'/order/{order_id}/edit/')
    else:
        data = {
            'id' : order_id,
            'customerName' : request.form['customerName'],
            'cookie' : request.form['cookie'],
            'num_boxes' : request.form['num_boxes']
        }
        Order.update(data)
        print('Updated Order', data)
        return redirect('/')
