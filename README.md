# healthcheck.py
Verify the system state of a vanilla ODL installation on standard ports.  

## Usage
```
./healthcheck.py
./healthcheck.py --brocade
./healthcheck.py --help
```

## Notes
Designed for ODL Boron and python3.4.  

Features:  
 - odl-restconf  
 - odl-netconf-all  
 - odl-l2switch-switch-ui  
 - odl-dlux-all  

To install python3.4 on Centos7:  
```
yum install epel-release  
yum install python34 python-pip  
yum install python34-setuptools  
easy_install-3.4 pip  
```
