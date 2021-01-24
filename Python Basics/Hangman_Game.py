import random

name = input("Hello, what is name?")

print("Hello " +name+ ", let's  play Hangman!!!")

words = ["hello", "secret", "rainbow", "goal", "stay", "computer", "maths", "style", "power", "juice", "play"]
word = random.choice(words)
guess = ''
turns = 10

while turns > 0:
    count = 0
    for char in word:
        if char in guess:
          print (char)
        else:
            print("_")
            count += 1

    if count == 0:
        print("You won")
        break

    g = input("Guess a character")
    guess += g
    if g not in word:
        turns -= 1
        print("Wrong")

        print("You have " +str(turns)+ " turns left")

        if turns == 0:
            print("You lose")


