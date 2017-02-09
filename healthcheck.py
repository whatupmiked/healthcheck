#!/usr/bin/python3
import odl.odlsys
import odl.odlopenflow
import odl.odlnetconf
import sys
import argparse

__author__= "Michael Doyle"
__copyright__= ""
__license__= "MIT"
__version__= "0.5"
__maintainer__= "Michael Doyle"
__email__= "whatupmiked@gmail.com"
__status__= "beta"

def healthcheck():
    """
    1. Check the state of mem, cpu, disk, network on the controller system.
    2. Return the current openflow topology
    3. Return the current netconf topology
    """
    controller_ip = 'localhost'

    parser = argparse.ArgumentParser()

    parser.add_argument('-u', action='store', dest='username', help='defaults to admin')
    parser.add_argument('-p', action='store', dest='password', help='defaults to password')
    parser.add_argument('-b', action='store_true', dest='brocade',default=False, help='capture brocade specific outputs')
    parser.add_argument('-l', action='store', dest='karaf_path', help='path to karaf.log')

    input_args = parser.parse_args()
    username = input_args.username
    password = input_args.password
    brocade = input_args.brocade

    if username is None :
        username = 'admin'

    if password is None :
        password = 'admin'

    if brocade:
        karaf_path = '/opt/brocade/bsc/controller/data/log/karaf.log'
    else:
        karaf_path = input_args.karaf_path

    ## Get some information about the system
    # 1. Check CPU count
    # 2. Check Memory
    # 3. Check Disk
    # 4. Check TCP ports (API:8181, Nodejs:9001, Openflow:6633, NETCONF:830, BGP, PCEP, Cluster:2550, SSL/TLS)
    # 5. Check Nodejs version
    # 6. Check Java version
    # 7. Check compatible OS
    odl.odlsys.check(karaf_path)

    # Health-check of Openflow nodes connected to controller.
    odl.odlopenflow.check(controller_ip,username,password)

    # Health-check of Netconf nodes connected to controller.
    odl.odlnetconf.check(controller_ip,username,password)

healthcheck()
