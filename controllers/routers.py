from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from database.database import get_db
from database.schemas import RequestUser, Response
from controllers import crud

router = APIRouter()

@router.post('/create')
async def create_user(request: RequestUser, db: Session = Depends(get_db)):
    created_user = crud.create_user(db, request)
    return Response(user=created_user).dict(exclude_none=True)

@router.get('/')
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return Response(user=users).dict(exclude_none=True)

@router.get('/{id}')
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    return Response(user=user).dict(exclude_none=True)

@router.put('/{id}')
async def update_user(request: RequestUser, id: int, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, id, request)
    return Response(user=updated_user).dict(exclude_none=True)

@router.delete('/{id}')
async def delete_user(id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, id)
    return {"success": deleted}
