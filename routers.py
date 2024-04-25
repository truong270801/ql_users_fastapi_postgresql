from fastapi import APIRouter,HTTPException,Path,Depends
from database import get_db
from sqlalchemy.orm import Session
from schemas import  RequestUser,Response
import crud

router = APIRouter()

@router.post('/create')
async def create(request: RequestUser ,db: Session = Depends(get_db)):
    crud.create_user(db,user = request.parameter)
    return dict(exclude_none = True)

@router.get('/')
async def get(db: Session = Depends(get_db)):
    g_user = crud.get_user(db,0,100)
    return Response( user = g_user).dict(exclude_none=True)

@router.get('/{id}')
async def get_by_id(id:int,db:Session =Depends(get_db) ):
    g_idUser = crud.get_user_by_id(db,id)
    return Response(user=g_idUser).dict(exclude_none=True)
