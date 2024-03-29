from db import db
from sqlalchemy.sql import text
import users

def add(title, description, genre_ids):
    creator_id = users.get_user_id()
    if (creator_id == 0):
        # User is not logged in
        return False
    
    sql = "INSERT INTO games (creator_id, title, description) VALUES (:creator_id, :title, :description) RETURNING id"
    result = db.session.execute(text(sql), {"creator_id": creator_id, "title": title, "description": description})
    game_id = result.fetchone()[0]

    sql = "INSERT INTO genres (game_id, genre) VALUES (:game_id, :genre)"
    for i in genre_ids:
        db.session.execute(text(sql), {"game_id": game_id, "genre": get_genres()[int(i)]})

    db.session.commit()
    return True

def get_games():
    result = db.session.execute(text("SELECT G.id, U.username, G.title FROM users U, games G WHERE G.creator_id = U.id")).fetchall()
    games = []
    for game in result:
        games.append((game.id, game.title, game.username))
    return games

def get_game(id):
    result = db.session.execute(text("SELECT U.username, G.title, G.description FROM users U, games G WHERE G.id =:id"), {"id": id}).fetchone()
    genre_result = db.session.execute(text("SELECT genre FROM genres WHERE game_id =:game_id"), {"game_id": id}).fetchall()
    genres = []
    for genre in genre_result:
        genres.append(genre[0])
    return (result.title, result.username, result.description, genres)

def get_genres():
    return [
        "Platformer",
        "Shooter",
        "Fighting",
        "Beat 'em up",
        "Survival",
        "Rhythm",
        "Battle Royale",
        "Metroidvania",
        "Adventure",
        "Puzzle",
        "RPG",
        "Roguelike",
        "Simulation",
        "Strategy",
        "Sports",
        "Racing",
        "Horror",
        "Arcade",
        "Board",
        "Card",
        "Sandbox",
        "Open world"
    ]