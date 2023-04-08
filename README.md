# OptimizeOrganizeChallenge

## NeuroHack Team

.env - нужно создать файл окружения

```
DB_URL = sqlalchemy.url
LOGGING_PATH = log file path
DEBUG = debug mode
SECRET=SECRET
```

### Alembic

https://testdriven.io/blog/fastapi-sqlmodel/

sqlalchemy.url = postgresql+asyncpg://login:password@db:5432/dbname

```shell
alembic init -t async migrations
alembic revision --autogenerate -m "init"
alembic upgrade head 
```

# Run

```shell
sudo docker-compose up
```
