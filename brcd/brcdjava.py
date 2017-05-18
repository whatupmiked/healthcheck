"""
Verify information about the java configuration for Brocade SDN Controller
"""
import os
import test_tools

def check():
    """
    Check if file for modifying java settings exists
    """
    java_config_path = '/opt/brocade/configuration/customer/bsc/etc/setenv.pre'

    test_tools.name("JAVA CONFIG")
    print("Path: {0}".format(java_config_path))
    print(" " * 1, "{0:{width}}".format("setenv.pre exists", width=99), end='')
    if os.access(java_config_path, os.F_OK):
        test_tools.Pass()
        test_tools.sysRun("cat {0}".format(java_config_path))
    else:
        test_tools.fail()
