import random
print(random.random())

print("***************************")

#To get value between 0 and 1000
print(random.random() * 1000)

print("***************************")

#To get value between 5000 and 1000
print((random.random() * 500) + 500)

print("***************************")

#To get value between a and b
def randomInteger(a,b):
    return int((b-a) * random.random() + a)
print(randomInteger(0,100))
print(randomInteger(10,20))
print(randomInteger(900,1000))