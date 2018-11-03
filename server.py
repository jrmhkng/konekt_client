import socket, random

def main():
    
    board = []
    
    def do_move(spot, player):
        spot -= 1
        size = len(board) - 1
        
        while size >= 0:
            if board[size][spot] == "*":
                board[size][spot] = player
                return False
            else:
                size -= 1
        
        return True
            
    def check_win_con(player):
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
                    
                        if board[row][column] == player and board[row][column_2] == player and \
                        board[row][column_3] == player and board[row][column_4] == player:
                            
                            return True
                except:
                    pass
                
                try:        #Win-con vertical
                    row_2 = row - 1
                    row_3 = row - 2
                    row_4 = row - 3
                    
                    if row_2 >= 0 and row_3 >= 0 and row_4 >= 0:
                    
                        if board[row][column] == player and board[row_2][column] == player and \
                        board[row_3][column] == player and board[row_4][column] == player:
                            
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
                    
                        if board[row][column] == player and board[row_2][column_2] == player \
                        and board[row_3][column_3] == player and board[row_4][column_4] == player:
                            
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
                        
                        if board[row][column] == player and board[row_2][column_2] == player \
                        and board[row_3][column_3] == player and board[row_4][column_4] == player:
                            
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
    
    def print_board():
        for row in board:
            print (" ".join(row))
        print ("-------------")
        print ("1 2 3 4 5 6 7")
    
   #--------------------------------------------------------# 
    
    for i in range(6):
        #here
        new_layer = []
        for x in range(7):
            new_layer.append("*")
        board.append(new_layer)
   
    s = socket.socket()
    host = "127.0.0.1"
    print("Host is: " + host)
    port = 12345         
    s.bind((host, port))
    s.listen(5)
    
    while True:
        c, addr = s.accept()
        
        print ('Got connection from', addr)
        c.send('Hey Man!'.encode())
        
        recv_buff = c.recv(4096).decode()
        if recv_buff == "SUP":
        
            c.send("GO AHEAD".encode())
            print ("Going through with connection")
            print ()
            while True:
                 
                try:
                    recv_buff = c.recv(4096).decode()
                except:
                    print ("Lost Connection")
                    print ("Terminating")
                    break
                
                print("They sent us: \"" + recv_buff + "\"")
                   
                if recv_buff[:-2] == "PUT":
                    print ("Valid put command")
                    player_move = recv_buff[-1]
                    print (player_move)
                    
                    if not player_move.isdigit():
                        print ("Not a digit")
                        c.send("ERROR 2".encode())
                        print ("Invalid column")
                        print ()
                        continue
                    
                    player_move = int(player_move)
                    if player_move < 0 or player_move > 7:
                        print ("Out of bounds")
                        c.send("ERROR 2".encode())
                        continue
                    
                    #validate move
                    #update
                    #check win
                    print ()
                    print ("PLAYER MOVE")
                    work = do_move(player_move, "X")
                    if work:
                        c.send("ERROR 1".encode())
                        print ("Column full")
                        print ()
                        continue
                    elif check_win_con("X"):
                        print ("Server lost, player won")
                        print ("Terminating connection")
                        c.send("LOSS".encode())
                        break
                    elif check_cat_game():
                        print ("It was a cat game")
                        print ("Terminating connection")
                        c.send("CAT GAME".encode())
                        break
                    
                    print ("They played in spot", recv_buff[:-1])
                    print_board()
                    
                    c.send("OK".encode())
                    print ("Sending okay")
                    move = random.randint(0, 6)
                    
                    #validate
                    #update
                    #check win
                    print ()
                    print ("SERVER MOVE")
                    while do_move(move, "O"):
                        move = random.randint(0, 6)
                        
                    print_board()
                        
                    if check_win_con("O"):
                        print ("Server won, player lost")
                        print ("Terminating connection")
                        c.send("WIN".encode())
                        break
                    elif check_cat_game():
                        print ("It was a cat game")
                        print ("Terminating connection")
                        c.send("CAT GAME".encode())
                        break
                    
                    c.send(str(move).encode())
                    print ("Server played at", move)
                elif recv_buff == "q":
                    print ("GOODBYE")
                    print ("Terminating connection")
                    c.send("GOODBYE".encode())
                    break
                else:
                    print ("Can't handle command")
                    try:
                        c.send("ERROR 3".encode())
                    except:
                        print ("Lost Connection")
                        print ("Terminating")
                        break
                    
                print ()
        else:
            print ("Imposter, you're not my client!")
            print ("Terminating shady connection")
                
        break
        
        c.close()


main()