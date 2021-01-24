isRaining = True
if isRaining:
    print("I need an umberella")
else:
    print("It is sunny today")
print("I am outside if-else statement")

print("***************************************")

isRaining = False
sunny = True
if isRaining:
    print("I need an umberella")
elif not isRaining and sunny:
    print("I will go to picnic")
else:
    print("I will stay home")
print("I am outside if-else statement")