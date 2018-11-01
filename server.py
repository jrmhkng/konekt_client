import socket
s = socket.socket()
host = "127.0.0.1"
print("Host is: " + host)
port = 12345         
s.bind((host, port))
s.listen(5)
while True:
   c, addr = s.accept()
   print ('Got connection from', addr)
   c.send('Thank you for connecting'.encode())
   while True:
       recv_buff = c.recv(4096).decode()
       print("They sent us:  \"" + recv_buff + "\"")
       c.send(recv_buff.upper().encode())
   
