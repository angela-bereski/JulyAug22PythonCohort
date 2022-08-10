# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'users_schema'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users_schema').query_db( query, data )
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate(users):
        isValid = True
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(User.db).query_db(query, users)
        if len(results) >= 1:
            isValid = False
            flash('Email is already in use in our database.')
        if len(users['first_name']) < 2:
            isValid = False
            flash('Please use at least 2 characters for first name.')
        if len(users['last_name']) < 2:
            isValid = False
            flash('Please use at least 2 characters for last name.')
        if len(users['password']) < 6:
            isValid = False
            flash('Please use at least 6 characters for the password.')
        if not EMAIL_REGEX.match(users['email']):
            isValid = False
            flash('Please use proper email format.')
        if users['password'] != users['confirm']:
            isValid = False
            flash('Passwords do not match.')
        return isValid