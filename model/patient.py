#!/usr/bin/python3
from model.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String


class Patient(BaseModel, Base):

    __tablename__ = "patients"
    name = ""
    national_id = ""
    email = ""
    Location = ""

    name = Column(String(256), nullable=False)
    national_id = Column(String(255), primary_key=True)
    email = Column(String(256))
    County = Column(String(256))
    Location = Column(String(256))

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
