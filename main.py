from fastapi import FastAPI
import model
from database import engine

model.Base.metadata.create_all(bind = engine)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}