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
        return render_template("login.html", message="")
    
    if (request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]
        if (not users.login(username, password)):
            return render_template("login.html", message="Incorrect username or password.")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register",methods=["POST", "GET"])
def register():
    if (request.method == "GET"):
        return render_template("register.html", message="")
    
    if (request.method == "POST"):
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if (len(username) < 1 or len(username) > 20):
            return render_template("register.html", message="Username should have 1-20 characters.")
        if (password1 != password2):
            return render_template("register.html", message="Passwords don't equal.")
        if (len(password1) < 5):
            return render_template("register.html", message="Password needs to be atleast 5 characters long.")
        
        value = users.register(username, password1)
        
        if (value == 1):
            return render_template("register.html", message="Username is taken.")
        elif (value == 2):
            return render_template("register.html", message="Login error.")

        return redirect("/")
