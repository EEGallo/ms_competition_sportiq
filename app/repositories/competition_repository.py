from app import db
from app.models import Competition
from .repository_base import Create, Read, Update, Delete


class CompetitionRepository(Create, Read, Update, Delete):
        
    def __init__(self):
            self.__model = Competition

    def create(self, model: Competition):
        db.session.add(model)
        db.session.commit()
        return model


    def find_all(self):
        try:
            competitions = db.session.query(self.__model).all()
            return competitions
        except Exception as e:
            raise Exception('Error a obtener la lista de competiciones'  + str(e))
    

    def find_by_id(self, id):
        try:
            entity = db.session.query(self.__model).filter(self.__model.id == id).one()
            return entity
        except Exception as e:
            raise Exception('Error a obtener competición por id' + str(e))


    def update(self, entity: Competition):
            db.session.merge(entity)
            db.session.commit()
            return entity


    def delete(self, competition_id) -> bool:
        competition = Competition.query.get(competition_id)
        if competition:
            db.session.delete(competition)
            db.session.commit()
            return True
        return False