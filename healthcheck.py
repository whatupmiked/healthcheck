#!/usr/bin/python3
import odlsys
import odlopenflow
import odlnetconf
import sys

def healthcheck():
    controller_ip = 'localhost'
    username = 'admin'
    password = 'admin'

    # !!!!!!!!!!!! Need to pass user-name/password as args to auth script !!!!!!!!!!!!!!!!!!!
    for i in range(len(sys.argv)):
        if(sys.argv[i] == '-h'):
            print(
                "Usage: ./healthcheck",
                "  -h help",
                "  -u Authentication",
                "    syntax: -u username:password (if no arguments are passed the default admin:admin is used)",
                sep='\n')
            return False
        elif(sys.argv[i] == '-u'):
            username = (sys.argv[i+1]).split(":")[0]
            password = (sys.argv[i+1]).split(":")[1]
            break

    ## Get some information about the system
    # 1. Check CPU count
    # 2. Check Memory
    # 3. Check Disk
    # 4. Check TCP ports (API:8181, Nodejs:9001, Openflow:6633, NETCONF:830, BGP, PCEP, Cluster:2550, SSL/TLS)
    # 5. Check Nodejs version
    # 6. Check Java version
    # 7. Check compatible OS
    odlsys.check()

    # Health-check of Openflow nodes connected to controller.
    odlopenflow.check(controller_ip,username,password)

    # Health-check of Netconf nodes connected to controller.
    odlnetconf.check(controller_ip,username,password)

healthcheck()
