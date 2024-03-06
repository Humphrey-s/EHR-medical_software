from model.base_model import BaseModel
from model.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
