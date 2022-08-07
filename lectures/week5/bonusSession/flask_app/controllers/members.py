from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.member import Member


@app.route('/members/')
def members():
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        theMembers = Member.getAll()
        return render_template('allMembers.html', user=theUser, members=theMembers)

@app.route('/addMember/')
def addMember():
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        return render_template('addMember.html', user=theUser)

@app.route('/createMember/', methods=['post'])
def createMember():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'listName': request.form['listName']
    }
    Member.save(data)
    return redirect('/members/')

@app.route('/member/<int:member_id>/view/')
def viewMember(member_id):
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        data = {
            'id': member_id
        }
        theMember = Member.getOne(data)
        theIdeas = Member.memberIdeas(data)
        # theIdeas is the join statement on the Member class that has all 1 members created Ideas
        return render_template('viewMember.html', user=theUser, member=theMember, theList=theIdeas)

@app.route('/member/<int:member_id>/edit/')
def editMember(member_id):
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
        data = {
            'id': member_id
        }
        theMember = Member.getOne(data)
        return render_template('editMember.html', user=theUser, member=theMember)

@app.route('/member/<int:member_id>/update/', methods=['post'])
def updateMember(member_id):
    data = {
        'id': member_id,
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'listName': request.form['listName']
    }
    Member.update(data)
    return redirect(f'/member/{member_id}/view/')

@app.route('/member/<int:member_id>/delete/')
def deleteMember(member_id):
    data = {
        'id': member_id
    }
    Member.delete(data)
    return redirect('/members/')