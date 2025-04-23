from employatron.employee import Employee

# We no longer want the hourly rate to be a property of the Employee class
# Instead we'd prefer a PayBand class that contains: the information of the hourly rate
# Example of how we'd like to use the code below...

programmer_band = PayBand(hourly_rate=7.5)

em = Employee(name='myname', role='programmer', pay_band=programmer_band)

pay = em.calculate_pay(hours=432.13)

print(pay)