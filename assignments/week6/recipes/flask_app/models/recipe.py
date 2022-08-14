from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import user

class Recipe:
    db = 'recipes'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.cookTime = data['cookTime']
        self.dayDate = data['dayDate']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.users = []
    
    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM recipe;'
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes
    
    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM recipe WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO recipe (name, description, instruction, cookTime, dayDate, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(cookTime)s, %(dayDate)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE recipe SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, user_id=%(user_id)s, cookTime=%(cookTime)s, dayDate=%(dayDate)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)


    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM recipe WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate(recipe):
        isValid = True
        if len(recipe['name']) < 1:
            isValid = False
            flash('Name cannot be left blank.')
        if len(recipe['description']) < 1:
            isValid = False
            flash('Description cannot be left blank.')
        if len(recipe['instruction']) < 1:
            isValid = False
            flash('Instructions cannot be left blank.')
        return isValid
    
    @classmethod
    def recipeUsers(cls, data):
        query = 'SELECT * FROM recipe JOIN user ON recipe.id = user.recipe_id WHERE recipe.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        recipes = cls(results[0])
        for row in results:
            userData = {
                'id' : row['user.id'],
                'firstName' : row['firstName'],
                'lastName' : row['lastName'],
                'email' : row['email'],
                'password' : row['password'],
            }
            recipes.users.append(user.User(userData))
        print(recipes.users)
        return recipes