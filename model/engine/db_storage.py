#!/usr/bin/python3
from sqlalchemy import create_engine
from model.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from model.doctor import Doctor
from model.patient import Patient

classes = {"Doctor": Doctor, "Patient": Patient}

user = "agoda"
db = "medical_HR"
passwd = "48maran88"
host = "localhost"

class DBStorage:

    def __init__(self):

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db), pool_pre_ping=True)
        
    def new(self, obj):
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e
    def all(self, cls=None):

        dic_t = {}

        for classs in classes.keys():
            if cls is None or cls is classes[classs]:
                objs = self.__session.query(classes[classs]).all()
                for obj in objs:
                    dic_t[obj.__class__.__name__ + "." + obj.id] = obj

        return dic_t

    def reload(self):
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
        
    def save(self):
        self.__session.commit()
    def close():
        self.__session.close()
