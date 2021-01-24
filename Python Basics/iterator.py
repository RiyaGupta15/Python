r = range(10)
print((type(r)))
iterator = r.__iter__()
print(type(iterator))

print("******************")

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

print("******************")

while True:
    try:
        num = iterator.__next__()
        print(num)
    except:
        print("Loop has ended")
        break