DROP TABLE IF EXISTS users, games, genres CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    title TEXT,
    description TEXT
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games,
    genre TEXT
);