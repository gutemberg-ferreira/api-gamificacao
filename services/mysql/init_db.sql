USE gamification_nexto;

CREATE TABLE IF NOT EXISTS USERS (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL ,
username VARCHAR(20) NOT NULL,
password  VARCHAR(250) NOT NULL,
name VARCHAR(50) NOT NULL,
email  VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS RULEEVENTS (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name_event VARCHAR(50) NOT NULL,
description  VARCHAR(200) NOT NULL,
score INT NOT NULL,
rule_description  VARCHAR(250),
status BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS LISTENEVENTS (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
user_id INT NOT NULL,
event_date DATETIME NOT NULL,
community_id INT NOT NULL,
event_id  INT NOT NULL,
generated_score INT NOT NULL,
FOREIGN KEY (event_id) REFERENCES RULEEVENTS(id)
);

CREATE TABLE IF NOT EXISTS CAMPAIGNSBONUS (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
date_begin DATETIME NOT NULL,
date_end DATETIME NOT NULL,
bonus INT NOT NULL,
community_id  INT NOT NULL,
event_ids VARCHAR(300) NOT NULL
);

INSERT INTO RULEEVENTS (name_event, description, score, rule_description, status)
VALUES ('Baixou e Abriu o APP', 'Evento que bonifica o usuario por ter baixado o aplicativo.', 100, 'Descricao a ser implementada', true);

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

INSERT INTO CAMPAIGNSBONUS (date_begin, date_end, bonus, community_id, event_ids)
VALUES('2023-01-31 00:00:00', '2023-02-28 23:59:00', 1.5, 1, '1');