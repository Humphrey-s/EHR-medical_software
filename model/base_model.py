#!/usr/bin/python3
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel:

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        dic_t = {}
        key = str(self.__class__.__name__) + "." + str(self.id)
        dic_t[key] = self.__dict__
        return(str(dic_t))
