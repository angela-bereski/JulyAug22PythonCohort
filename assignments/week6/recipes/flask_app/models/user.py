from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask_app.models import recipe

class User:
    db = 'recipes'
    def __init__(self,data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.recipes = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM user;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM user WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def getEmail(cls, data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email, password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE user SET firstName=%(firstName)s, lastName=%(lastName)s, email=%(email)s, password=%(password)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)


    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM user WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate(user):
        isValid = True
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            isValid = False
            flash('Email is already in use in our database.')
        if len(user['firstName']) < 2:
            isValid = False
            flash('First name must be at least 2 characters.')
        if len(user['lastName']) < 2:
            isValid = False
            flash('Last name must be at least 2 characters.')
        if len(user['password']) < 6:
            isValid = False
            flash('Password must be at least 6 characters.')
        if not EMAIL_REGEX.match(user['email']):
            isValid = False
            flash('Please use proper email format.')
        if user['password'] != user['confirm']:
            isValid = False
            flash("Passwords don't match.")
        return isValid

    @classmethod
    def userRecipes(cls, data):
        query = 'SELECT * FROM user LEFT JOIN recipe ON user.id = recipe.user_id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        users = cls(results[0])
        for row in results:
            recipeData = {
                'id' : row['recipe.id'],
                'name' : row['name'],
                'description' : row['description'],
                'instruction' : row['instruction'],
                'cookTime' : row['cookTime'],
                'dayDate' : row['dayDate'],
                'createdAt' : row['recipe.createdAt'],
                'updatedAt' : row['recipe.updatedAt'],
                'user_id' : row['user_id']
            }
            users.recipes.append(recipe.Recipe(recipeData))
        print(users.recipes)
        return users

