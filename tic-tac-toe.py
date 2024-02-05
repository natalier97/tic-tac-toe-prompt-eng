

# X = 'x'
# O = 'o'
# EMPTY = ' '

# board = [print('\n'),
#     [X, 0, EMPTY],
#     print('\n'),
#     [],
#     print('\n'),
#     []
# ]

# print(board)


# board = [' ' for _ in range(9)]

# # Function to print the Tic-Tac-Toe board
# def print_board(board):
#     print(f'{board[0]} | {board[1]} | {board[2]}')
#     print('-' * 9)
#     print(f'{board[3]} | {board[4]} | {board[5]}')
#     print('-' * 9)
#     print(f'{board[6]} | {board[7]} | {board[8]}')

# print(print_board(board))

import random
from rich import print
from rich.markup import escape
from rich.console import Console
from rich.emoji import Emoji

console = Console()

# Initialize the Tic-Tac-Toe board as a list of empty cells
board = [' ' for _ in range(9)]
cat_emoji = Emoji("cat")

# Function to print the Tic-Tac-Toe board
# def print_board(board):
#     table = "|[bold] 1 | 2 | 3 [/bold]|\n|[bold] 4 | 5 | 6 [/bold]|\n|[bold] 7 | 8 | 9 [/bold]|"
#     for row in board:
#         for cell in row:
#             table = table.replace(str(cell), f"[bold]{escape(cell)}[/bold]")
#     console.print(f"\n{table}\n")

# Function to print the Tic-Tac-Toe board
def print_board(board):
    table = "|[bold] {} | {} | {} [/bold]|\n|[bold] {} | {} | {} [/bold]|\n|[bold] {} | {} | {} [/bold]|".format(
        *[num if cell == ' ' else cell for num, cell in enumerate(board, start=1)]
    )

    for symbol in ['X', 'O']:
        table = table.replace(str(symbol), f"[bold]{escape(symbol)}[/bold]", 1)  # Replace only the first occurrence

    console.print(f"\n{table}\n")


# Function to get the human player's choice of symbol
def get_player_symbol():
    while True:
        player_symbol = input("Choose 'X' or 'O' as your symbol: ").upper()
        if player_symbol in ['X', 'O']:
            return player_symbol
        else:
            print("Invalid choice. Please enter 'X' or 'O'.")

# Function to get the human player's move
def get_human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")

# Function for the computer's random move
def computer_random_move(board):
    empty_cells = [i for i in range(9) if board[i] == ' ']
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None  # No available moves

def check_win(board, player_symbol):
    # Check rows for a win
    for i in range(0, 9, 3):
        if all(board[i + j] == player_symbol for j in range(3)):
            return True

    # Check columns for a win
    for i in range(3):
        if all(board[i + j] == player_symbol for j in range(0, 9, 3)):
            return True

    # Check diagonals for a win
    if all(board[i] == player_symbol for i in range(0, 9, 4)) or all(board[i] == player_symbol for i in range(2, 7, 2)):
        return True

    return False

 # Main game loop
def main():
    player_symbol = get_player_symbol()
    computer_symbol = 'X' if player_symbol == 'O' else 'O'
    player_turn = True  # Human player goes first

    while True:
        print_board(board)

        if player_turn:
            move = get_human_move(board)
            board[move] = player_symbol
        else:
            computer_move = computer_random_move(board)
            if computer_move is not None:
                board[computer_move] = computer_symbol
            else:
                print(f"CAT game{cat_emoji}")
                break

        # Check for a win condition
        if check_win(board, player_symbol):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif check_win(board, computer_symbol):
            print_board(board)
            print("Computer wins! You lose.")
            break

        # Check for a draw condition
        if all(cell != ' ' for cell in board):
            print_board(board)
            print(f"CAT game{cat_emoji}")
            break

        # Switch turns
        player_turn = not player_turn



    # while True:
    #     print_board(board)

    #     if player_turn:
    #         move = get_human_move(board)
    #         board[move] = player_symbol
    #     else:
    #         computer_move = computer_random_move(board)
    #         if computer_move is not None:
    #             board[computer_move] = computer_symbol
    #         else:
    #             print(f"CAT game{cat_emoji}")
    #             break



    # while True:
    #         print_board(board)

    #         if player_turn:
    #             move = get_human_move(board)
    #             board[move // 3][move % 3] = player_symbol
    #         else:
    #             computer_move = computer_random_move(board)
    #             if computer_move is not None:
    #                 board[computer_move // 3][computer_move % 3] = computer_symbol
    #             else:
    #                 print("It's a draw!")
    #                 break

    #         # Check for a win condition
    #         if check_win(board, player_symbol):
    #             print_board(board)
    #             print("Congratulations! You win!")
    #             break
    #         elif check_win(board, computer_symbol):
    #             print_board(board)
    #             print("Computer wins! You lose.")
    #             break

    #         # Check for a draw condition
    #         if all(cell != ' ' for row in board for cell in row):
    #             print_board(board)
    #             print(f"CAT game{cat_emoji}")
    #             break

    #         # Switch turns
    #         player_turn = not player_turn
print(main())
