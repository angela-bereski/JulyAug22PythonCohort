from flask import Flask, render_template, request, redirect, session # added request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")

@app.route('/show/')
def show_user():
    return render_template('show.html')



if __name__ == "__main__":
    app.run(debug=True)