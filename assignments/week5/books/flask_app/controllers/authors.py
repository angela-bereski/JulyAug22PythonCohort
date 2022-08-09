from crypt import methods
from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def read():
    theAuthors = Author.getAll()
    print(theAuthors)
    return render_template('authors.html', authors = theAuthors)

@app.route('/authors', methods=['POST'])
def createAuthor():
    data = {
        'name' : request.form['name']
    }
    Author.save(data)
    return redirect('/')

@app.route('/authors/<int:author_id>/view')
def showAuthor(author_id):
    data = {
        'id' : author_id
    }
    theAuthors=Author.authorBooks(data)
    print(theAuthors)
    return render_template('author_faves.html', author=theAuthors)

@app.route('/authorFave', methods=['post'])
def authorFaves():
    data = {
        'book_id' : request.form['book_id']
    }
    Author.save(data)
    return redirect('/authors/<int:author_id>/view')
