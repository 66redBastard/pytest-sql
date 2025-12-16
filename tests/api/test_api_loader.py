from src.api.poke_api_loader import load_pokemon_from_api
from src.database import init_database


def test_load_picachu():
    init_database()
    result = load_pokemon_from_api("pikachu")

    assert result is not None
    assert result["name"] == "pikachu"
    assert result["height"] == 4
    assert result["weight"] == 60
    assert result["base_experience"] == 112
    assert result["hp"] == 35
    assert result["hp_effort"] == 0
    assert result["attack"] == 55
    assert result["attack_effort"] == 0
