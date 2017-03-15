import os
import testTools

def check():
    https_file_path = '/opt/brocade/configuration/customer/bsc/etc/org.ops4j.pax.web.cfg'

    testTools.name("HTTPS UI CONFIG")
    print("Path: {0}".format(https_file_path))
    print(" " * 1, "{0:{width}}".format("org.ops4j.pax.web.cfg exists", width=99), end='')
    if os.access(https_file_path, os.F_OK):
        testTools.Pass()
        testTools.sysRun("grep http {0}".format(https_file_path))
    else:
        testTools.fail()
