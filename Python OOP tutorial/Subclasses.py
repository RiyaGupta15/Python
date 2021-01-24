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

class Developer(Employee):
    raise_amount = 1.15

    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print('---->', emp.fullname())


dev_1 = Developer('Riya', 'Gupta', 5000, 'Python')
dev_2 = Developer('Joe', 'Biden', 10000, 'Java')
mgr_1 = Manager('Due', 'Smith', 90000, [dev_1])

print(dev_1.email)
print(dev_2.lang)
print(dev_2.fullname())

print('--------------------')

print(dev_1.pay)
dev_1.apply_raise
print(dev_1.pay)

print('--------------------')

print(mgr_1.email)
mgr_1.print_employee()

mgr1.add_employee(dev_2)
mgr_1.print_employee()

mgr1.remove_employee(dev_1)
mgr_1.print_employee()
