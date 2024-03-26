from db import db
from flask import session

def login(username, password):
    session["username"] = username

def logout():
    del session["username"]