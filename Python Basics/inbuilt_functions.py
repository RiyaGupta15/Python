def abs(number):
    return -number if number < 0 else number

print(abs(10))
print(abs(-5))

print("**************************")

def all(iterable):
    for element in iterable:
        if not bool(element):
            return False
    return True

print(all(range(0)))
print(all(range(0,1,2)))
print(all([0,1,2]))

print("**************************")

def any(iterable):
    for element in iterable:
        if bool(element):
            return True
    return False

print(all(range(0)))
print(all(range(0,1,2)))
print(all([0,1,2]))

print("**************************")