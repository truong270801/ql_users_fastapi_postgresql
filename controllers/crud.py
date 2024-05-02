from sqlalchemy.orm import Session
from database.schemas import RequestUser, Response
from repositories.user_repository import UserRepository

def create_user(db: Session, request: RequestUser):
    repository = UserRepository(db)
    return repository.create_user(request.parameter.dict())

def get_users(db: Session):
    repository = UserRepository(db)
    return repository.get_users()

def get_user_by_id(db: Session, id: int):
    repository = UserRepository(db)
    return repository.get_user_by_id(id)

def update_user(db: Session, id: int, request: RequestUser):
    repository = UserRepository(db)
    return repository.update_user(id, request.parameter.dict())

def delete_user(db: Session, id: int):
    repository = UserRepository(db)
    return repository.delete_user(id)
