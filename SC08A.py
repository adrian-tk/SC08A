import serial
import time
import logging

class Servo:
    """Class for manipulate servo"""
    def __init__(self, channel):
        self.uart = 0
        self.channel = channel
        self.speed = 0
        self.position = 0
        self.scale = 1
    def pack_data(self, channel, speed, scale):
        """creates bytes data in SC08A format to send over uart"""
        tmp=bin(channel).replace("0b", "")
        tmp = '{:>05}'.format(tmp)
        byte1=int('111' + tmp, 2)
        speed =int(float(speed)*scale)
        logging.debug("pack_data(): input speed: " + str(speed))
        if speed > 8000: speed=8000
        if speed < 0: speed=0
        tmp = bin(speed).replace("0b", "")
        tmp = '{:>013}'.format(tmp)
        byte2=int(('0' + tmp[:7]), 2)
        byte3=int(('00'+ tmp[7:]), 2)
        byte4=int('00000000', 2)
        outp=bytes([byte1, byte2, byte3, byte4])
        logging.debug("pack_data(): returned value: ")
        logging.debug("      " + str(outp))
        return outp
    def set(self, val):
        self.val = val
        sdata= self.pack_data(self.channel, self.val, self.scale)
        self.uart.write(sdata)


class SC08A(Servo):
    def __init__(self):
        """Initialize class with default uart values"""
        self.uart_addr = "/dev/ttyS0"
        self.uart_bdr=9600
        logging.debug("SC08A initialized")
        self.no_of_srv =8
        self.servo=[Servo(i) for i in range (0, self.no_of_srv)]
        logging.info(f"SC08A created {self.no_of_srv} servos")


    def on(self):
        """initializes uart connection and servos"""
        logging.debug("SC08A: on(): start of uart connection")
        try:
            self.uart = serial.Serial (self.uart_addr)
            logging.debug("SC08A: on(): uart connected on: ")
            logging.debug("      " + str(self.uart_addr))
            logging.debug("SC08A: on(): uart: " + str(self.uart))
        except Exception as e:
            logging.error ("SC08A: on(): uart can't connect on " + self.uart_addr )
            logging.error ("SC08A: on(): " + str(e))
            return(-1)
        try:
            self.uart.baudrate = self.uart_bdr
        except Exception as e:
            logging.error ("on(): can't set baudrate")
            logging.error ("on(): " + str(e))
            
        logging.debug("INFO: on(): baudrate set to: " + str(self.uart_bdr))
        self.uart.write(b'\xC0\x01') #turn on
        logging.debug("INFO: on(): servos turend on")
        for i in self.servo:
            logging.debug (i)
            i.uart = self.uart

    def off(self):
        """stop and turn off servos"""
        outp = b'\xE0\x3E\x20\x00' #stop?
        self.uart.write(outp)
        logging.debug("off(): servos stopped")
        self.uart.write(b'\xC0\x00') #turn off
        logging.debug("off(): servos off")
        self.uart.close()
        logging.debug("off(): uart connection closed")


#driver=SC08A()
