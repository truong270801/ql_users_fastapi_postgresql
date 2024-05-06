from fastapi import FastAPI
#from database.database import engine
from controllers.routers import router 

app = FastAPI()
@app.get('/')
async def Home():
    return "Welcome Home"


app.include_router(router, prefix="/users", tags=["Users"])  