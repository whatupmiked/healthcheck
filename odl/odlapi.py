import requests

# Headers
j_headers = {"Accept": "application/json", "Content-type": "application/json"}

apis = "apidoc/apis/"

def api_list(**args):
    """Given controller access details, returns a list of api paths"""
    """curl -u admin:admin http://<controller_ip>:8181/apidoc/apis/"""
    api_uri = "http://{0}:8181/{1}".format(args['controller_ip'],apis)

    #print("Printing API list from {0}".format(api_uri), end='\n\n')

    ra = requests.get(
            api_uri,
            auth=(args['username'],args['password']),
            headers=j_headers)

    api_list = []
    api_json = ra.json()
    for i in range(len(api_json['apis'])):
        api_list.append(api_json['apis'][i]['path'])

    print( *api_list, sep='\n' )

