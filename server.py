import socket
import uart_SC08A

DEBUG=True

print ("")
print ("")
print ("INFO: =====server started=====")

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host="192.168.1.38"
#host=socket.gethostname()
port=12000
s.bind((host,port))
s.listen(10)
print("INFO: host: " + host +" is waiting for Connection")


while True:
    c,addr=s.accept()
    print("Client connected")
    try:
        ser = uart_SC08A.start_uart_conn()
        if DEBUG: print("INFO: uart connection started")
        if DEBUG: print(ser)
    except:
        print("ERROR: can't get uart connection to SC08A")
    while True:
        content=c.recv(100).decode()
        if not content:
            if DEBUG: print("INFO: No content, disconnect")
            if DEBUG: print("INFO: stop uart connection")
            uart_SC08A.close_uart_conn(ser)
            break
        print ("INFO: data from uart: " + str(content))
print("INFO: End of server")
