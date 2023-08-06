import requests
from .exceptions import *

# public_API_host = "https://ddhoutboundapiuat.asestg.worldbank.org"
public_API_host = "https://datacatalogapi.worldbank.org/ddhxext"

def get(endpoint, params=None, headers=None, session=None):
    '''Send a GET request

    Arguments:
        endpoint:		the endpoint (e.g., "datasets")
        params:			parameters
        headers:		additional headers

    Returns:
        a Response object (from the requests package)
    '''
    if session:
        session.check_tokens()
        return requests.get(get_endpoint(endpoint, session), params=params, verify=session.verify, headers=session.get_headers(headers))
    else:
        return requests.get(get_endpoint(endpoint), params=params)

def try_get(endpoint, params=None, headers=None, session=None, num_try=3, interval=300):
    '''Repeat sending a GET request until it succeeds or it tries {num_try} times

    Additional arguments:
        num_try:        number of tries
        interval:       interval between tries in seconds
    '''
    count = 0
    while True:
        try:
            count = count + 1
            if session:
                session.check_tokens()
                return requests.get(get_endpoint(endpoint, session), params=params, verify=session.verify, headers=session.get_headers(headers))
            else:
                return requests.get(get_endpoint(endpoint), params=params)
        except requests.exceptions.RequestException as e:
            print (f"[{count} try] Error: ", e)
            if count > num_try:
                raise Exception(f"Request failed after {count} tries.")
            continue



def get_all_in_generator(endpoint, params=None, headers=None, session=None):
    '''Fetch all data for endpoints that have top and skip parameters

    Returns:
        a Generator
    '''
    if "top" in params or "skip" in params:
        raise Exception("get_all function cannot be used with 'top' or 'skip' parameter.")
    if params == None:
        params = {}

    pageSize = 100
    def fetch(page):
        params['skip'] = page * pageSize
        params['top'] = pageSize
        response = get(endpoint, params=params)
        if response.status_code != 200:
            raise DDHRequestException(response)
        return response.json()
    
    count = None
    pageNum = 0
    while count is None or pageNum * pageSize <= count:
        batch = fetch(pageNum)
        if 'response' in batch:
            response_text = 'response'
            count_text = 'count'
            data_text = 'data'
        elif 'Response' in batch:
            response_text = 'Response'
            count_text = '@odata.count'
            data_text = 'value'
        count = batch[response_text][count_text]
        for row in batch[response_text][data_text]:
            yield row
        pageNum += 1



def get_all_in_list(endpoint, params=None, headers=None, session=None):
    '''Fetch all data for endpoints that have top and skip parameters

    Returns:
        a List
    '''
    if "top" in params or "skip" in params:
        raise Exception("get_all function cannot be used with 'top' or 'skip' parameter.")
    if params == None:
        params = {}

    pageSize = 100
    def fetch(page):
        params['skip'] = page * pageSize
        params['top'] = pageSize
        response = get(endpoint, params=params)
        if response.status_code != 200:
            raise DDHRequestException(response)
        return response.json()
    
    return_list = []
    count = None
    pageNum = 0
    while count is None or pageNum * pageSize <= count:
        batch = fetch(pageNum)
        if 'response' in batch:
            response_text = 'response'
            count_text = 'count'
            data_text = 'data'
        elif 'Response' in batch:
            response_text = 'Response'
            count_text = '@odata.count'
            data_text = 'value'
        count = batch[response_text][count_text]
        for row in batch[response_text][data_text]:
            return_list.append(row)
        pageNum += 1
    return return_list


    
def post(endpoint, params=None, json=None, headers=None, session=None):
    '''Send a POST request

    Arguments:
        endpoint:		the endpoint (e.g., "dataset/listpage")
        json:			data object
        params:			query parameters
        headers:		additional headers

    Returns:
        a Response object (from the requests package)
    '''
    if session:
        session.check_tokens()
        return requests.post(get_endpoint(endpoint, session), params=params, json=json, verify=session.verify, headers=session.get_headers(headers))
    else:
        raise DDHSessionException("DDH POST request requires a session")

def try_post(endpoint, params=None, json=None, headers=None, session=None, num_try=3, interval=300):
    '''Repeat sending a POST request until it succeeds or it tries {num_try} times

    Additional arguments:
        num_try:        number of tries
        interval:       interval between tries in seconds
    '''
    if session:
        count = 0
        while True:
            try:
                count = count + 1
                session.check_tokens()
                return requests.post(get_endpoint(endpoint, session), params=params, json=json, verify=session.verify, headers=session.get_headers(headers))
            except requests.exceptions.RequestException as e:
                print (f"[{count} try] Error: ", e)
                if count > num_try:
                    raise Exception(f"Request failed after {count} tries.")
                continue
                        
    else:
        raise DDHSessionException("DDH POST request requires a session")

def post_file(endpoint, files=None, headers=None, session=None):
    '''Send a POST request with file

    Arguments:
        endpoint:		the endpoint (e.g., "dataset/listpage")
        files:			multi-part form object
        headers:		additional headers

    Returns:
        a Response object (from the requests package)
    '''
    if session:
        session.check_tokens()
        return requests.post(get_endpoint(endpoint, session), files=files, verify=session.verify, headers=session.get_headers(headers))
    else:
        raise DDHSessionException("DDH POST request requires a session")


def get_endpoint(endpoint, session=None):
    if session:
        return '/'.join([session.api_host, endpoint.strip()])
    else:
        return '/'.join([public_API_host, endpoint.strip()])
    

def get_api_host(session=None):
    if session:
        return session.api_host
    else:
        return public_API_host
    

def set_api_host(url, session=None):
    if session:
        session.api_host = url
    else:
        global public_API_host
        public_API_host = url