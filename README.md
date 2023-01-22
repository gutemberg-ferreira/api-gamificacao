# API-Gamificação

## Passos para Configurar o ambiente (Doc Versão 2.0)
### Inicialização do serviço de gamificação : 

  * Instalar docker e docker-compose https://docs.docker.com/get-docker/


  * Subir a aplicação:  
  
  <code> sudo docker-compose up -d </code>

 * acessar documentação: http://127.0.0.1:5000/apidocs


 * criar usuário POST /addUser

## Passos para Configurar o ambiente (Doc Versão 1.0)

### Inicialização do banco de dados : 
  * Utilização de docker https://docs.docker.com/get-docker/
  * MYSQL : rodar o comando : sudo docker-compose up -d

### Criar ambiente virtual de desenvolvimento : 
  <code> python3 -m venv venv_api_gamificacao </code>

  * Ativar ambiente de desenvolvimento 

    * <code> source ~/ <repositorio> /venv_api_gamificacao/bin/activate </code>
    


* Instalar dependências
  * <code> pip install -r requirements.txt</code>


### Rodar aplicação
  * <code> flask --app hello_world run </code>
  
  * acessar documentação: http://127.0.0.1:5000/apidocs



