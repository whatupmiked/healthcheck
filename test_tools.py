#!/usr/bin/python3
"""
Simple tools for running test cases
"""
import subprocess
import urllib.request
import sys

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for foreg in range(30, 38):
            str1 = ''
            for backg in range(40, 48):
                format = ';'.join([str(style), str(foreg), str(backg)])
                str1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(str1)
        print('\n')

#print_format_table()

COLOR_START = '\x1b['
COLOR_END = '\x1b[0m'
RED = '1;31;40m'
GREEN = '1;32;40m'
BLUE = '1;34;40m'
YELLOW = '1;33;40m'
PURPLE = '1;35;40m'

def fail():
    """
    Print colored FAIL message.
    """
    print("[" + COLOR_START + RED + "FAIL" + COLOR_END + "]", end='\n')

def Pass():
    """
    Print colored PASS message.
    """
    print("[" + COLOR_START + GREEN + "PASS" + COLOR_END + "]", end='\n')

def name(test_name):
    """
    Print colored test name
    """
    print()
    print("=" * 40, end='\n')
    print(COLOR_START + YELLOW + "{0}".format(test_name) + COLOR_END)
    print("=" * 40, end='\n')

def sysRun(command):
    """
    Run a system command.
    """
    print("Running: {0}".format(command), end='\n\n')
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout.readlines():
        print(line.decode(), end='')
    retval = proc.wait()

def tryURL(test_url, username, password):
    """
    Handler for HTTP Get requests
    """
    passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, test_url, username, password)
    authhandler = urllib.request.HTTPBasicAuthHandler(passman)
    opener = urllib.request.build_opener(authhandler)
    urllib.request.install_opener(opener)

    try:
        print(" " * 1, "GET: {0:{width}}".format(test_url, width=94), end='')
        #Make a GET request
        urllib.request.urlopen(test_url)
        Pass()
    except:
        #Do not print error only that it failed.
        fail()
        print(" " * 1, "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
        return False
