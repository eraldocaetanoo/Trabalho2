from datetime import datetime, timedelta

class avancarData():
    def avancardt(self,dias):
        data_atual = datetime.today() + timedelta(days=dias)
        return data_atual
