from database.database import Base
from sqlalchemy import Column ,Integer, String, DATE



class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
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