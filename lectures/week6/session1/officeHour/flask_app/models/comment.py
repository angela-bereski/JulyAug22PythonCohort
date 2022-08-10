from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Comment:
    db = 'comments_notes'
    def __init__(self, data):
        self.id = data['id']
        self.comment = data['comment']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.receiver = data['receiver']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM comment;'
        results = connectToMySQL(cls.db).query_db(query)
        comments = []
        for row in results:
            comments.append(cls(row))
        return comments

    @classmethod
    def getOne(cls, data):
        pass

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO comment (comment, user_id, receiver) VALUES (%(comment)s, %(user_id)s, %(receiver)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass

    # @classmethod
    # def allComments(cls):
    #     query = 'SELECT * FROM comment LEFT JOIN user ON comment.user_id = user.id;'
    #     results = connectToMySQL(cls.db).query_db(query)
    #     print("model all Comments results", results)
    #     allComments = []
    #     for row in results:
    #         userData = {
    #             'id': row['user.id'],
    #             'firstName': row['firstName'],
    #             'lastName': row['lastName'],
    #             'createdAt': row['user.createdAt'],
    #             'updatedAt': row['user.updatedAt']
    #         }
