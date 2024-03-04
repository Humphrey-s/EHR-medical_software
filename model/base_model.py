#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:

    
    def __init__(self, *args):
        
        if args is not None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().strftime("%Y: %m: %d, %H%Mhrs")

    def __str__(self):
        dic_t = {}
        key = self.__class__.__name__ + "." + self.id
        dic_t[key] = self.__dict__
        return(str(dic_t))
