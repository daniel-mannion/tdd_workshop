class Employee:
    def __init__(self, name:str, role:str, hourly_rate:float):
        self._name = name
        self._role = role
        self._worked_hours = 0
        self.set_hourly_rate(hourly_rate)

    def log_hours(self, hours:float):
        self._worked_hours += hours

    def calculate_pay(self):
        return self._hourly_rate*self._worked_hours

    def set_hourly_rate(self, hourly_rate:int):
        self._hourly_rate = round(hourly_rate) #2001 out company has only integer hourly rates, if someone passes a float round to the nearest hourly rate. 

    def get_hourly_rate(self):
        return self._hourly_rate

    