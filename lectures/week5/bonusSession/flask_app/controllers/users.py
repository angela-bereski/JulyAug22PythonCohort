from flask_app import app
from flask import render_template, redirect, session, request

# All app.routes that have a method of post will ALWAYS and FOREVER be a redirect
# If the function will be loading a new page on activation it is a render_template


@app.route('/')
def index():
    if 'user' not in session:
        return render_template('index.html')
    else:
        return redirect('/members/')

@app.route('/logReg/', methods=['post'])
def logReg():
    session['user'] = request.form['fullName']
    return redirect('/members/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')