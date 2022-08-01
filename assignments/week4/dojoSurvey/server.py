from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret pizza'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def createUser():
    session['name']=request.form['name']
    session['dojo']=request.form['dojo']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    return redirect('/results')

@app.route('/results')
def showResults():
    return render_template('results.html')






if __name__ == '__main__':
    app.run(debug=True)