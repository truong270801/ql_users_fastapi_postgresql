from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database.schemas import RequestUser, Response
from controllers import crud
from security.middleware_check import check_jwt_token,check_admin

router = APIRouter()
#Đường dẫn thêm user
@router.post('/create')
async def create_user(request: RequestUser, db: Session = Depends(get_db), token_payload: dict = Depends(check_jwt_token)):
    await check_admin(token_payload)
    created_user = crud.create_user(db, request)
    return Response(user=created_user).dict(exclude_none=True)
#Đường dẫn lấy tất cả user
@router.get('/')
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return Response(user=users).dict(exclude_none=True)
#Đường dẫn lấy user theo id
@router.get('/{id}')
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    return Response(user=user).dict(exclude_none=True)
#Đường dẫn sửa user theo id
@router.put('/{id}')
async def update_user(request: RequestUser, id: int, db: Session = Depends(get_db), token_payload: dict = Depends(check_jwt_token)):
    updated_user = crud.update_user(db, id, request)
    return Response(user=updated_user).dict(exclude_none=True)
#Đường dẫn xóa user theo id
@router.delete('/{id}')
async def delete_user(id: int, db: Session = Depends(get_db), token_payload: dict = Depends(check_jwt_token)):
    await check_admin(token_payload)
    deleted = crud.delete_user(db, id)
    return {"success": deleted}
