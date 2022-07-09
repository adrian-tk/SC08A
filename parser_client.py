import argparse
from argparse import RawTextHelpFormatter

class ArgPar:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Gui for SC08A driver")
        self.parser.add_argument('-v', '--verbose', action="store_true", dest="verbose", default=False,
            help="set log level to info. Overrided by --log.")
        self.parser.add_argument('--log', action="store", dest="loglevel",
            help="set loglevel to desired value.",
            choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
        self.parser.add_argument('-s', '--hostname', action="store", dest="hostname",
            help="hostname to connect")
        self.parser.add_argument('-p', '--port', action="store", dest="port",
            help="port to connect")
                
        #dont use --log and -v similtaneously
        if self.parser.parse_args().loglevel != None: 
            self.parser.parse_args().verbose = False

        #return parser
