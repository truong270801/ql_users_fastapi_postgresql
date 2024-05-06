from sqlalchemy import Column ,Integer, String, DATE

#from sqlalchemy.ext.declarative import declarative_base 
from database.database import Base
from sqlalchemy.orm import Session

#Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,autoincrement=True)
    firstName = Column(String)
    lastName = Column(String)
    maidenName = Column(String)
    age = Column(Integer)
    gender = Column(String)
    email = Column(String)
    phone = Column(String)
    birthDate = Column(DATE)
    address = Column(String)
    city = Column(String)
    university = Column(String)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)   

    def check_password(self, password: str) -> bool:
        return password == self.password
    
    def authenticate_user(db: Session, username: str, password: str):
        user = db.query(User).filter(User.username == username).first()
        if not user or not user.check_password(password):
            return None 
        return user 