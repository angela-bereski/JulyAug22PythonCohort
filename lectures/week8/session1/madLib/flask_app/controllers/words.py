from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.word import *
import random
from   flask_app.controllers.loadWords import *


@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/madLib01/')
def madLib01():
    session['loaded'] = 'Mad Lib #1'
    madLib = session['loaded']
    nounRand01 = random.choice(nouns)
    nounRand02 = random.choice(nouns)
    nounPlurRand01 = random.choice(nounPlurals)
    verbRand01 = random.choice(verbs)
    verbingRand01 = random.choice(verbings)
    verbingRand02 = random.choice(verbings)
    verbpastRand01 = random.choice(verbpasts)
    adjectRand01 = random.choice(adjectives)
    adjectRand02 = random.choice(adjectives)
    nameRand01 = random.choice(names)
    liquidRand01 = random.choice(liquids)
    roomRand01 = random.choice(rooms)
    animalRand01 = random.choice(animals)
    bodyRand01 = random.choice(bodyparts)
    return render_template('lib01.html',madLib = madLib, adjective01=adjectRand01, adjective02=adjectRand02, animal=animalRand01, room=roomRand01, verb01=verbpastRand01, verb02=verbRand01, name=nameRand01, noun01=nounRand01, liquid=liquidRand01, verb03=verbingRand01, body=bodyRand01, noun02=nounPlurRand01, verb04=verbingRand02, noun03=nounRand02)

@app.route('/madLib02/')
def madLib02():
    session['loaded'] = 'Mad Lib #2'
    madLib = session['loaded']
    foodRand01 = random.choice(foods)
    foodRand02 = random.choice(foods)
    foodRand03 = random.choice(foods)
    nameRand01 = random.choice(names)
    adjectRand01 = random.choice(adjectives)
    nounRand01 = random.choice(nouns)
    nounRand02 = random.choice(nouns)
    nounRand03 = random.choice(nouns)
    nounRand04 = random.choice(nouns)
    verbingRand01 = random.choice(verbs)
    verbingRand02 = random.choice(verbs)
    verbingRand03 = random.choice(verbs)
    return render_template('lib02.html', madLib=madLib, food01=foodRand01, food02=foodRand02, food03=foodRand03, name=nameRand01, adjective=adjectRand01, noun01=nounRand01, noun02=nounRand02, noun03=nounRand03, noun04=nounRand04, verb01=verbingRand01, verb02=verbingRand02, verb03=verbingRand03)

@app.route('/madLib03/')
def madLib03():
    session['loaded'] = 'Mad Lib #3'
    madLib = session['loaded']
    adjectRand01 = random.choice(adjectives)
    adjectRand02 = random.choice(adjectives)
    adjectRand03 = random.choice(adjectives)
    adjectRand04 = random.choice(adjectives)
    nameRand01 = random.choice(names)
    nounRand01 = random.choice(nouns)
    nounRand02 = random.choice(nouns)
    nounRand03 = random.choice(nouns)
    nounPlurRand01 = random.choice(nounPlurals)
    foodRand01 = random.choice(foods)
    foodRand02 = random.choice(foods)
    shapeRand01 = random.choice(shapes)
    numRand01 = random.choice(numbers)
    numRand02 = random.choice(numbers)
    return render_template('lib03.html', madLib = madLib, adjective01=adjectRand01, adjective02=adjectRand02, adjective03=adjectRand03, adjective04=adjectRand04, name=nameRand01, noun01=nounRand01, noun02=nounRand02, noun03=nounRand03, noun04=nounPlurRand01, food01=foodRand01, food02=foodRand02, shape=shapeRand01, num01=numRand01, num02=numRand02)

@app.route('/madLib04/')
def madLib04():
    session['loaded'] = 'Mad Lib #4'
    madLib = session['loaded']
    holidayRand01 = random.choice(holidays)
    nounRand01 = random.choice(nouns)
    placeRand01 = random.choice(places)
    personRandRand01 = random.choice(persons)
    personRand01 = random.choice(personRandRand01)
    print("radom person", personRand01)
    adjRand01 = random.choice(adjectives)
    bodyRand01 = random.choice(bodyparts)
    verbRand01 = random.choice(verbs)
    adjRand02 = random.choice(adjectives)
    nounRand02 = random.choice(nouns)
    foodRand01 = random.choice(foods)
    nounplurRand01 = random.choice(nounPlurals)
    return render_template('lib04.html',madLib = madLib, holiday01=holidayRand01, noun01=nounRand01, place01=placeRand01, person01=personRand01, adjective01=adjRand01, body01=bodyRand01, verb01=verbRand01,adjective02=adjRand02, noun02=nounRand02, food01=foodRand01, nounPlural01=nounplurRand01)


@app.route('/refresh/')
def refresh():
    if session['loaded'] == 'Mad Lib #1':
        flash('You reloaded the page')
        return redirect('/madLib01/')
    if session['loaded'] == 'Mad Lib #2':
        flash('You reloaded the page')
        return redirect('/madLib02/')
    if session['loaded'] == 'Mad Lib #3':
        flash('You reloaded the page')
        return redirect('/madLib03/')
    if session['loaded'] == 'Mad Lib #4':
        flash('You reloaded the page')
        return redirect('/madLib04/')
    else:
        flash('Sorry Start over')
        return redirect('/')