from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import cohort

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
        self.cohorts = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM trainer;'
        results = connectToMySQL(cls.db).query_db(query)
        trainers = []
        for row in results:
            trainers.append(cls(row))
        return trainers

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM trainer WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO trainer (firstName, lastName, bio, user_id) VALUES (%(firstName)s, %(lastName)s, %(bio)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE trainer SET firstName=%(firstName)s, lastName=%(lastName)s, bio=%(bio)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM trainer WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def trainerCohorts(cls, data):
        # Left join our cohorts to our trainer
        # 1 trainer to multiple cohorts
        # create empty list in constructor to store all the cohorts that are queried
        # return the list of cohorts with the trainer information attached
        # start with the one join the many connect on the one then the many
        query = 'SELECT * FROM trainer LEFT JOIN cohort ON trainer.id = cohort.trainer_id WHERE trainer.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        trainer = cls(results[0])
        for row in results:
            cohortData = {
                'id': row['cohort.id'],
                'name': row['name'],
                'topic': row['topic'],
                'length': row['length'],
                'createdAt': row['cohort.createdAt'],
                'updatedAt': row['cohort.updatedAt'],
                'trainer_id': row['trainer_id']
            }
            # self.cohorts (the list is = trainer.cohort)
            # take the current trainer information append to it inside the list and instance of the trainer info plus this row's cohort info
            # cohort.Cohort(cohortData) = file.Class(current row data)
            trainer.cohorts.append(cohort.Cohort(cohortData))
        return trainer

    def fullName(self):
        return f'{self.firstName} {self.lastName}'