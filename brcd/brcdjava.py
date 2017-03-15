import os
import testTools

def check():
    java_config_path = '/opt/brocade/configuration/customer/bsc/etc/setenv.pre'

    testTools.name("JAVA CONFIG")
    print("Path: {0}".format(java_config_path))
    print(" " * 1, "{0:{width}}".format("setenv.pre exists", width=99), end='')
    if os.access(java_config_path, os.F_OK):
        testTools.Pass()
        testTools.sysRun("cat {0}".format(java_config_path))
    else:
        testTools.fail()
