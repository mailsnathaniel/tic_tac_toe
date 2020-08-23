import traceback

def get_gametype_selection():
    try:
       pos = input("Select Game Type from the below options:\n\
1: Two Player, Pattern based \n\
2: Two Player, Number based \n\
3: Single Player, Pattern based \n\
4: Single Player, Number based \n>")
       pos = int(pos.strip())
    except:
       print("Invalid Input - Please Provice Valid Input")
       return get_gametype_selection()

    if pos not in [1, 2, 3, 4]:
      print ("Invalid Input - Please Provice Valid Input")
      return get_gametype_selection()

    return pos

#Get Input For Player console
def get_player_input():
    try:
       pos = input("Enter Number of Players [1 or 2]: \n>")
       pos = int(pos)
    except:
       print ("Invalid Input - Please Provice Valid Input")
       return get_player_input()

    if pos not in [1, 2]:
       print ("Invalid Input - Please Provice Valid Input")
       return get_player_input()

    if pos==2:
       print("You Have Selected 2 Player Game.")
    else:
       print("You Are Now Playing Against Computer")

    return pos

class io_file:
    def __init__(self, metaObj):
        self.metaObj = metaObj

    def print_game_info(self, pos):
        if pos==1:
           print(" \n Player1: X \n Player2: O \nrow/col starts from 0")
        else:
           print(" \n Player1: range %s \n Player2: range %s \nrow/col starts from 0" %(str(self.metaObj.allowed_input1), str(self.metaObj.allowed_input2)))
        return pos

    #Pring board
    def print_board(self, board, m, n):
        pstr = ''
        my_dict = {}
        if self.metaObj.gametype in [1, 3]:
           my_dict = {'1': self.metaObj.disp_player1, '2': self.metaObj.disp_player2} 
        for i in range(m):
            pstr += "|"
            for j in range(n):
                p = str(board[i][j])
                p = my_dict.get(p, p)      
                pstr += str(p)+"|"
            pstr += "\n"
        print(pstr)
        return

    #Get Input From console
    def get_input_pattern_based(self, player):
        try:
             pos = input("Enter Position for %s Player Format: row,col:\n> "%player)
             pos = eval(pos)
             val = player
        except:
           print("Invalid Input - Please Provice Valid Input")
           return self.get_input_pattern_based(player)

        if not self.validate_input(pos, val):
           return self.get_input_pattern_based(player)

        self.metaObj.played_positions.append(pos)

        return pos, val

    #Get Input From console
    def get_input_number_based(self, player):
        if player==1:inputs = self.metaObj.allowed_input1
        else:inputs = self.metaObj.allowed_input2

        try:
            if self.metaObj.no_of_players==1:
                val = input("Enter Number for Player-%s: (Number should be in the range: %s):\n> "%(player, inputs))
                pos = self.metaObj.rev_nb_fixed_board_values[str(val)] 
                val = str(val)
            else:    
                val = input("Enter Position and Number for Player-%s Format: row,col|number (Number should be in the range: %s):\n> "%(player, inputs))
                pos, val = val.split('|')
                pos, val = pos.strip(), val.strip()
                pos, val = eval(pos), str(val)
        except:
           print("Invalid Input - Please Provice Valid Input")
           return self.get_input_number_based(player)

        if not self.validate_input(pos, val):
           print("Invalid Input2 - Please Provice Valid Input")
           return self.get_input_number_based(player)

        if (val not in inputs):
           print ("Invalid Input - Number Should be in the Range of %s" %str(inputs))
           return self.get_input_number_based(player)

        self.metaObj.played_positions.append(pos)
        inputs.remove(val)
        return pos, val

    def validate_input(self, pos, val):
        if type(pos) != tuple:
           print ("Invalid Input - Please Provice Position in Tuple Format (e.g. (0,0) for row=1, col=1)")
           return False

        if (pos not in [(i, j) for i in range(3) for j in range(3)]):
           print ("Invalid Input - Please Provice Position lies in 3x3 Matrix (e.g. (0,0) for row=1, col=1)")
           return False

        if pos in self.metaObj.played_positions:
           print("Position Already Filled")
           return False

        return True


if __name__=='__main__':
   obj = io_file()
