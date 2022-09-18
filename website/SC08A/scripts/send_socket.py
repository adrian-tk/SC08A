import pathlib
import logging
#logpath=str(pathlib.Path().resolve())+ "/sts.log"
logpath="var/log/website/sts.log"
print (logpath)
logging.basicConfig(filename=logpath, filemode='w')
logging.getLogger().setLevel(logging.DEBUG)
import socket
import json

 
def send_to_socket(ch, val):
    #host = socket.gethostname()  # as both code is running on same pc
    #host = 192.168.0.141
    host = "malina.local"
    logging.debug(f"host: {host}")
    port = 12000  # socket server port number
    logging.debug(f"port: {port}")

    try:
        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server
        logging.info(f"connected to: {host} on port {port}") 
    except:
        logging.error(f"can't connect to: {host} on port {port}") 
        return (1)

    #message = str(val)
    message={"name": "Scale", "number": ch, "value": val}
    js=json.dumps(message)
    logging.debug(f"data to send: {js}")
    client_socket.send(js.encode())  # send message
    try:
        client_socket.close()  # close the connection
        logging.info(f"connection closed on: {host} on port {port}") 
    except:
        logging.error(f"can't close connection on: {host} on port {port}") 

if __name__ == '__main__':
    send_to_socket("1", "30.2")
