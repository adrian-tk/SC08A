import logging
logging.basicConfig(level=logging.WARNING)
import socket
import tkinter as tk
import os
import json
import parser_client

hostname = 'malina'
port=12000


#parsing command line arguments
p = parser_client.ArgPar()
args = p.parser.parse_args()
#when command line arg is "-v" set loglevel to INFO
if args.verbose: logging.getLogger().setLevel(logging.INFO)
if args.loglevel!=None: 
    logl= (getattr(logging, args.loglevel))
    logging.getLogger().setLevel(logl)
logging.debug (f"loglevel is set to: {logging.getLogger().level}")
logging.debug(f"Command line arguments: {args}")

if args.hostname !=None: hostname=args.hostname
if args.port !=None: port=args.port

conn_status=False #is connected already?

def connect_to_rpi():
    logging.debug("will try to connect to: "+hostname)
    global conn_status
    global s
    try:
        if conn_status == False:
            host = socket.gethostbyname(hostname +".local")
            logging.debug(f"hostname: {hostname} has address: {host}")
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
for i in range(9):
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
