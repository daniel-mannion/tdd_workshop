from employatron.employee import Employee
from typing import Protocol

class ReportLike(Protocol):
    def append_entry(entry: dict)->None:
        ...

class InMemoryReport:
    def __init__(self):
        self.contents = {}
    def append_entry(self, entry:dict)->None:
        self.contents.update(entry)
    def get_contents(self)->dict:
        return self.contents


def produce_employee_report(employee:Employee, report_type=InMemoryReport):
    report = report_type()
    report.append_entry({'name':employee._name})
    report.append_entry({'role':employee._role})
    report.append_entry({'hourly_rate':employee._hourly_rate})
    return report



