# prompt: write a code thats lets us play tic tac toe with the computer, while displaying the board and updating after each move
#@title Tictactoe
import numpy as np
import random
from IPython.display import clear_output

superscripts = [
    'jj',
    '\u00b9',  # superscript 1
    '\u00B2',  # superscript 2
    '\u00B3',  # superscript 3
    '\u2074',  # superscript 4
    '\u2075',  # superscript 5
    '\u2076',  # superscript 6
    '\u2077',  # superscript 7
    '\u2078',  # superscript 8
    '\u2079'   # superscript 9
]
#+1//2
def print_board(board):
  for row in board:
    for cell in row:
      if cell == 0:
        print("|  ", end=" ")
      elif cell >0:
        print(f"|X{superscripts[cell]}", end=" ")
      elif cell < 0:
        print(f"|O{superscripts[(cell*-1)]}", end=" ")
    print("|")
    print("-------------")



def make_move(board, player, i, j, pboard, count):
  board[i][j] = player
  pboard[i][j] = player*count

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

      
def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]


def block(board, player):
   for m in available_moves(board):
      board[m] = player
      if check_win(board, player):
         board[m] = 0
         return m
      board[m] = 0
   return None


def best_move(board):
    check = block(board, -1)
    if check is not None: return check

    check = block(board, 1)
    if check is not None: return check

    return random.choice(available_moves(board))
###########################################################################

def play_game(player):
  print("--------------------------------------------------")
  print("New Game")
  board = np.zeros((3, 3), dtype=int)
  pboard = np.zeros((3, 3), dtype=int)
  count = 0
#   player = 1
  i,j = -1,-1
  while True:
    if(player==1):print_board(pboard)
    valid_moves = available_moves(board)
    if not valid_moves:
      print_board(pboard)
      print("Draw!")
      break
    if player == 1:
      k = int(input("Enter your move from numpad positions: "))
      j = (k+2)%3
      i = 2 - (k-1)//3
    else:
      i, j = best_move(board)
    if((i,j) in valid_moves):
      count+=1
      make_move(board, player, i, j, pboard, count)
      if check_win(board, player):
        print_board(pboard)
        player = "Bot" if player == -1 else "Player"
        print(f"{player} wins!")
        break
      player *= -1
    else:
      print("Invalid move")

while True :play_game(-1)
