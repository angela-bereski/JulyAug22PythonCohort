from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app.models import pet
from flask_app.models import enroll
from flask_app.models import cohort
from flask_app.models import trainer



class User:
    db = 'pet_training'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.access = data['access']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.pets = []
        self.pet = None
        self.enroll = None
        self.cohort = None
        self.trainer = None

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
        query = 'SELECT * FROM user WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getEmail(cls, data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email, password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def makeEmployee(cls, data):
        query = 'UPDATE user SET access=9 WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def makeCustomer(cls, data):
        query = 'UPDATE user SET access=1 WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE user SET firstName=%(firstName)s, lastName=%(lastName)s, email=%(email)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM user WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def ownerPets(cls, data):
        # join statement to show all the user/owners pets
        query = "SELECT * FROM user LEFT JOIN pet on user.id = pet.user_id WHERE user.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0])
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
            user.pets.append(pet.Pet(petData))
        return user

    @classmethod
    def ownerPetClasses(cls, data):
        # join statement to show all the classes the user/owners pets are enrolled in
        query = 'SELECT * FROM user LEFT JOIN pet on user.id = pet.user_id LEFT JOIN enroll on pet.id = enroll.pet_id LEFT JOIN cohort on enroll.cohort_id = cohort.id LEFT JOIN trainer on cohort.trainer_id = trainer.id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        allClasses = []
        for row in results:
            user = cls(results[0])
            petData = {
                'id': row['pet.id'],
                'name': row['name'],
                'age': row['age'],
                'breed': row['breed'],
                'createdAt': row['pet.createdAt'],
                'updatedAt': row['pet.updatedAt'],
                'user_id': row['user_id']
            }
            onePet = pet.Pet(petData)
            user.pet = onePet
            enrollData = {
                'id': row['enroll.id'],
                'startDate': row['startDate'],
                'pet_id': row['pet_id'],
                'cohort_id': row['cohort_id'],
                'createdAt': row['enroll.createdAt'],
                'updatedAt': row['enroll.updatedAt']
            }
            oneEnroll = enroll.Enroll(enrollData)
            user.enroll = oneEnroll
            cohortData = {
                'id': row['cohort.id'],
                'name': row['cohort.name'],
                'topic': row['topic'],
                'length': row['length'],
                'createdAt': row['cohort.createdAt'],
                'updatedAt': row['cohort.updatedAt'],
                'trainer_id': row['trainer_id']
            }
            oneCohort = cohort.Cohort(cohortData)
            user.cohort = oneCohort
            trainerData = {
                'id': row['trainer.id'],
                'firstName': row['trainer.firstName'],
                'lastName': row['trainer.lastName'],
                'bio': row['bio'],
                'createdAt': row['pet.createdAt'],
                'updatedAt': row['pet.updatedAt'],
                'user_id': row['trainer.user_id']
            }
            oneTrainer = trainer.Trainer(trainerData)
            user.trainer = oneTrainer
            allClasses.append(user)
        return allClasses


    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @staticmethod
    def validate(user):
        isValid = True
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            isValid = False
            flash("That email is already in our system")
        if not EMAIL_REGEX.match(user['email']):
            isValid = False
            flash("Invalid Email format")
        if len(user['firstName']) < 2:
            isValid = False
            flash("First Name must have at least 2 characters")
        if len(user['lastName']) < 2:
            isValid = False
            flash("Last Name must have at least 2 characters")
        if len(user['password']) < 8:
            isValid = False
            flash("Password must have at least 8 characters")
        if user['password'] != user['confirm']:
            isValid = False
            flash("Passwords are not matching")
        return isValid