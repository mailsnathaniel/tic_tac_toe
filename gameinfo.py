# importing all necessary libraries
import copy
import io_file
import minimax
import validate
import traceback

class GameInfo:
      def __init__(self, metaObj):
          self.metaObj = metaObj 
          self.minimaxObj = minimax.minimax(metaObj)
          self.validateObj = validate.Validate()
          self.ioObj = io_file.io_file(metaObj)

      def Play(self, board, player):
          if (self.metaObj.no_of_players==2) or (player==1):
             if self.metaObj.gametype in [1, 3]: 
                pos, val = self.ioObj.get_input_pattern_based(player)
             else:
                pos, val = self.ioObj.get_input_number_based(player)
          else:
             print("Please Wait while the computer makes the move")
             pos = self.minimaxObj.findBestMove(copy.deepcopy(board), '2', '1')
             val = player
             if self.metaObj.gametype==4:
                val = self.metaObj.nb_fixed_board_values.get(pos, '')

          board[pos[0]][pos[1]] = str(val)
          return pos, val

      def Evaluate(self, board, player):
          if player==1: win_num = self.metaObj.winning_number1 
          else: win_num = self.metaObj.winning_number2

          winner = self.validateObj.evaluate(board, win_num, player)
          return winner


if __name__=='__main__':
   board = [['-', 'O', 'X'],
          ['O', 'X', '-'],
          ['X', '-', '-']]
   pattern_map = {'X': 1, 'O': 2}
   print (TicTacToe(pattern_map).diag_win(board, 3)) ## Test case for Diag Win
   board = [['X', 'O', '-'],
          ['X', 'X', 'O'],
          ['X', '-', '-']]
   print (TicTacToe(pattern_map).col_win(board, 3)) ## Test case for Col Win
   board = [['X', 'X', 'X'],
          ['X', 'O', 'O'],
          ['O', '-', '-']]
   print (TicTacToe(pattern_map).row_win(board, 3)) ## Test case for Row Win
   board = [['8', '6', '1'],
          ['X', 'O', 'O'],
          ['O', '-', '-']]
   print (TicTacToe(pattern_map).row_win(board, 15)) ## Test case for Row Win
   board = [['1', '9', '5'],
          ['-', '-', '-'],
          ['-', '-', '-']]
   print (TicTacToe({}).row_win(board, 15)) ## Test case for Row Win
