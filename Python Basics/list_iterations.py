num = [2, True, False, 'hello world',[1,2,3], [], range(1,10,3), range(0,100)]
for x in num[6]:
    print(x)

print("***************************")

numbers = [2,3,4,5,6,67,8,9,90]
for num in numbers:
    print(num)

print("***************************")

num = [[], [1,2,3], 'hello', True, ['world', 3, range(1,2)], range(10)]
for number in num:
    print(number)

print("***************************")

num = [[], [1,2,3], 'hello', True, ['world', 3, range(1,2)], range(10)]
for element in num:
    if isinstance(element,list) or isinstance(element, range) or isinstance(element, str):
        print(str(element) + " : " + str(len(element)))