"""
Verify information about the HTTPS configuration of Brocade SDN Controller
"""
import os
import test_tools

def check():
    """
    Check if HTTPS configuration file exists
    """
    https_file_path = '/opt/brocade/configuration/customer/bsc/etc/org.ops4j.pax.web.cfg'

    test_tools.name("HTTPS UI CONFIG")
    print("Path: {0}".format(https_file_path))
    print(" " * 1, "{0:{width}}".format("org.ops4j.pax.web.cfg exists", width=99), end='')
    if os.access(https_file_path, os.F_OK):
        test_tools.Pass()
        test_tools.sysRun("grep http {0}".format(https_file_path))
    else:
        test_tools.fail()
