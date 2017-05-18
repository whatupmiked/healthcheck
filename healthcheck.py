#!/usr/bin/python3
"""
Verify the system state of an opendaylight intallation for several
standard modules like openflow and netconf.
"""
import os
import argparse
import odl.odlsys
import odl.odlopenflow
import odl.odlnetconf
import odl.odlapi
import brcd.brcdcluster
import brcd.brcdhttps
import brcd.brcdjava
import brcd.brcdctrl

__author__ = "Michael Doyle"
__copyright__ = ""
__license__ = "MIT"
__version__ = "0.5"
__maintainer__ = "Michael Doyle"
__email__ = "whatupmiked@gmail.com"
__status__ = "beta"

def healthcheck():
    """
    1. Check the state of mem, cpu, disk, network on the controller system.
    2. Return the current openflow topology
    3. Return the current netconf topology
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--user', action='store', dest='username',
                        default='admin', help='defaults to admin')
    parser.add_argument('--password', action='store', dest='password',
                        default='admin', help='defaults to password')
    parser.add_argument('--brocade', action='store_true', dest='brocade',
                        default=False, help='capture brocade specific outputs')
    parser.add_argument('--log-location', action='store', dest='karaf_path',
                        help='path to karaf.log')
    parser.add_argument('--apis', action='store_true', dest='get_apis',
                        help='Option for gathering ODL api list')
    parser.add_argument('--ip', action='store', dest='controller_ip',
                        default='localhost', help='define the controller IP to be used')

    input_args = parser.parse_args()
    username = input_args.username
    password = input_args.password
    brocade = input_args.brocade


    if os.access('/opt/brocade/', os.F_OK) or brocade:
        karaf_path = '/opt/brocade/bsc/controller/data/log/karaf.log'
    else:
        karaf_path = input_args.karaf_path

    # Options execution parser
    if input_args.get_apis:
        odl.odlapi.api_list(**input_args.__dict__)
    #if os.access('/opt/brocade/', os.F_OK):
    elif input_args.brocade:
        # Get the state of different configuration parameters for Brocade ODL installation
        brcd.brcdctrl.check()
        brcd.brcdcluster.check()
        brcd.brcdhttps.check()
        brcd.brcdjava.check()
    else:
        ## Get some information about the system
        # 1. Check CPU count
        # 2. Check Memory
        # 3. Check Disk
        # 4. Check TCP ports (API:8181, Nodejs:9001, Openflow:6633,
        #    NETCONF:830, BGP, PCEP, Cluster:2550, SSL/TLS)
        # 5. Check Nodejs version
        # 6. Check Java version
        # 7. Check compatible OS
        odl.odlsys.check(karaf_path, input_args.controller_ip, username, password)

        # Health-check of Openflow nodes connected to controller.
        odl.odlopenflow.check(input_args.controller_ip, username, password)

        # Health-check of Netconf nodes connected to controller.
        odl.odlnetconf.check(input_args.controller_ip, username, password)

healthcheck()
