import socket

host = '127.0.0.1'
port = 12345
mySocket = socket.socket()
mySocket.connect((host,port))

#game here











#message = input(" ? ")
#while message != 'q':
   #mySocket.send(message.encode())
   #data = mySocket.recv(1024).decode()
   #print ('Received from server: ' + data)
   #message = input(" ? ")
#mySocket.close()
