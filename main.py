from fastapi import FastAPI
#from database.database import engine
from controllers.routers import router 

app = FastAPI()


app.include_router(router, prefix="/users", tags=["Users"])  