# main.py

from fastapi import FastAPI
from database.database import engine
from controllers.routers import router  # Thay đổi import để import router mới

app = FastAPI()

# Tạo bảng cơ sở dữ liệu
from models.model import Base
Base.metadata.create_all(bind=engine)

# Include router từ controllers/router.py
app.include_router(router, prefix="/users", tags=["Users"])  # Thay đổi import để sử dụng router mới
