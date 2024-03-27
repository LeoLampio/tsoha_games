from db import db
from sqlalchemy.sql import text
from flask import session, request, abort
from werkzeug.security import check_password_hash, generate_password_hash
import secrets

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username =:username"
    result = db.session.execute(text(sql), {"username": username}).fetchone()

    if (result == None):
        # Invalid username
        return False
    
    if (not check_password_hash(result[0], password)):
        # Invalid password
        return False
    
    session["user_id"] = result[1]
    session["username"] = username
    session["csrf_token"] = secrets.token_hex(16)
    return True

def logout():
    del session["user_id"]
    del session["username"]
    del session["csrf_token"]

def register(username, password):
    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    password_hash = generate_password_hash(password)
    try:
        db.session.execute(text(sql), {"username": username, "password": password_hash})
        db.session.commit()
    except:
        # Username is taken
        return 1
    
    if (login(username, password)):
        # No error
        return 0
    else:
        # Login error
        return 2
    
def get_user_id():
    return session.get("user_id", 0)

def check_csrf():
    if (session["csrf_token"] != request.form("csrf_token")):
        abort(403)