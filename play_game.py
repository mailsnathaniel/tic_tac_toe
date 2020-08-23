import copy
import io_file
import metainfo
import gameinfo

# Creates an empty board
def create_board(m, n):
    return [['-' for j in range(n)] for i in range(m)]

# Main for 2 Players Pattern Based
def play_game():
    gametype = io_file.get_gametype_selection()
    metaObj = metainfo.metainfo(gametype) 
    m, n = 3, 3 ## Matrix MxN can be changed here
    board, winner, counter = create_board(m, n), 0, 1
    GameObj = gameinfo.GameInfo(metaObj)
    ioObj = io_file.io_file(metaObj)
    ioObj.print_board(board, m, n)
    player = 1

    while(counter<=9):
          pos, val = GameObj.Play(board, player)
          #print Board
          print("Board after " + str(counter) + " move")
          ioObj.print_board(board, m, n)
          #Get winning value
          winner = GameObj.Evaluate(board, player)
          
          if winner in [-1, 1, 2]:break #Break If Win or Draw
          if player==1: player=2 # Switch Player
          elif player==2: player=1
          counter += 1

    if winner in [1, 2]:
       return("Player %s has won" %winner)
    return("Match is Draw")

# Driver Code
print(str(play_game()))
