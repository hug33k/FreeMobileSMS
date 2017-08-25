# -*- coding: utf8 -*-

import sys
import argparse
from .sms import FreeMobileSMS


def main():
    parser = argparse.ArgumentParser(description="Free Mobile SMS Service for sending SMS")
    parser.add_argument("message", help="Your message")
    parser.add_argument("--config", help="Path for config file")
    parser.add_argument("-v", "--verbose", help="Verbose mode", action="store_true")
    args = parser.parse_args()
    sms = FreeMobileSMS(args.config)
    if not sys.stdin.isatty():
        msg = sys.stdin.read()
    else:
        try:
            msg = args.message.decode(sys.stdin.encoding)
        except:
            msg = args.message
    status, value = sms.send(msg)
    if args.verbose:
        print(str(status) + " " + value)
