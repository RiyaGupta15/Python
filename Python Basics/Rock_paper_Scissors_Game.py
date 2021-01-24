from random import randint

c = ["Rock", "Paper", "Scissors"]

computer = c[randint(0, 2)]

player = True

while player == True:
    player = input("Rock, Paper or Scissors?")
    print("Computer's input is: " +computer)
    if player == computer:
        print("Tie")
        inp = input("Do you want to play again? Y|N")
        if inp == "Y":
            player = True
        elif inp == "N":
            player = False
        else:
            print("Invalid input")
    elif player == "Rock":
        if computer == "paper":
            print("Computer covers player, hence computer wins")
            inp = input("Do you want to play again? Y|N")
            if inp == "Y":
                player = True
            elif inp == "N":
                player = False
            else:
                print("Invalid input")
        else:
            print("Computer is smashed by you, hence you win, Yayyyyyyy")
            inp = input("Do you want to play again? Y|N")
            if inp == "Y":
                player = True
            elif inp == "N":
                player = False
            else:
                print("Invalid input")
    elif player == "Paper":
        if computer == "scissors":
            print("Computer cuts you, hence computer wins")
            inp = input("Do you want to play again? Y|N")
            if inp == "Y":
                player = True
            elif inp == "N":
                player = False
            else:
                print("Invalid input")
        else:
            print("Computer is covered by you, hence you win, Yayyyyy")
            inp = input("Do you want to play again? Y|N")
            if inp == "Y":
                player = True
            elif inp == "N":
                player = False
            else:
                print("Invalid input")
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer smashed you, hence computer wins")
            inp = input("Do you want to play again? Y|N")
            if inp == "Y":
                player = True
            elif inp == "N":
                player = False
            else:
                print("Invalid input")
        else:
            print("Computer is cutted by you, hence you win, Yayyyyy")
            inp = input("Do you want to play again? Y|N")
            if inp == "Y":
                player = True
            elif inp == "N":
                player = False
            else:
                print("Invalid input")
    else:
        print("Invalid input")
        inp = input("Do you want to play again? Y|N")
        if inp == "Y":
            player = True
        elif inp == "N":
            player = False
        else:
            print("Invalid input")


