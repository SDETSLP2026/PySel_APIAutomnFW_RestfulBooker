import json

import requests


# requests.get()
# requests.post()
# requests.patch()
# requests.put()
# requests.delete()

# We may need to reuse above methods multiple times. So we can define our own methods just once & reuse them as per required.

def get_request(url, auth):
    response = requests.get(url=url, auth=auth)
    return response.json()


def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:  # Here, in_json will be given as True only if user wants response in JSON format
        return post_response.json()
    return post_response


def patch_request(url, auth, headers, payload, in_json):
    patch_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:  # Here, in_json will be given as True only if user wants response in JSON format
        return patch_response.json()
    return patch_response


def put_request(url, auth, headers, payload, in_json):
    put_request = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:  # Here, in_json will be given as True only if user wants response in JSON format
        return put_request.json()
    return put_request


def delete_request(url, auth, headers, payload, in_json):
    delete_request = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:  # Here, in_json will be given as True only if user wants response in JSON format
        return delete_request.json()
    return delete_request
