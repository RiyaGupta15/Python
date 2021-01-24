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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Riya', 'Gupta', 5000)
emp_2 = Employee('Joe', 'Biden', 10000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Jane-Gupta-8000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1)

import datetime
my_date=datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

print('------------------------------')

Employee.set_raise_amount(1.15)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('------------------------------')

emp_1.set_raise_amount(1.15)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('------------------------------')
