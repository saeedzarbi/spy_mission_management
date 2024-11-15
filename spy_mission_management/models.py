# models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(20), nullable=False)  # نقش کاربر ('M', 'Q', 'Agent', 'Analyst')

    missions = relationship('Mission', back_populates='assigned_agent')
    equipments = relationship('Equipment', back_populates='assigned_agent')

class Mission(Base):
    __tablename__ = 'missions'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    assigned_to = Column(Integer, ForeignKey('users.id'))

    assigned_agent = relationship('User', back_populates='missions')

class Equipment(Base):
    __tablename__ = 'equipments'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    assigned_to = Column(Integer, ForeignKey('users.id'), nullable=True)

    assigned_agent = relationship('User', back_populates='equipments')
