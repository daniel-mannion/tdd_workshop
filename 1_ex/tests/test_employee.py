from employatron.employee import Employee
from employatron.promoter import promote_employee
def test_promotes_employee():
    hourly_rate = 10
    em = Employee('test','test role', hourly_rate)
    promote_employee(em)
    assert em.get_hourly_rate() == 15

def test_ensures_non_int_rounded_to_int():
    hourly_rate = 10.5
    em = Employee('test','test role', hourly_rate)
    promote_employee(em)
    assert em.get_hourly_rate() == 15 

