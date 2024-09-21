from fastapi import FastAPI
from app.routes import app1

app = FastAPI()
app.include_router(app1.router)

