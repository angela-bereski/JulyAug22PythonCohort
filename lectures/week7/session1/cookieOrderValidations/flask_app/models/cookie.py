from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Cookie:
    db = 'cookies'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.number = data['number']
        self.createdAt = data['createdAt']
        self.updatedAT = data['updatedAT']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM cookie;'
        results = connectToMySQL(cls.db).query_db(query)
        cookies = []
        for row in results:
            cookies.append(cls(row))
        return cookies

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM cookie WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = 'INSERT INTO cookie (name, type, number) VALUES (%(name)s, %(type)s, %(number)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE cookie SET name=%(name)s, type=%(type)s, number=%(number) WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM cookie WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate(cookie):
        isValid = True
        if len(cookie['name']) < 2:
            isValid = False
            flash("Please use at least 2 characters for the Cookie Name")
        if len(cookie['type']) < 2:
            isValid = False
            flash("Please use at least 2 characters for the Cookie Type")
        if int(cookie['number']) < 1: # preventing negative numbers
            isValid = False
            flash("Must be a valid number")
        return isValid