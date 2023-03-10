CREATE DATABASE IF NOT EXISTS gamification_nexto;
USE gamification_nexto;
ALTER DATABASE gamification_nexto DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS USERS (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL ,
username VARCHAR(20) NOT NULL,
password  VARCHAR(250) NOT NULL,
name VARCHAR(50) NOT NULL,
email  VARCHAR(50) NOT NULL
)ENGINE=MyISAM DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS RULEEVENTS (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name_event VARCHAR(50) NOT NULL,
description  VARCHAR(200) NOT NULL,
score INT NOT NULL,
rule_description  VARCHAR(250),
status BOOLEAN NOT NULL
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS LISTENEVENTS (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
user_id INT NOT NULL,
event_date DATETIME NOT NULL,
community_id INT NOT NULL,
event_id  INT NOT NULL,
generated_score INT NOT NULL,
FOREIGN KEY (event_id) REFERENCES RULEEVENTS(id)
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS CAMPAIGNSBONUS (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(100) NOT NULL,
date_begin DATETIME NOT NULL,
date_end DATETIME NOT NULL,
bonus INT NOT NULL,
community_id  INT NOT NULL,
event_ids VARCHAR(300) NOT NULL,
status BOOLEAN NOT NULL
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Baixou e Abriu o APP', N'Evento que bonifica o usuario por ter baixado o aplicativo.', 100, N'Descrição a ser implementada', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Inscrição em comunidade', N'Inscrição em nova comunidade', 30, N'O usuário sempre irá pontuar quando criar uma nova comunidade', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Acessar/Abrir a aplicação', N'Quando usuário abrir a aplicação para acessar o Nexto', 10, N'A cada dia aumenta 0.1', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Registro na plataforma', N'O usuário realiza o cadastro na Nexto', 20, N'Pontuação recebida ao criar o cadastro na Nexto', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Realizar o login pela primeira vez', N'Usuário realiza login pela primeira vez na aplicação', 20, N'Pontuação recebida apenas no primeiro acesso', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Completar meu cadastro', N'Usuário atualiza as informações de perfil', 20, N'Pontos são associados ao usuário quando 100% dos cadastro estiver Pronto', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Criar Comunidades', N'Usuário cria uma nova comunidade', 50, N'Pontos associados no  momento da criação da comunidade e atribuidos aos criador da comunidade', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Criar Eventos', N'Usuário cria um novo evento', 30, N'Essa é uma funcionalidade de administrador e não deve ser bonificada', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Prêmio pelo crescimento da  Comunidade', N'Ser premiado pelo crescimento da comunidade', 28, N'Cada 10 usuários registrados em minhas comunidades', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Postagem de novo conteúdo na comunidade', N'Usuário quando inicia um novo tópico dentro da comunidade', 150, N'Cada novo tópico criado pelo usuário.
- Avaliar o upload de arquivos', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Tópicos que geram discussão', N'N/A', 1000, N'Avaliar premiação', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Convidar amigos para o Nexto', N'Usuário convida um amigo para entrar na plataforma', 20, N'Premiar o usuário sempre que o amigo indicado completar o registro', true);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES (N'Avaliar', 'Feedback Premiado', 10, N'Premiar o usuário sempre que o usuário avaliar o aplicativo', true);

INSERT INTO USERS (username, password, name, email)
VALUES('test', 'pbkdf2:sha256:260000$yPEqaSiYcba52Rs7$508bcb5499dafafe0e72ce4db502d1e7e979a94b61bb13d4d27e243361fadc64', 'Tester MIT', 'test@mit.test.com');

INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(1, '2023-01-28 00:10:00', 1, 1, 1000);
INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(2, '2023-01-28 00:10:00', 1, 1, 900);
INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(3, '2023-01-28 00:10:00', 1, 1, 800);
INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(4, '2023-01-28 00:10:00', 1, 1, 700);
INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(5, '2023-01-28 00:10:00', 1, 1, 600);
INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(6, '2023-01-28 00:10:00', 1, 1, 500);
INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(7, '2023-01-28 00:10:00', 1, 1, 400);
INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(8, '2023-01-28 00:10:00', 1, 1, 300);
INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(9, '2023-01-28 00:10:00', 1, 1, 200);
INSERT INTO LISTENEVENTS (user_id, event_date, community_id, event_id, generated_score)
VALUES(10, '2023-01-28 00:10:00', 1, 1, 100);

INSERT INTO CAMPAIGNSBONUS (name,date_begin, date_end, bonus, community_id, event_ids,status)
VALUES(N'Bonus Teste','2023-01-31 00:00:00', '2023-02-28 23:59:00', 1.5, 1, '1',true);