#!/usr/bin/python3
import os
import subprocess
import urllib.request
import sys

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

#print_format_table()

color_start = '\x1b['
color_end = '\x1b[0m'
red = '1;31;40m'
green = '1;32;40m'
blue = '1;34;40m'
yellow = '1;33;40m'
purple = '1;35;40m'

def fail():
    print("[" + color_start + red + "FAIL" + color_end + "]", end='\n')

def Pass():
    print("[" + color_start + green + "PASS" + color_end + "]", end='\n')

def name(n):
    print()
    print("=" * 40, end='\n')
    print(color_start + yellow + "{0}".format(n) + color_end)
    print("=" * 40, end='\n')

def sysRun(command):
    print("Running: {0}".format(command), end='\n\n')
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    for line in p.stdout.readlines():
        print(line.decode(), end='')
    retval = p.wait()

def tryURL(test_url,username,password):
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


