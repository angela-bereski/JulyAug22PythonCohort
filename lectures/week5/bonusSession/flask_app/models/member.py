from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import idea


class Member:
    db = 'bucket_list'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.listName = data['listName']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.ideas = []
    
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM member;'
        results = connectToMySQL(cls.db).query_db(query)
        members = []
        for row in results:
            members.append(cls(row))
        return members

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM member WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO member (firstName, lastName, listName) VALUES (%(firstName)s, %(lastName)s, %(listName)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE member SET firstName=%(firstName)s, lastName=%(lastName)s, listName=%(listName)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM member WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    # join showing 1 members ideas
    # from member left join idea on member.id = idea.member_id where id = ?
    # append idea data to the member data inside a special list
    def memberIdeas(cls, data):
        query = 'SELECT * FROM member LEFT JOIN idea ON member.id = idea.member_id WHERE member.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        member = cls(results[0])
        for row in results:
            ideaData = {
                'id': row['idea.id'],
                'ideaName': row['ideaName'],
                'info': row['info'],
                'createdAt': row['idea.createdAt'],
                'updatedAt': row['idea.updatedAt'],
                'member_id': row['member_id']
            }
            # self.ideas is our list to store each members ideas and is = member.ideas below
            #  we are taking the current members info adding to it an idea instance (inside our loop so this happens more than once) and saving it to this magical list of self.ideas
            member.ideas.append(idea.Idea(ideaData))
        return member
