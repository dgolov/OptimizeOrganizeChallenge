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

sqlalchemy.url = postgresql+asyncpg://login:password@db:5432/dbname

```shell
alembic init -t async migrations
web alembic revision --autogenerate -m "init"
```

# Run

```shell
sudo docker-compose up
```
