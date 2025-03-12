Para criar um essa API com integração a API do Pokemon, vamos precisar criar um ambiente virtual

    'python3 -m venv venv'
    'source venv/bin/activate'  # Ativa no Mac/Linux
    'venv\Scripts\activate'  # Ativa no Windows

Feito isso vamos instalar o FastApi

    'pip install fastapi uvicorn requests'

Após essa configurações, vamos criar o arquivo requirements.txt para registrar nossas dependencias:

    'pip freeze > requirements.txt'

Para executar a APP no servidor Uvicorn

    'uvicorn main:app --reload' /  'ENV=local uvicorn main:app --reload'

Caso alguma variavel fique locada em memoria, você pode ver o valor em memoria e excluir com os seguintes comandos

    echo $MONGO_URI  /  unset MONGO_URI

A URL local para essa APP será, http://127.0.0.1:8000/ 
dentro do FastApi já temos o Swagger gerado de forma automatica, podendo acessar http://127.0.0.1:8000/docs


lsof -i :8000 
kill -9 10874