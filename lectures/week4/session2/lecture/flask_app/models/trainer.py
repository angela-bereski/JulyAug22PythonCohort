from flask_app.config.mysqlconnection import connectToMySQL


class Trainer:
    db = 'pet_training'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.bio = data['bio']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM trainer;"
        results = connectToMySQL(cls.db).query_db(query)
        trainers = []
        for row in results:
            trainers.append(cls(row))
        return trainers

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM trainer WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO trainer (firstName, lastName, bio) VALUES (%(firstName)s, %(lastName)s, %(bio)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE trainer SET firstName=%(firstName)s, lastName=%(lastName)s, bio=%(bio)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM trainer WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def trainerCohorts(cls, data):
        # This will be our join statement between trainer and cohort
        pass