import requests

from src.database import get_connection
from src.poke_queries import INSERT_POKEMON
from utils.logger import log_api_request, log_api_request_failure, log_error_insertion


def load_pokemon_from_api(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.ok:
        log_api_request(url, response.status_code)

        data = response.json()

        stat_names = [
            "hp",
            "attack",
            "defense",
            "special-attack",
            "special-defense",
            "speed",
        ]
        stats_dict = {}

        for stat_name in stat_names:
            stat = next(
                (s for s in data["stats"] if s["stat"]["name"] == stat_name), None
            )
            if stat:
                stats_dict[stat_name.replace("-", "_")] = stat["base_stat"]
                stats_dict[f"{stat_name.replace('-', '_')}_effort"] = stat["effort"]

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                INSERT_POKEMON,
                (
                    data["id"],
                    data["name"],
                    data["height"],
                    data["weight"],
                    data["base_experience"],
                    stats_dict["hp"],
                    stats_dict["hp_effort"],
                    stats_dict["attack"],
                    stats_dict["attack_effort"],
                    stats_dict["defense"],
                    stats_dict["defense_effort"],
                    stats_dict["special_attack"],
                    stats_dict["special_attack_effort"],
                    stats_dict["special_defense"],
                    stats_dict["special_defense_effort"],
                    stats_dict["speed"],
                    stats_dict["speed_effort"],
                ),
            )
            return {
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "base_experience": data["base_experience"],
                **stats_dict,
            }
        except Exception as exc:
            log_error_insertion(str(exc))
            return None
        finally:
            conn.commit()
            cursor.close()
            conn.close()

    else:
        log_api_request_failure(url, response.status_code)
        return None
