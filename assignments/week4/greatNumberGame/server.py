from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secret numbers make the best games'

@app.route('/')
def index():
    random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess')
def guess():
    if input > random.int:
        print("Too high!")
    elif input < random.int:
        print("Too low!")
    elif input == random.randint:
        print("You got it!")










if __name__ == '__main__':
    app.run(debug=True)