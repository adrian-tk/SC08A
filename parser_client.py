import argparse
from argparse import RawTextHelpFormatter


def create_parser():
    parser = argparse.ArgumentParser(description="Gui for SC08A driver")
    parser.add_argument('-v', action="store_true", dest="verbose", default=False,
        help="verbose - set log level to info. Overrided by --log.")
    parser.add_argument('--log', action="store", dest="loglevel",
        help="set loglevel to desired value.",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
            
    #dont use --log and -v similtaneously
    if parser.parse_args().loglevel != None: 
        parser.parse_args().verbose = False

    return parser
