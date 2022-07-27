from flask import Flask, render_template
from data import trainingSchool

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', cohorts=trainingSchool)

@app.route('/cohort/<int:cohort_id>/view')
def viewCohort(cohort_id):
    print(trainingSchool[cohort_id-1])
    return render_template('viewCohort.html', cohort=trainingSchool[cohort_id-1])







if __name__ == '__main__':
    app.run(debug=True)