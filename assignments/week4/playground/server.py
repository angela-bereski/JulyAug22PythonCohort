from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/play')
def index():
    return render_template("index.html")


@app.route('/play/<int:x>')
def addBox(x):
    for i in range(0,x):
        
        
@app.route('/repeat/<int:num>/<word>')
def repeatWord(num, word):
    webWord = ''
    for i in range(0,num):
        webWord += f"<p>{word}</p>"
        print(webWord)
    return webWord


if __name__ == '__main__':
    app.run(debug=True)