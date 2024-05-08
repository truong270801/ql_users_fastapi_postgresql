from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from security.jwt import decode_jwt_token

async def check_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    payload = decode_jwt_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Mã token không hợp lệ")
    return payload

async def check_admin(payload: dict = Depends(check_jwt_token)):
    role = payload.get("role")
    if not role:
        raise HTTPException(status_code=403, detail="Mã token không chứa thông tin role")
    if role != "admin":
        raise HTTPException(status_code=403, detail="Người dùng không có quyền quản trị viên")
    return payload
