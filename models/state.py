#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, relationship

class State(BaseModel):
    """ State class """
    __tablename__ = 'State'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="State", cascade="Delete")