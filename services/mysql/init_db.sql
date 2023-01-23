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
rule_description  VARCHAR(250)
);


INSERT INTO RULEEVENTS (name_event, description, score, rule_description)
VALUES ('Evento de Teste', 'Evento de Teste', '100', 'Evento de Teste');

INSERT INTO USERS (username, password, name, email)
VALUES('Test','pbkdf2:sha256:260000$yPEqaSiYcba52Rs7$508bcb5499dafafe0e72ce4db502d1e7e979a94b61bb13d4d27e243361fadc64','Tester MIT','test@mit.test.com');