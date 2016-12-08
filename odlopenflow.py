import urllib.request
import json
import testTools
import sys

def check(controller_ip,username,password):

    testTools.name("OPENFLOW")

    #ODL query of opendaylight-inventory:nodes
    operational_db_odl = 'http://{0}:8181/restconf/operational/opendaylight-inventory:nodes/'.format(controller_ip)

    #Build urllib object
    passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, operational_db_odl, username, password)
    authhandler = urllib.request.HTTPBasicAuthHandler(passman)
    opener = urllib.request.build_opener(authhandler)
    urllib.request.install_opener(opener)

    try:
        print(" " * 1, "GET: {0:{width}}".format(operational_db_odl, width=94), end='')
        #Make a get call with default auth password admin:admin
        operational_openflow_request = urllib.request.urlopen(operational_db_odl)
    except:
        #Do not print error only that it failed.
        testTools.fail()
        print(" " * 1, "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
        return False

    if(operational_openflow_request.status is not (200 or 201)):
        testTools.fail()
        print(" " * 2, "Returned: ", operational_openflow_request.status)
        return False

    #Queried ODL Inventory successfully
    testTools.Pass()

    # Convert the request to a string and parse it into dictionary/lists using the json library
    operational_openflow_json = json.loads(operational_openflow_request.read().decode())

    operational_openflow = operational_openflow_json["nodes"]["node"]

    # Check if nodes exist
    print(" " * 1, "{0:{width}}".format("Openflow Node exists", width=99), end='')
    if len(operational_openflow) < 1:
        testTools.fail()
        return False
    else:
        #Check if Beryllium ODL opendaylight-inventory
        if ( "controller-config" in operational_openflow[0].get('id') ):
            testTools.fail()
        else:
            testTools.Pass()

    # Iterate over the Openflow list and print the first item in the dictionary
    for i in range(len(operational_openflow)):
        # Skip loop if this is Beryllium 
        if ( "controller-config" in operational_openflow[i].get('id') ):
            print(" " * 4, "{0:{width}}".format("BERYLLIUM TOPOLOGY (controller-config)", width= 96) , end='')
            testTools.fail()
            break

        #Print id, ip, hw-info, description, serial#
        print((" " * 5) + ("-" * 20))
        print((" " * 4), operational_openflow[i].get('id'))
        print((" " * 5) + ("-" * 20))
        print((" " * 8) +
              operational_openflow[i].get('flow-node-inventory:description'),
              operational_openflow[i].get('flow-node-inventory:ip-address'),
              operational_openflow[i].get('flow-node-inventory:hardware'),
              operational_openflow[i].get('flow-node-inventory:serial-number'),
              operational_openflow[i].get('flow-node-inventory:manufacturer'),
              sep='\n        ')
        #Print each discovered Openflow interface for the switch
        interface_list = operational_openflow[i].get('node-connector')
        if (type(interface_list) is list):
            for n in range(len(interface_list)):
                print((" " * 10) + interface_list[n].get('id') + " " + interface_list[n].get('flow-node-inventory:name'))

