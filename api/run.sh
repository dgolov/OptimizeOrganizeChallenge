#!/bin/bash
sleep 5
alembic revision --autogenerate -m "init"
alembic upgrade head
uvicorn main:app --reload --port 8000 --host 0.0.0.0