from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

bcrypt = Bcrypt(app)

@app.route('/addRecipe/')
def addRecipe():
    if 'user_id' not in session:
        return redirect('/')
    else: 
        return render_template('addRecipe.html')

@app.route('/createRecipe/', methods=['POST'])
def createRecipe():
    isValid = Recipe.validate(request.form)
    if not isValid:
        return redirect('/addRecipe/')
    else:
        data = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'instruction' : request.form['instruction'],
            'dayDate' : request.form['dayDate'],
            'cookTime' : request.form['cookTime'],
            'user_id': session['user_id']
        }
        Recipe.save(data)

        return redirect('/dashboard/')
        
@app.route('/recipe/view/<int:id>/')
def viewRecipe(id):
    if 'user_id' not in session:
        return redirect('/')
    else: 
        userData = {
            'id' : session['user_id']
        }
        theUser=User.getOne(userData)
        data = {
            'id' : id
        }
        theRecipe = Recipe.getOne(data)
        theUsers = User.getAll()
        theRecipes = Recipe.getAll()
        return render_template('viewRecipe.html', recipe=theRecipe, user=theUser, users=theUsers, recipes=theRecipes)

@app.route('/recipe/edit/<int:id>/')
def editRecipe(id):
    if 'user_id' not in session:
        return redirect('/')
    else: 
        userData = {
            'id' : session['user_id']
        }
        theUser=User.getOne(userData)
        data = {
            'id' : id
        }
        theRecipe = Recipe.getOne(data)

        return render_template('editRecipe.html', recipe=theRecipe, user=theUser)

@app.route('/recipe/update/<int:id>/', methods=['POST'])    
def updateRecipe(id):
    isValid = Recipe.validate(request.form)
    if not isValid:
        return redirect(f'/recipe/edit/{id}')
    else:
        data = {
            'id' : request.form['id'],
            'name' : request.form['name'], 
            'description' : request.form['description'],
            'instruction' : request.form['instruction'],
            'dayDate' : request.form['dayDate'],
            'cookTime' : request.form['cookTime'],
            'user_id' : request.form['user_id']
        }
        Recipe.update(data)
        print('updated Recipe:', data, id)
        return redirect('/dashboard/')

@app.route('/recipe/delete/<int:id>/')
def deleteRecipe(id):
    data = {
        'id' : id
    }
    Recipe.delete(data)
    return redirect ('/dashboard/')