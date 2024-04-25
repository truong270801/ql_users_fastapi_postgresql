from fastapi import FastAPI
import model
from database import engine
import routers

model.Base.metadata.create_all(bind = engine)
app = FastAPI()

app.include_router(routers.router,prefix="/users",tags=["Users"])

@app.get("/")
def read_root():
    return {"Hello": "World"}