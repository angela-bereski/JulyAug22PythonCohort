from crypt import methods
from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite

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
    theAuthors=Author.bookFaves(data)
    theBooks=Book.getAll()
    print(theAuthors)
    return render_template('author_faves.html', author=theAuthors, books=theBooks)

@app.route('/authorFave', methods=['POST'])
def authorFaves():
    data = {
        'book_id' : request.form['book_id'],
        'author_id' : request.form['author_id']
    }
    
    Author.addFave(data)
    return redirect(f"/authors/{request.form['author_id']}/view")


