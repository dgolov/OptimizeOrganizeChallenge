from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from routes import routes


app = FastAPI()

app.include_router(routes, prefix='/api')
