from database import collection
from bson import ObjectId
from logger import logger

class PokemonRepository:

    @staticmethod
    def find_by_name(nome: str):
        logger.info(f"Buscando Pokémon {nome} no banco de dados...")
        pokemon = collection.find_one({"nome": nome.lower()})
        if pokemon:
            logger.info(f"Pokémon {nome} encontrado no banco.")
            pokemon["_id"] = str(pokemon["_id"])  
        else:
            logger.warning(f"Pokémon {nome} não encontrado no banco.")
        return pokemon

    @staticmethod
    def save(pokemon_data: dict):
        logger.info(f"Salvando Pokémon {pokemon_data['nome']} no banco de dados...")
        inserted = collection.insert_one(pokemon_data)
        pokemon_data["_id"] = str(inserted.inserted_id)
        logger.info(f"Pokémon {pokemon_data['nome']} salvo com sucesso!")
        return pokemon_data