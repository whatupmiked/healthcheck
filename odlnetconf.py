import requests
import json
import jmespath
import testTools

def check(controller_ip):

    testTools.name("NETCONF")

    #ODL query of Network Topology Operational Inventory
    operational_db = 'http://{0}:8181/restconf/operational/network-topology:network-topology/'.format(controller_ip)

    try:
        print(" " * 1, "GET: {0:{width}}".format(operational_db, width=94), end='')
        #Make an HTTP GET Request with default auth password admin:admin
        operational_request = requests.get(operational_db,auth=('admin','admin'))
    except:
        #Do not print error only that it failed.
        testTools.fail()
        return False

    if(operational_request.status_code is not (200 or 201)):
        testTools.fail()
        print(" " * 2 , "Returned: ", operational_request.status_code)
        return False

    #Queried ODL Inventory successfully
    testTools.Pass()

    # Convert the request to a string and parse it into dictionary/lists using the json library
    operational_json = json.loads(operational_request.text)

    # This expression takes all nodes and puts them in a list. The objects inside the list are dictionaries
    operational_netconf = ((jmespath.search('"network-topology".topology[?"topology-id" == `topology-netconf`]',operational_json))[0]).get('node')

    # Check if nodes exist
    print(" " * 1, "{0:{width}}".format("NETCONF Node exists", width=99), end='')
    if not(type(operational_netconf) is list):
        testTools.fail()
        return False
    else:
        testTools.Pass()

    #Iterate over the Netconf nodes list and print the name and status
    for i in range(len(operational_netconf)):
        #Print Node-id, connection-status, and IP address
        print((" " * 5) + ("-"* 20))
        print((" " * 4), operational_netconf[i].get('node-id'))
        print((" " * 5) + ("-"* 20))
        print((" " * 8) +
              operational_netconf[i].get('netconf-node-topology:connection-status'),
              operational_netconf[i].get('netconf-node-topology:host'),
              sep='\n        ')
        ##### If states != connected print warnings
        ##### Check available capabilities of each node like Netconf1.0, Netconf1.1, Candidate, Startup, Running
