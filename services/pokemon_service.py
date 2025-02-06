from repositories.pokemon_repository import PokemonRepository
from clients.pokeapi_client import PokeAPIClient

class PokemonService:

    @staticmethod
    def get_pokemon(nome: str):
        pokemon = PokemonRepository.find_by_name(nome)
        if pokemon:
            return pokemon

        pokemon = PokeAPIClient.get_pokemon(nome)
        if pokemon:
            return PokemonRepository.save(pokemon)

        return None