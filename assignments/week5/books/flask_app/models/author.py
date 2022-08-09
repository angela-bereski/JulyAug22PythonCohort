from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    db = 'books_authors'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.createdAt= data['createdAt']
        self.updatedAt= data['updatedAt']
        self.book_faves = []


    @classmethod
    def getAll(cls):
        query= 'SELECT * FROM author;'
        results= connectToMySQL(cls.db).query_db(query)
        authors = []
        for row in results:
            authors.append(cls(row))
        return authors
    
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
    def bookFaves(cls,data):
        query = 'SELECT * FROM author LEFT JOIN favorite ON author.id=favorite.author_id LEFT JOIN book ON book.id=favorite.book_id WHERE author.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        author = cls(results[0])
        print(results)
        for row in results:
            if row['book.id'] == None:
                break
            bookData = {
                'id' : row['book.id'],
                'title' : row['title'],
                'num_pages' : row['num_pages'],
                'createdAt' : row['book.createdAt'],
                'updatedAt' : row['book.updatedAt']
            }
            author.book_faves.append(book.Book(bookData))
        return author
    
    @classmethod
    def addFave(cls, data):
        query = 'INSERT INTO favorite (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)