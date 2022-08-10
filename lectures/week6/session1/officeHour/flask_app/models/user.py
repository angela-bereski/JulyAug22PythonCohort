from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'comments_notes'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    def fullName(self):
        return f'{self.firstName} {self.lastName}'

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
        pass

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email) VALUES (%(firstName)s, %(lastName)s, %(email)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass