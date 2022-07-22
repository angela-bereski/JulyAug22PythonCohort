from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello class"

@app.route('/honeybee')
def honeyBee():
        return "Melissa in Greek means HoneyBee"









if __name__ == '__main__':
    app.run(debug=True)