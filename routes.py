from app import app
from db import db
from sqlalchemy.sql import text
from flask import render_template, request, redirect
import users
import games

@app.route("/")
def index():
    return render_template("index.html", games=games.get_games())

@app.route("/game/<int:id>", methods=["GET"])
def game(id):
    return render_template("game.html", game=games.get_game(id))

@app.route("/add",methods=["POST", "GET"])
def add_game():
    if (request.method == "GET"):
        return render_template("addGame.html", message="", genres=games.get_genres(), genres_len=len(games.get_genres()))
    
    if (request.method == "POST"):
        users.check_csrf()

        title = request.form["title"]
        description = request.form["description"]
        genre_ids = request.form.getlist("genres")

        if (len(title) > 50 or len(title) < 1):
            return render_template("addGame.html", message="Title needs to have 1-50 characters.", genres=games.get_genres(), genres_len=len(games.get_genres()))
        if (len(description) > 1000):
            return render_template("addGame.html", message="Description is too long.", genres=games.get_genres(), genres_len=len(games.get_genres()))
        if (len(genre_ids) < 1):
            return render_template("addGame.html", message="You need to select atleast one genre.", genres=games.get_genres(), genres_len=len(games.get_genres()))

        if (not games.add(title, description, genre_ids)):
            return render_template("addGame.html", message="You need to login to add games.", genres=games.get_genres(), genres_len=len(games.get_genres()))

        return redirect("/")

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
