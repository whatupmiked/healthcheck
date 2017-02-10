import subprocess
import testTools

## Get some information about the system
def check(karaf_path):

    # 0. Uptime
    testTools.name("TIME")
    testTools.sysRun("date")
    print()
    testTools.sysRun("uptime")

    # 1. Check CPU count 'lscpu' or /proc/cpuinfo
    testTools.name("CPU")
    testTools.sysRun("lscpu | egrep '(CPU\(s\)|endor)' | grep -v NUMA")

    # 2. Check memory 'free -h' or /proc/meminfo
    testTools.name("MEMORY")
    testTools.sysRun("free -h")

    # 3. Checking Disk  with 'df -ahl --total' or /proc/diskstats
    testTools.name("DISK")
    testTools.sysRun("df -ahl --total | egrep '(total|Used)'")

    # 4. Check TCP ports 'netstat' (API, Nodejs, Openflow, NETCONF, BGP, PCEP, Clustering)
    #   a. Check if listening on 8181 - RESTCONF
    #   b. Check if listening on 9001 - NODEJS
    #   c. Check if listening on 6633,6653 - OPENFLOW
    #   d. Check if listening on 830, 1830 - NETCONF
    #   e. Check if listening on 2550 - CLUSTERING
    #   e. check if listening on 179 - BGP
    #   f. check if listening on 4189 - PCEP
    #   g. check if listening on 8443 - RESTCONF (HTTPS)
    testTools.name("TCP PORTS")
    testTools.sysRun("netstat -nl | egrep '(Address|8181|8443|9001|830|6653|6633|2550|179|4189)'")

    # 5. Check Nodejs version
    testTools.name("NODEJS")
    testTools.sysRun("node --version")

    # 6. Check Java version, stdout is run in external java process so cannot capture.
    testTools.name("JAVA")
    print("Running: java -version", end='\n\n')
    j = subprocess.Popen('java -version', shell=True, stdout=subprocess.PIPE)
    retvalJ = j.wait()

    # 7. Check Compatible OS
    testTools.name("OPERATING SYSTEM")
    testTools.sysRun("cat /etc/*release | grep NAME")

    # 8. Check karaf.log for errors
    if karaf_path is not None:
        testTools.name("KARAF.LOG")
        testTools.sysRun("grep ERROR " + karaf_path + " | cut -d \| -f 1,2,6 | tail")

