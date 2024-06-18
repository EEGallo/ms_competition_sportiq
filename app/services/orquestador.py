from saga import SagaBuilder, SagaError
from ms_user_sportiq.app.services import UserService
from ms_team_sportiq.app.services import TeamService
from ms_statistics_sportiq.app.services import StatisticService
from app.services.competition_services import CompetitionService


class Orquestador:
    
    """ Clase que implementa la funcionalidad de Orquestador en el patron SAGA de microservicios"""

    def funcionalidad(self) -> None:
        ms1 = UserService()
        ms2 = TeamService()
        ms3 = StatisticService()
        ms4 = CompetitionService()
        try:
            SagaBuilder.create()\
                .action(lambda: ms1.get_data(), lambda: ms1.get_compensation())\
                .action(lambda: ms2.get_data(), lambda: ms2.get_compensation())\
                .action(lambda: ms3.get_data(), lambda: ms3.get_compensation())\
                .action(lambda: ms4.get_data(), lambda: ms4.get_compensation())\
                .build().execute()
    
        except SagaError as e:
            print(e) # wraps the BaseException('same error happened')
