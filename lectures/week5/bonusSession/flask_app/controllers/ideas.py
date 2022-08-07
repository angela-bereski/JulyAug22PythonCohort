from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.idea import Idea
from flask_app.models.member import Member

@app.route('/ideas/')
def ideas():
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        theIdeas = Idea.getAll()
        theMembers = Member.getAll()
        return render_template('allIdeas.html', user=theUser, ideas=theIdeas, members=theMembers)

@app.route('/addIdea/')
def addIdea():
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        theMembers = Member.getAll()
        return render_template('addIdea.html', user=theUser, members=theMembers)

@app.route('/createIdea/', methods=['post'])
def createIdea():
    data = {
        'ideaName': request.form['ideaName'],
        'info': request.form['info'],
        'member_id': request.form['member_id']
    }
    Idea.save(data)
    return redirect('/ideas/')

@app.route('/idea/<int:idea_id>/view/')
def viewIdea(idea_id):
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        data = {
            'id': idea_id
        }
        theIdea = Idea.getOne(data)
        return render_template('viewIdea.html', user=theUser, idea=theIdea)

@app.route('/idea/<int:idea_id>/edit/')
def editIdea(idea_id):
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        data = {
            'id': idea_id
        }
        theIdea = Idea.getOne(data)
        return render_template('editIdea.html', user=theUser, idea=theIdea)

@app.route('/idea/<int:idea_id>/update/', methods=['post'])
def updateIdea(idea_id):
    data = {
        'id': idea_id,
        'ideaName': request.form['ideaName'],
        'info': request.form['info']
    }
    Idea.update(data)
    return redirect(f'/idea/{idea_id}/view/')

@app.route('/idea/<int:idea_id>/delete/')
def deleteIdea(idea_id):
    data = {
        'id': idea_id
    }
    Idea.delete(data)
    return redirect('/idea/')