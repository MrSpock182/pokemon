import os
from dotenv import load_dotenv

# Determinar qual arquivo .env carregar
env_file = ".env.local" if os.getenv("ENV") == "local" else ".env"
# Carregar variáveis do arquivo correspondente
load_dotenv(env_file)

print(f"Carregando {env_file}...") 
print(f"DEBUG: MONGO_URI='{os.getenv('MONGO_URI')}'")

# Obter variáveis do ambiente
POKEAPI_URL = os.getenv("POKEAPI_URL")
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# Verificação de erro: garantir que variáveis críticas não estejam vazias
if not POKEAPI_URL:
    raise ValueError("Erro: A variável de ambiente POKEAPI_URL não está definida!")

if not MONGO_URI:
    raise ValueError("Erro: A variável de ambiente MONGO_URI não está definida!")

if not DATABASE_NAME:
    raise ValueError("Erro: A variável de ambiente DATABASE_NAME não está definida!")

if not COLLECTION_NAME:
    raise ValueError("Erro: A variável de ambiente COLLECTION_NAME não está definida!")