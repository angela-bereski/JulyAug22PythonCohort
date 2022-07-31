from operator import methodcaller
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secrets dont make friends'

@app.route('/')
def index():
    if 'num' in session:
        session['num'] += 1
    else:
        session['num'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroySession():
    session.clear()
    return redirect('/')

@app.route('/plus2')
def plusTwo():
    session['num'] += 2
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)