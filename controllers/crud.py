from sqlalchemy.orm import Session
from models.model import User
from database.schemas import userSchema
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

#Cập nhật user     
def update_user(db: Session,
                id: int,
                firstName: str,
                lastName: str,
                maidenName: str,
                age: int,
                gender: str,
                email: str,
                phone: str,
                birthDate: date,
                address: str,
                city: str,
                university: str
                ):
    u_user = get_user_by_id(db=db, id=id)
    if u_user:
        u_user.firstName = firstName
        u_user.lastName = lastName
        u_user.maidenName = maidenName
        u_user.age = age
        u_user.gender = gender
        u_user.email = email
        u_user.phone = phone
        u_user.birthDate = birthDate
        u_user.address = address
        u_user.city = city
        u_user.university = university
        db.commit()
        db.refresh(u_user)
    return u_user


#Xóa user
def remove_user(db:Session, id=int):
    r_user = get_user_by_id(db=db,id=id)
    db.delete(r_user)
    db.commit()
