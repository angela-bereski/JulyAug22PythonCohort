from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = "dojos_ninjas"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM ninjas WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s,NOW(), NOW(), %(dojo_id)s );'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, dojo_id=%(dojo_id)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM ninjas WHERE id= %(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)

