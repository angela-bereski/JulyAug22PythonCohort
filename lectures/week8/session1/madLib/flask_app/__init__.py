from flask import Flask
# from .env import KEY

app = Flask(__name__)
# app.secret_key = KEY
app.secret_key = 'MadLibs are fun...add your own'

