import validate

class minimax:
    ## in: board(list) out: bool(True/False)
    ## Checks if any moves left on the board? If Yes: return True else: False
    def __init__(self, gameObj):
        self.gameObj = gameObj
           
    def isMovesLeft(self, board):
        for i in range(3):
            for j in range(3):
                if (board[i][j]=='-'):
                    return True
        return False

    # Checks whether the player has three of their marks in a horizontal row
    def row_win(self, board, player):
        for x in range(len(board)):
            win = True
            for y in range(len(board)):
                if board[x][y] != player:
                    win = False
                    continue

            if win == True:
                return(win)
        return(win)

    # Checks whether the player has three
    # of their marks in a vertical row
    def col_win(self, board, player):
        for x in range(len(board)):
            win = True
            for y in range(len(board)):
                if board[y][x] != player:
                    win = False
                    continue

            if win == True:
                return(win)
        return(win)


    # Checks whether the player has three
    # of their marks in a diagonal row
    def diag_win(self, board, player):
        win = True

        for x in range(len(board)):
            if board[x][x] != player:
                win = False

        if not win:
           win = True
           j = len(board)-1
           for i in range(len(board)):
               if board[i][j-i] != player:
                  win = False

        return(win)


    #This is the evaluation function as discussed
    def evaluate(self, board, player, opponent):
        #Checking for Rows for X or O victory.
        Valobj = validate.Validate()
        win_p, win_o = self.gameObj.winning_number1, self.gameObj.winning_number2

        if Valobj.evaluate(board, win_p, player)==player:
           return +10
        elif Valobj.evaluate(board, win_o, opponent)==opponent:
           return -10

        #Else if none of them have won then return 0
        return 0

    def minimax(self, board, depth, isMax, player, opponent):
        score = self.evaluate(board, player, opponent)

        #If Maximizer has won the game return his/her
        #evaluated score
        if (score == 10):
            return score-depth

        #If Minimizer has won the game return his/her
        #evaluated score
        if (score == -10):
            return score+depth

        #If there are no more moves and no winner then
        #it is a tie
        if (self.isMovesLeft(board)==False):
            return 0

        if player=='1':
           input1 = self.gameObj.allowed_input1
           input2 = self.gameObj.allowed_input2
        else:   
           input1 = self.gameObj.allowed_input2
           input2 = self.gameObj.allowed_input1
        #If this maximizer's move
        if (isMax):
            best = -1000;
            #Traverse all cells
            for i in range(3):
               for j in range(3):
                    move= self.gameObj.nb_fixed_board_values.get((i, j), str(player)) 
                    if move not in input1: continue
                    #Check if cell is empty
                    if (board[i][j]=='-'):
                        #Make the move
                        board[i][j] = move;

                        #Call minimax recursively and choose
                        #the maximum value
                        best = max(best, self.minimax(board, depth+1, not isMax, player, opponent))

                        #Undo the move
                        board[i][j] = '-'

            return best-depth
        else:#If this minimizer's move
            best = 1000;
            #Traverse all cells
            for i in range(3):
               for j in range(3):
                    move = self.gameObj.nb_fixed_board_values.get((i, j), str(opponent)) 
                    if move not in input2: continue
                    #Check if cell is empty
                    if (board[i][j]=='-'):
                        #Make the move
                        board[i][j] = move;

                        #Call minimax recursively and choose the minimum value
                        best = min(best, self.minimax(board, depth+1, not isMax, player, opponent))

                        #Undo the move
                        board[i][j] = '-';

            return best+depth

    #This will return the best possible move for the player
    def findBestMove(self, board, player, opponent):
        if self.gameObj.gametype==3:
           player, opponent = opponent, player 
        bestVal = -1000;
        row = -1;
        col = -1;
        bval = -1

        #Traverse all cells, evaluate minimax function for all empty cells. And return the cell with optimal value.
        if player=='1':
           input1 = self.gameObj.allowed_input1
        else:   
           input1 = self.gameObj.allowed_input2


        for i in range(3):
            for j in range(3):
                move = self.gameObj.nb_fixed_board_values.get((i, j), str(player)) 
                #Check if cell is empty
                if move not in input1: continue
                if (board[i][j]=='-'):
                    #Make the move
                    board[i][j] = move

                    #compute evaluation function for this move.
                    moveVal = self.minimax(board, 0, False, player, opponent)

                    #Undo the move
                    board[i][j] = '-';

                    #If the value of the current move is more than the best value, then update best/
                    if (moveVal > bestVal):
                        row = i
                        col = j
                        bestVal = moveVal

        return (row, col)

if __name__=='__main__':
   ## Test case for next best move
   #board = [['1', '2', '-'],
   #       ['-', '1', '-'],
   #       ['-', '-', '-']]

   board = [['4', '-', '-'],
          ['-', '5', '-'],
          ['-', '-', '-']]

   gtype = 1
   import metainfo
   metaObj = metainfo.metainfo(1, 2)
   obj = minimax(metaObj)
   #x = obj.findBestMove(board, '1', '2')
   x = obj.findBestMove(board, '2', '1')
   print ('-->', x)
