smallest = None
for value in [2,3,4,5,6,6,77,8,9]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
print(smallest)
