FROM mysql

ADD ./init_db.sql /docker-entrypoint-initdb.d/init_db.sql

RUN chmod -R 775 /docker-entrypoint-initdb.d

EXPOSE 3306

