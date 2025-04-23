from employee import Employee

hourly_rate = 10
em = Employee('alexa', 'programmer', hourly_rate)

worked_hours = 1
em.log_hours(1)
pay = em.calculate_pay()

print(pay)