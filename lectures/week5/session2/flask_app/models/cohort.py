from flask_app.config.mysqlconnection import connectToMySQL

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
        return