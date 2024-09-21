from fastapi import FastAPI
from app.routes import app1, app2

app = FastAPI()
app.include_router(app1.router)
app.include_router(app2.router)

