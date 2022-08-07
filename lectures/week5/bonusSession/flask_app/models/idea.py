from flask_app.config.mysqlconnection import connectToMySQL


class Idea:
    db = 'bucket_list'
    def __init__(self, data):
        self.id = data['id']
        self.ideaName = data['ideaName']
        self.info = data['info']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.member_id = data['member_id']


    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM idea;'
        results = connectToMySQL(cls.db).query_db(query)
        ideas = []
        for row in results:
            ideas.append(cls(row))
        return ideas

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM idea WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO idea (ideaName, info, member_id) VALUES (%(ideaName)s, %(info)s, %(member_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE idea SET ideaName=%(ideaName)s, info=%(info) WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM member WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)