import logging
logging.basicConfig(level=logging.DEBUG)
import socket
import SC08A
import json

logging.info("=====server started=====")

s=socket.socket()
hostname=socket.gethostname()
host=socket.gethostbyname(hostname +".local")
port=12000
logging.debug(f"trying to get socket on: {host}:{port} ({hostname})")
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#host="192.168.0.141"
s.bind((host,port))
s.listen(10)
logging.info("host: " + host +" is waiting for Connection")


while True:
    c,addr=s.accept()
    logging.info("Client connected on socket")
    try:
        driver = SC08A.SC08A()
        driver.on()
        logging.debug("server: uart connection started")
        logging.debug("      " + str(driver))
    except Exception as e:
        logging.error("server: can't get uart connection to SC08A")
        logging.error("       " + str(e))
    while True:
        content=c.recv(1024).decode()
        if not content:
            logging.info("server: No content, disconnect")
            logging.info("server: stop socket connection")
            #driver.off()
            break
        logging.info("server: data from client: " + str(content))
        data = json.loads(content)
        print (data["number"])
        servo_no = int(data["number"])
        servo_val = float(data["value"])
        driver.servo[servo_no].set(servo_val)
        #driver.uart.write(ser.pack_data(8, float(content), 1.0))
        #driver.servo[1].set(float(content))
logging.info("server: End of server")
