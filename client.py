import socket
import tkinter as tk
import os
import json

DEBUG = True
#host = 'malina'
host = "192.168.1.38"
port=12000

conn_status=False #is connected already?

def connect_to_rpi():
    if DEBUG: print("INFO: will try to connect to: "+host)
    global conn_status
    global s
    try:
        if conn_status == False:
            s=socket.socket()
            s.connect((host,port))
            button_connect.config(text="disconnect")
            conn_status = True
            print("INFO: Connected to: " + host)
        else:
            print("INFO: Disconected from: " + host)
            button_connect.config(text="connect")
            conn_status = False
            s.shutdown(socket.SHUT_RDWR)
            s.close()

    except Exception as e:
        if DEBUG: print ("ERROR: " + str(e))

def send_test_message():
    s.send("dupa".encode())

#def servo_t(event):
def servo_t(i):
    if DEBUG: print(f"INFO: scale {i} value: {(scale_list[i].get())}")
    if conn_status:
        data = {"name": "Scale", "number": i, "value": scale_list[i].get()}
        ts = json.dumps(data)
        s.send(ts.encode())
        if DEBUG: print (f"INFO: data sended to RPI: {ts}")
    else:
        if DEBUG: print("WARNING: there is no connection between rpi and SC08A")

if DEBUG: print("INFO: =====Start of client=====")
if DEBUG: print(f"INFO: actual directory: {os.getcwd()}")
root=tk.Tk()
root.title('SC08A servo commander')
root.geometry('600x200')
try:
    icopath=f"@{os.getcwd()}/img/AT.xbm"
    root.iconbitmap(icopath)
except Exception as e:
    print("ERROR: can't set icon:")
    print(f"       {e}")
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
    scale_list[i].pack(side=tk.LEFT)
root.mainloop()
try:
    s.close()
except:
    if DEBUG: print("WARNING: socket already closed")

if DEBUG: print("INFO: End of client")
