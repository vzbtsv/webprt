from sqlalchemy import Column, Integer, String, DateTime
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    age = Column(Integer)
    position = Column(String)
    speciality = Column(String)
    address = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    modified_date = Column(DateTime)

    def __repr__(self):
        return (f"{self.surname} {self.name} {self.age} "
                f"{self.position} {self.speciality}\n"
                f"{self.address} {self.email} {self.hashed_password}")
