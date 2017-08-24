#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import json
import os
import sys
import urllib
import argparse


class FreeMobileSMS(object):
    def __init__(self, config=None):
        self._URL = "https://smsapi.free-mobile.fr/sendmsg?user={0}&pass={1}&msg={2}"
        self._codes = {
            200: "Message send",
            400: "Missing parameter",
            402: "Too much messages send",
            403: "Service not enable",
            500: "Server not available"
        }
        if config:
            with open(config, "r") as conf_file:
                try:
                    data_file = json.load(conf_file)
                    self._login = data_file["login"]
                    self._token = data_file["token"]
                except:
                    raise Exception("Error with file " + config + "\n")
        else:
            if "SMS_LOGIN" not in os.environ:
                raise Exception("Missing SMS_LOGIN")
            if "SMS_TOKEN" not in os.environ:
                raise Exception("Missing SMS_TOKEN")
            self._login = os.environ["SMS_LOGIN"]
            self._token = os.environ["SMS_TOKEN"]

    def _make_route(self, message):
        return self._URL.format(self._login, self._token, urllib.quote(message))

    def _check_code(self, code):
        if code in self._codes:
            return code, self._codes[code]
        else:
            return code, "Error message not found"

    def send(self, message):
        route = self._make_route(message)
        res = urllib.urlopen(route)
        return self._check_code(int(res.getcode()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Free Mobile SMS Service for sending SMS")
    parser.add_argument("message", help="Your message")
    parser.add_argument("--config", help="Path for config file")
    parser.add_argument("-v", "--verbose", help="Verbose mode", action="store_true")
    args = parser.parse_args()
    sms = FreeMobileSMS(args.config)
    if not sys.stdin.isatty():
        msg = sys.stdin.read()
    else:
        msg = args.message.decode(sys.stdin.encoding)
    status, value = sms.send(msg)
    if args.verbose:
        print (str(status) + " " + value)
