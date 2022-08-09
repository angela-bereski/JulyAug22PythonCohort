from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/books')
def readBooks():
    theBooks = Book.getAll()
    print(theBooks)
    return render_template('books.html', books = theBooks)

@app.route('/more_books', methods=['POST'])
def createBook():
    data = {
        'title' : request.form['title'],
        'num_pages' : request.form['num_pages']
    }
    Book.save(data)
    return redirect('/books')

@app.route('/books/<int:book_id>/view')
def showBook(book_id):
    data = {
        'id' : book_id
    }
    theBooks=Book.favoritedBy(data)
    theAuthors=Author.getAll()
    return render_template('book_faves.html', book=theBooks, authors=theAuthors)

@app.route('/bookFave', methods=['POST'])
def bookFaves():
    data = {
        'book_id' : request.form['book_id'],
        'author_id' : request.form['author_id']
    }
    
    Book.addFave(data)
    return redirect(f"/books/{request.form['book_id']}/view")

