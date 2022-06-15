from tabnanny import check
from turtle import pos, position


game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

game_in_progress = True

winner = None

current_player = 'x'

def display_game_board():
    print(f'{game_board[0]}|{game_board[1]}|{game_board[2]}')
    print('-+-+-')
    print(f'{game_board[3]}|{game_board[4]}|{game_board[5]}')
    print('-+-+-')
    print(f'{game_board[6]}|{game_board[7]}|{game_board[8]}')


def main():
    display_game_board()

    while game_in_progress:
        handle_turn(current_player)

        check_if_game_over()

        change_player()

    if winner == 'x' or winner == 'o':
        print("Hurray! The winner is" + " " + winner)
    elif winner == None:
        print("It's a tie!")

def handle_turn(player):
    position = int(input('Please choose the postion from 1 to 9: '))
    position = position - 1
    game_board[position] = player
    display_game_board()

def check_if_game_over():
    check_winner()

def check_winner():
    global winner

    row_won = check_row()
    column_won = check_column()
    diagonal_won = check_diagonal()

    if row_won:
        winner = row_won
    elif column_won:
        winner = column_won
    elif diagonal_won:
        winner = diagonal_won
    else:
        winner = None
    return

def check_row():
    global game_in_progress
    first_row = game_board[0] == game_board[1] == game_board[2] != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9"
    second_row = game_board[3] == game_board[4] == game_board[5] != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9"
    third_row = game_board[6] == game_board[7] == game_board[8] != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9"

    if first_row or second_row or third_row:
        game_in_progress = False
    if first_row:
        return game_board[0]
    elif second_row:
        return game_board[3]
    elif third_row:
        return game_board[6]
    return

def check_column():
    global game_in_progress
    first_column = game_board[0] == game_board[3] == game_board[6] != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9"
    second_column = game_board[1] == game_board[4] == game_board[7] != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9"
    third_column = game_board[2] == game_board[5] == game_board[8] != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9"

    if first_column or second_column or third_column:
        game_in_progress = False
    if first_column:
        return game_board[0]
    elif second_column:
        return game_board[1]
    elif third_column:
        return game_board[2]
    return

def check_diagonal():
    global game_in_progress
    first_diagonal = game_board[0] == game_board[4] == game_board[8] != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9"
    second_diagonal = game_board[6] == game_board[4] == game_board[2] != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9"

    if first_diagonal or second_diagonal:
        game_in_progress = False
    if first_diagonal:
        return game_board[0]
    elif second_diagonal:
        return game_board[6]
    return

def change_player():
    global current_player

    if current_player == 'x':
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'
    return



main()