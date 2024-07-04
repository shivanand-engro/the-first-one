# prompt: write a code thats lets us play tic tac toe with the computer, while displaying the board and updating after each move
#@title Tictactoe
import numpy as np
import random
from IPython.display import clear_output

def print_board(board):
  for row in board:
    for cell in row:
      # print("|")
      if cell == 0:
        print("| ", end=" ")
      elif cell == 1:
        print("|X", end=" ")
      elif cell == -1:
        print("|O", end=" ")
    print("|")
    print("----------")


def get_valid_moves(board):
  valid_moves = []
  for i in range(3):
    for j in range(3):
      if board[i][j] == 0:
        valid_moves.append((i, j))
  return valid_moves

def make_move(board, player, i, j):
  board[i][j] = player

def check_win(board, player):
  win_conditions = [
    [board[0][0], board[0][1], board[0][2]],
    [board[1][0], board[1][1], board[1][2]],
    [board[2][0], board[2][1], board[2][2]],
    [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],
    [board[0][0], board[1][1], board[2][2]],
    [board[2][0], board[1][1], board[0][2]],
  ]
  for condition in win_conditions:
    if all(cell == player for cell in condition):
      return True
  return False
# def bot_move(board):
#   win_conditions = [
#     [board[0][0], board[0][1], board[0][2]],
#     [board[1][0], board[1][1], board[1][2]],
#     [board[2][0], board[2][1], board[2][2]],
#     [board[0][0], board[1][0], board[2][0]],
#     [board[0][1], board[1][1], board[2][1]],
#     [board[0][2], board[1][2], board[2][2]],
#     [board[0][0], board[1][1], board[2][2]],
#     [board[2][0], board[1][1], board[0][2]],
#   ]
#   for condition in win_conditions:
#     if sum(condition) == 2:
      
def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_win(board, -1)
    if winner != 0:
        return winner * (10 - depth)
    if not available_moves(board):
        return 0
    
    if is_maximizing:
        max_eval = -np.inf
        for move in available_moves(board):
            board[move] = -1
            eval = minimax(board, depth + 1, False)
            board[move] = 0
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = np.inf
        for move in available_moves(board):
            board[move] = 1
            eval = minimax(board, depth + 1, True)
            board[move] = 0
            min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the bot
def best_move(board):
    best_val = -np.inf
    move = None
    for m in available_moves(board):
        board[m] = -1
        move_val = minimax(board, 0, False)
        board[m] = 0
        if move_val > best_val:
            best_val = move_val
            move = m
    return move
###########################################################################
def play_game():
  board = np.zeros((3, 3), dtype=int)
  player = 1
  i,j = -1,-1
  while True:
    clear_output()
    if(player==1):print_board(board)
    valid_moves = get_valid_moves(board)
    if not valid_moves:
      print_board(board)
      print("Draw!")
      break
    if player == 1:
    #   while
      k = int(input("Enter your move from numpad positions: "))
      j = (k+2)%3
      i = 2 - (k-1)//3
      # print(i,j)
    else:
    #   i, j = random.choice(valid_moves)
      i, j = best_move(board)
    if((i,j) in valid_moves):
      make_move(board, player, i, j)
      if check_win(board, player):
        print_board(board)
        print(f"Player {player} wins!")
        break
      player *= -1
    else:
      print("Invalid move")

play_game()
