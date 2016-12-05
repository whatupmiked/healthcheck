# healthcheck.py
pip3 install jmespath  
pip3 install requests  
./healthcheck.py  

Verify the system state of a vanilla ODL installation on standard ports.  

Designed for ODL Boron and python3.4.  

Check the system state, Openflow Nodes and NETCONF nodes.  

To install python3.4 on Centos7:  
yum install epel-release  
yum install python34 python-pip  
yum install python34-setuptools  
easy_install-3.4 pip  
