def print_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num
for number in print_even([1,2,3,4,56,7,8,9,12,45,77]):
    print(number)