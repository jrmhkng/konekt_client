import socket, random
s = socket.socket()
host = "127.0.0.1"
print("Host is: " + host)
port = 12345         
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    
    print ('Got connection from', addr)
    recv_buff = c.recv(4096).decode()
    c.send('Thank you for connecting'.encode())
    
    while True:
        
       
        recv_buff = c.recv(4096).decode()
        print("They sent us:  \"" + recv_buff + "\"")
        print (recv_buff[:-2])
           
        if recv_buff[:-2] == "PUT":
            print ("Valid put command")
            #validate move
            #check win
            c.send("OK".encode())
            c.send(str(random.randint(0, 6)).encode())
        elif recv_buff == "q":
            c.send("GOODBYE".encode())
            break
        else:
            print ("Can't handle command")
            c.send("ERROR 3".encode())
            
    break
    
    c.close()
    