FROM postgres:latest

ENV POSTGRES_DB neurohack
ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD password
ENV PGDATA /var/lib/postgresql/data/pgdata

EXPOSE 5432