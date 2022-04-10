import socket
import tkinter as tk

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

def servo_t(event):
    if DEBUG: print("INFO: scale value: " + str(scale_servo_t.get()))
    if conn_status:
        s.send(("set servo to: " + str(scale_servo_t.get())).encode())
    else:
        if DEBUG: print("WARNING: there is no connection between rpi and SC08A")

if DEBUG: print("INFO: =====Start of client=====")
root=tk.Tk()
root.title('SC08A servo commander')
root.geometry('300x200')
#root.iconbitmap(r'/home/domel/repo/Python/SC08A/img/AT_32.ico')
root.iconbitmap('@/home/domel/repo/Python/SC08A/img/AT.xbm')
button_connect=tk.Button(root, text="connect", command=connect_to_rpi)
button_connect.pack()

lframe_ServosControl = tk.LabelFrame(root, text="Servos Control")
lframe_ServosControl.pack()

scale_servo_t = tk.Scale(lframe_ServosControl, from_=0, to=100)
scale_servo_t.bind("<ButtonRelease-1>", servo_t)
scale_servo_t.pack()
root.mainloop()
try:
    s.close()
except:
    if DEBUG: print("WARNING: socket already closed")

if DEBUG: print("INFO: End of client")
