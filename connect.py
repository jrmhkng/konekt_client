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
                return
            else:
                size -= 1
        
        if turn % 2 == 0:
            print ("That column is full, try again")
            new_move = get_move()
            do_move(new_move, turn)
        else:
            new_move = random.randint(0, 6)
            do_move(new_move, turn)
            
            
    def print_board():
        for row in board:
            print (" ".join(row))
        print ("-------------")
        print ("1 2 3 4 5 6 7")
        
        
    def check_win_con():
        size = len(board)
        size -= 1
        
        while size >= 0:
            for x in range(7):
                
                row = size
                column = x
                
                try:        #Win-con horizontal
                    column_2 = column + 1
                    column_3 = column + 2
                    column_4 = column + 3
                    
                    if column_2 >= 0 and column_3 >= 0 and column_4 >= 0:
                    
                        if board[row][column] == "X" and board[row][column_2] == "X" and \
                        board[row][column_3] == "X" and board[row][column_4] == "X":
                            
                            return True
                except:
                    pass
                
                try:        #Win-con vertical
                    row_2 = row - 1
                    row_3 = row - 2
                    row_4 = row - 3
                    
                    if row_2 >= 0 and row_3 >= 0 and row_4 >= 0:
                    
                        if board[row][column] == "X" and board[row_2][column] == "X" and \
                        board[row_3][column] == "X" and board[row_4][column] == "X":
                            
                            return True
                except:
                    pass
                
                try:        #Win-con slanted right
                    
                    row_2 = row - 1
                    row_3 = row - 2
                    row_4 = row - 3
                    column_2 = column + 1
                    column_3 = column + 2
                    column_4 = column + 3
                    
                    if row_2 >= 0 and row_3 >= 0 and row_4 >= 0 and column_2 >= 0 \
                    and column_3 >= 0 and column_4 >= 0:
                    
                        if board[row][column] == "X" and board[row_2][column_2] == "X" \
                        and board[row_3][column_3] == "X" and board[row_4][column_4] == "X":
                            
                            return True
                        
                except:
                    pass
        
                try:    #Win-con slanted left
                    
                    row_2 = row - 1
                    row_3 = row - 2
                    row_4 = row - 3
                    column_2 = column - 1
                    column_3 = column - 2
                    column_4 = column - 3
                   
                    if row_2 >= 0 and row_3 >= 0 and row_4 >= 0 and column_2 >= 0 \
                    and column_3 >= 0 and column_4 >= 0:
                        
                        if board[row][column] == "X" and board[row_2][column_2] == "X" \
                        and board[row_3][column_3] == "X" and board[row_4][column_4] == "X":
                            
                            return True
                except:
                    pass
                
            size -= 1
       
         
    def check_cat_game():
        cat_game = True
        
        for i in range(len(board)):
            for x in range(7):
                if board[i][x] == "*":
                    cat_game = False
                    
        return cat_game
    
#----------------------------------------------------------------------------#
        
    for i in range(6):
        new_layer = []
        for x in range(7):
            new_layer.append("*")
        board.append(new_layer)
        
    turn = 0
    while True:
        print_board()
        print()
        
        if turn % 2 == 0:
            move = get_move()
            do_move(move, turn)
        else:
            move = random.randint(0, 6)
            do_move(move, turn)
            print ("The computer played in column", move)
        
        if check_win_con():
            print_board()
            print ("YOU WON!")
            break
        elif check_cat_game():
            print_board()
            print ("No one won")
            break
            
        os.system("clear")
        turn += 1
        
connect_main()
                    