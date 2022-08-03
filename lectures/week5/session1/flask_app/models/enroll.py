from flask_app.config.mysqlconnection import connectToMySQL

class Enroll:
    db = 'pet_training'
    def __init__(self, data):
        self.id = data['id']
        self.startDate = data['startDate']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.pet_id = data['pet_id']
        self.cohort_id = data['cohort_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM enroll;'
        results = connectToMySQL(cls.db).query_db(query)
        enrolls = []
        for row in results:
            enrolls.append(cls(row))
        return enrolls

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM enroll WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO enroll (startDate, pet_id, cohort_id) VALUES (%(startDate)s, %(pet_id)s, %(cohort_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE enroll SET startDate=%(startDate)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM enroll WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def cohortPets(cls, data):
        # join statement showing all the pets in the cohort
        return