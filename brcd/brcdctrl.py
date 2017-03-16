import testTools

def check():
   testTools.name("BROCADE VERSION")
   testTools.sysRun("cat /opt/brocade/bsc/versions/version.properties")

