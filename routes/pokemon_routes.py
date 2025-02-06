from fastapi import APIRouter, HTTPException
from services.pokemon_service import PokemonService

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Bem-vindo à API de Pokémon com MongoDB!"}


@router.get("/pokemon/{nome}")
def get_pokemon(nome: str):
    pokemon = PokemonService.get_pokemon(nome)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return pokemon