from abc import abstractmethod, ABC
from app.models import *
from app import db

entityDb = db.Model

class Create(ABC):
    @abstractmethod
    def create(self, entity: entityDb):
        pass

class Read(ABC):
    @abstractmethod
    def find_by_id(self, id:int):
        pass
    @abstractmethod
    def find_all(self):
        pass


class Update(ABC):
    @abstractmethod
    def update(self, entity:entityDb, id:int):
        pass

class Delete(ABC):
    @abstractmethod
    def delete(self, entity:entityDb, id:int):
        pass