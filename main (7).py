from random import randint
from time import sleep
from replit import clear
board = [' ']*10

def display(board):
  print()
  print(f'{board[0]} | {board[1]} | {board[2]}')
  print('---------')
  print(f'{board[3]} | {board[4]} | {board[5]}')
  print('---------')
  print(f'{board[6]} | {board[7]} | {board[8]}')
  print()

def assign():
  c = input("X or O : ").upper()
  if c == 'X':
    return ('X','O')
  else:
    return ('O','X')

def replacement(marker,board,space):
    board[space] = marker

def win(board,marker,turn):
  if board[0:3] == [marker]*3 or board[3:6] == [marker]*3 or board[6:9] == [marker]*3 or board[0:7:3] == [marker]*3 or board[1:8:3] == [marker]*3 or board[2:9:3] == [marker]*3 or board[0:9:4] == [marker]*3 or board[2:7:2] == [marker]*3:
    print(f'Player {turn} wins !')
    return True
  else:
    return False
    

def full(board):
  return all(space != ' ' for space in board)
  

def computer(board,marker,turn):
  while True:
    space = randint(0,8)
    if board[space] == ' ':
      replacement(marker,board,space)
      break
      
def human(board,marker,turn):
  space = int(input(f'P{turn} Enter Space : '))
  replacement(marker,board,space)
        
def welcome():
  print('Welcome to TIC TAC TOE !\n1. P vs P\n2. C vs P\n3. C vs C')
  gm = int(input('Choose Game Mode : '))
  if gm == 1:
    return (human,human)
  elif gm == 2:
    return (human,computer)
  else:
    return (computer,computer)
gameon = True

while gameon:
  clear()
  a,b = welcome()
  p1,p2 = assign()
  print(p1,p2)
  turn = randint(1,2)
  while not(full(board)):
    if turn==1:
      a(board,p1,turn)
      display(board)
      if win(board,p1,turn):
        break
      else:
        turn = 2
    else:
      b(board,p2,turn)
      display(board)
      if win(board,p2,turn):
        break
      else:
        turn = 1
          
  print('GAME OVER')
  gameon = False
  
          
      

  
    