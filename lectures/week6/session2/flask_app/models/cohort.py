from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import pet

class Cohort:
    db = 'pet_training'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.topic = data['topic']
        self.length = data['length']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.trainer_id = data['trainer_id']
        self.pets = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM cohort;'
        results = connectToMySQL(cls.db).query_db(query)
        cohorts = []
        for row in results:
            cohorts.append(cls(row))
        return cohorts

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM cohort WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO cohort (name, topic, length, trainer_id) VALUES (%(name)s, %(topic)s, %(length)s, %(trainer_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE cohort SET name=%(name)s, topic=%(topic)s, length=%(length)s, trainer_id=%(trainer_id)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM cohort WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def cohortPets(cls, data):
        # join statement showing all the pets in the cohort
        query = 'SELECT * FROM  cohort LEFT JOIN pet on cohort.id = pet.cohort_id WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        cohort = cls(results[0])
        for row in results:
            petData = {
                'id': row['pet.id'],
                'name': row['name'],
                'age': row['age'],
                'breed': row['breed'],
                'createdAt': row['pet.createdAt'],
                'updatedAt': row['pet.updatedAt'],
                'user_id': row['user_id']
            }
            cohort.pets.append(pet.Pet(petData))
        return cohort