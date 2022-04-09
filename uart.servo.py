import serial
import time

def pack_data(channel, speed, scale):
    DEBUG = False

    tmp=bin(channel).replace("0b", "")
    tmp = '{:>05}'.format(tmp)
    byte1=int('111' + tmp, 2)
    speed =int(float(speed)*scale)
    print (speed)
    if speed > 8000: speed=8000
    if speed < 0: speed=0
    tmp = bin(speed).replace("0b", "")
    tmp = '{:>013}'.format(tmp)
    byte2=int(('0' + tmp[:7]), 2)
    byte3=int(('00'+ tmp[7:]), 2)
    byte4=int('00000000', 2)
    outp=bytes([byte1, byte2, byte3, byte4])
    if DEBUG: print ("returned value: ")
    if DEBUG: print (outp)
    return outp

def on()

print("start of program")
ser = serial.Serial ("/dev/ttyS0")
ser.baudrate = 9600

ser.write(b'\xC0\x01') #turn on
print ("turend on")
time.sleep(1.0)
outp = pack_data(1, 5000, 1.052)
ser.write(outp)
outp = pack_data(2, 5000, 1.0)
ser.write(outp)
print ("runned")
time.sleep(1.0)
outp = b'\xE0\x3E\x20\x00' #stop?
ser.write(outp)
print ("stopped")
time.sleep(1.0)
ser.write(b'\xC0\x00') #turn off
print ("turned off")
time.sleep(1.0)
ser.close()
print("End of program")

