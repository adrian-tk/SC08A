import socket
import tkinter as tk

#host = 'malina'
host = "192.168.1.38"
print(host)
port=12000

conn_status=False #is connected already?

def connect_to_rpi():
    global conn_status
    global s
    print("conn_status: " + str(conn_status))
    try:
        if conn_status == False:
            s=socket.socket()
            s.connect((host,port))
            button_connect.config(text="disconnect")
            conn_status = True
            print("Connected to: " + host)
        else:
            print("Disconected from: " + host)
            button_connect.config(text="connect")
            conn_status = False
            s.shutdown(socket.SHUT_RDWR)
            s.close()

    except Exception as e:
        print ("ERROR: " + str(e))

def send_test_message():
    s.send("dupa".encode())

root=tk.Tk()
button_connect=tk.Button(root, text="connect", command=connect_to_rpi)
button_connect.pack()
root.mainloop()
try:
    s.close()
except:
    print("WARNING: socket already closed")

print("End of program")
