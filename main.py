from fastapi import FastAPI
from routes.pokemon_routes import router

app = FastAPI(title="PokeAPI Wrapper", version="1.0")

app.include_router(router)