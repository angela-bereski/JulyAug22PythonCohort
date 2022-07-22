from flask import Flask, render_template
from data import trainingSchool


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello class"

# @app.route('/honeybee')
# def honeyBee():
#     return "Melissa in Greek means HoneyBee"

@app.route('/honeybee')
def honeyBee():
    return render_template('index.html')

@app.route('/school')
def school():
    return render_template('school.html', cohorts=trainingSchool)







if __name__ == '__main__':
    app.run(debug=True)