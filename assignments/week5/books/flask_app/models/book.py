from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    db = 'books_authors'
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_pages = data['num_pages']
        self.createdAt= data['createdAt']
        self.updatedAt= data['updatedAt']
        self.author = []

    @classmethod
    def getAll(cls):
        query= 'SELECT * FROM book;'
        results= connectToMySQL(cls.db).query_db(query)
        book = []
        for row in results:
            book.append(cls(row))
        return book
    
    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM book WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def save (cls, data):
        query = 'INSERT INTO book (title, num_pages, createdAt, updatedAt) VALUES (%(title)s, %(num_pages)s, NOW(), NOW() );'
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls, data):
        query = 'INSERT INTO book SET title = %(title)s, num_pages= %(num_pages)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM book WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def bookAuthors(cls, data):
        query = 'SELECT * FROM book LEFT JOIN favorite ON favorite.book_id=book.id LEFT JOIN author ON favorite.author_id=author.id WHERE book.id= %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        book = cls(results[0])
        for row in results:
            authorData = {
                'id' : row['author.id'],
                'name' : row['name'],
                'createdAt' : row['author.createdAt'],
                'updatedAt' : row['author.updatedAt']
            }
            book.author.append(author.Author(authorData))
        return book