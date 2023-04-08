FROM postgres:latest


ENV POSTGRES_USER user_pg
ENV POSTGRES_PASSWORD password_pg
ENV PGDATA /var/lib/postgresql/data/pgdata

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432