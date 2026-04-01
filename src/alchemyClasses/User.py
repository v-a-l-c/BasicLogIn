from sqlalchemy import Column, Integer, String, DateTime
from alchemyClasses import db


class User(db.Model):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=None)

    def __init__(self, name, email):
        pass

    def __str__(self):
        return f'User: {self.name}\nEmail: {self.email}'