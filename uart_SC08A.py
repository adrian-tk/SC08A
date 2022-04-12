import serial
import time

DEBUG = True

def pack_data(channel, speed, scale):

    tmp=bin(channel).replace("0b", "")
    tmp = '{:>05}'.format(tmp)
    byte1=int('111' + tmp, 2)
    speed =int(float(speed)*scale)
    if DEBUG: print ("INFO: pack_data(): input speed: " + str(speed))
    if speed > 8000: speed=8000
    if speed < 0: speed=0
    tmp = bin(speed).replace("0b", "")
    tmp = '{:>013}'.format(tmp)
    byte2=int(('0' + tmp[:7]), 2)
    byte3=int(('00'+ tmp[7:]), 2)
    byte4=int('00000000', 2)
    outp=bytes([byte1, byte2, byte3, byte4])
    if DEBUG: print ("INFO: pack_data(): returned value: ")
    if DEBUG: print ("      " + str(outp))
    return outp

def on():
    #DEBUG = global DEBUG
    if DEBUG: print("INFO: on(): start of uart connection")
    uart_addr = "/dev/ttyS0"
    uart_bdr=9600
    try:
        uart = serial.Serial (uart_addr)
        if DEBUG: print ("INFO: on(): uart connected on " + uart_addr )
    except Exception as e:
        print ("ERROR: on(): uart can't connect on " + uart_addr )
        print ("ERROR: on(): " + str(e))
        return(-1)
    try:
        uart.baudrate = uart_bdr
    except Exception as e:
        print ("ERROR: on(): can't set baudrate")
        print ("ERROR: on(): " + str(e))
        
    if DEBUG: print ("INFO: on(): baudrate set to: " + str(uart_bdr))
    uart.write(b'\xC0\x01') #turn on
    if DEBUG: print ("INFO: on(): servos turend on")
    return (uart)

def off(ser):
    outp = b'\xE0\x3E\x20\x00' #stop?
    ser.write(outp)
    if DEBUG: print ("INFO: off(): servos stopped")
    ser.write(b'\xC0\x00') #turn off
    if DEBUG: print ("INFO: off(): servos off")
    ser.close()
    if DEBUG: print ("INFO: off(): uart connection closed")


ser=on()

time.sleep(1.0)
outp = pack_data(1, 5000, 1.052)
ser.write(outp)
outp = pack_data(2, 5000, 1.0)
ser.write(outp)
time.sleep(1.0)
off(ser)
print("End of program")

