"""
Tools for verifying the system state of an ODL application
"""
import subprocess
import platform
import test_tools

## Get some information about the system
def check(karaf_path, controller_ip, username, password):
    """
    Verify system parameters for the installation
    """
    # 0. Uptime
    test_tools.name("TIME")
    test_tools.sysRun("date")
    print()
    test_tools.sysRun("uptime")

    # 1. Check CPU count 'lscpu' or /proc/cpuinfo
    test_tools.name("CPU")
    test_tools.sysRun("lscpu | egrep '(CPU\(s\)|endor)' | grep -v NUMA")

    # 2. Check memory 'free -h' or /proc/meminfo
    test_tools.name("MEMORY")
    test_tools.sysRun("free -h")

    # 3. Checking Disk  with 'df -ahl --total' or /proc/diskstats
    test_tools.name("DISK")
    test_tools.sysRun("df -ahl --total | egrep '(total|Used)'")

    # 4. Check TCP ports 'netstat' (API, Nodejs, Openflow, NETCONF, BGP, PCEP, Clustering)
    #   a. Check if listening on 8181 - RESTCONF
    #   b. Check if listening on 9001 - NODEJS
    #   c. Check if listening on 6633,6653 - OPENFLOW
    #   d. Check if listening on 830, 1830 - NETCONF
    #   e. Check if listening on 2550 - CLUSTERING
    #   e. check if listening on 179 - BGP
    #   f. check if listening on 4189 - PCEP
    #   g. check if listening on 8443 - RESTCONF (HTTPS)
    test_tools.name("TCP PORTS")
    distro = (platform.linux_distribution())[0].casefold()
    if ('centos' in distro) or ('rhel' in distro) or ('redhat' in distro):
        test_tools.sysRun("ss -nl | egrep '(Address|8181|8443|9001|830|6653|6633|2550|179|4189)'")
    else:
        test_tools.sysRun("netstat -nl | egrep '(Address|8181|8443|9001|830|6653|6633|2550|179|4189)'")

    # 5. Check Nodejs version
    test_tools.name("NODEJS")
    test_tools.sysRun("node --version")

    # 6. Check Java version, stdout is run in external java process so cannot capture.
    test_tools.name("JAVA")
    print("Running: java -version", end='\n\n')
    java = subprocess.Popen('java -version', shell=True, stdout=subprocess.PIPE)
    retval_j = java.wait()

    # 7. Check Compatible OS
    test_tools.name("OPERATING SYSTEM")
    test_tools.sysRun("cat /etc/*release | grep NAME")

    # 8. Check standard RESTCONF services
    # http://{controller-ip}:8181/apidoc/explorer/index.html
    # http://{controller-ip}:8181/restconf/modules
    # http://{controller-ip}:9001
    test_tools.name("STANDARD SERVICES")
    test_tools.tryURL("http://{0}:8181/apidoc/explorer/index.html".format(controller_ip),
                     username, password)
    test_tools.tryURL("http://{0}:8181/restconf/modules".format(controller_ip),
                     username, password)
    # For DLUX ui the default is http://{0}:8181/index.html 9001 is for Brocade UI
    test_tools.tryURL("http://{0}:9001".format(controller_ip), username, password)

    # 9. Check karaf.log for errors
    if karaf_path is not None:
        test_tools.name("KARAF.LOG")
        test_tools.sysRun("grep ERROR " + karaf_path + " | cut -d \| -f 1,2,6 | tail")
