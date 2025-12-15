import requests

from src.database import get_connection
from src.poke_queries import INSERT_POKEMON
from utils.logger import log_api_request, log_api_request_failure


def load_pokemon_from_api(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.ok:
        log_api_request(url, response.status_code)

        data = response.json()

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                INSERT_POKEMON,
                (
                    data["name"],
                    data["height"],
                    data["weight"],
                    data["base_experience"],
                ),
            )
            return data
        finally:
            conn.commit()
            cursor.close()
            conn.close()

    else:
        log_api_request_failure(url, response.status_code)
        return None
