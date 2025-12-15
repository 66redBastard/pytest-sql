CREATE TABLE IF NOT EXISTS pokemon (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    height INTEGER,
    weight INTEGER,
    base_experience INTEGER
)