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

    def __regr__(self):
        return "Employee('{}', '{}', {})".format(Self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Riya', 'Gupta', 5000)
emp_2 = Employee('Joe', 'Biden', 10000)

print(emp_1) #regr method is responsible for this format of output
print(regr(emp_1))
print(str(emp_1))

print(emp_1 + emp_2)
print(len(emp_1))
