DROP TABLE IF EXISTS pokemon CASCADE;

CREATE TABLE IF NOT EXISTS pokemon (
    id SERIAL PRIMARY KEY,
    api_id INTEGER UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    height INTEGER,
    weight INTEGER,
    base_experience INTEGER,
    hp INTEGER,
    hp_effort INTEGER,
    attack INTEGER,
    attack_effort INTEGER,
    defense INTEGER,
    defense_effort INTEGER,
    special_attack INTEGER,
    special_attack_effort INTEGER,
    special_defense INTEGER,
    special_defense_effort INTEGER,
    speed INTEGER,
    speed_effort INTEGER
)