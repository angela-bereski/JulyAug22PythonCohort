from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_ninjas"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojo = []
        for row in results:
            dojo.append(cls(row))
        return dojo
    
    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW() );'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE dojos SET name=%(name)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM dojos WHERE id= %(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def dojoNinjas(cls, data):
        # Left join our cohorts to our trainer
        # 1 trainer to multiple cohorts
        # create empty list in constructor to store all the cohorts that are queried
        # return the list of cohorts with the trainer information attached
        # start with the one join the many connect on the one then the many
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            ninjaData = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age' : row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id' : row['dojo_id']
            }
            # self.cohorts (the list is = trainer.cohort)
            # take the current trainer information append to it inside the list and instance of the trainer info plus this row's cohort info
            # cohort.Cohort(cohortData) = file.Class(current row data)
            dojo.ninjas.append(ninja.Ninja(ninjaData))
        print(dojo.ninjas)
        return dojo