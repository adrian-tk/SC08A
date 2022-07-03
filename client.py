import socket
import tkinter as tk
import os
import json
import logging

logging.basicConfig(level=logging.DEBUG)
hostname = 'malina'
host = socket.gethostbyname(hostname +".local")
#host = "192.168.0.141"
port=12000

conn_status=False #is connected already?

def connect_to_rpi():
    logging.debug("will try to connect to: "+host)
    global conn_status
    global s
    try:
        if conn_status == False:
            s=socket.socket()
            s.connect((host,port))
            button_connect.config(text="disconnect")
            conn_status = True
            logging.info("Connected to: " + host)
        else:
            logging.info("Disconected from: " + host)
            button_connect.config(text="connect")
            conn_status = False
            s.shutdown(socket.SHUT_RDWR)
            s.close()

    except Exception as e:
        logging.error("ERROR: " + str(e))

def send_test_message():
    s.send("dupa".encode())

#def servo_t(event):
def servo_t(i):
    logging.debug(f"scale {i} value: {(scale_list[i].get())}")
    if conn_status:
        data = {"name": "Scale", "number": i, "value": scale_list[i].get()}
        ts = json.dumps(data)
        s.send(ts.encode())
        logging.info(f"data sended to RPI: {ts}")
    else:
        logging.warning("there is no connection between rpi and SC08A")

logging.info("=====Start of client=====")
logging.debug(f"actual directory: {os.getcwd()}")
logging.debug(socket.gethostbyname("malina" +".local"))
root=tk.Tk()
root.title('SC08A servo commander')
root.geometry('600x200')
try:
    icopath=f"@{os.getcwd()}/img/AT.xbm"
    root.iconbitmap(icopath)
except Exception as e:
    logging.warning("Warning: can't set icon:")
    logging.warning(f"       {e}")
button_connect=tk.Button(root, text="connect", command=connect_to_rpi)
button_connect.pack()

lframe_ServosControl = tk.LabelFrame(root, text="Servos Control")
lframe_ServosControl.pack()

scale_list=[]
for i in range(8):
    def func(event, x=i):
        return servo_t(x)
    scale_list.insert(i, tk.Scale(lframe_ServosControl, from_=0, to=8000))
    scale_list[i].bind("<ButtonRelease-1>", func)
    scale_list[i].set(4000)
    scale_list[i].pack(side=tk.LEFT)
root.mainloop()
try:
    s.close()
except:
    logging.warning("socket already closed")

logging.info("End of client")
