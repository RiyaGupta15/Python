def hello():
    print("Hello")
print(type(hello()))
hello()

print("*************************")

def fullName(firstName, lastName):
    print(str(firstName) + " " + str(lastName))
fullName('Riya', 'Gupta')


print("*************************")


def fullName(firstName, lastName, middleName = " "):
    print(str(firstName) + " " + str(middleName) + " " + str(lastName))
fullName('Riya', 'Gupta')
fullName('Riya', 'Kansal', 'Gupta')
