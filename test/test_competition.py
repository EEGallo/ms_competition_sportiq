import unittest
from flask import current_app
from app import create_app, db
from app.models.competition import Competition
from app.services.competition_services import CompetitionService

service = CompetitionService()

class CompetitionTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_competition(self):
        competition = Competition()  
        competition.category = "beginner" 
        competition.discipline = "voleyball"
        competition.start_date = "01/01/2024"
        competition.end_date = "01/01/2024"
        competition.team_event = True
        competition.winner = "Canguros"
        
        self.assertEqual(competition.category, "beginner")
        self.assertEqual(competition.discipline, "voleyball")
        self.assertEqual(competition.start_date, "01/01/2024")
        self.assertEqual(competition.end_date, "01/01/2024")
        self.assertEqual(competition.team_event, True)
        self.assertEqual(competition.winner, "Canguros")

    def test_create_competition(self):
        competition = self.__createcompetition()
        self.assertGreaterEqual(competition.id, 1)

    def __createcompetition(self):
        competition = Competition()
        competition.category = "beginner" 
        competition.discipline = "voleyball"
        competition.start_date = "01/01/2024"
        competition.end_date = "01/01/2024"
        competition.team_event = True
        competition.winner = "Canguros"
        service.create(competition)
        return competition

    def test_find_by_id(self):
        _ = self.__createcompetition()
        competition = service.find_by_id(1)
        self.assertIsNotNone(competition) 
        self.assertEqual(competition.category, "beginner")
        self.assertEqual(competition.discipline, "voleyball")
        self.assertEqual(competition.start_date, "01/01/2024")
        self.assertEqual(competition.end_date, "01/01/2024")
        self.assertEqual(competition.team_event, True)
        self.assertEqual(competition.winner, "Canguros")
        

    def test_find_all(self):
        _ = self.__createcompetition()
        competitions = service.find_all()
        self.assertGreaterEqual(len(competitions), 1)

    def test_update(self):
        competition=self.__createcompetition()
        competition.category = "beginner" 
        competition.discipline = "voleyball"
        competition.start_date = "01/01/2024"
        competition.end_date = "01/01/2024"
        competition.team_event = True
        competition.winner = "Canguros"
        service.update(competition, 1)
        result = service.find_by_id(1)
        self.assertEqual(competition.category, competition.category)
        self.assertEqual(competition.discipline, competition.discipline)
        self.assertEqual(competition.start_date, competition.start_date)
        self.assertEqual(competition.end_date, competition.end_date)
        self.assertEqual(competition.team_event, competition.team_event)
        self.assertEqual(competition.winner, competition.winner)

    def test_delete(self):
        _ = self.__createcompetition()
        service.delete(1)
        competitions = service.find_all()
        self.assertEqual(len(competitions), 0)

if __name__ == '_main_':
    unittest.main()