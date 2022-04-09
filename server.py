import socket

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host="192.168.1.38"
#host=socket.gethostname()
port=12000
s.bind((host,port))
s.listen(10)
print("host: " + host +" is waiting for Connection")

while True:
    c,addr=s.accept()
    print("Client connected")
    while True:
        content=c.recv(100).decode()
        if not content:
            print("No content, disconnect")
            break
        print (content)

