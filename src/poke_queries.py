INSERT_POKEMON = """
    INSERT INTO pokemon (api_id, name, height, weight, base_experience,
        hp, hp_effort,
        attack, attack_effort,
        defense, defense_effort,
        special_attack, special_attack_effort,
        special_defense, special_defense_effort,
        speed, speed_effort)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id;
"""

GET_ALL_POKEMON = """
    SELECT * FROM pokemon;
"""

GET_POKEMON_BY_NAME = """
    SELECT * FROM pokemon WHERE name = %s;
"""

GET_POKEMON_WITH_TYPES = """
    SELECT p.name, p.height, pt.type_name
    FROM pokemon p
    LEFT JOIN pokemon_types pt ON p.id = pt.pokemon_id
    WHERE p.name = %s;
"""
