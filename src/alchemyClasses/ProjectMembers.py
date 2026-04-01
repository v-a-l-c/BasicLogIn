from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from alchemyClasses import db


class ProjectMembers(db.Model):
    __tablename__ = 'project_members'
    id_user = Column(Integer, ForeignKey('user.id_user'), primary_key=True)
    id_project = Column(Integer, ForeignKey('project.id_project'), primary_key=True)
    role = Column(String, nullable=False)
    joined_at = Column(DateTime, nullable=False)

    def __init__(self, id_user, id_project, role):
        pass

    def __str__(self):
        return f"User with id {self.id_user} is working on project {self.id_project} as a {self.role}"