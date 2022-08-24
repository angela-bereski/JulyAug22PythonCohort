from flask_app.models.word import *


nouns = Noun.getAll()
nounPlurals = Nounplural.getAll()
foods = Food.getAll()
verbs = Verb.getAll()
verbings = Verbing.getAll()
verbpasts = Verbpast.getAll()
adjectives = Adjective.getAll()
shapes = Shape.getAll()
names = Name.getAll()
numbers = Number.getAll()
liquids = Liquid.getAll()
rooms = Room.getAll()
animals = Animal.getAll()
bodyparts = Bodypart.getAll()
holidays = Holiday.getAll()
places = Place.getAll()
girls = GirlName.getAll()
boys = BoyName.getAll()
colors = Color.getAll()
emotions = Emotion.getAll()
sounds  = Sound.getAll()
genres = Genre.getAll()

person = []
person.append(names)
person.append(girls)
person.append(boys)
persons = person
# print("persons", persons)