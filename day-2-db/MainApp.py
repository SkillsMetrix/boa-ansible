from fastapi import FastAPI
from .database import engine,get_connection

from . import crudapp,models

models.Base.metadata.create_all(bind=engine)
app= FastAPI()

app.include_router(crudapp.router)
