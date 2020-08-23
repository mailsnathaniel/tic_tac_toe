Execution Steps:
1. Install python3
2. pip3 install -r requirements.txt
3. python play_game.py


Design and Implementation Details:

I have a used these classes to design the game for 4 modes of play.
  1. metainfo.py - This class contains the constaints and attributes of every game types.
	   
  2. io_file.py - This class contains all the input and output for the game
	 
  3. gameinfo.py - This class contains the flow for every game type:
     - Method "Play" - Makes a move either by user input from command line or optimal move by computer.
     - Method "Evaluate" - Evalutes the board after every move and returns states win/draw.
     
  4. validate.py - This class contains all the evalution conditions for all 4 types of game.
  
  5. Algorithm: "Minimax" (minimax.py)
      - Minimax is a kind of backtracking algorithm. In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible. 
     
     I have used this algorithm here to find optimal move, assuming that human also plays optimally. 
      - Pattern based - input charecters are fixed, but positions are not fixed
      - Number based  - input characters are not fixed, but positions are fixed (used Magic Square 3x3)

  6. run pytest test_game.py (for running test cases)
