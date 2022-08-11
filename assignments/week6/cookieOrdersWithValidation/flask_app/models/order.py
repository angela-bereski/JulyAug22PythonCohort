# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Order:
    db = 'cookie_orders'
    def __init__(self, data):
        self.id = data['id']
        self.customerName = data['customerName']
        self.cookie = data['cookie']
        self.num_boxes = data['num_boxes']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM cookieOrder;'
        results = connectToMySQL('cookie_orders').query_db(query)
        orders = []
        for row in results:
            orders.append(cls(row))
        return orders
    
    @classmethod
    def getOne(cls,data):
        query = 'SELECT * FROM cookieOrder WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])    
    
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO cookieOrder (customerName, cookie, num_boxes, createdAt, updatedAt) VALUES (%(customerName)s, %(cookie)s, %(num_boxes)s, NOW(), NOW() );'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE cookieOrder SET customerName = %(customerName)s, cookie = %(cookie)s, num_boxes = %(num_boxes)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM cookieOrder WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def validate(cookieOrder):
        isValid = True
        if len(cookieOrder['customerName']) < 2:
            isValid = False
            flash('Please use at least 2 characters for name.', 'customerName')
        if len(cookieOrder['cookie']) < 2:
            isValid = False
            flash('Please use at least 2 characters for cookie type.', 'cookie')
        if int(cookieOrder['num_boxes']) < 0:
            isValid = False
            flash('Must order at least 1 box of cookies.', 'num_boxes')
        return isValid