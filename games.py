from db import db
from sqlalchemy.sql import text
import users

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