from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.admin.conditions import ConditionView
from app.views import router as api_router
from sqladmin import Admin

from core.engine import engine

app = FastAPI()

admin = Admin(
    app=app,
    engine=engine,
    title="Админ",
    base_url="/admin",

)

admin.add_view(ConditionView)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/api')
