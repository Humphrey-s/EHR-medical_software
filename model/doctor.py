#!/usr/bin/python3
from model.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String


class Doctor(BaseModel, Base):

    __tablename__ = "doctors"
    name = ''
    national_id = ''
    email = ''
    Location = ''

    name = Column(String(256), nullable=False)
    national_id = Column(String(255), nullable=False)
    email = Column(String(256), nullable=True)
    County = Column(String(256), nullable=True)
    Location = Column(String(256), nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
