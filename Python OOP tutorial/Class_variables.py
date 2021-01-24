class Employee:

    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Riya', 'Gupta', 5000)
emp_2 = Employee('Joe', 'Biden', 10000)

print(emp_1.pay)
print(emp_1.apply_raise)
print(emp_1.raise_amount)
print(Employee.num_of_emp)

print('---------------------------------')

Employee.raise_amount = 1.10
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('---------------------------------')

emp_1.raise_amount = 1.10
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
