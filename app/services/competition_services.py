from app.repositories import CompetitionRepository
from app import db
from sqlalchemy.orm.exc import NoResultFound

class CompetitionService():
    def __init__(self):
        self.__repository = CompetitionRepository()


    def create(self, entity):
        return self.__repository.create(entity)
    

    def find_all(self):
        try:
            competitions = self.__repository.find_all()
            if competitions:
                return competitions
            else:
                return []
            
        except Exception as e:
            raise Exception('Error al obtener la lista de competiciones' + str(e))

    
    def find_by_id(self, entity_id):
        try:
            entity = self.__repository.find_by_id(entity_id)
            if entity:
                return entity
            else:
                return None 
        except NoResultFound:
            return None
        except Exception as e:
            raise Exception('Error al obtener competiciones por id: ' + str(e))


    
    def update(self, entity_id, updated_fields):
        try:
            competition = self.__repository.find_by_id(entity_id)

            if competition:
                for field, value in updated_fields.items():
                    setattr(competition, field, value)

                db.session.commit()

            return competition
        except Exception as e:
            raise Exception('Error al actualizar la competición: ' + str(e))
    
    def delete(self, entity_id):
        return self.__repository.delete(entity_id) 