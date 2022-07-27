from flask import Flask, render_template, redirect, session, request
from data import trainingSchool

app = Flask(__name__)
app.secret_key = "My internet company is killing"

@app.route('/')
def index():
    return render_template('index.html')

# This will be a hidden route and there for use redirect
@app.route('/createUser', methods=['post'])
def createUser():
    session['name'] = request.form['name']
    return redirect('/cohorts')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/cohorts')
def cohorts():
    if 'name' not in session:
        return redirect('/')
    else:
        theUser = session['name']
        return render_template('cohorts.html', cohorts=trainingSchool, user = theUser)
    # cohorts = trainingSchool means the html will use the word cohorts to reference the data that is called trainingSchool

@app.route('/cohort/<int:cohort_id>/view')
def viewCohort(cohort_id):
    if 'name' not in session:
        return redirect('/')
    else:
        theUser = session['name']
        print(trainingSchool[cohort_id-1])
        return render_template('viewCohort.html', cohort=trainingSchool[cohort_id-1], user = theUser)




if __name__ == '__main__':
    app.run(debug=True)