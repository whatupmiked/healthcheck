"""
Interpret the ODL apis
"""
import requests

# Headers
J_HEADERS = {"Accept": "application/json", "Content-type": "application/json"}

APIS = "apidoc/apis/"

def api_list(**args):
    """
    Given controller access details, returns a list of api paths
    curl -u admin:admin http://<controller_ip>:8181/apidoc/apis/
    """
    api_uri = "http://{0}:8181/{1}".format(args['controller_ip'], APIS)

    #print("Printing API list from {0}".format(api_uri), end='\n\n')

    r_a = requests.get(
        api_uri,
        auth=(args['username'], args['password']),
        headers=J_HEADERS)

    api_l = []
    api_json = r_a.json()
    for i in range(len(api_json['apis'])):
        api_l.append(api_json['apis'][i]['path'])

    print(*api_l, sep='\n')
