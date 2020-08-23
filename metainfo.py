class metainfo:
    def __init__(self, gametype):
        self.board_values = {}
        self.played_positions = []
        self.gametype = gametype
        self.nb_fixed_board_values = {} 
        self.rev_nb_fixed_board_values = {}
        if gametype==1:
           self.name = 'PB'
           self.disp_player1 = 'X'
           self.disp_player2 = 'O'
           self.winning_number1 = 3 
           self.winning_number2 = 6 
           self.allowed_input1 = ['1']
           self.allowed_input2 = ['2']
           self.no_of_players = 2
        elif gametype==2:
           self.name = 'NB'
           self.disp_player1 = ''
           self.disp_player2 = ''
           self.winning_number1 = 15 
           self.winning_number2 = 15 
           self.allowed_input1 = ['1', '3', '5', '7', '9']
           self.allowed_input2 = ['2', '4', '6', '8']
           self.no_of_players = 2
        elif gametype==3:
           self.name = 'PB'
           self.disp_player1 = 'X'
           self.disp_player2 = 'O'
           self.winning_number1 = 3 
           self.winning_number2 = 6 
           self.allowed_input1 = ['1']
           self.allowed_input2 = ['2']
           self.no_of_players = 1
        elif gametype==4:
           self.name = 'NB'
           self.disp_player1 = ''
           self.disp_player2 = ''
           self.winning_number1 = 15 
           self.winning_number2 = 15 
           self.allowed_input1 = ['1', '3', '5', '7', '9']
           self.allowed_input2 = ['2', '4', '6', '8']
           self.no_of_players = 1
           self.nb_fixed_board_values = {
                                               (0, 0): '4', (0, 1): '3', (0, 2): '8', 
                                               (1, 0): '9', (1, 1): '5', (1, 2): '1', 
                                               (2, 0): '2', (2, 1): '7', (2, 2): '6'
                                           }

           for k, vs in self.nb_fixed_board_values.items():
               self.rev_nb_fixed_board_values[vs] = k

    def __del__(self):
        del self.name
        del self.allowed_input1
        del self.allowed_input2
        del self.winning_number1
        del self.winning_number2
