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

@router.post('/update')
async def update_user(request:RequestUser,db:Session = Depends(get_db)):
    u_user = crud.update_user(db, 
                            id=request.parameter.id,
                            firstName = request.parameter.firstName,
                            lastName = request.parameter.lastName,
                            maidenName = request.parameter.maidenName,
                            age = request.parameter.age,
                            gender = request.parameter.gender,
                            email = request.parameter.email,
                            phone = request.parameter.phone,
                            birthDate = request.parameter.birthDate,
                            address = request.parameter.address,
                            city = request.parameter.city,
                            university = request.parameter.university)
    return Response( user = u_user)

@router.delete('/{id}')
async def delete(id:int,db:Session = Depends(get_db)):
    crud.remove_user(db,id=id)
    return dict(exclude_none=True)
