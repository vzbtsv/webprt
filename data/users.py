from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
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
    led_jobs = relationship(
        "Job",
        back_populates="team_leader",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            self.id,
            self.surname,
            self.name,
            self.age,
            self.position,
            self.speciality,
            self.address,
            self.email,
            self.hashed_password,
            self.modified_date
        )
