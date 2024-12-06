import requests
import json
import random
import uuid
import pathlib
import logging
import sys
import os
import base64
import time

from configparser import ConfigParser
from sign_up import register
from datatier import web_service_get
from sign_in import signin
from modify_password import modify_pwd

############################################################
#
# classes
#
class User:
    def __init__(self, row):
        self.userid = row[0]
        self.username = row[1]
        self.pwdhash = row[2]


############################################################
#
# prompt
#
def prompt():
    """
    Prompts the user and returns the command number

    Parameters
    ----------
    None

    Returns
    -------
    Command number entered by user (0, 1, 2, ...)
    """
    try:
        print()
        print(">> Enter a command:")
        print("   0 => end")
        print("   1 => sign up")
        print("   2 => sign in")
        print("   3 => forget password")

        cmd = input()

        if cmd == "":
            cmd = -1
        elif not cmd.isnumeric():
            cmd = -1
        else:
            cmd = int(cmd)

        return cmd

    except Exception as e:
        print("**ERROR")
        print("**ERROR: invalid input")
        print("**ERROR")
        return -1

############################################################
# main
#
try:
    print('** Welcome to Trade Platform **')
    print()

    # eliminate traceback so we just get error message:
    sys.tracebacklimit = 0

    #
    # what config file should we use for this session?
    #
    config_file = 'tradeapp-client-config.ini'

    print("Config file to use for this session?")
    print("Press ENTER to use default, or")
    print("enter config file name>")
    s = input()

    if s == "":  # use default
        pass  # already set
    else:
        config_file = s

    #
    # does config file exist?
    #
    if not pathlib.Path(config_file).is_file():
        print("**ERROR: config file '", config_file, "' does not exist, exiting")
        sys.exit(0)

    #
    # setup base URL to web service:
    #
    configur = ConfigParser()
    configur.read(config_file)
    baseurl = configur.get('client', 'webservice')

    #
    # make sure baseurl does not end with /, if so remove:
    #
    if len(baseurl) < 16:
        print("**ERROR: baseurl '", baseurl, "' is not nearly long enough...")
        sys.exit(0)

    if baseurl == "https://YOUR_GATEWAY_API.amazonaws.com":
        print("**ERROR: update config file with your gateway endpoint")
        sys.exit(0)

    if baseurl.startswith("http:"):
        print("**ERROR: your URL starts with 'http', it should start with 'https'")
        sys.exit(0)

    lastchar = baseurl[len(baseurl) - 1]
    if lastchar == "/":
        baseurl = baseurl[:-1]

    #
    # main processing loop:
    #
    cmd = prompt()

    while cmd != 0:
        #
        if cmd == 1:
            register(baseurl)
        elif cmd == 2:
            signin(baseurl)
        elif cmd == 3:
            modify_pwd(baseurl)
        else:
            print("** Unknown command, try again...")
        #
        cmd = prompt()

    #
    # done
    #
    print()
    print('** done **')
    sys.exit(0)

except Exception as e:
    logging.error("**ERROR: main() failed:")
    logging.error(e)
    sys.exit(0)
