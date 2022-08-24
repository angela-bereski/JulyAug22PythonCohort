from flask_app.config.mysqlconnection import connectToMySQL

class Noun:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.noun = data['noun']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM noun;'
        results = connectToMySQL(cls.db).query_db(query)
        nouns = []
        for row in results:
            nouns.append(cls(row))
        return nouns

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO noun (noun) VALUE %(noun)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Nounplural:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.nounPlural = data['nounPlural']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM nounplural;'
        results = connectToMySQL(cls.db).query_db(query)
        nouns = []
        for row in results:
            nouns.append(cls(row))
        return nouns

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO nounplural (nounPlural) VALUE %(nounPlural)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Food:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.food = data['food']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM food;'
        results = connectToMySQL(cls.db).query_db(query)
        foods = []
        for row in results:
            foods.append(cls(row))
        return foods

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO food (food) VALUE %(food)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Verb:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.verb = data['verb']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM verb;'
        results = connectToMySQL(cls.db).query_db(query)
        verbs = []
        for row in results:
            verbs.append(cls(row))
        return verbs

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO verb (verb) VALUE %(verb)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Verbing:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.verbING = data['verbING']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM verbing;'
        results = connectToMySQL(cls.db).query_db(query)
        verbs = []
        for row in results:
            verbs.append(cls(row))
        return verbs

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO verbing (verbING) VALUE %(verbING)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Verbpast:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.verbPast = data['verbPast']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM verbpast;'
        results = connectToMySQL(cls.db).query_db(query)
        verbs = []
        for row in results:
            verbs.append(cls(row))
        return verbs

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO verbpast (verbPast) VALUE %(verbPast)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Adjective:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.adjective = data['adjective']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM adjective;'
        results = connectToMySQL(cls.db).query_db(query)
        adjectives = []
        for row in results:
            adjectives.append(cls(row))
        return adjectives

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO adjective (adjective) VALUE %(adjective)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Shape:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.shape = data['shape']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM shape;'
        results = connectToMySQL(cls.db).query_db(query)
        shapes = []
        for row in results:
            shapes.append(cls(row))
        return shapes

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO shape (shape) VALUE %(shape)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Name:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM name;'
        results = connectToMySQL(cls.db).query_db(query)
        names = []
        for row in results:
            names.append(cls(row))
        return names

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO name (name) VALUE %(name)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Number:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.number = data['number']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM number;'
        results = connectToMySQL(cls.db).query_db(query)
        numbers = []
        for row in results:
            numbers.append(cls(row))
        return numbers

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO number (number) VALUE %(number)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Liquid:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.liquid = data['liquid']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM liquid;'
        results = connectToMySQL(cls.db).query_db(query)
        liquids = []
        for row in results:
            liquids.append(cls(row))
        return liquids

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO liquid (liquid) VALUE %(liquid)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Room:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.roomInHouse = data['roomInHouse']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM room;'
        results = connectToMySQL(cls.db).query_db(query)
        rooms = []
        for row in results:
            rooms.append(cls(row))
        return rooms

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO room (roomInHouse) VALUE %(roomInHouse)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Animal:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.animal = data['animal']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM animal;'
        results = connectToMySQL(cls.db).query_db(query)
        animals = []
        for row in results:
            animals.append(cls(row))
        return animals

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO animal (animal) VALUE %(animal)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Bodypart:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.bodyPart = data['bodyPart']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM bodypart;'
        results = connectToMySQL(cls.db).query_db(query)
        bodyParts = []
        for row in results:
            bodyParts.append(cls(row))
        return bodyParts

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO bodypart (bodyPart) VALUE %(bodyPart)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Holiday:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.holiday = data['holiday']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM holiday;'
        results = connectToMySQL(cls.db).query_db(query)
        holidays = []
        for row in results:
            holidays.append(cls(row))
        return holidays

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO holiday (holiday) VALUE %(holiday)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Place:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.place = data['place']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM place;'
        results = connectToMySQL(cls.db).query_db(query)
        places = []
        for row in results:
            places.append(cls(row))
        return places

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO place (place) VALUE %(place)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class GirlName:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.girlName = data['girlName']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM girlname;'
        results = connectToMySQL(cls.db).query_db(query)
        girlNames = []
        for row in results:
            girlNames.append(cls(row))
        return girlNames

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO girlname (girlName) VALUE %(girlName)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class BoyName:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.boyName = data['boyName']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM boyname;'
        results = connectToMySQL(cls.db).query_db(query)
        boyNames = []
        for row in results:
            boyNames.append(cls(row))
        return boyNames

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO boyname (boyName) VALUE %(boyName)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Color:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.color = data['color']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM color;'
        results = connectToMySQL(cls.db).query_db(query)
        colors = []
        for row in results:
            colors.append(cls(row))
        return colors

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO color (color) VALUE %(color)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Emotion:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.emotion = data['emotion']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM emotion;'
        results = connectToMySQL(cls.db).query_db(query)
        emotions = []
        for row in results:
            emotions.append(cls(row))
        return emotions

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO emotion (emotion) VALUE %(emotion)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Sound:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.sound = data['sound']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM sound;'
        results = connectToMySQL(cls.db).query_db(query)
        sounds = []
        for row in results:
            sounds.append(cls(row))
        return sounds

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO sound (sound) VALUE %(sound)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Genre:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.genre = data['genre']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM genre;'
        results = connectToMySQL(cls.db).query_db(query)
        genres = []
        for row in results:
            genres.append(cls(row))
        return genres

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO genre (genre) VALUE %(genre)s;'
        return connectToMySQL(cls.db).query_db(query, data)

class Instrument:
    db = 'madLib'
    def __init__(self, data):
        self.id = data['id']
        self.instrument = data['instrument']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM instrument;'
        results = connectToMySQL(cls.db).query_db(query)
        instruments = []
        for row in results:
            instruments.append(cls(row))
        return instruments

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO instrument (instrument) VALUE %(instrument)s;'
        return connectToMySQL(cls.db).query_db(query, data)