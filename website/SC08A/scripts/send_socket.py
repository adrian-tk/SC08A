import socket
 
def send_to_socket(val):
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = str(val)
    client_socket.send(message.encode())  # send message
    client_socket.close()  # close the connection

if __name__ == '__main__':
     send_to_socket()
