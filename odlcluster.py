import os

def check():
    #/opt/brocade/configuration/customer/bsc/configuration/initial/modules-shards.conf
    #/opt/brocade/configuration/customer/bsc/configuration/initial/akka.conf
    cluster_dir = "/opt/brocade/configuration/customer/bsc/configuration/initial/"
    akka = '0.akka.conf'
    modules = '0.module-shards.conf'
    os.chdir(cluster_dir)
    f = open(akka,'r')
    akka_file = f.read()
    for i in range(len(akka_file.splitlines())):
        print((akka_file.splitlines())[i])
