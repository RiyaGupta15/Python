import random

name = input("Hello, Whats your name?")
print("Hello " +name)
print("Okay " +name+ " I am going to guess a number between 1 to 10")
print("Now guess what's the number: ")

number = random.randint(1,10)

count = 0

while(count >= 0):
    guess = int(input())
    count += 1
    if guess < number:
        print("Your number is too small")
    if guess > number:
        print("Your number is too big")
    if guess == number:
        break

if guess == number:
    print("You guessed the number in " +str(count)+ "turns")
else:
    print("You didn't guessed the number. The correct number was " +str(number))
