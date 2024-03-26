from app import app
from db import db
from sqlalchemy.sql import text
from flask import render_template, request, redirect
import users

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/login",methods=["POST", "GET"])
def login():
    if (request.method == "GET"):
        return render_template("login.html")
    
    if (request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]
        users.login(username, password)
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
