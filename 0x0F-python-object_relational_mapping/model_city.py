#!/usr/bin/python3
""" City module """

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City Class defining a table """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
