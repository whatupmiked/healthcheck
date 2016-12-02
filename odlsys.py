import subprocess
import testTools

def sysRun(command):
    print("Running {0}".format(command), end='\n\n')
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    for line in p.stdout.readlines():
        print(line.decode(), end='')
    retval = p.wait()

## Get some information about the system
def check():
    # 1. Check CPU count 'lscpu' or /proc/cpuinfo
    testTools.name("CPU")
    sysRun("lscpu | egrep '(CPU\(s\)|endor)' | grep -v NUMA")

    # 2. Check memory 'free -h' or /proc/meminfo
    testTools.name("MEMORY")
    sysRun("free -h")

    # 3. Checking Disk  with 'df -ahl --total' or /proc/diskstats
    testTools.name("DISK")
    sysRun("df -ahl --total")

    # 4. Check TCP ports 'netstat' (API, Nodejs, Openflow, NETCONF, BGP, PCEP, Clustering)
    #   a. Check if listening on 8181
    #   b. Check if listening on 9001
    testTools.name("TCP PORTS")
    sysRun("netstat -nl | egrep '(8181|9001)'")

    # 5. Check Nodejs version
    testTools.name("NODEJS")
    sysRun("nodejs --version")

    # 6. Check Java version, stdout is run in external java process so cannot capture.
    testTools.name("JAVA")
    print("Running 'java -version'", end='\n\n')
    j = subprocess.Popen('java -version', shell=True, stdout=subprocess.PIPE)
    retvalJ = j.wait()

    # 7. Check Compatible OS
    testTools.name("OPERATING SYSTEM")
    sysRun("cat /etc/*release")
