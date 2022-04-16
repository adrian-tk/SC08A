import serial
import time

class Servo:
    """Class for manipulate servo"""
    def __init__(self, channel):
        self.channel = channel
        self.speed = 0
        self.position = 0
        self.scale = 1

class SC08A(Servo):
    def __init__(self):
        """Initialize class with default uart values"""
        self.DEBUG = True
        self.uart_addr = "/dev/ttyS0"
        self.uart_bdr=9600
        if self.DEBUG: print ("INFO: SC08A __init__: initialized:")
        if self.DEBUG: print ("      " + str(self))
        self.no_of_srv =8
        self.servo=[Servo(i) for i in range (0, self.no_of_srv)]
        if self.DEBUG: print(f"INFO: SC08A created {self.no_of_srv} servos")

    def pack_data(self, channel, speed, scale):
        """creates bytes data in SC08A format to send over uart"""
        tmp=bin(channel).replace("0b", "")
        tmp = '{:>05}'.format(tmp)
        byte1=int('111' + tmp, 2)
        speed =int(float(speed)*scale)
        if self.DEBUG: print ("INFO: pack_data(): input speed: " + str(speed))
        if speed > 8000: speed=8000
        if speed < 0: speed=0
        tmp = bin(speed).replace("0b", "")
        tmp = '{:>013}'.format(tmp)
        byte2=int(('0' + tmp[:7]), 2)
        byte3=int(('00'+ tmp[7:]), 2)
        byte4=int('00000000', 2)
        outp=bytes([byte1, byte2, byte3, byte4])
        if self.DEBUG: print ("INFO: pack_data(): returned value: ")
        if self.DEBUG: print ("      " + str(outp))
        return outp

    def on(self):
        """initializes uart connection and servos"""
        if self.DEBUG: print("INFO: SC08A: on(): start of uart connection")
        try:
            self.uart = serial.Serial (self.uart_addr)
            if self.DEBUG: print ("INFO: SC08A: on(): uart connected on: ")
            if self.DEBUG: print ("      " + str(self.uart_addr))
            if self.DEBUG: print ("INFO: SC08A: on(): uart: " + str(self.uart))
        except Exception as e:
            print ("ERROR: SC08A: on(): uart can't connect on " + self.uart_addr )
            print ("ERROR: SC08A: on(): " + str(e))
            return(-1)
        try:
            self.uart.baudrate = self.uart_bdr
        except Exception as e:
            print ("ERROR: on(): can't set baudrate")
            print ("ERROR: on(): " + str(e))
            
        if self.DEBUG: print ("INFO: on(): baudrate set to: " + str(self.uart_bdr))
        self.uart.write(b'\xC0\x01') #turn on
        if self.DEBUG: print ("INFO: on(): servos turend on")

    def off(self):
        """stop and turn off servos"""
        outp = b'\xE0\x3E\x20\x00' #stop?
        self.uart.write(outp)
        if self.DEBUG: print ("INFO: off(): servos stopped")
        self.uart.write(b'\xC0\x00') #turn off
        if self.DEBUG: print ("INFO: off(): servos off")
        self.uart.close()
        if self.DEBUG: print ("INFO: off(): uart connection closed")


driver=SC08A()
print (driver.servo[1].speed)

