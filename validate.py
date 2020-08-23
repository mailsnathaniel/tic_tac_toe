
class Validate:
    def __init__(self):
        pass

    # Checks whether the player has three of their marks in a horizontal row
    def row_win(self, board, win_num):
        for x in range(len(board)):
            tmp = []
            for y in range(len(board)):
                if board[x][y]=='-': continue
                p = board[x][y]
                tmp.append(int(p))

            if len(tmp)!=3: continue

            if (sum(tmp)==win_num):
                return True

        return False

    # Checks whether the player has three # of their marks in a vertical row
    def col_win(self, board, win_num):
        for x in range(len(board)):
            tmp = []
            for y in range(len(board)):
                if board[y][x]=='-': continue
                p = board[y][x]
                tmp.append(int(p))

            if len(tmp)!=3: continue
            if (sum(tmp)==win_num):
                return True
        return False

    # Checks whether the player has three
    # of their marks in a diagonal row
    def diag_win(self, board, win_num):
        tmp = []
        for x in range(len(board)):
            if board[x][x]=='-': continue
            p = board[x][x]
            tmp.append(int(p))

        if len(tmp)==3 and (sum(tmp)==win_num):
           return True

        tmp = []
        j = len(board)-1
        for i in range(len(board)):
            if board[i][j-i]=='-': continue
            p = board[i][j-i]
            tmp.append(int(p))

        if len(tmp)==3 and (sum(tmp)==win_num):
           return True

        return False

    # Evaluates whether there is a winner or a tie
    def evaluate(self, board, win_num, player):
        winner = 0
        if (self.row_win(board, win_num) or self.col_win(board, win_num) or self.diag_win(board, win_num)):
            winner = player

        if (not [c for row in board for c in row if c == '-']) and winner == 0:
            winner = -1

        return winner

if __name__=='__main__':
   obj = Validate()
   board = [['-', '2', '1'],
          ['2', '1', '-'],
          ['1', '-', '-']]
   print (obj.diag_win(board, 3)) ## Test case for Diag Win
   board = [['1', '2', '-'],
          ['1', '1', '2'],
          ['1', '-', '1']]
   print (obj.col_win(board, 3)) ## Test case for Col Win
   board = [['1', '1', '1'],
          ['1', '2', '2'],
          ['2', '-', '-']]
   print (obj.row_win(board, 3)) ## Test case for Row Win
   board = [['8', '6', '1'],
          ['1', '1', '1'],
          ['2', '-', '-']]
   print (obj.row_win(board, 15)) ## Test case for Row Win
   board = [['1', '9', '5'],
          ['-', '-', '-'],
          ['-', '-', '-']]
