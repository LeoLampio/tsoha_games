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
        users.login(username, password)
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
        if (password1 != password2):
            return render_template("register.html", message="Passwords don't equal.")
        users.login(username, password1)
        return redirect("/")
