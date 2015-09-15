#!/usr/bin/python2.7

import json
import sys
import urllib

class FreeMobileSMS():

    def __init__(self, config="config.json"):
        self.baseURL = "https://smsapi.free-mobile.fr"
        self.route = "/sendmsg"
        self.file = config
        self.codes = [200, 400, 402, 403, 500]
        self.messages = ["Message send", "Missing parameter", "Too much messages send", "Service not enable", "Server not available"]
        try:
            configFile = open(self.file)
            dataFile = json.load(configFile)
            self.login = dataFile["login"]
            self.token = dataFile["token"]
        except:
            raise Exception("Error with file " + self.file + "\n")

    def makeRoute(self, message):
        route = self.baseURL + self.route
        route += "?user=" + self.login
        route += "&pass=" + self.token
        route += "&msg=" + urllib.quote(message)
        return route

    def checkCode(self, code):
        index = self.codes.index(code)
        if index >= 0:
            return self.messages[index]
        else:
            return "Error message not found"

    def send(self, message):
        route = self.makeRoute(message)
        res = urllib.urlopen(route)
        code = int(res.getcode())
        message = self.checkCode(code)
        return code, message

def usage():
    print("Usage :")
    print("./sms.py [--config=file] message")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        config = "config.json"
        for arg in sys.argv:
            if arg.startswith("--config="):
                tab = arg.split("=")
                if (len(tab) > 1 and len(tab[1])):
                    config = tab[1]
                    sys.argv.remove(arg)
                else:
                    usage()
                    sys.exit(1)
        sms = FreeMobileSMS(config)
        code, message = sms.send(sys.argv[1])
        print (str(code) + " " + message)
    else:
        usage()
        sys.exit(1)
