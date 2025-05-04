from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )
    job = Column(Text)
    work_size = Column(Integer)
    collaborators = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime, default=datetime.now)
    is_finished = Column(Boolean, default=False)
    team_leader = relationship("User", back_populates="led_jobs")

    def all_content(self):
        return (
            self.id,
            self.team_leader_id,
            self.job,
            self.work_size,
            self.collaborators,
            self.start_date.isoformat() if self.start_date else None,
            self.end_date.isoformat() if self.end_date else None,
            self.is_finished
        )

    def __repr__(self):
        return f'{self.id},\
        {self.team_leader_id},\
        {self.job},\
        {self.work_size},\
        {self.collaborators},\
        {self.start_date.isoformat() if self.start_date else None},\
        {self.end_date.isoformat() if self.end_date else None},\
        {self.is_finished}'
