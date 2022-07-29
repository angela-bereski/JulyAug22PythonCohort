from flask import Flask, render_template, redirect, session, request
from data import trainingSchool
from env import KEY

app = Flask(__name__)
app.secret_key = KEY


@app.route('/')
def index():
    if 'user' not in session:
        print("No user in session")
        return render_template('logReg.html')
    else:
        theUser = session['user']
        print(theUser)
        return render_template('index.html', cohorts=trainingSchool, user=theUser)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/createUser', methods=['post'])
def createUser():
    session['user'] = request.form['fullName']
    return redirect('/')

@app.route('/cohort/<int:cohort_id>/view')
def viewCohort(cohort_id):
    if 'user' not in session:
        return render_template('logReg.html')
    else:
        print(trainingSchool[cohort_id-1])
        return render_template('viewCohort.html', cohort=trainingSchool[cohort_id-1])







if __name__ == '__main__':
    app.run(debug=True)