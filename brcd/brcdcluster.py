import os
import test_tools

def check():
    modules_shards_path = '/opt/brocade/configuration/customer/bsc/configuration/initial/modules-shards.conf'
    akka_path = '/opt/brocade/configuration/customer/bsc/configuration/initial/akka.conf'

    test_tools.name("CLUSTER CONFIG")
    print("Path: /opt/brocade/configuration/customer/bsc/configuration/initial/")
    print(" " * 1, "{0:{width}}".format("modules-shards.conf exists", width=99), end='')
    if os.access(modules_shards_path, os.F_OK):
        #print modules_shards config file
        test_tools.Pass()
        print(modules_shards_path)
    else:
        test_tools.fail()

    print(" " * 1, "{0:{width}}".format("akka.conf exists", width=99), end='')
    if os.access(akka_path, os.F_OK):
        #print akka config file
        test_tools.Pass()
        print(akka_path)
    else:
        test_tools.fail()

# Documentation on HOCON https://github.com/typesafehub/config/blob/master/HOCON.md
# Documentation for clustering https://lists.opendaylight.org/pipermail/controller-dev/2016-July/012388.html
        
#    cluster_dir = "/opt/brocade/configuration/customer/bsc/configuration/initial/"
#    akka = '0.akka.conf'
#    modules = '0.module-shards.conf'
#    os.chdir(cluster_dir)
#    f = open(akka,'r')
#    akka_file = f.read()
#    for i in range(len(akka_file.splitlines())):
#        print((akka_file.splitlines())[i])
