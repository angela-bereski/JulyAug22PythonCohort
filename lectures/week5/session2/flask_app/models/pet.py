from flask_app.config.mysqlconnection import connectToMySQL


class Pet:
    db = 'pet_training'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.breed = data['breed']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM pet;'
        results = connectToMySQL(cls.db).query_db(query)
        pets = []
        for row in results:
            pets.append(cls(row))
        return pets

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM pet WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO pet (name, age, breed, user_id) VALUES (%(name)s, %(age)s, %(breed)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE pet SET name=%(name)s, age=%(age)s, breed=%(breed)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM pet WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)