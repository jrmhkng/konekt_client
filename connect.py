import random, os

def connect_main():
    os.system("clear")
    
    board = []
    
    def get_move():
        while True:
            print ()
            
            move = input("What column would you like to play in? > ")
            if move.isdigit():
                move = int(move)
                if move < 8:
                    return move
                else:
                    print ("That's not a good column")
                    print ()
                    
            else:
                print ("That's not a good column")
                print ()
                
    
    def do_move(spot, turn):
        spot -= 1
        size = len(board) - 1
        
        while size >= 0:
            if board[size][spot] == "*":
                if turn % 2 == 0:
                    board[size][spot] = "X"
                else:
                    board[size][spot] = "O"
                    
#I changed something here...