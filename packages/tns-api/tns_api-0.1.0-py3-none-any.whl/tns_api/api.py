import json
import requests
from tns_api._constants import TNS_ID, NAME, API_KEY

def get_response(url, iau_name):
    """Obtains the response from a given TNS URL.

    Parameters
    ----------
    url: str
        TNS URL.

    Returns
    -------
    response: requests.Response
        Response object.
    """
    headers = {
        "User-Agent": 'tns_marker{"tns_id": "' + str(TNS_ID) + '", "type": "bot",'
        ' "name": "' + str(NAME) + '"}'
    }
    sn_data = {"objname": iau_name}
    json_data = [('api_key', (None, API_KEY)),
                            ('data', (None, json.dumps(sn_data)))]

    http_errors = {
        304: "Error 304: Not Modified: There was no new data to return.",
        400: "Error 400: Bad Request: The request was invalid. "
        "An accompanying error message will explain why.",
        403: "Error 403: Forbidden: The request is understood, but it has "
        "been refused. An accompanying error message will explain why.",
        404: "Error 404: Not Found: The URI requested is invalid or the "
        "resource requested, such as a category, does not exists.",
        500: "Error 500: Internal Server Error: Something is broken.",
        503: "Error 503: Service Unavailable.",
    }

    ###############################################################
    response = requests.post(url, headers=headers, files = json_data)

    if response.status_code == 200:
        return response
    else:
        print('Response error:', http_errors[response.status_code])
        print(url)
        return None

def validate_response(response):
    """Checks if the content was retrieved.

    Parameters
    ----------
    response : requests.Response
        Response object from TNS.

    Returns
    -------
    reply
        Dictionary with the targets data.
    """
    response.raise_for_status()
    data = response.json()['data']

    if 'reply' in data:
        reply = data['reply']
        if not reply:
            return None
        if 'objname' not in reply:
            return None
        
        return reply
    else:
        return None
    
def get_object(iau_name, verbose=False):
    """Obtains the objects information.

    Parameters
    ----------
    iau_name: str
        IAU name of the target (e.g. 2020xne).
    verbose: bool, default 'False'
        If True, print some of the intermediate information

    Returns
    -------
    obj_id: str
        The object's Wiserep ID. Returns 'Unknown' if not found
        or None if there is a problem of some other kind.
    """
    # look for the target ID in the search webpage
    tns_url = "https://www.wis-tns.org/api/get/object"
    response = get_response(tns_url, iau_name)
    target_dict = validate_response(response)

    return target_dict
