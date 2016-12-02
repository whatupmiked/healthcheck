import requests
import json
import jmespath
import testTools

def check(controller_ip):

    testTools.name("OPENFLOW")

    #ODL query of opendaylight-inventory:nodes
    operational_db_odl = 'http://{0}:8181/restconf/operational/opendaylight-inventory:nodes/'.format(controller_ip)

    try:
        print(" " * 1, "GET: {0:{width}}".format(operational_db_odl, width=94), end='')
        #Make a get call with default auth password admin:admin
        operational_openflow_request = requests.get(operational_db_odl,auth=('admin','admin'))
    except:
        #Do not print error only that it failed.
        testTools.fail()
        return False

    #Queried ODL Inventory successfully
    testTools.Pass()

    # Convert the request to a string and parse it into dictionary/lists using the json library
    operational_openflow_json = json.loads(operational_openflow_request.text)

    # This expression takes all nodes and puts them in a list. The objects inside the list are dictionaries
    operational_openflow = jmespath.search('nodes.node', operational_openflow_json)

    # Check if nodes exist
    print(" " * 1, "{0:{width}}".format("Openflow Node exists", width=99), end='')
    if not(type(operational_openflow) is list):
        testTools.fail()
        return False
    else:
        testTools.Pass()

    # Iterate over the Openflow list and print the first item in the dictionary
    for i in range(len(operational_openflow)):
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

