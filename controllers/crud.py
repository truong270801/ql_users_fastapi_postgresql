from sqlalchemy.orm import Session
from database.schemas import RequestUser, Response
from repositories.user_repository import UserRepository
#hàm thêm mới user
def create_user(db: Session, request: RequestUser):
    repository = UserRepository(db)
    return repository.create_user(request.parameter.dict())
#hàm lấy tất cả user
def get_users(db: Session):
    repository = UserRepository(db)
    return repository.get_users()
#hàm lấy user theo id
def get_user_by_id(db: Session, id: int):
    repository = UserRepository(db)
    return repository.get_user_by_id(id)
#hàm sửa user theo id
def update_user(db: Session, id: int, request: RequestUser):
    repository = UserRepository(db)
    return repository.update_user(id, request.parameter.dict())
#hàm xóa user theo id
def delete_user(db: Session, id: int):
    repository = UserRepository(db)
    return repository.delete_user(id)
