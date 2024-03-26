from db import db
from sqlalchemy.sql import text
from flask import session

def login(username, password):
    session["username"] = username

def logout():
    del session["username"]

def register(username, password):
    pass