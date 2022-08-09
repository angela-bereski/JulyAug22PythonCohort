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