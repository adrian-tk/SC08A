import socket
import uart_SC08A
import json

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
        driver = uart_SC08A.SC08A()
        driver.on()
        if DEBUG: print("INFO: server: uart connection started")
        if DEBUG: print("      " + str(driver))
    except Exception as e:
        print("ERROR: server: can't get uart connection to SC08A")
        print("       " + str(e))
    while True:
        content=c.recv(1024).decode()
        if not content:
            if DEBUG: print("INFO: server: No content, disconnect")
            if DEBUG: print("INFO: server: stop socket connection")
            driver.off()
            break
        if DEBUG: print ("INFO: server: data from client: " + str(content))
        data = json.loads(content)
        print (data["number"])
        servo_no = data["number"]
        servo_val = data["value"]
        driver.servo[servo_no].set(float(servo_val))
        #driver.uart.write(ser.pack_data(8, float(content), 1.0))
        #driver.servo[1].set(float(content))
print("INFO: server: End of server")
