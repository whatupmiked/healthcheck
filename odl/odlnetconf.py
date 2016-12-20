import urllib.request
import json
import testTools
import sys

def check(controller_ip,username,password):

    testTools.name("NETCONF")

    #ODL query of Network Topology Operational Inventory
    operational_db = 'http://{0}:8181/restconf/operational/network-topology:network-topology/'.format(controller_ip)

    #Build urllib object
    passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, operational_db, username, password)
    authhandler = urllib.request.HTTPBasicAuthHandler(passman)
    opener = urllib.request.build_opener(authhandler)
    urllib.request.install_opener(opener)

    try:
        print(" " * 1, "GET: {0:{width}}".format(operational_db, width=94), end='')
        #Make an HTTP GET Request with default auth password admin:admin
        operational_request = urllib.request.urlopen(operational_db)
    except:
        #Do not print error only that it failed.
        testTools.fail()
        print(" " * 1, "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
        return False

    if(operational_request.status is not (200 or 201)):
        testTools.fail()
        print(" " * 2 , "Returned: ", operational_request.status)
        return False

    #Queried ODL Inventory successfully
    testTools.Pass()

    # Convert the request to a string and parse it into dictionary/lists using the json library
    operational_json = json.loads(operational_request.read().decode())

    #Pull the network topology and instantiate an empty list to place our list of netconf nodes
    topology_list = operational_json["network-topology"]["topology"]

    operational_netconf = []

    #Search for netconf nodes and populate operational_netconf with that list
    for i in range(len(topology_list)):
        if (topology_list[i]["topology-id"] == "topology-netconf"):
            # Check if nodes exit
            print(" " * 1, "{0:{width}}".format("NETCONF Node exists", width=99), end='')

            if(len(topology_list[i]) < 1):
                #Boron Failure
                testTools.fail()
                return False
            elif(len(topologylist[i]["node"]) < 1):
                #Beryllium Failure
                testTools.fail()
                return False
            else:
                operational_netconf = topology_list[i]["node"]
                testTools.Pass()

    # Check if nodes exist
#    if len(operational_netconf) < 1:
#        testTools.fail()
#        return False
#    else:
#        testTools.Pass()

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
