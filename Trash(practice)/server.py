from socket import *
s1=socket()
s1.bind(("Localhost",1200))
s1.listen(5)
print("Waiting for connection")
con,add=s1.accept()
print("Client Connected")
meg=input("enter msg:")
con.send(msg.encode())