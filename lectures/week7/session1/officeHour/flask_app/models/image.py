from flask_app.config.mysqlconnection import connectToMySQL


class Image:
    db = 'dojo_images'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.url = data['url']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM image;'
        results = connectToMySQL(cls.db).query_db(query)
        images = []
        for row in results:
            images.append(cls(row))
        return images

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM image WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO image (title, url, user_id) VALUES (%(title)s, %(url)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE image SET title=%(title)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM image WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)