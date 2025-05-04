from datetime import datetime, time
from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean, orm, Table, ForeignKey
from .db_session import SqlAlchemyBase

association_table = Table(
    'association',
    SqlAlchemyBase.metadata,
    Column('users', Integer, ForeignKey('users.id')),
    Column('jobs', Integer, ForeignKey('jobs.team_leader'))
)


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey("users.id"), nullable=True)
    job = Column(Text, nullable=True)
    work_size = Column(Integer, nullable=True)
    collaborators = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, default=datetime.now, nullable=True)
    is_finished = Column(Boolean, nullable=True)

    def __repr__(self):
        return (f"{self.team_leader} {self.job} {self.work_size} "
                f"{self.collaborators} {self.start_date}\n"
                f"{self.end_date} {self.is_finished}")
