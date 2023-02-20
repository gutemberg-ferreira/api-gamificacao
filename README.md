# API-Gamificação


## Passos para realizar o escalonamento da aplicação)

#### Realizar a instalação do Kubernetes  https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
#### Realizar a build das aplicações para gerar a imagem:
    docker build -t api-gamificacao-database ../services/mysql/.
    docker build -t api-gamificacao-api_gamification ../.

#### cd k8s-specification/ 

#### kubectl create -f namespaces/mit_gamification.yaml --save-config 

#### kubectl create -f secrets.yaml --save-config

#### kubectl create -f mysql-pv.yaml --save-config

#### kubectl create -f mysql-pvc.yaml --save-config

#### kubectl create -f deployements/ --save-config

#### kubectl create -f services/ --save-config

#### minikube tunnel

## Passos para Configurar o ambiente (Doc Versão 2.0)
### Inicialização do serviço de gamificação : 

  * Instalar docker e docker-compose https://docs.docker.com/get-docker/

  * Abrir o command-line na pasta do projeto e rodar o camando para subir a aplicação:  
  
  <code> sudo docker-compose up -d </code>

 * acessar documentação: http://127.0.0.1:5000/apidocs
<br>
<br>
 * acessar Leaderbord Model: http://localhost:5000/dashrank
<br>
<br>
  * Obs: Para modificações na estrutura do banco de dados, será necessario deletar o volume de dados do docker com o comando: 


* <code> docker compose rm --volumes </code>
Obs: esse comando irá deletar todos os dados já cadastrados.
  
<br>
Depois, rodar o comando para subir novamente: 

* <code> docker compose up -d --build </code>

<br>

# Usuário e Senha para autenticação (http://localhost:5000/auth) da API

  * **USER** : test
  * **PASS** : test123

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






