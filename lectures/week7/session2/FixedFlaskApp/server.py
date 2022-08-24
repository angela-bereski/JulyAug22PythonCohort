from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "unicorns"


@app.route('/') 
def index():

    return render_template("index.html", )

@app.route('/leaderboard')
def leaderBoard():
    if 'user_name' not in session:
        return redirect('/')
    name = session['user_name']
    if 'first' not in session:
        first = ''
        second = ''
        third = ''
        return render_template("leaderboard.html", name=name, first=first, second=second, third=third)
    else:
        first = session['first']
        second = session['second']
        third = session['third']
        print("what is printing with name: ", name)
        print("why is first a key error", first)
        return render_template("leaderboard.html", name=name, first=first, second=second, third=third)



@app.route('/show/<int:rank>')
def show(rank):
    print("what is the current rank:", rank)
    if rank == 1:
        name = session['first']
    elif rank == 2:
        name = session['second']
    else:
        name = session['third']

    return render_template("showFriend.html", rank=rank, name=name)



@app.route('/enter', methods = ['POST'])
def enter():
    print(request.form)
    name = request.form["firstName"] + " " + request.form["lastName"]
    session['user_name'] = name
    return redirect('/leaderboard')



@app.route("/changeRanks", methods = ['POST'])
def changeRanks():

    first = request.form['first']
    second = request.form['second']
    third = request.form['third']
    session['first'] = first
    session['second'] = second
    session['third'] = third
    return redirect('/leaderboard')

    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)