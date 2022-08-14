from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import enroll
from flask_app.models import cohort
from flask_app.models import trainer

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
        self.enroll = None
        self.cohort = None
        self.trainer = None

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

    @classmethod
    def petCohorts(cls, data):
        query = 'SELECT * FROM pet LEFT JOIN enroll on pet.id = enroll.pet_id LEFT JOIN cohort on enroll.cohort_id = cohort.id LEFT JOIN trainer on cohort.trainer_id = trainer.id WHERE pet.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        allClasses = []
        for row in results:
            pet = cls(results[0])
            enrollData = {
                'id': row['enroll.id'],
                'startDate': row['startDate'],
                'pet_id': row['pet_id'],
                'cohort_id': row['cohort_id'],
                'createdAt': row['enroll.createdAt'],
                'updatedAt': row['enroll.updatedAt']
            }
            pet.enroll = enroll.Enroll(enrollData)
            cohortData = {
                'id': row['cohort.id'],
                'name': row['cohort.name'],
                'topic': row['topic'],
                'length': row['length'],
                'createdAt': row['cohort.createdAt'],
                'updatedAt': row['cohort.updatedAt'],
                'trainer_id': row['trainer_id']
            }
            pet.cohort = cohort.Cohort(cohortData)
            trainerData = {
                'id': row['trainer.id'],
                'firstName': row['firstName'],
                'lastName': row['lastName'],
                'bio': row['bio'],
                'createdAt': row['trainer.createdAt'],
                'updatedAt': row['trainer.updatedAt'],
                'user_id': row['trainer.user_id']
            }
            pet.trainer = trainer.Trainer(trainerData)
            allClasses.append(pet)
        return allClasses