from fastapi import FastAPI
from models import model
from database.database import engine
from controllers import routers

model.Base.metadata.create_all(bind = engine)
app = FastAPI()

app.include_router(routers.router,prefix="/users",tags=["Users"])

@app.get("/")
def read_root():
    return {"Hello": "World"}