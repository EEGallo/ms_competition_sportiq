import requests
from saga import SagaBuilder, SagaError

class AtomicProcess:
    def execute_ms_user(self):
        result = requests.get("http://localhost:5001/api/v1")
        if result.status.code != 200:
            result = self.compensation_ms_user()
        return result
    
    def compensation_ms_user(self):
        result = requests.get("http://localhost:5001/api/v1")
        return result
    
    def execute_ms_team(self):
        result = requests.get("http://localhost:5002/api/v1")
        if result.status.code != 200:
            result = self.compensation_ms_team()
        return result

    def compensation_ms_team(self):
        result = requests.get("http://localhost:5002/api/v1")
        self.compensation_ms_user()
        return result
    
    def execute_ms_statistics(self):
        result = requests.get("http://localhost:5003/api/v1")
        if result.status.code != 200:
            result = self.compensation_ms_statistics()
        return result

    def compensation_ms_statistics(self):
        result = requests.get("http://localhost:5003/api/v1")
        self.compensation_ms_team()
        self.compensation_ms_statistics()
        return result
    
    def execute(self):
        ms1 = self.execute_ms_user()
        ms2 = self.execute_ms_team()
        ms3 = self.execute_ms_statistics()
        
        try:
            SagaBuilder.create()\
                .action(lambda: ms1.get_data(), lambda: ms1.get_compensation())\
                .action(lambda: ms2.get_data(), lambda: ms2.get_compensation())\
                .action(lambda: ms3.get_data(), lambda: ms3.get_compensation())\
                .build().execute()
        
        except SagaError as e:
            print(e)
        #if ms1.status_code == 200 and ms2.status_code == 200 and ms3.status_code == 200:
        #    return ms3
        #else:
        #    return self.compensation_ms3()