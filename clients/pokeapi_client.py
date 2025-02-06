import requests
import config
from logger import logger

class PokeAPIClient:
    """Cliente HTTP para consumir a PokeAPI."""

    @staticmethod
    def get_pokemon(nome: str) -> dict:
        """Busca informações de um Pokémon na PokeAPI."""
        url = f"{config.POKEAPI_URL}/{nome.lower()}"
        logger.info(f"Consultando PokeAPI: {url}")

        response = requests.get(url)

        if response.status_code != 200:
            logger.warning(f"Pokémon {nome} não encontrado na PokeAPI.")
            return None

        data = response.json()
        logger.info(f"Pokémon {nome} encontrado na PokeAPI.")
        
        return {
            "nome": data["name"],
            "id": data["id"],
            "altura": data["height"],
            "peso": data["weight"],
            "tipos": [tipo["type"]["name"] for tipo in data["types"]],
            "habilidades": [habilidade["ability"]["name"] for habilidade in data["abilities"]],
            "imagem": data["sprites"]["front_default"],
        }