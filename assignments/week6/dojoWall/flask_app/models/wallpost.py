from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Wallpost:
    db = 'dojo_wall'
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM wallpost;'
        results = connectToMySQL(cls.db).query_db(query)
        wallposts = []
        for row in results:
            wallposts.append(cls(row))
        return wallposts
    
    @classmethod
    def getOne(cls, data):
        pass

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO wallpost (content, user_id) VALUES ( %(content)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM wallpost WHERE wallpost.id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def validate(wallpost):
        isValid = True
        if len(wallpost['content']) < 1:
            isValid = False
            flash('Content cannot be left blank.')
        return isValid

    