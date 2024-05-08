from fastapi import HTTPException, Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from controllers.routers import router 
from security.jwt import create_jwt_token
from database.database import get_db 
from sqlalchemy.orm import Session  
from models.model import User
import os
from dotenv import load_dotenv

load_dotenv()

TIME = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")) 
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#Đăng nhập lấy mã token
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = User.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Sai tài khoản hoặc mật khẩu")
    
    access_token_expires = timedelta(minutes=TIME)
    access_token = create_jwt_token(data={"sub": user.username,"role": user.role}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get('/')
async def Home():
    return "Welcome Home"

app.include_router(router, prefix="/users", tags=["Users"])
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
