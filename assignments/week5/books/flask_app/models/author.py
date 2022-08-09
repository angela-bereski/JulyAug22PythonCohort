from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    db = 'books_authors'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.createdAt= data['createdAt']
        self.updatedAt= data['updatedAt']
        self.book = []

    @classmethod
    def getAll(cls):
        query= 'SELECT * FROM author;'
        results= connectToMySQL(cls.db).query_db(query)
        author = []
        for row in results:
            author.append(cls(row))
        return author
    
    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM author WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def save (cls, data):
        query = 'INSERT INTO author (name, createdAt, updatedAt) VALUES (%(name)s, NOW(), NOW() );'
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls, data):
        query = 'INSERT INTO author SET name = %(name)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM author WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def authorBooks(cls,data):
        query = 'SELECT * FROM author LEFT JOIN favorite ON favorite.author_id=author.id LEFT JOIN book ON favorite.book_id=book.id WHERE author.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        author = cls(results[0])
        for row in results:
            bookData = {
                'id' : row['book.id'],
                'title' : row['title'],
                'num_pages' : row['num_pages'],
                'createdAt' : row['book.createdAt'],
                'updatedAt' : row['book.updatedAt']
            }
            author.book.append(book.Book(bookData))
        return author