from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Joke:
    db = 'jokes'
    def __init__(self, data):
        self.id = data['id']
        self.question = data['question']
        self.punchline = data['punchline']
        self.user_id = data['user_id']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']


    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM joke;'
        results = connectToMySQL(cls.db).query_db(query)
        jokes = []
        for row in results:
            jokes.append(cls(row))
        return jokes

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM joke WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO joke (question, punchline, user_id) VALUES (%(question)s, %(punchline)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM joke WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)