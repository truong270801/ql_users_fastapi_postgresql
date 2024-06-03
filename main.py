from fastapi import FastAPI, Depends
#from database.database import engine, Base
from controllers.routers import router 
from sqlalchemy.orm import Session
from database.database import get_db
from models.model import User


app = FastAPI()

# Tạo tất cả các bảng trong cơ sở dữ liệu
#Base.metadata.create_all(bind=engine)

# Đăng ký router
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
@app.get("/all")
def get_all_user(db: Session = Depends(get_db),  skip: int = 0, limit: int = 100):
     return db.query(User).offset(skip).limit(limit).all()
