"""
Tools for reviewing the Brocade SDN Controller
"""
import testTools

def check():
    """
    Determine the version of the Brocade SDN Controller
    """
    testTools.name("BROCADE VERSION")
    testTools.sysRun("cat /opt/brocade/bsc/versions/version.properties")
