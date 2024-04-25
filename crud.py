from sqlalchemy.orm import Session
from model import User
from schemas import userSchema
from datetime import date

#Tạo dữu liệu cho user
def create_user(db:Session, user:userSchema):
    c_user = User(
                 firstName=user.firstName,
                 lastName=user.lastName,
                 maidenName=user.maidenName,
                 age=user.age,
                 gender=user.gender,
                 email=user.email,
                 phone=user.phone,
                 birthDate=user.birthDate,
                 address=user.address,
                 city=user.city,
                 university=user.university, )
    db.add(c_user)
    db.commit()
    db.refresh(c_user)
    return(c_user)

#Lấy tất cả dữ liệu user
def get_user(db: Session,skipt: int = 0, limit: int = 100):
    return db.query(User).offset(skipt).limit(limit).all()

#Lấy dữ liệu user từ id
def get_user_by_id(db:Session,id: int):
    return db.query(User).filter(User.id == id).first()
