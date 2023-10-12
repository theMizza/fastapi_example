from fastapi import FastAPI

from app import models, routers
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routers.router, tags=['questions'], prefix='/api/questions')


@app.get("/api/healthchecker", tags=['healthchecker'])
def root():
    return {"message": "These aren't the droids you're looking for"}
