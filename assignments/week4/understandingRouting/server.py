from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def sayHi(name):
    print(name)
    return "Hi " + name.capitalize() + "!"

@app.route('/repeat/<int:num>/<word>')
def repeatWord(num, word):
    webWord = ''
    for i in range(0,num):
        webWord += f"<p>{word}</p>"
        print(webWord)
    return webWord



if __name__ == '__main__':
    app.run(debug=True)
