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
    print("INFO: Client connected on socket")
    try:
        ser = uart_SC08A.SC08A()
        ser.on()
        if DEBUG: print("INFO: server: uart connection started")
        if DEBUG: print("      " + str(ser))
    except Exception as e:
        print("ERROR: server: can't get uart connection to SC08A")
        print("       " + str(e))
    while True:
        content=c.recv(100).decode()
        if not content:
            if DEBUG: print("INFO: server: No content, disconnect")
            if DEBUG: print("INFO: server: stop socket connection")
            ser.off()
            break
        if DEBUG: print ("INFO: server: data from client: " + str(content))
        ser.uart.write(ser.pack_data(8, float(content), 1.0))
print("INFO: server: End of server")
