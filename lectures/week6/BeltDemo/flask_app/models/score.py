from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Scores:
    db = 'baseball'
    def __init__(self,data):
        self.id = data['id']
        self.teamOne = data['teamOne']
        self.teamTwo = data['teamTwo']
        self.finalScore = data['finalScore']
        self.info = data['info']
        self.gameDate = data['gameDate']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM scores;'
        results = connectToMySQL(cls.db).query_db(query)
        games = []
        for row in results:
            games.append(cls(row))
        return games

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM scores WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO scores (teamOne, teamTwo, finalScore, info, gameDate, user_id) VALUES (%(teamOne)s, %(teamTwo)s, %(finalScore)s, %(info)s, %(gameDate)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE scores SET teamOne=%(teamOne)s, teamTwo=%(teamTwo)s, finalScore=%(finalScore)s, info=%(info)s, gameDate=%(gameDate)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM scores WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def gameUser(cls, data):
        query = 'SELECT * FROM scores LEFT JOIN user ON scores.user_id = user.id WHERE scores.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print('gameuser results', results)
        allScores = []
        for row in results:
            game = cls(results[0])
            userData = {
                'id': row['user.id'],
                'firstName': row['firstName'],
                'lastName': row['lastName'],
                'email': row['email'],
                'password': row['password'],
                'createdAt': row['user.createdAt'],
                'updatedAt': row['user.updatedAt']
            }
            print('userdata model', userData)
            oneUser = user.User(userData)
            game.user = oneUser
            allScores.append(game)
            print('allscores', allScores)
        return allScores