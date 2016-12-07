#!/usr/bin/python3
import odlsys
import odlopenflow
import odlnetconf

# !!!!!!!!!!!! Need to pass user-name/password as args to auth script !!!!!!!!!!!!!!!!!!!

controller_ip = 'localhost'

## Get some information about the system
# 1. Check CPU count
# 2. Check Memory
# 3. Check Disk
# 4. Check TCP ports (API:8181, Nodejs:9001, Openflow:6633, NETCONF:830, BGP, PCEP, Cluster:2550, SSL/TLS)
# 5. Check Nodejs version
# 6. Check Java version
# 7. Check compatible OS
odlsys.check()

# Health-check of Openflow nodes connected to controller.
odlopenflow.check(controller_ip)

# Health-check of Netconf nodes connected to controller.
odlnetconf.check(controller_ip)
