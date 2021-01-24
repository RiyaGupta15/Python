import random

# input would be either X or O.
game_input = ['None', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


# This function is used to design the board game
def board_game(game_input):
    print(game_input[1] + '|' + game_input[2] + '|' + game_input[3] + '|')
    print(game_input[4] + '|' + game_input[5] + '|' + game_input[6] + '|')
    print(game_input[7] + '|' + game_input[8] + '|' + game_input[9] + '|')


# Player chooses the marker and if marker is none of X or O then the user will ask to input again
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player1: Please choose your marker")
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# This function is used to mark the position of given input
def position_marker(game_input, marker, position):
    game_input[position] = marker


# This checks the cases where the player wins
def win_game(game_input, marker):
    return ((game_input[1] == game_input[2] == game_input[3] == marker) or (
                game_input[4] == game_input[5] == game_input[6] == marker)
            or (game_input[7] == game_input[8] == game_input[9] == marker) or (
                        game_input[1] == game_input[4] == game_input[7] == marker)
            or (game_input[2] == game_input[5] == game_input[8] == marker) or (
                        game_input[3] == game_input[6] == game_input[9] == marker)
            or (game_input[1] == game_input[5] == game_input[9] == marker) or (
                        game_input[3] == game_input[5] == game_input[7] == marker))


# This function is used to select number of players
def choose_player():
    player = random.randint(1, 2)
    if player == '1':
        return 'player1'
    else:
        return 'player2'


# Check if there are empty spaces
def space(game_input, position):
    return game_input[position] == ' '


# Checks empty spaces in full board
def full_board_check(game_input):
    for i in range(1, 10):
        if space(game_input, i):
            return False
    return True


# player choice of position
def player_choice(game_input):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space(game_input, position):
        position = int(input("Please enter your choice of position[1-9]"))
    return position


# Would you like to play again
def play_again():
    choice = input("Would you like to play again [Y|N]")
    return choice == "Y"


# Game mechanism
while True:

    the_board = [' '] * 10
    player_1, player_2 = player_input()
    print(player_1 + ' is playre_1 sign')
    print(player_2 + ' is playre_2 sign')

    turn = choose_player()
    print(turn + ' will Play first')

    play_game = input('Ready to play[Y/N]: ')

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'player_1':
            board_game(the_board)
            position = player_choice(the_board)

            position_marker(the_board, player_1, position)

            if win_game(the_board, player_1):
                board_game(the_board)
                print('Player 1 has Won, Yeyeyeyey')
                game_on = False
            else:
                if full_board_check(the_board):
                    board_game(the_board)
                    print('Game Tie')
                    game_on = False

                else:
                    turn = 'player_2'
        else:
            board_game(the_board)
            position = player_choice(the_board)

            position_marker(the_board, player_2, position)

            if win_game(the_board, player_2):
                board_game(the_board)
                print('Player 2 has Won, Yeyeyeyey')
                game_on = False
            else:
                if full_board_check(the_board):
                    board_game(the_board)
                    print('Game Tie')
                    game_on = False

                else:
                    turn = 'player_1'

    if not play_again():
        break