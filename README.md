Para criar um essa API com integração a API do Pokemon, vamos precisar criar um ambiente virtual

    'python3 -m venv venv'
    'source venv/bin/activate'  # Ativa no Mac/Linux
    'venv\Scripts\activate'  # Ativa no Windows

Feito isso vamos instalar o FastApi

    'pip install fastapi uvicorn requests'

Após essa configurações, vamos criar o arquivo requirements.txt para registrar nossas dependencias:

    'pip freeze > requirements.txt'

Para executar a APP no servidor Uvicorn

    'uvicorn main:app --reload'

A URL local para essa APP será, http://127.0.0.1:8000/ 
dentro do FastApi já temos o Swagger gerado de forma automatica, podendo acessar http://127.0.0.1:8000/docs
