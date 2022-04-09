import serial

DEBUG=False

def start_uart_conn():
    if DEBUG: print("starting of uart connection")
    try:
        ser = serial.Serial ("/dev/ttyS0")
        ser.baudrate = 9600
        return(ser)
    except Exception as e:
        print ("Can't connect to uart")
        print ("ERROR: "+str(e))
        return(-1)

def close_uart_conn(ser):
    ser.close()
    if DEBUG: print("End of program")

