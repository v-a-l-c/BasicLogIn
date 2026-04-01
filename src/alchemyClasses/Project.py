from sqlalchemy import Column, Integer, String, DateTime
from alchemyClasses import db


class Project(db.Model):
    __tablename__ = 'project'
    id_project = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_date = Column(DateTime, default=None)

    def __init__(self, name, description, start_date):
        pass

    def __str__(self):
        return f"Project: {self.name}"