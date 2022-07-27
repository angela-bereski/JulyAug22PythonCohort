from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/play')
def index():
    return render_template("index.html", color= "#6dc2ef", num=3)

@app.route('/play/<int:x>')
def addBox(x):
    for i in range(0,x):
        return render_template("index.html", color= "#6dc2ef", num=x)
        
@app.route('/play/<int:x>/<string:color>')
def changeColor(x,color):
    for i in range(0,x):
        return render_template("index.html", color=color, num=x)


if __name__ == '__main__':
    app.run(debug=True)