from ast import operator
import json
from constants import AUTH_USER_URL
import libs.request as request
from modules.storage import get_kvs


def get_token(username, password):
    body = json.dumps({"email": username, "password": password})

    response = request.post(AUTH_USER_URL, data=body, headers={
                            'content-type': 'application/json'})

    token = "Bearer " + response.json()["token"]

    kvs = get_kvs()
    kvs.set('AUTH_TOKEN', token)

    return token


