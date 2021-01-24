"""
range object has 3 constructors:
range(stop)
range(start,stop)
range(start,stop,step)
"""

r = range(10)
print(r.start)
print(r.stop)
print(r.step)

print("************************")

r = range(10,100)
print(r.start)
print(r.stop)
print(r.step)

print("************************")

r = range(10,100,2)
print(r.start)
print(r.stop)
print(r.step)