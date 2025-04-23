from employatron.employee import Employee
PAY_BANDS = {
    10:15,
    15:20,
    20:25,
    25:30
}

def promote_employee(employee:Employee):
    employee.set_hourly_rate(PAY_BANDS[employee.get_hourly_rate()])
    
