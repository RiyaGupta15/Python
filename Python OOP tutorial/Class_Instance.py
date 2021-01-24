class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Riya', 'Gupta', 5000)
emp_2 = Employee('Joe', 'Biden', 10000)

print(emp_1.first)
print(emp_2.email)
print(emp_1.fullname()) #Same as Employee.fullname(emp_1)
