from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', color1='pink', color2='green', row=8, column=8)

@app.route('/<int:x>')
def rows(x):
    return render_template('index.html', color1='pink', color2='green', row=x, column=8)

@app.route('/<int:x>/<int:y>')
def rowCol(x,y):
    return render_template('index.html', color1='pink', color2='green', row=x, column=y)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def changeAll(x,y, color1, color2):
    return render_template('index.html', color1=color1, color2=color2, row=x, column=y)



if __name__ == '__main__':
    app.run(debug=True)