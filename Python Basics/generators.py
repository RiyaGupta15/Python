value = (x ** 2 for x in range(1, 11))
for element in value:
    print(element)

print("******************")

value = list(x ** 2 for x in range(1, 11))
print(value)

print("******************")

n = int(input("Enter a number "))
num = list(number for number in range(1, n+1))
print(num)

print("******************")

n = int(input("Enter a number "))
odd_even = list('even' if num % 2 == 0 else 'odd' for num in range(0, n+1))
print(odd_even)