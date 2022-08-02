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
    if 'secretNum' in session:
        session['num']=request.form['num']
        for i in range(0,random.randint):
            if i > random.randint:
                print("Too high!")
            elif i < random.randint:
                print("Too low!")
            else:
                print("That was the number!")


        










if __name__ == '__main__':
    app.run(debug=True)