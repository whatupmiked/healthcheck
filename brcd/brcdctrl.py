"""
Tools for reviewing the Brocade SDN Controller
"""
import test_tools

def check():
    """
    Determine the version of the Brocade SDN Controller
    """
    test_tools.name("BROCADE VERSION")
    test_tools.sysRun("cat /opt/brocade/bsc/versions/version.properties")
