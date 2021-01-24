class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{} {}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting Name')
        self.first = None
        self.last = None

emp_1 = Employee('Riya', 'Gupta')
emp_2 = Employee('Joe', 'Biden')

emp_1.fullname = 'Corey Schafar'

print(emp_1.first)
print(emp_2.email)
print(emp_1.fullname #Same as Employee.fullname(emp_1)

del emp_1.fullname
