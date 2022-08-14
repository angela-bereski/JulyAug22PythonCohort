from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import pet
from flask_app.models import enroll

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
        self.enroll = None
        self.pet = None

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
        query = 'SELECT * FROM  cohort LEFT JOIN enroll on cohort.id = enroll.cohort_id LEFT JOIN pet on enroll.pet_id = pet.id WHERE cohort.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print('cohortPets results:', results)
        thePets = []
        for row in results:
            cohort = cls(results[0])
            enrollData = {
                'id': row['enroll.id'],
                'startDate': row['startDate'],
                'pet_id': row['pet_id'],
                'cohort_id': row['cohort_id'],
                'createdAt': row['enroll.createdAt'],
                'updatedAt': row['enroll.updatedAt']
            }
            oneEnroll = enroll.Enroll(enrollData)
            cohort.enroll = oneEnroll
            petData = {
                'id': row['pet.id'],
                'name': row['pet.name'],
                'age': row['age'],
                'breed': row['breed'],
                'createdAt': row['pet.createdAt'],
                'updatedAt': row['pet.updatedAt'],
                'user_id': row['user_id']
            }
            onePet = pet.Pet(petData)
            cohort.pet = onePet
            thePets.append(cohort)
        return thePets